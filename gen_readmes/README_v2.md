# Project 2: Crowdfunding ETL

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Required Deliverables](#required-deliverables)  
3. [Directory Structure](#directory-structure)  
4. [Installation & Setup](#installation--setup)  
5. [ETL Process](#etl-process)  
6. [Schema Creation & (Optional) Data Import](#schema-creation--optional-data-import)  
7. [Regex Approach (Optional)](#regex-approach-optional)  
8. [ERD Overview](#erd-overview)  
9. [Usage Notes & Tips](#usage-notes--tips)  
10. [Credits & Citations](#credits--citations)

---

## Project Overview
This project focuses on **Extract, Transform, and Load (ETL)** processes to handle crowdfunding data. The main tasks include:

1. **Extracting** data from Excel files (`crowdfunding.xlsx` and `contacts.xlsx`).  
2. **Transforming** the data into clean, structured CSV outputs (`campaign.csv`, `contacts.csv`, `category.csv`, and `subcategory.csv`).  
3. **Loading** these CSVs into a Postgres database via a SQL schema, along with an optional import script.

---

## Required Deliverables
According to the rubric, the **minimum required** files for this project are:

1. **`ETL_FINAL.ipynb`** (formerly `main_ETL.ipynb`)  
   - Contains your primary code for extracting, transforming, and loading the data.
2. **`crowdfunding_db_schema.sql`**  
   - A SQL script that creates the necessary Postgres tables for your cleaned CSV files.
3. **`ERD.jpg`**  
   - The final diagram illustrating how your tables are related.

Any additional scripts or notebooks (e.g., the optional **`schema_writer.ipynb`** or any import .sql file) are helpful but **not strictly required** by the rubric.

---

## Directory Structure

```plaintext
CROWDFUNDING_ETL/
├── ETL
│   ├── Deliverables
│   │   ├── crowdfunding_db_schema.sql   <-- (Required)
│   │   └── ETL_FINAL.ipynb             <-- (Required, main ETL notebook)
│   └── Extras
│       ├── crowdfunding_db_import.sql  <-- (Optional) Auto-generated import script
│       └── schema_writer.ipynb         <-- (Optional) Notebook that generates .sql files
├── Resources
│   ├── Input
│   │   ├── contacts.xlsx
│   │   └── crowdfunding.xlsx
│   └── Output
│       ├── campaign.csv
│       ├── category.csv
│       ├── contacts.csv
│       └── subcategory.csv
├── .gitignore
├── ERD.jpg                              <-- (Required)
└── README.md
```

---

## Installation & Setup

1. **Clone/Download** this repository.
2. Install **pandas** (and any other dependencies like `pathlib`) if not already present:
   ```bash
   pip install pandas
   ```
3. (Optionally) create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate     # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

---

## ETL Process

### 1. Extraction
- **Input**: `crowdfunding.xlsx` and `contacts.xlsx` in `Resources/Input/`.
- **ETL_FINAL.ipynb** (the main ETL notebook):
  - Reads these files with pandas.
  - Drops unneeded columns, renames columns, and converts data types (e.g., goal/pledged as floats, date columns to datetime, etc.).

### 2. Transformation
- Splits `"category & sub-category"` into `"category"` and `"subcategory"`.
- Creates cleaned DataFrames for `campaign.csv`, `contacts.csv`, `category.csv`, and `subcategory.csv`.
- Saves these to `Resources/Output/`.

### 3. Loading (Demonstration)
- The main deliverable here is **`crowdfunding_db_schema.sql`**:
  - A schema script that can be run in a Postgres environment to create tables matching your CSV structure.

---

## Schema Creation & (Optional) Data Import

**`crowdfunding_db_schema.sql`** is **required**, but how you create it is up to you. If desired, you can use the **`schema_writer.ipynb`** to generate or update SQL scripts **programmatically**.

### Example: Table Creation Snippet
```sql
CREATE TABLE campaign (
    cf_id CHAR(5) NOT NULL,
    contact_id INT NOT NULL,
    company_name VARCHAR(60),
    description VARCHAR(60),
    goal DEC,
    pledged DEC,
    outcome VARCHAR(10),
    backers_count INT,
    country CHAR(2),
    currency CHAR(3),
    launch_date DATE,
    end_date DATE,
    category_id CHAR(4),
    subcategory_id VARCHAR(8)
);
```

### Example: Import Snippet (Optional)
```sql
COPY
    campaign
FROM
    '/your/local/path/Resources/Output/campaign.csv'
DELIMITER ','
CSV HEADER;
```
- This is included in **`crowdfunding_db_import.sql`**, which is **optional**. You do **not** need it to fulfill the rubric. It’s simply a convenience script to bulk-load CSVs into Postgres if you wish to demonstrate the entire ETL pipeline.

### Usage
- **In pgAdmin or psql**:
  ```sql
  \i crowdfunding_db_schema.sql
  -- Optionally:
  \i crowdfunding_db_import.sql
  ```
- Verify with quick queries like:
  ```sql
  SELECT * FROM campaign;
  ```

---

## Regex Approach (Optional)
In scenarios where data might be stored as unstructured strings, you can use **regular expressions** to parse columns (e.g., contact names, emails, IDs). Below is a small snippet demonstrating how you might extract elements from text fields (though the main project uses pandas for efficiency).

```python
import re

# Suppose 'contact_info_df' is read in from 'contacts.xlsx'
pattern_id = r'\d{4}'            # 4-digit contact ID
pattern_email = r'"email": "(.+)"'
pattern_name = r'(\w+\s\w+)'

for row in contact_info_df['raw_data_column']:
    found_id = re.search(pattern_id, row).group()
    found_email = re.search(pattern_email, row).group(1)
    found_name = re.search(pattern_name, row).group()
    # Then split or store as needed

# Convert final lists into a DataFrame and export as CSV
```

While interesting, this **regex** approach is **not** required and was only included as an alternative method.

---

## ERD Overview
![ERD Diagram](./ERD.jpg)

**Relationships**:
- `campaign.contact_id` → references → `contacts.contact_id`
- `campaign.category_id` → references → `category.category_id`
- `campaign.subcategory_id` → references → `subcategory.subcategory_id`

This structure ensures each campaign has a linked contact and category.

---

## Usage Notes & Tips

- **Paths**: If you relocate the CSVs or the `.sql` scripts, update `ETL_FINAL.ipynb` (and/or `schema_writer.ipynb`) accordingly.
- **Manual Editing**: You can manually revise `crowdfunding_db_schema.sql` if you need additional constraints like `PRIMARY KEY` or `FOREIGN KEY`.
- **Optional Tools**: The `schema_writer.ipynb` and the import script are purely optional. They demonstrate an automated approach but aren’t required per the rubric.

---

## Credits & Citations

1. **Author**: Project ETL pipeline authored by _[Your Name]_, fulfilling the UT/edX/2U Data Analytics Bootcamp **Project 2** requirements.
2. **Starter Code & Data**: Provided by **edX/2U**, including `crowdfunding.xlsx` and `contacts.xlsx`.
3. **OpenAI & ChatGPT**: Assisted in generating parts of the README structure and code commentary.
4. **PostgreSQL Docs**: [postgresql.org/docs](https://www.postgresql.org/docs/)  
5. **pandas Docs**: [pandas.pydata.org/docs](https://pandas.pydata.org/docs)  

---

**Thank you for exploring this Crowdfunding ETL project!**  
Feel free to open issues or submit pull requests for any improvements.