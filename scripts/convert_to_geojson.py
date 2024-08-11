import geopandas as gpd

def convert_shapefile_to_geojson(shapefile_path, output_geojson_path):
    # Read the shapefile
    gdf = gpd.read_file(shapefile_path)

    # Ensure the CRS is set to WGS84 (EPSG:4326)
    gdf = gdf.to_crs(epsg=4326)

    # Print information about each feature
    for index, row in gdf.iterrows():
        print(f"Feature {index}:")
        for column in gdf.columns:
            if column != 'geometry':
                print(f"  {column}: {row[column]}")
        print("  Geometry type:", row['geometry'].geom_type)
        print()

    # Save as GeoJSON
    gdf.to_file(output_geojson_path, driver='GeoJSON')

    print(f"GeoJSON file saved to {output_geojson_path}")

# Example usage
shapefile_path = ''
output_geojson_path = ''
convert_shapefile_to_geojson(shapefile_path, output_geojson_path)