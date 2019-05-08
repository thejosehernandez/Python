#import arcpy
import arcpy,numpy

#set the environment
arcpy.env.workspace = r"C:\StudentData\JoseH\Exam-06\Exam_06.gdb"

aQuery = 'Value_06 > 100'
aFC = "LandParcels"

with arcpy.da.UpdateCursor(aFC, "*", aQuery) as cursor:
    for row in cursor:
        row[5] = (row[4] * 0.08)
        cursor.updateRow(row)

aQuery1 = 'UseCode = \'C\''

anArray = arcpy.da.FeatureClassToNumPyArray(aFC, ['TAX_06'], aQuery1)
#print anArray['TAX_06']

#sq the array
sqList = [ numpy.square(item) for item in anArray['TAX_06'] ]
#print sqList

#sum the array
aSum = numpy.sum(sqList)
#print numpy.sum(sqList)

aRoot = numpy.sqrt(aSum)
#print numpy.sqrt(aSum)

#divide each value by the sq root
theList = [ (item / aRoot) for item in anArray['TAX_06'] ]
#print theList

Outfile = open("C:\StudentData\JoseH\Exam-06\msg.txt", "w")
for anitem in theList:
    print anitem
    Outfile.write(str(anitem) + "\n")

Outfile.close()  
print "\nEnd of File"
