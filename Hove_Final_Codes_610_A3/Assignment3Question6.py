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


# Add a field to feature class

arcpy.AddField_management(r"C:\Users\dhove\Desktop\Exercise3.gdb\Exercise3.gdb\CallsforService", "Crime_Explanation", "TEXT")

fields = ['CFSType', 'Crime_Explanation']


with arcpy.da.UpdateCursor(r"C:\Users\dhove\Desktop\Exercise3.gdb\Exercise3.gdb\CallsforService", fields) as cursor:
    # For each row, evaluate the WELL_YIELD value (index position 
    # of 0), and update WELL_CLASS (index position of 1)
    for row in cursor:
        if (row[0] == "Burglary Call"):
            row[1] = "This is a burglary"

        # Update the cursor with the updated list
        cursor.updateRow(row)

print("done!")
def burgFunc(CFSType): 
    if (CFSType == "Burglary Call"):
        print("This is a burglary")

print("done")
