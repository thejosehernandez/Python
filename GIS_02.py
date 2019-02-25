Lab 2
#Jose Hernandez

# import arcpy site-package
import arcpy

# Set geoprocessing environment:
aWS = r"C:\StudentData\JoseH\Assignment_02\Assignment_02.gdb"
arcpy.env.workspace = aWS

# List All Feature Classes
fcList = arcpy.ListFeatureClasses()
fcList.sort(reverse = True)

#Open file
OutFile = open(r"C:\StudentData\JoseH\Assignment_02\Msg.txt", "w")

#for list to iterate
for aFC in fcList:
    aDesc = arcpy.Describe(aFC).shapeType #Describes the shape
    aCount = arcpy.GetCount_management(aFC) # Gets Count
    aProjec = arcpy.Describe(aFC).SpatialReference.type #will get projection

#if statements    
    if arcpy.Describe(aFC).spatialReference.type == 'Projected':
        print "{0} feature class is a {1} type and has {2} features. It is {3}\n".format(aFC, aDesc.lower(), aCount, aProjec)
        OutFile.write("{0} feature class is a {1} type and has {2} features. It is {3}\n".format(aFC, aDesc.lower(), aCount, aProjec))
    else:
        if arcpy.Exists(aFC + "_P"):
              arcpy.Delete_management(aFC + "_P")
        arcpy.Project_management(aFC, aFC + "_P", arcpy.SpatialReference(26945))
        print "{0} feature class is a {1} type and has {2} features. It is not projected. It has been projected to {3}.\n".format(aFC, aDesc.lower(), aCount, aFC + "_P")
        OutFile.write("{0} feature class is a {1} type and has {2} features. It is not projected. It has been projected to {3}.\n".format(aFC, aDesc.lower(), aCount, aFC + "_P"))
        
OutFile.close()
print "\nEnd of the script!"
