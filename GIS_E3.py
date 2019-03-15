import arcpy, os

aWS = r"C:\StudentData\JoseH\Exam-03\Exam_3.gdb"
arcpy.env.workspace = aWS

OutFile = open(r"C:\StudentData\JoseH\Exam-03\Msg.txt", "w")

aFC = "LandParcels"
aQuery = '(UseCode = \'A\' OR UseCode = \'B\') AND (TaxVal06 > 0 AND TaxVal00 > 0)'

with arcpy.da.UpdateCursor(aFC, "*", aQuery) as aCursor:
    for aRow in aCursor:
        aRow[10] = ((float(aRow[3]) - aRow[5]) / aRow[5]) * 100.00
        aCursor.updateRow(aRow)

del aRow
del aCursor

OutFile.write(str(datetime.datetime.now()))
OutFile.close()

print "\nEnd of file"