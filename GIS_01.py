#Jose Hernandez

# import arcpy site-package
import arcpy

# Set geoprocessing environment:
# a) set the workspace environment - fill in the path to your Exercise_Data.gdb
aWS = r"C:\Student\Jose\Assignment_01\Assignment_01.gdb"
arcpy.env.workspace = aWS

print "Current directory is {0}".format(arcpy.env.workspace)

# List All Feature Classes [stand-alone feature classes that are NOT in a Dataset]
fcList = arcpy.ListFeatureClasses()

#Open File to write ouput in
OutFile = open(r"C:\Student\Jose\Assignment_01\Msg.txt", "w")

#For loop to iterate through the feature classes. 
for aFC in fcList:
   aDesc = arcpy.Describe(aFC).shapeType #Describes Shape Type
   aCount = arcpy.GetCount_management(aFC)#Gets Count
   aProjec = arcpy.Describe(aFC).SpatialReference.type#List Projection

   #if loop will check to see if the condition is met for projection. Will ouput to file
   if arcpy.Describe(aFC).spatialReference.type == 'Geographic':
      print "{0} feature class is a {1} type and has {2} features. It is not projected\n".format(aFC, aDesc, aCount)
      OutFile.write("{0} feature class is a {1} type and has {2} features. It is NOT projected\n".format(aFC, aDesc, aCount, aProjec))
   else:
      print "{0} feature class is a {1} type and has {2} features. It is {3}\n".format(aFC, aDesc, aCount, aProjec)
      OutFile.write("{0} feature class is a {1} type and has {2} features. It is {3}\n".format(aFC, aDesc, aCount, aProjec))

# Script end message
OutFile.close()
print "\nEnd of the script!"
