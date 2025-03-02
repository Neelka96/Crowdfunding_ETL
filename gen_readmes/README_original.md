# Project 2: Crowdfunding ETL

## Table of Contents
1. [Project Overview](#project-overview)  
2. [File Structure & Descriptions](#file-structure--descriptions)  
3. [Installation & Setup](#installation--setup)  
4. [ETL Process](#etl-process)  
5. [Schema Creation & Data Import](#schema-creation--data-import)  
6. [Regex Alternative (Optional)](#regex-alternative-optional)  
7. [ERD Overview](#erd-overview)  
8. [Usage Notes & Tips](#usage-notes--tips)  
9. [Credits & Citations](#credits--citations)

---

## Project Overview
This project focuses on **Extract, Transform, and Load (ETL)** processes to handle crowdfunding data. The main tasks include:

1. **Extracting** data from Excel (`crowdfunding.xlsx`, `contacts.xlsx`) into structured CSV files.  
2. **Transforming** that data by cleaning columns, splitting attributes, and merging into final tables (e.g., `campaign.csv`, `contacts.csv`, `category.csv`, `subcategory.csv`).  
3. **Loading** these CSVs into a Postgres database by first generating a SQL schema script (`crowdfunding_db_schema.sql`) and then importing the data with a separate SQL file (`crowdfunding_db_import.sql`).

While many ETL pipelines might use an ORM (like SQLAlchemy), this project demonstrates how to automate the generation of schema and import statements **directly** from Python and pandas.

---

## File Structure & Descriptions

```plaintext
your-project/
├── Resources/
│   ├── Input/
│   │   ├── crowdfunding.xlsx
│   │   └── contacts.xlsx
│   └── Output/
│       ├── campaign.csv
│       ├── category.csv
│       ├── contacts.csv
│       ├── subcategory.csv
│       └── (other CSV outputs)
├── schema_writer.py
├── main_ETL.py
├── regex_sol.py (optional/alternative method)
├── crowdfunding_db_schema.sql
├── crowdfunding_db_import.sql
├── ERD.jpg
└── README.md  <-- (You are here)
```

### Key Files

- **main_ETL.py**  
  - Extracts data from the Excel files in `Resources/Input/`.  
  - Creates and cleans separate DataFrames for categories, subcategories, campaigns, and contacts.  
  - Outputs final CSVs to `Resources/Output/`.  

- **schema_writer.py**  
  - Reads the newly created CSVs and **auto-generates** SQL statements for schema creation (table definitions, data types, etc.) and separate SQL import statements to load CSV data.  
  - Outputs `.sql` files that you can copy directly into your database tool or CLI.  

- **crowdfunding_db_schema.sql** & **crowdfunding_db_import.sql**  
  - Finished SQL scripts that contain **(1)** the table creation statements including constraints, and **(2)** the COPY statements to load data from CSV files, respectively.  

- **regex_sol.py (Optional)**  
  - An alternative approach using regex to parse contact data.  
  - Demonstrates how you could extract name, email, and contact ID from raw strings without relying on pandas methods.  
  - Provided mainly for posterity; the pandas-based approach in `main_ETL.py` is more concise and efficient.  

- **ERD.jpg**  
  - Entity Relationship Diagram showing how the final tables relate to each other in the database.  

---

## Installation & Setup

1. **Clone/Download** this repository to your local machine.
2. Ensure you have **Python 3.x** and the following libraries installed:
   ```bash
   pip install pandas
   ```
3. (Optional) Create a virtual environment to keep dependencies clean:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

---

## ETL Process

### 1. Extraction
- **Input Files**: 
  - `crowdfunding.xlsx`  
  - `contacts.xlsx`
- Using **pandas**, the `main_ETL.py` script:
  - Reads each sheet/data range from these Excel files.
  - Performs basic cleaning (dropping unnecessary columns, renaming columns, converting data types, etc.).

### 2. Transformation
- Splits columns such as `"category & sub-category"` into separate `category` and `subcategory` columns.
- Creates tidy DataFrames for each logical entity (like `campaign`, `contacts`, `category`, and `subcategory`).
- Ensures columns match the required schema data types (e.g., `goal` as float, timestamps as datetime objects).
- Exports each transformed DataFrame to CSV in `Resources/Output/`.

### 3. Loading
- The actual **Load** process is orchestrated by the Postgres schema and import SQL statements:
  - `crowdfunding_db_schema.sql` sets up tables in your database.
  - `crowdfunding_db_import.sql` loads CSV data via **COPY** statements (paths can be updated to match your file structure).

---

## Schema Creation & Data Import

1. **schema_writer.py**  
   - When run, it automatically generates two SQL scripts:
     - A **schema** script with `CREATE TABLE` statements.  
     - An **import** script with `COPY` statements to bulk-load CSV files into Postgres.  
   - If you make changes to your CSV structure (e.g., add columns), simply re-run `schema_writer.py` to regenerate updated SQL.

2. **crowdfunding_db_schema.sql**  
   - Example code snippet:
     ```sql
     CREATE TABLE campaign (
         cf_id CHAR(5) NOT NULL,
         contact_id INT NOT NULL,
         company_name VARCHAR(255) NOT NULL,
         ...
     );
     ```
   - **Primary and Foreign Key constraints** can be manually added or modified to ensure referential integrity.

3. **crowdfunding_db_import.sql**  
   - Example COPY statement:
     ```sql
     COPY
         campaign
     FROM
         '/your/local/path/Resources/Output/campaign.csv'
     DELIMITER ',' CSV HEADER;
     ```
   - Update file paths if your repository is located elsewhere.

4. **Usage**:
   - In **pgAdmin** or **psql** CLI:
     ```sql
     \i crowdfunding_db_schema.sql
     \i crowdfunding_db_import.sql
     ```
   - Verify tables and data with simple `SELECT *` statements.

---

## Regex Alternative (Optional)

In addition to the main pandas-based approach, there is a **regex-based** workflow in [`regex_sol.py`](./regex_sol.py).  
- **Why regex?**  
  - Shows how to parse strings (names, emails, IDs) purely with regular expressions.  
  - It is more manual (find patterns, slice strings, build columns), but helps illustrate how text extraction can be done in Python without relying on dataframe operations.  

Below is a concise snippet if you wish to integrate the regex logic directly into your README or main script. Feel free to remove the separate `.py` file if you just want to keep a reference in your documentation.

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
```

---

## ERD Overview
![ERD Diagram](./ERD.jpg)

- **campaign** <-> **contacts**: Linked via `contact_id`
- **campaign** <-> **category** / **subcategory**: Linked via `category_id` and `subcategory_id`
- Reflects a many-to-one relationship where multiple campaigns can share one category or subcategory, etc.

---

## Usage Notes & Tips

1. **Modifying Paths**  
   - If your CSV outputs or `.sql` scripts need a different directory structure, update them in `schema_writer.py` accordingly.
2. **Avoiding pgAdmin GUI**  
   - This project intentionally generates `.sql` files so you can load them manually via CLI or in pgAdmin’s query tool, removing the need for the built-in import wizard.
3. **Future Data**  
   - The schema is designed to accommodate new data—especially with the `VARCHAR` usage for textual fields and default constraints where necessary.

---

## Credits & Citations

- **Pandas** documentation: [pandas.pydata.org/docs](https://pandas.pydata.org/docs)  
- **Official Postgres Documentation**: [postgresql.org/docs](https://www.postgresql.org/docs/)  
- **Regex Approach**  
  - Demonstrated for instructional purposes.  
- **Class Rubric**  
  - Followed guidelines from the Crowdfunding_ETL Project 2 assignment specifications.  

---

**Thank you for using this ETL pipeline!**  
Feel free to open issues or pull requests if you find bugs or want to suggest improvements.