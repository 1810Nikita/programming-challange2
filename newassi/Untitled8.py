#!/usr/bin/env python
# coding: utf-8

# In[21]:


import csv
import os

# Define the folder path
path = r'C:\AFiles'


# Get all the files in the folder
all_files = os.listdir(path)

# Define the file extension you want to filter by
file_extension = '.tsv'

# Filter the files by the specified file extension
filtered_files = [f for f in all_files if f.endswith(file_extension)]

# Print the filtered files
print(filtered_files)


# list to hold contents of all files
all_rows = []




for filename in filtered_files :
    with open( path,filename,'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            all_rows.append(ch(row))

# write combined data to a new file
with open('combined_file.tsv', 'w') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(all_rows)


# In[ ]:




