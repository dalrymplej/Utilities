# Roy Haggerty, Jun 11 2015
"""
script finds all csv files with name "HBV_Flows" and splits columns to individual files
"""
import os
import re
from shutil import copyfile
directory_path = "C:\\Users\\haggertr\\Desktop\\Roy\\Research\\WW2100\\Research\\results2\\Files\\"
new_directory = directory_path + 'muni\\'
#directory_path = "C:\\code\\data repository\\"
#directory_path = "C:\\Users\\haggertr\\Desktop\\Documents\\work - OSU\\research\\WW2100\\Research\\results2\\files\\"
s_trm1 = 'AltWaterMaster_Daily_Metrics'
s_trm2 = 'Ref'
s_trm3 = 'junk'
# Find all scenarios with searchname ending with 'csv'
files_list = []
for filename in os.listdir(directory_path):
    if (s_trm1 in filename and \
        (s_trm2 in filename or s_trm3 in filename)) \
        and filename[-4:]=='.csv':
        copyfile(directory_path+filename, new_directory+filename)
        print filename
