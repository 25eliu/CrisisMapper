from tkinter import *
from tkinter import ttk
import requests
import urllib.parse


import maps
#import leftTab
import sideTab


win = Tk()
win.geometry(f"{1050}x{750}")
win.title("UCrisis")

# Create a notebook that holds the tabs
notebook = ttk.Notebook(win)

# Create tab frames
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Add the tab frames to the notebook
notebook.add(tab1, text="Map")
notebook.add(tab2, text="User Information")

notebook.pack(expand=1, fill='both')

# Place widgets in tab1
#map_widget.place(relx=1, rely=0, anchor=tkinter.NE)
maps.tabbed_window(tab1)



# Place widgets in tab2
location_label = Label(text="Location:")
#location_label.grid(row=0, column=0, padx=10, pady=5)
location_entry = Entry()
#location_entry.grid(row=0, column=1, padx=10, pady=5)

# Notification Type Label and Dropdown
notification_type_label = Label(text="Notification Type:")
#notification_type_label.grid(row=1, column=0, padx=10, pady=5)
notification_type_var = StringVar()
notification_type_combo = ttk.Combobox(textvariable=notification_type_var, values=["Email", "SMS", "Push"])
#notification_type_combo.grid(row=1, column=1, padx=10, pady=5)
notification_type_combo.set("Email")

Label(tab2, text="Type your location:").pack()
Entry(tab2, width=100).pack()

#location_label(tab2).pack()



#leftTab.create_tab2_contents(tab2)

win.mainloop()