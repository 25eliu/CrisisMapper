import tkintermapview
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, "offline_tiles_ca.db")
zoom_min = 3
zoom_max = 15

areas = [[(38.11126840107527, -123.0964549602353), (37.57989563478757, -122.20656238355589)]]



# create OfflineLoader instance
for locations in areas:
     loader = tkintermapview.OfflineLoader(path=database_path, tile_server="https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
     top_left_position = locations[0]
     bottom_right_position = locations[1]
     loader.save_offline_tiles(top_left_position, bottom_right_position, zoom_min, zoom_max)

loader.print_loaded_sections()