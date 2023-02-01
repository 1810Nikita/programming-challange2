#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import hashlib
import glob

#path for files
path=r"C:\AFiles"
all_files=glob.glob
def aggregate_tsv_files(input_files, output_file):
    # Create an empty dataframe to store the aggregated data
    aggregated_data = pd.DataFrame(columns=['Id', 'username', 'email', 'hashed_password', 'plaintext_password', 'ip'])
    
    # Loop through the input files
    for input_file in input_files:
        # Read the data from each file into a separate dataframe
        data = pd.read_csv(input_files, sep='\t')
        
        # Merge the data into the aggregated data dataframe
        aggregated_data = pd.concat([aggregated_data, data], ignore_index=True)
    
    # Remove duplicates based on the 'Id' column
    aggregated_data = aggregated_data.drop_duplicates(subset='Id', keep='first')
    
    # Hash the password and store the hashed version
    aggregated_data['hashed_password'] = aggregated_data['plaintext_password'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())
    
    # Drop the plaintext password from the dataframe
    aggregated_data.drop(columns=['plaintext_password'], inplace=True)
    
    # Write the aggregated data to the output file
    aggregated_data.to_csv(output_file, sep='\t', index=False)


# In[15]:


input_files = ["ip_1m.tsv", "plain_32m.tsv", "user_email_hash.1m.tsv"]
output_file = 'output.tsv'
aggregate_tsv_files(input_files, output_file)


# In[ ]:




