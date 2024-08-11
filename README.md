# Uruguay Electoral Data Processing

This project processes electoral data for the Órgano Deliberativo Departamental (ODD) and Órgano Deliberativo Nacional (ODN) in Uruguay. It provides a set of tools to clean, transform, and analyze voting data for different departments.

## Table of Contents

1. [Data Sources](#data-sources)
2. [Project Structure](#project-structure)
3. [Data Processing Steps](#data-processing-steps)
4. [Output Files](#output-files)
5. [Setup and Usage](#setup-and-usage)
6. [Adding New Departments](#adding-new-departments)
7. [GeoJSON Processing](#geojson-processing)
8. [Dependencies](#dependencies)
9. [Credits](#credits)

## Data Sources

The project uses the following data sources:

1. Excel files containing ODD data located in `data/raw/results/ODD`
2. Excel files containing ODN data located in `data/raw/results/ODN`
3. JSON files for mapping series to zones located in `maps/zonasxseries`

## Project Structure

The project consists of the following key components:

1. Jupyter notebooks for data processing:

   - `notebooks/ODD/data_processing_notebook_ODD.ipynb`: Processes ODD data for all departments
   - `notebooks/ODN/data_processing_notebook_ODN.ipynb`: Processes ODN data for all departments
   - `notebooks/mapas/add_zones_to_geojson.ipynb`: Adds zone information to GeoJSON files

2. Python scripts for GeoJSON preparation:

   - `scripts/convert_to_geojson_by_depto.py`: Converts the original shapefile to separate GeoJSON files for each department
   - `scripts/convert_to_geojson.py`: Converts the original shapefile to a single GeoJSON file

3. Mapping files:
   - JSON files in `maps/zonasxseries/` containing manual mappings of series to zones for each department

Currently supported departments:

- Montevideo
- Maldonado
- Colonia
- Treinta y Tres

## Data Processing Steps

The data processing involves several steps:

1. Prepare GeoJSON files:
   - Run `scripts/convert_to_geojson_by_depto.py` to create separate GeoJSON files for each department
2. Add zone information to GeoJSON:
   - Run `notebooks/mapas/add_zones_to_geojson.ipynb` to incorporate zone information into the GeoJSON files
3. Process ODD and ODN data:
   - Use the respective notebooks to clean and transform the data

For both ODD and ODN data in each department, the following steps are performed:

1. Read Excel files from the specified folders
2. Combine data from all files into a single DataFrame
3. Filter data for the specific department
4. Clean and transform the data:
   - Rename columns
   - Modify party names
   - Remove unnecessary columns
5. Add zone information based on the series codes
6. Save the processed data to CSV files at various stages

## Output Files

The project generates the following output files for each department:

1. `data/processed/ODD/[department]/[department]_odd_filtered.csv`: Initial filtered ODD data
2. `data/processed/ODD/[department]/[department]_odd_cleaned.csv`: Cleaned ODD data
3. `data/final/odd/[department]/[department]_odd_final.csv`: Final ODD data with zone information
4. `data/processed/ODN/[department]/[department]_odn_filtered.csv`: Initial filtered ODN data
5. `data/processed/ODN/[department]/[department]_odn_cleaned.csv`: Cleaned ODN data
6. `data/final/odn/[department]/[department]_odn_final.csv`: Final ODN data with zone information
7. `maps/deptosconzona/[department]_con_zona.geojson`: GeoJSON file with added zone information

## Setup and Usage

1. Ensure all required data files are in their respective folders:
   - ODD data in `data/raw/results/ODD`
   - ODN data in `data/raw/results/ODN`
   - Mapping files in `maps/zonasxseries`
   - Original shapefile in the project root directory
2. Install the required dependencies (see [Dependencies](#dependencies) section)
3. Run the GeoJSON preparation scripts:
   - `python scripts/convert_to_geojson_by_depto.py`
4. Open the Jupyter notebooks in your preferred environment:
   - `notebooks/ODD/data_processing_notebook_ODD.ipynb` for ODD data
   - `notebooks/ODN/data_processing_notebook_ODN.ipynb` for ODN data
   - `notebooks/mapas/add_zones_to_geojson.ipynb` for adding zones to GeoJSON files
5. Update the `department` variable in the notebooks to process data for different departments
6. Run all cells in each notebook to process the data
7. Check the output files in the respective folders for the results

## Adding New Departments

To add a new department:

1. Ensure you have the necessary Excel files for the new department in the ODD and ODN data folders
2. Create a new JSON mapping file in `maps/zonasxseries` if the department requires zone mapping
3. Update the `department` variable in the notebooks to include the new department name
4. Run the notebooks with the new department to generate the processed data
5. Update this README to include the new department in the "Currently supported departments" list

## GeoJSON Processing

The project includes steps to process GeoJSON files and add zone information:

1. Initial GeoJSON creation:

   - The script `scripts/convert_to_geojson_by_depto.py` converts the original shapefile into separate GeoJSON files for each department, stored in `maps/deptos/`.

2. Adding zones to GeoJSON:
   - The notebook `notebooks/mapas/add_zones_to_geojson.ipynb` reads the GeoJSON files created in step 1.
   - It uses the manually created mappings in `maps/zonasxseries/` to add zone information to each feature in the GeoJSON.
   - The resulting GeoJSON files with zone information are saved in `maps/deptosconzona/`.

This process enriches the geographical data with zone information, which is crucial for further analysis and visualization.

## Dependencies

This project requires the following Python libraries:

- pandas
- numpy
- geopandas
- os
- json

Ensure these libraries are installed in your Python environment before running the scripts and notebooks.

## Credits

Both the data for the results of the ODD and ODN elections and the shapefile for the geographic data was provided by the [Corte Electoral de la Republica Oriental del Uruguay](https://www.gub.uy/corte-electoral/).
