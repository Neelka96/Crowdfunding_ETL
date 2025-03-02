# %% [markdown]
# # ETL_Mini_Project

# %% [markdown]
# ## Setup

# %% [markdown]
# ### **Imports and Settings**

# %%
# Import dependencies
import pandas as pd
import numpy as np
from datetime import datetime as dt
import json

pd.set_option('max_colwidth', 400)

# %% [markdown]
# ### **Extract crowdfunding.xlsx Data**

# %%
# Read the data into a Pandas DataFrame
crowdfunding_info_df = pd.read_excel('../../Resources/Input/crowdfunding.xlsx')
crowdfunding_info_df.head()

# %%
# Get a brief summary of the crowdfunding_info DataFrame.
crowdfunding_info_df.info()

# %% [markdown]
# ## Category & Subcategory DFs

# %% [markdown]
# ---

# %% [markdown]
# **Create a Category DataFrame that has the following columns:**
# - A "category_id" column that is numbered sequential form 1 to the length of the number of unique categories.
# - A "category" column that has only the categories.
# 
# Export the DataFrame as a `category.csv` CSV file.
# 
# **Create a SubCategory DataFrame that has the following columns:**
# - A "subcategory_id" column that is numbered sequential form 1 to the length of the number of unique subcategories.
# - A "subcategory" column that has only the subcategories. 
# 
# Export the DataFrame as a `subcategory.csv` CSV file.

# %% [markdown]
# ### **Split Category Column in Two**

# %%
# Get the crowdfunding_info_df columns.
crowdfunding_info_df.columns

# %%
# Assign the category and subcategory values to category and subcategory columns.
crowdfunding_info_df[['category', 'subcategory']] = (
    crowdfunding_info_df['category & sub-category']
        .str.split(
            pat = '/'
            ,n = 1
            ,expand = True
        )
)

# %%
# Assign the category and subcategory values to category and subcategory columns.
crowdfunding_info_df.head()

# %% [markdown]
# ### **Get Distinct Categories**

# %%
# Get the unique categories and subcategories in separate lists.
categories = crowdfunding_info_df['category'].unique()
subcategories = crowdfunding_info_df['subcategory'].unique()

print(categories, '\n')
print(subcategories)

# %% [markdown]
# ### **Create IDs for Primary Key**

# %%
# Get the number of distinct values in the categories and subcategories lists.
print(f'Category Length:    {len(categories)}')
print(f'Subcategory Length: {len(subcategories)}')

# %%
# Create numpy arrays from 1-9 for the categories and 1-24 for the subcategories.
category_ids = np.arange(1, 10)
subcategory_ids = np.arange(1, 25)

print(category_ids)
print(subcategory_ids)

# %%
# Use a list comprehension to add "cat" to each category_id. 
cat_ids = [f'cat{num}' for num in category_ids]

# Use a list comprehension to add "subcat" to each subcategory_id.    
subcat_ids = [f'subcat{num}' for num in subcategory_ids]

print(cat_ids)
print(subcat_ids)

# %% [markdown]
# ### **Initialize New DataFrames**

# %%
# Create a category DataFrame with the category_id array as the category_id and categories list as the category name.
category_df = pd.DataFrame(
    {
        'category_id': cat_ids
        ,'category': categories
    }
)

# Create a category DataFrame with the subcategory_id array as the subcategory_id and subcategories list as the subcategory name. 
subcategory_df = pd.DataFrame(
    {
        'subcategory_id': subcat_ids
        ,'subcategory': subcategories
    }
)

# %%
category_df

# %%
subcategory_df

# %% [markdown]
# ### **Export as CSVs**

# %%
# Export categories_df and subcategories_df as CSV files.
category_df.to_csv('../../Resources/Output/category.csv', index = False)

subcategory_df.to_csv('../../Resources/Output/subcategory.csv', index = False)

# %% [markdown]
# ## Campaign DF

# %% [markdown]
# ----

# %% [markdown]
# **Create a Campaign DataFrame that has the following columns:**
# - The "cf_id" column.
# - The "contact_id" column.
# - The “company_name” column.
# - The "blurb" column is renamed as "description."
# - The "goal" column.
# - The "goal" column is converted to a `float` datatype.
# - The "pledged" column is converted to a `float` datatype. 
# - The "backers_count" column. 
# - The "country" column.
# - The "currency" column.
# - The "launched_at" column is renamed as "launch_date" and converted to a datetime format. 
# - The "deadline" column is renamed as "end_date" and converted to a datetime format.
# - The "category_id" with the unique number matching the “category_id” from the category DataFrame. 
# - The "subcategory_id" with the unique number matching the “subcategory_id” from the subcategory DataFrame.
# - And, create a column that contains the unique four-digit contact ID number from the `contact.xlsx` file.
#  
# 
# Then export the DataFrame as a `campaign.csv` CSV file.

# %% [markdown]
# ### **Setup from Copy**

