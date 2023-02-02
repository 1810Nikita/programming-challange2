#!/usr/bin/env python
# coding: utf-8

# In[43]:


import numpy as np
import pandas as pd
import glob
import os


# In[24]:


file_dir = 'C:\AFiles'
get_ipython().system('ls $file_dir')


# In[19]:


get_ipython().system('ls $file_dir | wc -l')


# In[29]:


files = glob.glob(os.path.join(file_dir, "*.tsv"))


# In[39]:


output_file = 'output.tsv'


# In[31]:


os.chdir(r'C:\AFiles')
df1 = pd.read_csv(files[0],sep='\t')
df2 = pd.read_csv(files[1],sep='\t')
df3 = pd.read_csv(files[2],sep='\t')

print(df1.head(), "\n")
print(df2.head(), "\n")
print(df3.head(), "\n")


# In[ ]:


pd.head()


# In[33]:


aggregated_data = pd.DataFrame(columns=['Id', 'username', 'email', 'hashed_password', 'plaintext_password', 'ip'])


# In[41]:



    aggregated_data = pd.concat([aggregated_data, data], ignore_index=True)
    
    # Remove duplicates based on the 'Id' column
    aggregated_data = aggregated_data.drop_duplicates(subset='Id', keep='first')
    
    

    
    # Write the aggregated data to the output file
    aggregated_data.to_csv(output_file, sep='\t', index=False)


# In[42]:


df.head()


# In[ ]:




