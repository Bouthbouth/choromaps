'''
Python script that creates Choropleth Maps based on a CSV file

Simply a sandbox to experiment with plotly :) 
'''
from pickle import FALSE
from urllib.request import urlopen  # To Manipulate Urls
import json                         # To Manipulate Json
import pandas as pd                 # For data frame creation 
import plotly.express as px         # For Choropleth Map Creation 
import os                           # For checking file integrity
import sys                          # For command line arguments

# Name of the data to extract in the CSV file (so the column name) 
map_locs_name   = "departement"

### Parse input arguments (if any) ###
if len(sys.argv) > 2:
    CSV_DATA_PATH   = str(sys.argv[1])

    # Safety Check 
    if(os.path.exists(CSV_DATA_PATH) == False):
        print("Invalid file ! Exiting application...")
        exit()

    map_data_name   = str(sys.argv[2])

    print("Processing file \"{}\" and using column \"{}\" as a data for the Choropleth Map".format(CSV_DATA_PATH,map_data_name))

elif len(sys.argv) == 1:
    # No Arguments were provided, using default file
    CSV_DATA_PATH   = "ressources/vaches.csv"
    map_data_name   = "vaches"      
    print("Processing file \"{}\" and using column \"{}\" as a data for the Choropleth Map".format(CSV_DATA_PATH,map_data_name))
else:
    # Invalid Number of Arguments 
    print("Usage should be :")
    print("choromaps.py csv_file_name.csv column_of_interest")
    print("Example : choromaps.py ressources/vaches.csv vaches")

### Declarations ###

# URL for the Json description of the French Departements 
URL_GEOJSON_FR  = 'https://france-geojson.gregoiredavid.fr/repo/departements.geojson'

# Plotly Constants

PLTLY_SCOPE     = "europe"          # Scope that modifies the choropleth map, see documentation for more detail
PLTLY_CCS       = "aggrnyl_r"         # Color Continuous Scale for the map, see https://plotly.com/python/builtin-colorscales/ for more possibilities
PLTLY_FIK       = "properties.nom"  # Feature ID Key for Plotly, basically the path to field in GeoJSON feature object with which to match the values passed in to locations

# Constants
DEBUG           = 0

### Read the geojson data with France's borders ###
with urlopen(URL_GEOJSON_FR) as response:
    france_regions_geo = json.load(response)

### Extract appropriate data from the CSV files ###
col_list        = [map_locs_name,map_data_name]
df              = pd.read_csv(CSV_DATA_PATH,usecols=col_list)

### Debug Prints ### 
if DEBUG==1:
    print(df[map_data_name])

### Choropleth representing the input data ###
fig = px.choropleth(data_frame              = df, 
                    geojson                 = france_regions_geo, 
                    locations               = map_locs_name,            # Name of the dataframe column for locations
                    featureidkey            = PLTLY_FIK,         
                    color                   = map_data_name,            # Value that will indicate the "intensity" of our map 
                    color_continuous_scale  = PLTLY_CCS,
                    scope                   = PLTLY_SCOPE,
                   )
fig.update_geos(showcountries=False, showcoastlines=False, showland=False, fitbounds="locations")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
