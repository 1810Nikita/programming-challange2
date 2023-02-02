#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
df = pd.read_csv(r"C:\\AFiles\\plain_32m.tsv", sep="\t", header=None, names=["email", "plaintext_password"])


# In[13]:


from pandas import read_csv

df = pd.read_csv(r"C:\\AFiles\\plain_32m.tsv", sep="\t")
df.columns = ["email", "plaintext_password"]
df.to_csv('test_2.tsv')


# In[7]:


import pandas as pd

# Load  file into a pandas dataframe
user_email = pd.read_csv(r"C:\\AFiles\\user_email_hash.1m.tsv", sep="\t", usecols=["email", "id", "username", "password"])


ip = pd.read_csv(r"C:\\AFiles\\ip_1m.tsv", sep="\t", usecols=["id", "ip_address"])


plain_text = pd.read_csv(r"C:\\AFiles\\plain_32m.tsv", sep="\t", usecols=['email', 'plaintext_password'])

# Create a dictionary for storing ip data based on id
ip_dict = ip.set_index('id').to_dict()['ip_address']

# Create a dictionary for storing user email data based on email
user_email_dict = user_email.set_index('email').to_dict()

# Create a list for storing the final result
result = []

# Loop through each record in the plain_text dataframe
for i, row in plain_text.iterrows():
    email = row["email"]
    
    # Check if the email exists in the user_email_dict
    if email in user_email_dict["email"]:
        # Extract the id from user_email_dict
        id = user_email_dict["email"][email]
        
        # Retrieve the corresponding ip from the ip_dict
        user_ip = ip_dict[id]
        
        # Extract the username and hashed_password from user_email_dict
        username = user_email_dict["username"][email]
        hashed_password = user_email_dict["password"][email]
        
        # Extract the plaintext_password from plain_text dataframe
        plaintext_password = row["plaintext_password"]
        
        # Append the final result to the result list
        result.append([id, username, email, password, plaintext_password, user_ip])

# Write the final result to an output file in TSV format
result_df = pd.DataFrame(result, columns=["Id", "Username", "Email", "Hashed_Password", "Plaintext_Password", "IP"])
result_df.to_csv("output.tsv", sep="\t", index=False)






