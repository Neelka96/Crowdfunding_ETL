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

This project is designed to showcase an end-to-end **Extract, Transform, and Load (ETL)** process for crowdfunding campaign data as part of the UT/edX/2U Data Analytics Bootcamp.

The objectives of this project are:
1. **Extract** crowdfunding data from provided Excel spreadsheets.
2. **Transform** and clean the data into a relational database-friendly format.
3. **Load** the cleaned data into a PostgreSQL database using custom SQL scripts.

The project emphasizes reproducibility and scalability by providing optional automation through notebook-driven SQL generation, all while fulfilling the assignment rubric. It avoids GUI-based imports (like pgAdmin's CSV import tool) to maintain cross-environment compatibility.

---

## Required Deliverables

According to the project rubric, the following are required:
- **`ETL_FINAL.ipynb`**: The main notebook that handles extraction, transformation, and CSV creation.
- **`crowdfunding_db_schema.sql`**: Defines the database schema for the transformed data.
- **`ERD.jpg`**: Visual representation of the Entity Relationship Diagram (ERD) of the database.

### Optional Enhancements:
- **`schema_writer.ipynb`**: Automatically generates SQL schema and import statements.
- **`crowdfunding_db_import.sql`**: Optional script to bulk-load CSVs into the database using `COPY` commands.

These optional files offer automation and flexibility, ensuring that future changes to the data model or CSV structures can be incorporated efficiently.

---

## Directory Structure

```plaintext
CROWDFUNDING_ETL/
├── ETL
│   ├── Deliverables
│   │   ├── crowdfunding_db_schema.sql (Required)
│   │   └── ETL_FINAL.ipynb (Required)
│   └── Extras
│       ├── crowdfunding_db_import.sql (Optional)
│       └── schema_writer.ipynb (Optional)
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
  - `pathlib`
  - `re` (built-in)
  - `json` (built-in)
  - `datetime` (built-in)
- **Jupyter Notebook**: For running `.ipynb` files (install via `pip install notebook` if needed)
- **PostgreSQL GUI (optional)**: pgAdmin 4 or any compatible interface
- **Disk Space**: Minimum 500 MB free for project files, CSV outputs, and database storage
- **Memory (RAM)**: Minimum 4 GB recommended for smooth execution

### Installation Summary
To set up your environment, install required Python libraries with:
```bash
pip install pandas numpy notebook
```

Ensure PostgreSQL is installed and running on your system before executing the SQL scripts.


## Installation & Setup

1. **Clone or download** this repository.
2. Ensure you have **Python 3.x** installed with **pandas**:
   ```bash
   pip install pandas
   ```
3. (Optional) Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scriptsctivate     # Windows
   ```

---

## ETL Process

### 1. Extraction
- Read `crowdfunding.xlsx` and `contacts.xlsx` from the `Resources/Input/` directory.
- Use pandas to load and inspect the data.
- Clean the raw datasets by removing unneeded columns and standardizing data types.

### 2. Transformation
- Split combined fields (such as `"category & sub-category"`) into individual `"category"` and `"subcategory"` fields.
- Generate four separate, tidy datasets (`campaign`, `contacts`, `category`, `subcategory`).
- Output cleaned datasets as CSV files in `Resources/Output/`.

### 3. Loading
- Load transformed CSVs into a PostgreSQL database using the `crowdfunding_db_schema.sql` schema.
- (Optional) Use `crowdfunding_db_import.sql` to automate CSV imports via `COPY` commands.

---

## Schema Creation & (Optional) Data Import

While **`crowdfunding_db_schema.sql`** is a required deliverable, you may manually create it or generate it programmatically with **`schema_writer.ipynb`**.

### Example Table Creation
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

### Example Import (Optional)
```sql
COPY campaign
FROM '/your/local/path/Resources/Output/campaign.csv'
DELIMITER ','
CSV HEADER;
```

### Usage
Run in pgAdmin or psql:
```sql
\i crowdfunding_db_schema.sql
-- Optional:
\i crowdfunding_db_import.sql
```

Verify tables with:
```sql
SELECT * FROM campaign;
```

---

## Regex Approach (Optional)

An alternative method explored for parsing the contacts data involves **regular expressions** to extract IDs, names, and emails from semi-structured text data.

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

While interesting, the regex-based method was ultimately replaced by a more efficient pandas solution in the final deliverable notebook.

---

## ERD Overview

![ERD Diagram](./ERD.jpg)

### Relationships:
- `campaign.contact_id` references `contacts.contact_id`
- `campaign.category_id` references `category.category_id`
- `campaign.subcategory_id` references `subcategory.subcategory_id`

This relational structure enables effective storage and querying of campaign data across contacts, categories, and subcategories.

---

## Usage Notes & Tips

- **File Paths**: If you move files, update paths within `ETL_FINAL.ipynb` and `schema_writer.ipynb`.
- **Constraints**: You may enhance `crowdfunding_db_schema.sql` with constraints (e.g., `PRIMARY KEY`, `FOREIGN KEY`).
- **Automation**: Utilize `schema_writer.ipynb` for future schema regeneration if CSV structures evolve.

---

## Credits & Citations

1. **Author**: _[Your Name]_ - UT/edX/2U Data Analytics Bootcamp, Project 2.
2. **Starter Code & Data**: Provided by **edX/2U**, including sample datasets and rubric guidance.
3. **ChatGPT**: Supported README drafting and refinement.
4. **PostgreSQL Documentation**: [postgresql.org/docs](https://www.postgresql.org/docs/)
5. **pandas Documentation**: [pandas.pydata.org/docs](https://pandas.pydata.org/docs)

---

Thank you for exploring the Crowdfunding ETL project! Contributions and feedback are welcome.