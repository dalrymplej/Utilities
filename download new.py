# Jun 10 2015
"""
Downloads and unzips a bunch of zip files in a specified directory
"""

import urllib2
import zipfile
from StringIO import StringIO
import shutil
import os
from ftplib import FTP

# Download latest csv files for Envision, and save them to a local directory.

directory_path = "C:\\Users\\haggertr\\Desktop\\Roy\\Research\\WW2100\\Research\\results2\\files\\"
#directory_path = "C:\\code\\data repository\\"
version = 'WW2100_1.0'

ftp = FTP('131.252.97.79')
ftp.login('anonymous')
ftp.cwd('WW2100/OutputData/'+version+'/')
filenames = ftp.nlst() # get filenames within the directory
try:
    filenames.remove('Ref_with_maps.zip')
except ValueError:
    pass
filenamescp = list(filenames)
for filen in filenamescp:
    if filen[-4:] != '.zip': filenames.remove(filen)
print filenames

for filen in filenames:
    response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/'+filen)
    zipdata = response.read()
    with zipfile.ZipFile(StringIO(zipdata), "r") as z:
        z.extractall(directory_path)

for dirname in os.listdir(directory_path):
    if dirname[0] is not '_' and "." not in dirname:
        for filename in os.listdir(directory_path+dirname):
            if filename[-4:]=='.csv' or filename[-5:]=='.xlsx' or filename[-4:]=='.txt':
                source = directory_path+dirname+"\\"+filename
                dest = directory_path+filename
                shutil.move(source,dest)
for filename in os.listdir(directory_path):
    if filename[-4] == '.png': os.remove(directory_path+filename)
