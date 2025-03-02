# %% [markdown]
# # Auto Schema Writer

# %% [markdown]
# ---

# %% [markdown]
# The purpose of this Notebook is to automate the tedious process of writing the code for the Entity Relationship Diagram and the PostgreSQL schema creation. This is all to fulfill the requirements of the Project 2 Crowdfunding_ETL assignment, as a more streamlined way of doing so all in one file would be with SQL Alchemy as opposed to creating text output to be copy and pasted or written to a file!
# 
# In this case I chose the latter just to show how easy it is to write something that auto generates a SQL script to write as necessary.  
# Some of this was a little hardcoded but that was due to the lack of this being a sufficiently complex repository/project to warrant that.

# %%
from pathlib import Path
import pandas as pd

# %% [markdown]
# ## f(x): Schema Writer
# ---
# A generator function that is used to read the new CSV files and return schemas for each one.  
# Can be used to create both the ERD code for QuickDraw or for the PostgreSQL schema creation itself.  
# 
# The results returned are simply to help ensure integrity in the results transferred to pgAdmin 4, as opposed to less calculated methods.  
# After copying and pasting only slight modifications and Primary/Foreign Key constraints are required.

# %%
def schema_info(
        path_suffix: str
        ,start: int = None
        ,stop: int = None
        ,root: str = '../../Resources/Output'
    ):
    type_map = {
        'int64': 'INT'
        ,'float64': 'DEC'
        ,'object': 'CHAR'
    }
    path = f'{root}/{path_suffix}.csv'
    df = pd.read_csv(path)

    columns = [*df.columns]
    for col in columns[start:stop]:
        counts = df[col].astype(str).str.len()
        min = counts.min()
        max = counts.max()
        _type = type_map[df[col].dtype.name]
        if _type == 'CHAR':
            if min != max:
                _type = 'VARCHAR'
            result = f'{col} {_type}({max})'
        else:
            result = f'{col} {_type}'
        yield result

# %% [markdown]
# ### ERD Code for Quick Draw

# %%
csv_files = ['campaign', 'contacts', 'category', 'subcategory']

for csv in csv_files:
    print(
        f'{csv}\n' +
        '-'
    )
    for col in schema_info(csv):
        print(col)
    print()

# %% [markdown]
# ### PostgreSQL Schema Code

# %%
csv_files = ['contacts', 'category', 'subcategory', 'campaign']

db_schema_lines = ['-- Schema Creation and Validation\n']

db_schema_lines += \
    [f'DROP TABLE IF EXISTS {csv} CASCADE;\n' for csv in csv_files]
db_schema_lines += '\n'

for csv in csv_files:
    db_schema_lines.append(
        f'CREATE TABLE {csv} (\n' +
        f'    {next(schema_info(csv))}\n'
    )
    for col in schema_info(csv, 1):
        constr = ''
        cond1 = col.find('end_date') != -1
        cond2 = col.find('description') != -1
        cond3 = col.find('id') == -1
        if cond1 or cond2:
            pass
        elif cond3: 
            constr = 'NOT NULL'
        db_schema_lines.append(f'    ,{col} {constr}\n')
    db_schema_lines.append(
        ');\n\n' +
        f'SELECT * FROM {csv};\n\n'
    )

db_schema_lines.append('\n-- CSV Import Validation\n')
db_schema_lines += [f'SELECT * FROM {csv};\n' for csv in csv_files]
db_schema_lines += '\n'

# %%
for line in db_schema_lines[:15]:
    print(line)

# %%
with open('TEST_autoSchema.sql', 'w') as sql:
    sql.writelines(db_schema_lines)

# %% [markdown]
# ---

# %% [markdown]
# ---

# %% [markdown]
# ## f(x): CSV Import Writer
# When used, generates statements in SQL that can be copied and pasted into a `.sql` file in the `crowdfunding_db` after cloning repository.  
# Must be run after after `schema_info()` has been utilized to create a schema and added to `crowdfunding_db` as well.

# %%
def import_info(sortBy: list, parent_path: str = '../../Resources/Output'):
    dir_path = sorted(
        [*Path(parent_path).resolve().iterdir()]
        ,key = lambda path: sortBy.index(path.stem)
    )
    for count, csv in enumerate(dir_path, 1):
        result = (
            f"-- ({count})\n" +
            "COPY\n" +
            f"    {csv.stem}\n" +
            "FROM\n" +
            f"    '{csv}'\n" +
            "DELIMITER ',' CSV HEADER;\n\n"
        )
        yield result

# %% [markdown]
# ### PostgreSQL Import Code

# %%
csv_files = ['contacts', 'category', 'subcategory', 'campaign']
db_import_lines = ['-- Local CSV POSIX Path from Drive\n']
db_import_lines.append('-- Written from schema_writer.ipynb safely\n\n')
db_import_lines += [sql_stmt for sql_stmt in import_info(sortBy = csv_files)]

# %%
for line in db_import_lines:
    print(line)

# %%
with open('TEST_autoImport.sql', 'w') as sql:
    sql.writelines(db_import_lines)


