import pandas as pd
import os
from datetime import datetime
from typing import List

# Specify the directory containing the .xlsx files
directory = './dataset'

# Get a list of all .xlsx files in the directory
files = [file for file in os.listdir(directory) if file.endswith('.xlsx')]
files.sort()
#files = files[0:1]


# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate over each file
for file in files:
    # Read the .xlsx file
    filepath = os.path.join(directory, file)
    data = pd.read_excel(filepath, sheet_name=1)  # Assuming the target table is in the 2nd sheet
    
    # Get the header row and set it as the column names
    column_names = data.iloc[0].tolist()  # Assuming the header is in the 2nd row
    data = data[1:]  # Skip the header row
    data.columns = column_names
    #print(data.columns)
    
    # Get the index column and set it as the index of the DataFrame
    index_column = data.columns[0]  # Assuming the index is in the 2nd column
    data.set_index(index_column, inplace=True)
    
    # Extract prefecture number, prefecture name, and year-month from the file name
    filename = os.path.splitext(file)[0]  # Remove the file extension
    
    #Show pref and date    
    print(filename)
    

    # Read Sheet2 for lookup
    sheet2 = pd.read_excel(filepath, sheet_name=0, header=None, skiprows=4)  # Assuming the lookup data is in the 1st sheet and starts at B3

    sheet2[11] = pd.TimedeltaIndex(sheet2[11].astype(int), unit='d') + datetime(1900, 1, 1)

    # Perform the lookup and add the desired columns from Sheet1 to the merged dataset
    data['新規認定日'] = data['設備ID'].map(sheet2.set_index(1)[11]).fillna('')
    data['運転開始報告年月'] = data['設備ID'].map(sheet2.set_index(1)[12]).fillna('')
    data['調達期間終了年月'] = data['設備ID'].map(sheet2.set_index(1)[17]).fillna('')
    

    parts = filename.split('_')  # Split the file name by underscore
    pref_num, pref_name = parts[0].split('.')  # Split the first part by dot to get pref_num and pref_name
    year_month = parts[1]  # Get the year-month part
    
    # Add columns for prefecture number, prefecture name, and year-month
    data['pref_num'] = pref_num
    data['pref_name'] = pref_name
    data['year_month'] = year_month

    data.head(2)
    
    # Merge the data with the existing dataset
    merged_data = pd.concat([merged_data, data])  
      
    ## Append the data to the merged dataset
    #merged_data = merged_data.append(data)
        
# Print the merged dataset
print(merged_data.head(5))
print(merged_data.info())

# Sace the merged dataset
print("saved csv:", merged_data.to_csv("merged_data_" + year_month + ".csv", header = True, index=False))
