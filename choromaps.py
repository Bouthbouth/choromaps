'''
Python script that creates Choropleth Maps based on a CSV file

Simply a sandbox to experiment with plotly :) 
'''
from urllib.request import urlopen  # To Manipulate Urls
import json                         # To Manipulate Json
import pandas as pd                 # For data frame creation 
import plotly.express as px         # For Choropleth Map Creation 


### Declarations ###

# URL for the Json description of the French Departements 
URL_GEOJSON_FR  = 'https://france-geojson.gregoiredavid.fr/repo/departements.geojson'

# CSV Data
CSV_FOLDER      = "ressources/"
CSV_DATA        = "vaches.csv"
CSV_DATA_PATH   = "{}{}".format(CSV_FOLDER,CSV_DATA)

# Plotly Constants

PLTLY_SCOPE     = "europe"          # Scope that modifies the choropleth map, see documentation for more detail
PLTLY_CCS       = "aggrnyl_r"         # Color Continuous Scale for the map, see https://plotly.com/python/builtin-colorscales/ for more possibilities
PLTLY_FIK       = "properties.nom"  # Feature ID Key for Plotly, basically the path to field in GeoJSON feature object with which to match the values passed in to locations

# Constants
DEBUG           = 0

# Name of the data to extract in the CSV file (so the column name) 
map_locs_name   = "departement"
map_data_name   = "vaches"


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