# %%
# Create a copy of the crowdfunding_info_df DataFrame name campaign_df. 
campaign_df = crowdfunding_info_df.copy()
campaign_df.head()

# %% [markdown]
# ### **Renaming Columns**

# %%
# Rename the blurb, launched_at, and deadline columns.
campaign_df = campaign_df.rename(
    columns = {
        'blurb': 'description'
        ,'launched_at': 'launch_date'
        ,'deadline': 'end_date'
    }
)

campaign_df.head()

# %% [markdown]
# ### **Float Conversion**

# %%
# Convert the goal and pledged columns to a `float` data type.
campaign_df[['goal', 'pledged']] = \
    campaign_df[['goal', 'pledged']].astype(float)

campaign_df.head()

# %%
# Check the datatypes
campaign_df.dtypes

# %% [markdown]
# ### **Datetime Conversion**

# %% [markdown]
# Please note that the statement `from datetime import datetime as dt` has been moved to the top of the notebook

# %%
# Format the launched_date and end_date columns to datetime format
campaign_df[['launch_date', 'end_date']] = \
    campaign_df[['launch_date', 'end_date']].map(dt.fromtimestamp)

campaign_df.head()

# %%
category_df

# %% [markdown]
# ### **Merge with Cat/Subcat DFs**

# %%
# Merge the campaign_df with the category_df on the "category" column and 
# the subcategory_df on the "subcategory" column.
campaign_merged_df = (
    campaign_df
        .merge(
            category_df
            ,how = 'left'
            ,on = 'category'
        )
        .merge(
            subcategory_df
            ,how = 'left'
            ,on = 'subcategory'
        )
)

campaign_merged_df.tail(10)

# %% [markdown]
# ### **Column Drops**

# %%
# Drop unwanted columns
campaign_cleaned = campaign_merged_df.drop(
    columns = [
        'staff_pick'
        ,'spotlight'
        ,'category & sub-category'
        ,'category'
        ,'subcategory'
    ]
)
campaign_cleaned.head()

# %%
campaign_cleaned

# %% [markdown]
# ### **Export New DF as CSV**

# %%
# Export the DataFrame as a CSV file. 
campaign_cleaned.to_csv('../../Resources/Output/campaign.csv', index = False)

# %% [markdown]
# ## Contacts DF

# %% [markdown]
# ---

# %% [markdown]
# ### **Extract contacts.xlsx Data**

# %%
# Read the data into a Pandas DataFrame. Use the `header=2` parameter when reading in the data.
contact_info_df = pd.read_excel('../../Resources/Input/contacts.xlsx', header = 3)
contact_info_df.head()

# %% [markdown]
# ### **Create Contacts DataFrame**

# %% [markdown]
# ---

# %% [markdown]
# **Create a Contacts DataFrame that has the following columns:**
# - A column named "contact_id"  that contains the unique number of the contact person.
# - A column named "first_name" that contains the first name of the contact person.
# - A column named "last_name" that contains the first name of the contact person.
# - A column named "email" that contains the email address of the contact person
# 
# Then export the DataFrame as a `contacts.csv` CSV file.

# %% [markdown]
# ### **Using Pandas**
# 
# Please note that the statement `import json` has been moved to the top of the notebook

# %% [markdown]
# #### *Iterate through DF*

# %%
# Iterate through the contact_info_df and convert each row to a dictionary.
dict_values = []
for _, row in contact_info_df.iterrows():
    data = json.loads(row.iloc[0])
    values = [entry for entry in data.values()]
    dict_values.append(values)

# Print out the list of values for each row.
for dict in dict_values:
    print(dict)

# %% [markdown]
# #### *Setup DF*

# %%
# Create a contact_info DataFrame and add each list of values, i.e., each row 
# to the 'contact_id', 'name', 'email' columns.
contact_info = pd.DataFrame(
    data = dict_values
    ,columns = ['contact_id', 'name', 'email']
)
contact_info.head()

# %%
# Check the datatypes.
contact_info.info()

# %% [markdown]
# #### *Split Name into Two Columns*

# %%
# Create a "first"name" and "last_name" column with the first and last names from the "name" column. 
contact_info[['first_name', 'last_name']] = \
    contact_info['name'].str.split(' ', n = 1, expand = True)

# Drop the contact_name column
contact_info = contact_info.drop(columns = 'name')

contact_info.head(10)

# %% [markdown]
# #### *Reordering*

# %%
# Reorder the columns
contact_info = \
    contact_info[['contact_id', 'first_name', 'last_name', 'email']]

contact_info.head(10)

# %%
# Check the datatypes one more time before exporting as CSV file.
contact_info.info()

# %% [markdown]
# #### *Export as CSV*

# %%
# Export the DataFrame as a CSV file.   
contacts_df_clean = contact_info.copy()
contacts_df_clean.to_csv('../../Resources/Output/contacts.csv', index=False)


