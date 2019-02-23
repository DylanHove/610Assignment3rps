# Dylan Hove
# GIS610
# Assignment: 3 Question: 6
# Due 2/22/19 @ 11:59 PM

# Import system modules
import arcpy
from arcpy import env

# Set workspace

current_workspace = r"C:\Users\dhove\Desktop\Exercise3.gdb\Exercise3.gdb"
arcpy.env.workspace = current_workspace

# Select a subset of records

arcpy.SelectLayerByAttribute_management ('CFSType', "SUBSET_SELECTION")

# Write the selected features to a different feature class

arcpy.CopyFeatures_management('CFSType', 'Burglaries')

print("finished!")
