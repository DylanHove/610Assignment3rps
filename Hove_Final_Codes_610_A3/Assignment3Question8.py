# Dylan Hove
# GIS610
# Assignment: 3 Question: 8
# Due 2/22/19 @ 11:59 PM


import arcpy

arcpy.env.workspace = r"C:\Users\dhove\Desktop\610Assignment3\610Assignment3.gdb"

print(arcpy.GetCount_management('CallsforService'))

