# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 21:50:40 2014

@author: haggertr
"""

import urllib2
import zipfile
from StringIO import StringIO

# Download latest csv files for Envision, and save them to a local directory.

#directory_path = "C:\\Users\\haggertr\\Desktop\\Documents\\work - OSU\\research\\WW2100\\Research\\results2\\files\\"
directory_path = "C:\\Users\\haggertr\\Desktop\\Roy\\Research\\WW2100\\Research\\results2\\files\\"

response = urllib2.urlopen('http://envision.bioe.orst.edu/StudyAreas/WW2100/Outputs/Ref/Model_Outputs_Ref_Run0.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('http://envision.bioe.orst.edu/StudyAreas/WW2100/Outputs/LowClim/Model_Outputs_LowClim_Run0.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('http://envision.bioe.orst.edu/StudyAreas/WW2100/Outputs/HighClim/Model_Outputs_HighClim_Run0.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('http://envision.bioe.orst.edu/StudyAreas/WW2100/Outputs/FireSuppress/Model_Outputs_FireSuppress_Run0.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('http://envision.bioe.orst.edu/StudyAreas/WW2100/Outputs/UrbExpand/Model_Outputs_UrbExpand_Run0.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)

response = urllib2.urlopen('http://envision.bioe.orst.edu/StudyAreas/WW2100/Outputs/HighPop/Model_Outputs_HighPop_Run0.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
response = urllib2.urlopen('http://envision.bioe.orst.edu/StudyAreas/WW2100/Outputs/FullCostUrb/Model_Outputs_FullCostUrb_Run0.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
#response = urllib2.urlopen('http://envision.bioe.orst.edu/StudyAreas/WW2100/Outputs/EarlyReFill/Model_Outputs_EarlyReFill_Run0.zip')
#zipdata = response.read()
#with zipfile.ZipFile(StringIO(zipdata), "r") as z:
#    z.extractall(directory_path)
    
response = urllib2.urlopen('http://envision.bioe.orst.edu/StudyAreas/WW2100/Outputs/Extreme/Model_Outputs_Extreme_Run0.zip')
zipdata = response.read()
with zipfile.ZipFile(StringIO(zipdata), "r") as z:
    z.extractall(directory_path)
    
#response = urllib2.urlopen('http://envision.bioe.orst.edu/StudyAreas/WW2100/Outputs/Historic/Model_Outputs_Historic_Run0.zip')
#zipdata = response.read()
#with zipfile.ZipFile(StringIO(zipdata), "r") as z:
#    z.extractall(directory_path)
