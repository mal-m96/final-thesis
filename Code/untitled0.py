# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:03:22 2021

@author: Miguel Madeira
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import gzip

df = pd.read_table("SNV/MANIFEST.TXT")
fileslist = []

for file_name in df[0:33]["filename"]:
    fileslist.append(file_name)
print(fileslist[0])
f = gzip.open("SNV/"+fileslist[0],"rb")
print(f)
for line in gzip.open("SNV/"+fileslist[0], "rt"):
    print(line)