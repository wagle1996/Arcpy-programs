import arcpy
import os
#Give output workspace
out_workspace = "D:/Final/iterate"
def unique_values(table, field):
	with arcpy.da.SearchCursor(table, [field]) as cursor:
		dict = sorted({x[0] for x in cursor})
		print type(dict) #testing to find type 
	for i in range(len(dict)):
		whereD = dict[i]
		fname = whereD #just to make a filename for outputs
		arcpy.MakeFeatureLayer_management(table, fname)
		query = "Name = '" + whereD + "'"
		arcpy.SelectLayerByAttribute_management(fname, "NEW_SELECTION",query)
		out_featureclass = os.path.join(out_workspace, fname)
		arcpy.CopyFeatures_management(fname,out_featureclass)

#give input shapefile and name of the field
unique_values("D:/Final/lines.shp","Name")