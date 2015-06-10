
import pandas as pd
#directory_path = "C:\\Users\\haggertr\\Desktop\\Roy\\Research\\WW2100\\Research\\results2\\Files\\"
#directory_path = "C:\\Users\\haggertr\\Desktop\\test\\"
directory_path = "C:\\Users\\haggertr\\Desktop\\Documents\\work - OSU\\research\\WW2100\\Research\\results2\\files\\"
scenarios_list = ['HighClim']
basic_name = 'HBV_Flows_(m3_s)_Ref_Run0.csv'

for scenario in scenarios_list:
    file_model_csv_w_path = directory_path + basic_name.replace('Ref', scenario)
    df = pd.read_csv(file_model_csv_w_path)
    new_file_list = list(df.columns.values)
    for new_file in new_file_list[1:9]:
        new_file2 = new_file.replace('/','_')
        new_file_name = directory_path + new_file2[1:].replace(' ','_') + '.csv'
        columns = [new_file]
        df.to_csv(new_file_name,columns=columns)
        print new_file_name
assert False