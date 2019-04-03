import arcpy

#1. Set the workspace to Assignment_04.gdb
aFolderPath = r"C:\StudentData\JoseH\Assignment_04"
aGDB = "Assignment_04.gdb"
bGDB = "PCS_Data.gdb"

#if exists delete
if arcpy.Exists(r"C:\StudentData\JoseH\Assignment_04\PCS_Data.gdb"):
    arcpy.Delete_management(r"C:\StudentData\JoseH\Assignment_04\PCS_Data.gdb")
arcpy.CreateFileGDB_management(aFolderPath, bGDB)
 
arcpy.env.workspace = aFolderPath + "\\" + aGDB

#2. Create a list of all feature classes within the geodatabase
aFCList = arcpy.ListFeatureClasses()

#4. Check the feature classes in your list, if they are not projected do it into 26945
for aFC in aFCList:
    if arcpy.Describe(aFC).SpatialReference.type == 'Geographic':
        outFile = aFolderPath + "\\" + bGDB + "\\" + aFC
        arcpy.Project_management(aFC, outFile, 26945)

arcpy.env.workspace = aFolderPath + "\\" + bGDB
#5. Select SFV_BG feature class for calculation
aFC = "SFV_BG "

aQuery = 'POP_16 > 0 AND POP_16 IS NOT NULL'

arcpy.AddField_management("SFV_BG", "DI", "DOUBLE")
with arcpy.da.UpdateCursor(aFC, "*", aQuery) as aCursor:
    for aRow in aCursor:
        aRow[14] = 1 - ( ((aRow[4] / aRow[3])**2) + ((aRow[5] / aRow[3])**2) + ((aRow[6] / aRow[3])**2) + ((aRow[7] / aRow[3])**2) + ((aRow[8] / aRow[3])**2) + ((aRow[9] / aRow[3])**2) + ((aRow[10] / aRow[3])**2) + ((aRow[11] / aRow[3])**2) )
        aCursor.updateRow(aRow)

print "\nEnd of File"
