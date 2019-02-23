# Dylan Hove
# GIS610
# Assignment: 3 Question: 9
# Due 2/22/19 @ 11:59 PM

# Import system modules
import arcpy
from arcpy import env

# Set workspace

current_workspace = r"C:\Users\dhove\Desktop\Exercise3.gdb\Exercise3.gdb"
arcpy.env.workspace = current_workspace

arcpy.CreateFeatureclass_management(r"C:\Users\dhove\Desktop\Exercise3.gdb\Exercise3.gdb", "FavoriteColor.shp", "POINT")

# Add a field to feature class

arcpy.AddField_management(r"C:\Users\dhove\Desktop\Exercise3.gdb\Exercise3.gdbFavoriteColor", "Color", "TEXT")

# Add domain

arcpy.CreateDomain_management(r"C:\Users\dhove\Desktop\Exercise3.gdb\Exercise3.gdb","Color", "ColorChoice", "SHORT", "CODED", "DUPLICATE", "DEFAULT")

# Add values to domain

arcpy.AddCodedValueToDomain_management(current_workspace, "Color", 0, 'Green')
arcpy.AddCodedValueToDomain_management(current_workspace, "Color", 1, 'RED')
arcpy.AddCodedValueToDomain_management(current_workspace, "Color", 2, 'BLUE')
arcpy.AddCodedValueToDomain_management(current_workspace, "Color", 3, 'ORANGE')
arcpy.AddCodedValueToDomain_management(current_workspace, "Color", 4, 'PINK')

print("done")