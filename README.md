# programming-challange2



Read the data from each of the input TSV files into a pandas dataframe.
Merge the dataframes into a single dataframe, ensuring that each row has unique ID.
Generate a new column for the hashed password and plaintext password.
Write the final dataframe to a new TSV file with the required columns.
It is important to note that the hashed password and plaintext password should not be stored in the output file for security reasons. Instead, consider using a secure hashing algorithm to hash the password and store only the hashed version.
Aggregate the data as needed (e.g. grouping by username, summing values, etc.).
Write the aggregated data to a new TSV file with the specified fields (Id, username, email, hashed_password, plaintext_password, ip).
