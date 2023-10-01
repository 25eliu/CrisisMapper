import tkinter
import os
from PIL import Image, ImageTk

import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Notification Form")

def create_tab2_contents(parent_frame):
    # Create the contents for tab2
    label = tk.Label(parent_frame, text="User Information")
    label.pack()

    # Location Label and Entry
    location_label = tk.Label(top_frame, text="Location:")
    location_label.grid(row=0, column=0, padx=10, pady=5)
    location_entry = tk.Entry(top_frame)
    location_entry.grid(row=0, column=1, padx=10, pady=5)

    # Notification Type Label and Dropdown
    notification_type_label = tk.Label(top_frame, text="Notification Type:")
    notification_type_label.grid(row=1, column=0, padx=10, pady=5)
    notification_type_var = tk.StringVar()
    notification_type_combo = ttk.Combobox(top_frame, textvariable=notification_type_var, values=["Email", "SMS", "Push"])
    notification_type_combo.grid(row=1, column=1, padx=10, pady=5)
    notification_type_combo.set("Email")

    # Create a frame for the bottom section (User Info)
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(anchor=tk.NW, padx=20, pady=20)

    # User Name Label and Entry
    username_label = tk.Label(bottom_frame, text="User Name:")
    username_label.grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(bottom_frame)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    # Phone Number Label and Entry
    phone_label = tk.Label(bottom_frame, text="Phone Number:")
    phone_label.grid(row=1, column=0, padx=10, pady=5)
    phone_entry = tk.Entry(bottom_frame)
    phone_entry.grid(row=1, column=1, padx=10, pady=5)

    # Email Label and Entry
    email_label = tk.Label(bottom_frame, text="Email:")
    email_label.grid(row=2, column=0, padx=10, pady=5)
    email_entry = tk.Entry(bottom_frame)
    email_entry.grid(row=2, column=1, padx=10, pady=5)


    location = location_entry.get()
    notification_type = notification_type_var.get()
    username = username_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    
    # Handle the input data as needed
    # You can replace the print statements with your desired logic
    print(f"Location: {location}")
    print(f"Notification Type: {notification_type}")
    print(f"Username: {username}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")

    # Submit Button
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.pack(pady=20)

def submit():
    # Create a frame for the top section (Location and Notification Type)
    top_frame = tk.Frame(root)
    top_frame.pack(anchor=tk.NW, padx=20, pady=20)

    

root.geometry("400x300")
root.mainloop()

