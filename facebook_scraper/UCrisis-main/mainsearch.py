import facebook_scraper as fs
from facebook_scraper import get_posts
from datetime import datetime, timedelta
import pandas as pd

# Get the current date and time
current_datetime = datetime.now()

# Initialize an empty list to store the post data
post_data_list = []

# Specify the group or page ID
group_id_list = ['305407624063112', '660519427666787', '768120791123543','539836509530743', '660953494027689', '544879115576157', '386377711439937', '1310115422351233','1896100413812241'] #south utah, Siskiyou Alerts, Shasta County, Las Vegas News, Oakdale California, Tuolumne County, Incident Scanner,Public Safety Incidents, CocoCounty, Romona
#group_id_list = ['2016156348627511','362946857620532','2783158301696787','685717354814836']
pages = 2  # Number of pages to scrape

# Define the time threshold (12 hours ago from the current time)
time_threshold = current_datetime - timedelta(hours=24)

# Loop through the posts
for group_id in group_id_list:
    for post in get_posts(group_id, pages=pages):
        print(post)
        post_time_str = str(post['time'])
        # Parse the post time string into a datetime object
        post_datetime = datetime.strptime(post_time_str, '%Y-%m-%d %H:%M:%S')
        # Check if the post time is within 12 hours of the current time
        if post_datetime >= time_threshold:
            post_data = {
                'Text': post['text'],
                'Post URL': post['post_url'],
                'Time': post['time'],
            }
            post_data_list.append(post_data)

# Create a Pandas DataFrame from the collected post data
df = pd.DataFrame(post_data_list)
df['Number'] = range(1, len(df) + 1)
# Save the DataFrame to a CSV file
csv_filename = 'facebook_postsold.csv'
df.to_csv(csv_filename, index=False)

# Print the collected post data
print("Data saved to", csv_filename)

# Print the collected post data
#for post_data in post_data_list:
    #print(post_data)
