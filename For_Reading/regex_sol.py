import pandas as pd
import re

# Create a New Copy
contact_info_df = pd.read_excel('../../Resources/Input/contacts.xlsx', header = 3)
contact_info_df_copy = contact_info_df.copy()
contact_info_df_copy.head()


# The following are all methods that can be used for extracting data:

# re.findall(pattern, string)
# re.search(pattern, string)
# re.split(pattern, string)


# Regex for 4-Digit ID Number

# Extract the four-digit contact ID number.
contacts = contact_info_df_copy.values
pattern = r'\d+'

contact_ids = [re.findall(pattern, contact[0])[0] for contact in contacts]

contact_info_df_copy['contact_id'] = contact_ids
contact_info_df_copy.head()



# Check the datatypes.
contact_info_df_copy.info()


# Note: This step could've been done before adding values to df
# Convert the "contact_id" column to an int64 data type.
contact_info_df_copy['contact_id'] = contact_info_df_copy['contact_id'].astype(int)
contact_info_df_copy.info()


# Regex for Name
# Extract the name of the contact and add it to a new column.
pattern = r'\w+\s\w+'

names = [re.findall(pattern, contact[0])[0] for contact in contacts]

contact_info_df_copy['name'] = names
contact_info_df_copy.head(10)


# **Please note** that the later step of splitting up the name into `first_name` and `last_name`   
# could've and perhaps szould've been done during the extraction of the name with the following code:

first_names = [re.findall(r'(\w+)(?:\s)', contact[0])[0] for contact in contacts]
last_names = [re.findall(r'(?:\w\s)(\w+)', contact[0])[0] for contact in contacts]

contact_info_df_copy['first_name'] = first_names
contact_info_df_copy['last_name'] = last_names


# Regex for Email

# Extract the email from the contacts and add the values to a new column.
pattern = r'(?:"email": ")(.+)(?:")'

emails = [re.findall(pattern, contact[0])[0] for contact in contacts]

contact_info_df_copy['email'] = emails
contact_info_df_copy.head(10)


# Create Copy - Only New Fields

# Create a copy of the contact_info_df with the 'contact_id', 'name', 'email' columns.
contact_info_df_copy = \
    contact_info_df_copy[['contact_id', 'name', 'email']].copy()

contact_info_df_copy.head(10)


# Regex for Splitting Name
# (Could have been done while extracting name as explained previously)

# Create a "first"name" and "last_name" column with the first and last names from the "name" column. 
contact_info_df_copy[['first_name', 'last_name']] = \
    contact_info_df_copy['name'].str.split(r'\s', n = 1, expand = True)

# Drop the contact_name column
contact_info_df_copy = contact_info_df_copy.drop(columns = 'name')

contact_info_df_copy.head(10)


# Reordering

# Reorder the columns
contact_info_df_copy = \
    contact_info_df_copy[['contact_id', 'first_name', 'last_name', 'email']]

contact_info_df_copy.head(10)


# Finalizing New DF

# Check the datatypes one more time before exporting as CSV file.
contact_info_df_copy.info()

# Export the DataFrame as a CSV file. 
contacts_df_clean = contact_info_df_copy.copy()
contacts_df_clean.to_csv('Resources/Output/contacts.csv', encoding = 'utf8', index = False)
