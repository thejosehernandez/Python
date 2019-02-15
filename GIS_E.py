#Jose Hernandez
#Exam 1
import arcpy

#set up workspace
aWS = r"C:\StudentData\JoseH\Exam_01_408E\Exam_1.gdb"
arcpy.env.workspace = aWS

#print "The workspace is " + arcpy.env.workspace

#Make the File
OutFile = open(r"C:\StudentData\JoseH\Exam_01_408E\msg.txt", "w")

#make a list of the feature classes
fcList = arcpy.ListFeatureClasses()
print "There are " + str(len(fcList)) + " feature classes in this geodatabase!\n"

for aFC in fcList:
    if arcpy.Describe(aFC).SpatialReference.type == 'Geographic':
        print aFC.lower() + " has " + str(arcpy.GetCount_management(aFC)) + " features, it is a " + arcpy.Describe(aFC).shapetype.upper() + ". it must be projected!"
        OutFile.write(aFC.lower() + " has " + str(arcpy.GetCount_management(aFC)) + " features, it is a " + arcpy.Describe(aFC).shapetype.upper() + ". it must be projected!\n")
    else:
        print aFC.lower() + " has " + str(arcpy.GetCount_management(aFC)) + " features, it is a " + arcpy.Describe(aFC).shapetype.upper() + "."
        OutFile.write(aFC.lower() + " has " + str(arcpy.GetCount_management(aFC)) + " features, it is a " + arcpy.Describe(aFC).shapetype.upper() + ". \n")

OutFile.close()
print "End of the script!"