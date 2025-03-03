# Crowdfunding ETL
`Project 2`  
`EdX(2U) & UT Data Analytics and Visualization Bootcamp`  
`Cohort UTA-VIRT-DATA-PT-11-2024-U-LOLC`  
By:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Manny Guevara**,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Neel Agarwal**,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Rob LaPreze**,  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Samora Machel**  

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Deliverables](#deliverables)
    - [Required Files](#required-files)
    - [Optional Enhancements](#optional-enhancements)
3. [Directory Structure](#directory-structure)
4. [System Requirements](#system-requirements)
5. [Installation & Setup](#installation--setup)
6. [ETL Process](#etl-process)
7. [Schema Creation & (Optional) Data Import](#schema-creation--optional-data-import)
8. [Regex Approach (Optional)](#regex-approach-optional)
9. [ERD Overview](#erd-overview)
10. [Usage Notes & Tips](#usage-notes--tips)
11. [Credits & Citations](#credits--citations)

---

## Project Overview  

This project is designed to showcase an end-to-end **Extract, Transform, and Load (ETL)** process for crowdfunding campaign data as part of the edX/2U Data Analytics Bootcamp.

The objectives of this project are:
1. **Extract** crowdfunding data from provided Excel spreadsheets.
2. **Transform** and clean the data into a relational database-friendly format.
3. **Load** the cleaned data into a PostgreSQL database using SQL scripts.

The project emphasizes reproducibility and scalability by providing optional automation through notebook-driven SQL generation, all while fulfilling the assignment rubric. It avoids GUI-based imports (like pgAdmin's CSV import tool) to maintain cross-environment compatibility, even though doing so would be a reasonable option as well.

---

## Deliverables  
### Required Files  
According to the project rubric, the following are required:  
- **`ETL_FINAL.ipynb`**: The main notebook that handles extraction, transformation, and CSV creation.  
- **`crowdfunding_db_schema.sql`**: Defines the database schema for the transformed data. Rough draft generated by `schema_writer.ipynb`.
- **`ERD.jpg`**: Visual representation of the Entity Relationship Diagram (ERD) of the database.  

### Optional Enhancements  
- **`schema_writer.ipynb`**: Automatically generates rough-draft SQL schema and fully-functional import statements to bulk upload CSV Files
- **`crowdfunding_db_import.sql`**: Optional script to bulk-load CSVs into the database using `COPY` commands. <ins>Not part of repo, but generated SQL code that comes from `schema_writer.ipynb` when all cells are run.</ins>

---

## Directory Structure

```plaintext
Crowdfunding_ETL/
│
├── ETL/
│   ├── Deliverables/
│   │   ├── crowdfunding_db_schema.sql (Required)
│   │   └── ETL_FINAL.ipynb (Required)
│   └── Extras/
│       ├── crowdfunding_db_import.sql (Generated/Optional)
│       ├── RAW_autoSchema.sql (Generated/NOT FOR USE)
│       └── schema_writer.ipynb (Optional)
│
├── Resources/
│   ├── Input/
│   │   ├── contacts.xlsx
│   │   └── crowdfunding.xlsx
│   └── Output/
│       ├── campaign.csv
│       ├── category.csv
│       ├── contacts.csv
│       └── subcategory.csv
│
├── .gitignore
├── ERD.jpg (Required)
└── README.md
```

---

## System Requirements

To successfully run this project, the following environment is recommended:

- **Operating System**: macOS, Windows, or Linux
- **Python Version**: 3.9 or higher
- **PostgreSQL**: Version 13 or higher
- **Required Python Libraries**:
    - `pandas`
    - `numpy`
    - `pathlib` (built-in)
    - `re` (built-in)
    - `json` (built-in)
    - `datetime` (built-in)
- **Jupyter Notebook**: For running `.ipynb` files (install via `pip install notebook` if needed)
- **PostgreSQL GUI (optional)**: pgAdmin 4 or any compatible interface
- **Disk Space**: Minimum 500 MB free
- **Memory (RAM)**: Minimum 4 GB recommended

Ensure PostgreSQL is installed and running before executing the SQL scripts.

---

## Installation & Setup

1. **Clone or download** this repository.
2. Ensure you have **Python 3.x** installed with **pandas**:
    ```bash
    pip install pandas numpy 
    # You should have ipykernel already, if not, install it
    pip install ipykernel
    ```
3. (Optional) Set up a virtual environment:
    ```bash
    cd YOUR/PATH/TO/REPO/HERE       # Move to your local repo

    python -m venv venv             # Create a new virtual env

    source venv/bin/activate        # Mac/Linux or with
    venv\Scripts\activate           # Windows

    pip install requirements.txt    # Install logged dependencies

    deactivate                      # Deactivate your virtual env
    ```
4. Now you're ready to move to the Jupyter Notebook view!

> [!TIP]  
> As you might've gathered, a helper filer to automate SQL code was written. It has the ability to generate a SQL file to bulk-upload CSV type files. Feel free to upload in any way that is easiest, but to create this file please run all cells in `schema_writer.ipynb`. 
---

## ETL Process

### 1. Extraction
- Decide on most efficient python based ETL tool.
- Install dependencies.
- Setup DataFrames so large rows of data can be read on-screen.
- Read in `crowdfunding.xlsx` and `contacts.xlsx` as DataFrames.  
- Quick look at data values, types, and structure before transformation to grasp what kind of database is being built. 

### 2. Transformation
Create four CSVs: `campaign.csv`, `contacts.csv`, `category.csv`, `subcategory.csv` by cleaning, editing, and normalizing data.  
- Split `"category & sub-category"` into separate `"category"` and `"subcategory"`:
    + `crowdfunding.xlsx` hold combined info that needed to be methodically separated
    + Create new identifiers for each entry in new tables to be linked with main table
    + Move into one new table for each along with unique identifiers
- Clean the `crowdfunding` (main) DataFrame and perform major edits:  
    + removing unnecessary sets from tables  
    + renaming/reordering columns to be more informative and match conventions  
    + merging to insert foreign key designations
    + standardizing data types for pandas ETL and SQL Schema  
- Mitigate bad input formatting to allow `contacts.xlsx` to be usable  
    + Select one of two methods to parse through the DataFrame created from `contacts.xlsx` (Pandas or Regular Expressions)
    + While both methods were completed for learning's sake and to measure efficiency, the Pandas method was selected for said reasoning.
    + Original Data was stored incorrectly using dictionary i.e. {} curly-brackets within excel, rendering the data unreadable by normal means.


### 3. Loading
- Create/connect to `crowdfunding_db` in PostgreSQL
- Add Schema into db using `crowdfunding_db_schema.sql`.
- Load data into db:
    - Using PostgreSQL's importing tool in the pgAdmin GUI
    - Using psql
    - Open `schema_writer.ipynb` and run all cells. Afterwards a `crowdfunding_db_import.sql` file can be found which can bulk-import CSV when run in pgAdmin 4.

While the basic requirements for this Project specify the inclusion of a schema file, the process of converting a pandas DataFrame into PostgreSQL Schema can be arduous and error-prone, so a helper notebook file was written to do most of the heavy lifting and data validation. Constraint edting, rounding up VARCHARs, and fixing DATE type in particular were done after the automatic building of the schema file. However, the bulk-imports that come from this helper file are fine to use if not even easier!

---

## Schema Creation & (Optional) Data Import  

> [!NOTE]  
> The `VARCHAR` lengths for variable fields (like `first_name`, `last_name`, `email`, `company_name`, and `description`) were determined by the maximum string lengths from the dataset. These lengths were **manually rounded up** to accommodate longer entries in future datasets, preventing any data truncation issues.  

### Example Table Creation  

#### RAW_autoSchema
```sql
CREATE TABLE campaign (
    cf_id INT
    ,contact_id INT 
    ,company_name VARCHAR(33) NOT NULL
    ,description VARCHAR(53) 
    ,goal DEC NOT NULL
    ,pledged DEC NOT NULL
    ,outcome VARCHAR(10) NOT NULL
    ,backers_count INT NOT NULL
    ,country CHAR(2) NOT NULL
    ,currency CHAR(3) NOT NULL
    ,launch_date CHAR(10) NOT NULL
    ,end_date CHAR(10) 
    ,category_id CHAR(4) 
    ,subcategory_id VARCHAR(8) 
);
```

#### crowdfunding_db_schema
```sql
CREATE TABLE campaign (
    cf_id INT
    ,contact_id INT 
    ,company_name VARCHAR(40) NOT NULL
    ,"description" VARCHAR(60)
    ,goal DEC NOT NULL
    ,pledged DEC NOT NULL
    ,outcome VARCHAR(10) NOT NULL
    ,backers_count INT NOT NULL
    ,country CHAR(2) NOT NULL
    ,currency CHAR(3) NOT NULL
    ,launch_date DATE NOT NULL
    ,end_date DATE
    ,category_id CHAR(4) 
    ,subcategory_id VARCHAR(8) 
    ,CONSTRAINT pk_cf_id 
        PRIMARY KEY (cf_id)
    ,CONSTRAINT fk_contact_id 
        FOREIGN KEY (contact_id) 
        REFERENCES contacts(contact_id)
    ,CONSTRAINT fk_cat_id 
        FOREIGN KEY (category_id) 
        REFERENCES category(category_id)
    ,CONSTRAINT fk_subcat_id 
        FOREIGN KEY (subcategory_id) 
        REFERENCES subcategory(subcategory_id)
);
```

### Example Import (Optional)
```sql
COPY 
    campaign
FROM 
    '/your/local/path/Resources/Output/campaign.csv'
DELIMITER ',' CSV HEADER;
```

### Usage
```sql
\i crowdfunding_db_schema.sql
-- Optional:
\i crowdfunding_db_import.sql
```

---

## Regex Approach (Optional)

An alternative method explored involved using **regular expressions** to extract fields from semi-structured text. This was ultimately replaced by pandas-based logic for efficiency.

### Example Regex Parsing
```python
import re

pattern_id = r'\d{4}'
pattern_email = r'"email": "(.+)"'
pattern_name = r'(\w+\s\w+)'

for row in contact_info_df['raw_data_column']:
    found_id = re.search(pattern_id, row).group()
    found_email = re.search(pattern_email, row).group(1)
    found_name = re.search(pattern_name, row).group()
```

---

## ERD Overview

<img src="../ERD.jpg" alt="ERD_JPEG" width="1000"/>

### Normalization:

This database schema follows **normalization** principles to minimize redundancy, maintain data integrity, and ensure scalability. By splitting data into tables like `category`, `subcategory`, `contacts`, and `campaign`, we:
- Reduce repeated data entries.
- Simplify updates to shared information.
- Improve database performance.

For example:
- Categories and subcategories are separated to prevent repeated text entries in multiple campaigns.
- Contacts are stored independently to link multiple campaigns to a single contact entry.

### Relationships:
- `campaign.contact_id` → `contacts.contact_id`
- `campaign.category_id` → `category.category_id`
- `campaign.subcategory_id` → `subcategory.subcategory_id`

---

## Usage Notes & Tips

- Update file paths if moving files.
- Enhance the schema with constraints as needed.
- Regenerate schema with `schema_writer.ipynb` if CSV structures change.

---

## Credits & Citations

1. **Collaborators**:  
    - *Manny Guevara*  
    - *Neel Agarwal*  
    - *Rob LaPreze*  
    - *Samora Machel*  
2. **Starter Code & Data**: Provided by **UT/edX/2U Data Analytics Bootcamp**.
3. **README.md**: Created using OpenAI's [ChatGPT LLM](https://www.chatgpt.com), trained using prior READMEs, all the deliverables, and the provided rubric given by edX/2U  
4. **PostgreSQL Docs**: [postgresql.org/docs](https://www.postgresql.org/docs/)
5. **pandas Docs**: [pandas.pydata.org/docs](https://pandas.pydata.org/docs)

---