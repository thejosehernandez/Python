# import arcpy site-package and os module
import arcpy, datetime

# Set geoprocessing environment:
aWS = r"C:\StudentData\JoseH\Assignment_03\Assignment_03.gdb"
arcpy.env.workspace = aWS

OutFile = open(r"C:\StudentData\JoseH\Assignment_03\Msg.txt", "w")
# Define a feature class
aFC = "LandParcels"

aQuery = 'TaxVal06 > 100 AND TaxVal04 >100'

# Create an Update Cursor
with arcpy.da.UpdateCursor(aFC, "*", aQuery) as aCursor:
    for aRow in aCursor:
        aRow[6] = ((aRow[2] - aRow[3]) / aRow[3]) * 100
        if aRow[6] < -3:
            aRow[7] = "A"
        if aRow[6] >= -3 and aRow[6] <= 0:
            aRow[7] = "B"
        if aRow[6] == 0:
            aRow[7] = "C"
        if aRow[6] >= 0 and aRow[6] <= 3:
            aRow[7] = "D"
        if aRow[6] > 3:
            aRow[7] = "E"
        aCursor.updateRow(aRow)
    
# Delete row object and cursor object
del aRow
del aCursor

#print datetime.datetime.now().time()
OutFile.write(str(datetime.datetime.now()))

OutFile.close()
# Script end message
print "\nEnd of the script!"