## Data Sources

The project uses the following data sources:

1. Excel files containing ODD data located in `[ODD_DATA_FOLDER]`
2. Excel files containing ODN data located in `[ODN_DATA_FOLDER]`
3. Reference CSV files for mapping series to zones (if applicable):
   - `votos_por_barrio_pn_mapeado_odd.csv`
   - `votos_por_barrio_pn_mapeado_odn.csv`

## Project Structure

The project consists of Jupyter notebooks for each department:

1. `procesamiento de datos ODD [Department].ipynb`: Processes ODD data for a specific department
2. `procesamiento de datos ODN [Department].ipynb`: Processes ODN data for a specific department

Current departments:

- Montevideo
- Maldonado

## Data Processing Steps

For both ODD and ODN data in each department, the following steps are performed:

1. Read Excel files from the specified folders
2. Combine data from all files into a single DataFrame
3. Filter data for the specific department
4. Clean and transform the data:
   - Rename columns
   - Modify party names
   - Remove unnecessary columns
5. Add zone information based on the series (if applicable)
6. Save the processed data to CSV files

## Output Files

The project generates the following output files for each department:

1. `[department]_odd_dataset.csv`: Initial ODD data for the department
2. `[department]_odd_dataset_modificado.csv`: Cleaned ODD data
3. `[department]_odd_dataset_con_zona.csv`: Final ODD data with zone information (if applicable)
4. `[department]_odn_dataset.csv`: Initial ODN data for the department
5. `[department]_odn_dataset_modificado.csv`: Cleaned ODN data
6. `[department]_odn_dataset_con_zona.csv`: Final ODN data with zone information (if applicable)

## Usage

1. Ensure all required data files are in their respective folders
2. Update the `[ODD_DATA_FOLDER]` and `[ODN_DATA_FOLDER]` placeholders in the notebooks with the actual paths on your system
3. Open the Jupyter notebooks for the desired department in your preferred environment
4. Run all cells in each notebook to process the data
5. Check the output CSV files for the results

## Adding New Departments

To add a new department:

1. Create new Jupyter notebooks for ODD and ODN data processing, naming them according to the department
2. Update the data processing steps as needed, considering any department-specific requirements
3. Adjust the zone mapping process if applicable for the new department
4. Update this README to include the new department in the "Current departments" list
