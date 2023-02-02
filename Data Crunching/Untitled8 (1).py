#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv, glob

Dir = r"C:\AFiles"
Avg_Dir = r"C:\AFiles\output"

tsv_file_list = glob.glob(os.path.join(Dir, '*.tsv')) 
print (tsv_file_list)

with open(os.path.join(Avg_Dir, 'Output.tsv'), 'w', newline='') as f:
    wf = csv.writer(f,delimiter='\t', lineterminator='\n')

    for files in tsv_file_list:
        with open(files, 'r') as r: 
            next(r)                   
            rr = csv.reader(r, )
            for row in rr:
                wf.writerow(row)


# In[9]:


import pandas as pd
import numpy as np
data=pd.read_csv('C:\AFiles\output\output.tsv', delimiter=",", encoding='utf-8')
data.head(5)


# In[5]:


import pandas as pd
data=pd.read_csv('C:\AFiles\output\output.tsv',sep='\t')
data.head()


# In[ ]:




