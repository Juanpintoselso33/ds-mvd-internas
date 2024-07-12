## Data Sources

The project uses the following data sources:

1. Excel files containing ODD data located in `[ODD_DATA_FOLDER]`
2. Excel files containing ODN data located in `[ODN_DATA_FOLDER]`
3. Reference CSV files for mapping series to zones:
   - `votos_por_barrio_pn_mapeado_odd.csv`
   - `votos_por_barrio_pn_mapeado_odn.csv`

## Project Structure

The project consists of two main Jupyter notebooks:

1. `procesamiento de datos ODD.ipynb`: Processes ODD data
2. `procesamiento de datos ODN.ipynb`: Processes ODN data

## Data Processing Steps

For both ODD and ODN data, the following steps are performed:

1. Read Excel files from the specified folders
2. Combine data from all files into a single DataFrame
3. Filter data for the Montevideo department
4. Clean and transform the data:
   - Rename columns
   - Modify party names
   - Remove unnecessary columns
5. Add zone information based on the series
6. Save the processed data to CSV files

## Output Files

The project generates the following output files:

1. `montevideo_odd_dataset.csv`: Initial ODD data for Montevideo
2. `montevideo_odd_dataset_modificado.csv`: Cleaned ODD data
3. `montevideo_odd_dataset_con_zona.csv`: Final ODD data with zone information
4. `montevideo_odn_dataset.csv`: Initial ODN data for Montevideo
5. `montevideo_odn_dataset_modificado.csv`: Cleaned ODN data
6. `montevideo_odn_dataset_con_zona.csv`: Final ODN data with zone information

## Usage

1. Ensure all required data files are in their respective folders
2. Update the `[ODD_DATA_FOLDER]` and `[ODN_DATA_FOLDER]` placeholders in the notebooks with the actual paths on your system
3. Open the Jupyter notebooks in your preferred environment
4. Run all cells in each notebook to process the data
5. Check the output CSV files for the results
