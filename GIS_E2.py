import arcpy

aWS = r"C:\StudentData\JoseH\Exam-02\Exam_2.gdb"
arcpy.env.workspace = aWS

Outfile = open(r"C:\StudentData\JoseH\Exam-02\msg.txt","w")

fcList = arcpy.ListFeatureClasses()
fcList.sort()

print "There are {0} feature classes in this geodatabase!\n".format(len(fcList))
Outfile.write("There are {0} feature classes in this geodatabase!\n".format(len(fcList)))
Outfile.write("\n")

for aFC in fcList:
    aDesc = arcpy.Describe(aFC).shapeType
    aCount = arcpy.GetCount_management(aFC)
    aProjec = arcpy.Describe(aFC).SpatialReference.type
    name = aFC + "_P"

    if aProjec == "Projected":
        print "{0} has {1} features, it is a {2}.".format(aFC.lower(), aCount, aDesc.upper())
        Outfile.write("{0} has {1} features, it is a {2}.\n".format(aFC.lower(), aCount, aDesc.upper()))
    else:
        if arcpy.Exists(name):
            arcpy.Delete_management
        arcpy.Project_management(aFC, name, arcpy.SpatialReference(3310))
        print "{0} has {1} features, it is a {2}. it has been projected into {3}.".format(aFC.lower(), aCount, aDesc.upper(), name)
        Outfile.write("{0} has {1} features, it is a {2}. it has been projected into {3}.\n".format(aFC.lower(), aCount, aDesc.upper(), name))
Outfile.close()
print "\nEnd of file"
