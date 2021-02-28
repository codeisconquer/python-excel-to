import pandas as pd

#Source file
path_to_excel_file = 'source/Beispiel-Mappe.xlsx'
#Target file
path_of_target_file = 'target/Namen.csv'

#Read excel file, extract the sheet named "Namen"
read_file = pd.read_excel (path_to_excel_file, sheet_name="Namen")
#Save the extracted table to csv
read_file.to_csv (path_of_target_file, index = None, header=True)