import arcpy, numpy

# Set geoprocessing environment:
aWS = r"C:\StudentData\JoseH\Exam-04\Exam_04.gdb"
arcpy.env.workspace = aWS

# Define a feature class
aFC = "LandParcels"
Outfile = open(r"C:\StudentData\JoseH\Exam-04\msg.txt", "w")

aQuery = 'TaxVal04 > 100 OR TaxVal06 > 100'

#Create a a list of fields
fList = ['TaxVal06', 'TaxVal04']

#Converts a feature class to NumPy structured array.
aNumpyArray = arcpy.da.FeatureClassToNumPyArray(aFC, fList, aQuery)

a = numpy.sum(aNumpyArray['TaxVal04'] * .07) 
b = numpy.sum(aNumpyArray['TaxVal06'] * .08)
print a
print b

Outfile.write("Total collected Tax for 2004 is $" + str(a) + "\n")
Outfile.write("Total collected Tax for 2006 is $" + str(b))

Outfile.close()
print "\nEnd of the script!"