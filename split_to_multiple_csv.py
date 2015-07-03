# Roy Haggerty, Jun 11 2015
"""
script finds all csv files with name "HBV_Flows" and splits columns to individual files
"""
import os
import re
import pandas as pd
directory_path = "C:\\Users\\haggertr\\Desktop\\Roy\\Research\\WW2100\\Research\\results2\\Files\\"
#directory_path = "C:\\code\\data repository\\"
#directory_path = "C:\\Users\\haggertr\\Desktop\\Documents\\work - OSU\\research\\WW2100\\Research\\results2\\files\\"
scenarios_list = ['NoReservoirs']
basic_name = 'HBV_Flows_(m3_s)_Ref_Run0.csv'

# Find all scenarios with searchname ending with 'csv'
searchname = 'HBV_Flows_(m3_s)' 
scenarios_list = []
for filename in os.listdir(directory_path):
    if filename.startswith(searchname) and filename[-4:]=='.csv':
        match = re.search("(m3_s)", filename)  
        scenarios_list.append(filename[match.end()+2:-9])  # grabs part of name like 'HighClim' that comes after "(m3_s)"
#scenarios_list = ['NoReservoirs']
# split the searchname file into its columns and make those individual csv files
for scenario in scenarios_list:
    file_model_csv_w_path = directory_path + basic_name.replace('Ref', scenario)
    print '\n FILENAME = ', file_model_csv_w_path
    df = pd.read_csv(file_model_csv_w_path)
    new_file_list = list(df.columns.values)
    match = re.search("(m3_s)", file_model_csv_w_path)  
    file_name_end = file_model_csv_w_path[match.end()+1:-4]  # grabs part of name like '_HighClim_Run0' that comes after "(m3_s)"
    for new_file in new_file_list[1:9]:
        new_file2 = new_file.replace('/','_')
        new_file_name = directory_path + new_file2[1:].replace(' ','_') + file_name_end + '.csv'
        columns = [new_file]
        df.to_csv(new_file_name,columns=columns)
        print new_file_name
