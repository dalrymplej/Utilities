# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 21:50:40 2014
Modified for new ftp site 4/24/2015
Updated for v3.0 Jul 17 2016

@author: haggertr
"""

import urllib2
import zipfile
from StringIO import StringIO
import shutil
import os

# Download latest csv files for Envision, and save them to a local directory.

#directory_path = "C:\\Users\\haggertr\\Desktop\\Documents\\work - OSU\\research\\WW2100\\Research\\results2\\altFiles\\"
directory_path = "C:\\Users\\haggertr\\Desktop\\Roy\\Research\\WW2100\\Research\\results2\\Files\\"
version = 'WW2100_3.0'

response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/AllFallow.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
#response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/Extreme.zip')
#zipdata = response.read()
#with zipfile.ZipFile(StringIO(zipdata), "r") as z:
#    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/EconExtreme.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/FireSuppress.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
#response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/FullCostUrb.zip')
#zipdata = response.read()
#with zipfile.ZipFile(StringIO(zipdata), "r") as z:
#    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/HighClim.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/HighIrrig.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/HighPop.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)

#response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/HistoricHadGEM.zip')
#zipdata = response.read()
#with zipfile.ZipFile(StringIO(zipdata), "r") as z:
#    z.extractall(directory_path)
    
#response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/HistoricRef.zip')
#zipdata = response.read()
#with zipfile.ZipFile(StringIO(zipdata), "r") as z:
#    z.extractall(directory_path)
    
#response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/LateRefill.zip')
#zipdata = response.read()
#with zipfile.ZipFile(StringIO(zipdata), "r") as z:
#    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/LowClim.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/LowIrrig.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
            
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/Managed.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/NewInstream.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/NewIrrig.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/NoGrow.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)

#response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/NoIncGrowth.zip')
#zipdata = response.read()
#with zipfile.ZipFile(StringIO(zipdata), "r") as z:
#    z.extractall(directory_path)

response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/NoPopGrowth.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)

response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/NoReservoirs.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)

response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/Ref.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/StationaryClim.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('ftp://131.252.97.79/WW2100/OutputData/'+version+'/UrbExpand.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)

for dirname in os.listdir(directory_path):
    if dirname[0] is not '_':
        for filename in os.listdir(directory_path+dirname):
            if filename[-4:]=='.csv' or filename[-5:]=='.xlsx' or filename[-4:]=='.txt':
                source = directory_path+dirname+"\\"+filename
                dest = directory_path+filename
                shutil.move(source,dest)
