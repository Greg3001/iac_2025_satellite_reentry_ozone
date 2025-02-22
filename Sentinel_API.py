# Import required packages
import openeo
import json
import csv
from openeo.processes import process

# Connect and authentificate
connection = openeo.connect("https://openeo.dataspace.copernicus.eu").authenticate_oidc()

#Data and coordenates 
load1 = connection.load_collection(collection_id = "SENTINEL_5P_L2", spatial_extent = {"west": -74.14119488733773, "east": -73.02339426798693, "south": 39.89652653464046, "north": 40.59264137612317}, temporal_extent = ["2020-12-28T00:00:00Z", "2020-12-30T23:59:59Z"], bands = ["SO2"])
save2 = load1.save_result(format = "JSON") 

# The process can be executed synchronously
result = connection.execute(save2)

with open('YOUR DIRECTORY', 'w') as f:
    json.dump(result, f, indent=4)


with open('YOUR DIRECTORY', 'r') as f:
    data = json.load(f)


with open('YOUR DIRECTORY', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    header = list(data.keys())
    writer.writerow(header)

    # Write the data row
    writer.writerow(list(data.values()))