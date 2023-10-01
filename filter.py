# Python Imports
from transformers import RobertaTokenizer, RobertaForSequenceClassification
import shutil
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import transformers
from transformers import AutoModel, BertTokenizerFast
import csv
import re
import io

# GPT Imports
import os
import openai

LLM_prompt = "I will give you a list of prompts that revolve around crises/incidents, and I would like you to output a list. Within this list, I would like you to output one line per prompt, prompts separated by a blank line. The lines will include: what the crisis/incident is, the Area/Address/Region of where the crisis/incident happened (no commas between the address, city, and country please), a description of the original crisis message, and the number that was given in the list. Even if a prompt doesn’t specify an address, please use context to try and give an approximate region/area as to where this happened. This list can only have crises that are WITHIN a 40 mile RADIUS of the location that I will give you. If the crisis is not within a 40 mile radius of the given location, DO NOT PRINT IT OUT. If the crisis does not have an address mention in it, DO NOT PRINT IT OUT. For each separate prompt, I will give the text that is in the prompt, a link to where the prompt was posted, and the time it was posted. Each individual prompt outputed in the list must be unique; that is if two prompts describe the same incident/crisis, output only one line for both prompts. Example: Crisis/Incident: Gas Leak (nextline) Area/Address/Region: 550 West Diagonal St George (nextline) Description: Strong smell of gas- All occupants have exited the condo.(nextline) Number: 10   The location is: "
df = pd.read_csv("facebook_postsold.csv")

links = df[["Number", "Post URL", "Time"]]
newdf = df[["Number", "Text"]]


prompt_list = newdf.to_csv(index=False)

user_location = input("Please enter your location: ")

# GPT
api_key = "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"
openai.api_key = api_key

system_msg = "You are a helpful assistant who knows the map of the world and knows distances between different addresses."
prompt = LLM_prompt + user_location + "Here are the prompts: " + ". \n" + prompt_list


response = openai.ChatCompletion.create(
    model="gpt-4",  # Use the appropriate engine for your task.
    messages=[
        {"role": "system", "content": system_msg},
        {"role": "user", "content": prompt},
    ],
    temperature=0.3,
    max_tokens=450,  # Adjust based on desired response length.
)

generated_text = response["choices"][0]["message"]["content"]

print(generated_text)


crisis_reports = re.split(r"\n\n+", generated_text.strip())

# Initialize empty lists to store data
crisis_list = []
area_list = []
description_list = []
link_list = []

# Extract data from each crisis report
for report in crisis_reports:
    # Use regular expressions to extract data
    crisis_match = re.search(r"Crisis/Incident:\s+(.+)", report)
    area_match = re.search(r"Area/Address/Region:\s+(.+)", report)
    description_match = re.search(r"Description:\s+(.+)", report)
    link_match = re.search(r"Number:\s+(.+)", report)

    if crisis_match and area_match and description_match and link_match:
        crisis_list.append(crisis_match.group(1))
        area_list.append(area_match.group(1))
        description_list.append(description_match.group(1))
        link_list.append(int(link_match.group(1)))

# Create a pandas DataFrame
data = {
    "title": crisis_list,
    "address": area_list,
    "description": description_list,
    "Number": link_list,
}
df = pd.DataFrame(data)


# Initialize empty lists to store 'Post URL' and 'Time' values
post_url_list = []
time_list = []

# Iterate through the sample DataFrame and populate 'Post URL' and 'Time'
column_data_type = df['Number'].dtype
print(f"Data type of 'Number': {column_data_type}")

linkscolumn_data_type = links['Number'].dtype
print(f"Data type of 'Number': {linkscolumn_data_type}")
for index, row in df.iterrows():
    number = row['Number']
    print(number)
    # Use the 'Number' value to find the corresponding row in 'df'
    matching_row = links[links['Number'] == number]
    if not matching_row.empty:
        post_url = matching_row.iloc[0]['Post URL']
        time = matching_row.iloc[0]['Time']
        post_url_list.append(post_url)
        time_list.append(time)
    else:
        post_url_list.append(None)
        time_list.append(None)

# Add 'Post URL' and 'Time' columns to the sample DataFrame
df['url'] = post_url_list
df['time'] = time_list

# Save the DataFrame to a CSV file
csv_file_path = "crisis_data.csv"
df.to_csv(csv_file_path, mode='a', header=False, index=False)

# Display the DataFrame
print(df)

# Confirm that the CSV file has been saved
print(f"Data saved to {csv_file_path}")
