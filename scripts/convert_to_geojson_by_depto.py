import geopandas as gpd
import os

# Crear la carpeta 'deptos' si no existe
if not os.path.exists('deptos'):
    os.makedirs('deptos')

# Leer el archivo shapefile
gdf = gpd.read_file('')

# Asegurarse de que el CRS sea WGS84 (EPSG:4326)
gdf = gdf.to_crs(epsg=4326)

# Agrupar por departamento
grouped = gdf.groupby('depto')

# Iterar sobre cada grupo y guardar como un archivo GeoJSON separado
for depto, group in grouped:
    # Crear un nombre de archivo para cada departamento
    filename = f"deptos/{depto.lower().replace(' ', '_')}.geojson"
    
    # Guardar como GeoJSON
    group.to_file(filename, driver='GeoJSON')
    
    print(f"Archivo guardado: {filename}")

print("Proceso completado.")