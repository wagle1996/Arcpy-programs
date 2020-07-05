import arcpy
import os
import math
fc = r'D:\Pythoning\288205C\Database\288205C.gdb\Sheets\sheets_1'
print "a"
input_gdb = r'D:\Pythoning\288205C\Database\288205C.gdb'
print "b.."
output_folder = r'D:\Pythoning\outPut'
print "c...."
xmlFolder=r'D:\Pythoning'
prj_file =  r'D:\Pythoning\Nepal_Nagarkot_TM_81.prj'
sr = arcpy.SpatialReference(prj_file)
i = 1
print str(i) + "igzo..."
fields = ['SHAPE@','SHEET_NO']
with arcpy.da.SearchCursor(fc, fields) as rows:
    for row in rows:
        print "Starting Sheet : "
        clipper = row[0]
        gdb_name = str(row[1]) + '.gdb'
        xml_name= "Nagarkot25000TM81GridGraticule"+".xml"
        arcpy.CreateFileGDB_management(output_folder, gdb_name)
        arcpy.env.workspace = input_gdb
        x=output_folder + "/" + gdb_name
        grid_dataset=arcpy.CreateFeatureDataset_management(x,"grid_graticule",sr)
        feature_class=row[0]
    
        area_of_interest= feature_class
        outputlayer=str(row[1])
        template=xmlFolder+"\\"+xml_name
        arcpy.MakeGridsAndGraticulesLayer_cartography (template, area_of_interest, grid_dataset, outputlayer)
        
        input_datasets = arcpy.ListDatasets('*', 'Feature')
        for ds in input_datasets:
            print str(ds).lower()
            gdb = output_folder + '/' + gdb_name
            sr = arcpy.SpatialReference(prj_file)
            if str(ds) == "Admin_layer":
                input_location = input_gdb + '/' + str(ds)
                out_location = gdb + "/" + str(ds)
                print "Copying Admin_layer...."
                arcpy.Copy_management(input_location, out_location)
            elif str(ds).lower() == "grid_graticule" or str(ds).lower() == "sheets" :
                continue
            else:
                out_dataset = arcpy.CreateFeatureDataset_management(gdb, str(ds), sr)
                in_dataset = input_gdb + '/' + str(ds)
                
                arcpy.env.workspace = in_dataset
                in_feature_class = arcpy.ListFeatureClasses()
                for fc in in_feature_class:
                    print "Clipping " + str(fc)
                    out_fc = str(out_dataset) + '/' + str(fc)
                    arcpy.Clip_analysis(str(fc), clipper, out_fc)
            
                
            print "Yatta..."
del rows
print " All done !"
        
