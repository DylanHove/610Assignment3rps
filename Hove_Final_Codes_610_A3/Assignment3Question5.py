# Dylan Hove
# GIS610
# Assignment: 3 Question: 5
# Due 2/22/19 @ 11:59 PM

# Import system modules
import arcpy
from arcpy import env

env.overwriteOutput = True

# Set workspace
current_workspace = r"C:\Users\dhove\Desktop\610Assignment3\610Assignment3.gdb"
arcpy.env.workspace = current_workspace


# Set local variables
out_folder_path = r"C:\Users\dhove\Desktop\610Assignment3"
out_name = "610Assignment3"


# Create Geodatabase
arcpy.CreateFileGDB_management(out_folder_path, out_name)

# Feature Class Variables
featureClassNamesList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']


# Execute tool
for feature in featureClassNamesList:
    arcpy.CreateFeatureclass_management (r"C:\Users\dhove\Desktop\610Assignment3\610Assignment3.gdb", feature, "POINT")
    
print("done")