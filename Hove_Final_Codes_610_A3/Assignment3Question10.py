# Dylan Hove
# GIS610
# Assignment: 3 Question: 10
# Due 2/22/19 @ 11:59 PM


import arcpy

arcpy.env.workspace = r"C:\Users\dhove\Desktop\610Assignment3\610Assignment3.gdb"


target_features = r"C:\Users\dhove\Desktop\610Assignment3\610Assignment3.gdb\CensusTracts.shp"
join_features = r"C:\Users\dhove\Desktop\610Assignment3\610Assignment3.gdb\GeneralOffense.shp"
out_feature_class = r"C:\Users\dhove\Desktop\610Assignment3\610Assignment3.gdb\JoinedTractsOffense"

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)