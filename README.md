# choromaps
A repository to mess around with Choropleth Maps in Python

## Context

This repository is made to create Choromap [Choropleth Maps](https://en.wikipedia.org/wiki/Choropleth_map) in Python.

This mainly uses the plotly library.

## Dependencies 

`pandas` and `plotly` are required to use this script, as well as some possible other libraries (`urllib`, `numpy`)

To install : 

```python
python -m pip install plotly
python -m pip install pandas
```


## Run Script

Either use :
`python choromaps.py` to use the default example 

or 

`python choromaps.py ressources/my_custom-file.csv my-data`

with 
* `my_custom-file.csv` a custom CSV file with your data in it
* `my-data` the column name of the CSV file containing the data

## Add Custom Files

A custom CSV file can be added in the `resources` folder (or actually, whereever you want), just make sure that :
* It has two columns, one "departement" and the other "my-data"
* Values are separated by commas ( "," ) and not semicolons (";")


## Todos 

* Better handling of command line and CSV files

## Useful Links

* [Plotly Tutorial on Chloropeth Maps](https://plotly.com/python/choropleth-maps/)
* [Stackoverflow Example that was useful for me](https://stackoverflow.com/questions/60870063/plotly-express-choropleth-for-country-regions)
* [GeoJson Data of France](https://france-geojson.gregoiredavid.fr/)