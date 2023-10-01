import tkinter
import tkintermapview
import os
import pandas as pd
from PIL import Image, ImageTk
import csv
import sideTab
import requests
import urllib.parse

images = {}
marker_data = []
image_titles = ["car break-in", "arson", "robbery", "alert"]
image_extesnions = [".jpeg", ".jpeg", ".jpeg", ".png"]

window = None
info_text = None


def add_marker(marker_data, map_widget):
    map_markers = []
    #print(marker_data)

    for j in range(len(marker_data)):
        try:
            row = marker_data.iloc[j]

            # url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(row["address"]) +'?format=json'

            # response = requests.get(url).json()
            # x = response[0]["lat"]
            # y = response[0]["lon"]
            x, y = tkintermapview.convert_address_to_coordinates(row["address"])

            marker_data.at[j, "latitude"] = x
            marker_data.at[j, "longitude"] = y

          #   for i in range(len(image_titles)):
          #       if image_titles[i] in row["title"].lower():
          #           map_markers.append(
          #               map_widget.set_marker(
          #                   x,
          #                   y,
          #                   text=row["title"],
          #                   image=images[image_titles[i]],
          #                   icon=images["alert.png"],
          #                   command=on_marker_click,
                            
          #               )
          #           )
          #           break
          #   else:
            map_markers.append(
               map_widget.set_marker(
               x,
               y,
               text=row["title"],
               # image=images["robbery"],
               icon=images["alert"],
               command=on_marker_click,
               )
          )
        except:
            print(row["address"])
            pass
        


def on_marker_click(marker):
    # find index of marker in marker_data using longitude and latitude
    for i in range(len(marker_data)):
        if (
            marker_data["latitude"][i] == marker.position[0]
            and marker_data["longitude"][i] == marker.position[1]
        ):
            #(marker_data["address"][i])
            sideTab.update_info(
                marker_data["title"][i],
                marker_data["url"][i],
                marker_data["description"][i],
                marker_data["address"][i],
                marker_data["time"][i],
            )

            break


def create_info_dict(marker_data):
    info_dict = {}

    for i in range(len(marker_data)):
        title = marker_data["title"][i]
        address = marker_data["address"][i]
        info_dict[i] = {"title": title, "address": address}

    return info_dict


def csv_to_marker_data(csv_file):
    marker_data = {"title": [], "address": []}

    with open(csv_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            marker_data["title"].append(row["title"])
            marker_data["address"].append(row["address"])

    return marker_data


def get_data():
    data = pd.read_csv("crisis_data.csv")
    return data


def tabbed_window(tab):
    global window
    global entry_var

    popup = tkinter.Toplevel(tab)
    popup.geometry("200x100")
    popup.title("Address Input")
    
    window = tab

    script_directory = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(script_directory, "offline_tiles_ca.db")

    map_widget = tkintermapview.TkinterMapView(
        tab,
        width=1000,
        height=750,
        corner_radius=0,
        database_path=database_path,
        use_database_only=False,
    )

    map_widget.place(relx=1, rely=0, anchor=tkinter.NE)
    map_widget.set_tile_server(
        "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22
    )

    map_widget.set_position(37.77493, -122.41942)  # SF
    map_widget.set_zoom(10)

    entry_var = tkinter.StringVar()
    entry = tkinter.Entry(popup)
    entry.pack(padx=20, pady=10)

    close_button = tkinter.Button(popup, text="Submit", command=lambda: submit_and_close(entry.get()))
    close_button.pack(pady=10)

    def submit_and_close(input_string):
     try:
          x, y = tkintermapview.convert_address_to_coordinates(input_string)
          map_widget.set_position(x, y)
     except:
         #badEntry = tkinter.Labelp(popup, text="Invalid Address")
         pass
     
     popup.destroy()


    global marker_data
    marker_data = get_data()
    marker_data["latitude"] = 0
    marker_data["longitude"] = 0

    current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    for i in range(len(image_titles)):
        images[image_titles[i]] = ImageTk.PhotoImage(
            Image.open(
                os.path.join(
                    current_path, "images", image_titles[i] + image_extesnions[i]
                )
            ).resize((50, 50))
        )

    add_marker(marker_data, map_widget)
    global addressLabel
    global titleLabel
    addressLabel = " "
    titleLabel = " "

    sideTab.LeftWing_init(window)

    map_widget.set_zoom(11)


def get_address():
    user_address = input("Please enter your address")
    filter.get_crisis_data(user_address)


def main():
    root_tk = tkinter.Tk()
    root_tk.geometry(f"{1000}x{750}")
    root_tk.title("UCrisis")

    tabbed_window(root_tk)

    root_tk.mainloop()


if __name__ == "__main__":
    main()
