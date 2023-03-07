import geopandas

shp_file = geopandas.read_file(r"C:\Users\snytko\Desktop\projekty\load\True_Ortho_0953_62969.shp")
shp_file.to_file("json_output.geojson", driver="GeoJSON")

# zmiana