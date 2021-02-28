import pandas as pd

#Source file
path_to_excel_file = 'source/Beispiel-Mappe.xlsx'


#Read excel file, extract the sheet named "Namen"
read_file = pd.read_excel (path_to_excel_file, sheet_name="Namen")


#Saving all columns to item arrays in json file

#Target file
path_of_target_file = 'target/Namen-items-array-by-column.json'

#Save the extracted table to json
read_file.to_json (path_of_target_file)



#Saving all rows to object arrays in json file

#Target file
path_of_target_file = 'target/Namen-items-array-by-row.json'

#Save the extracted table to json
read_file.to_json (path_of_target_file, orient="records")