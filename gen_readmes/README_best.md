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
This ETL project extracts, transforms, and loads crowdfunding data. It demonstrates:

1. Extracting data from Excel files.
2. Transforming data into clean CSV outputs (`campaign.csv`, `contacts.csv`, `category.csv`, and `subcategory.csv`).
3. Loading data into a Postgres database via a SQL schema with optional import automation.

---

## Required Deliverables
According to the rubric, the required files are:

- **ETL_FINAL.ipynb**: Extracts, transforms, and outputs CSV files.
- **crowdfunding_db_schema.sql**: Creates Postgres tables.
- **ERD.jpg**: Visualizes table relationships.

Additional helpful (but optional) files include:

- **schema_writer.ipynb**: Auto-generates SQL schema and import scripts.
- **crowdfunding_db_import.sql**: Auto-generated import script.

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

## Installation & Setup

1. Clone/download this repository.
2. Install pandas:
   ```bash
   pip install pandas
   ```
3. Optionally create a virtual environment.

---

## ETL Process

### Extraction
- Read `crowdfunding.xlsx` and `contacts.xlsx`.
- Clean and standardize data.

### Transformation
- Split and normalize categories.
- Export CSV outputs.

### Loading
- Demonstrated with `crowdfunding_db_schema.sql` and optionally with `crowdfunding_db_import.sql`.

---

## Schema Creation & (Optional) Data Import

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
```sql
\i crowdfunding_db_schema.sql
-- Optional:
\i crowdfunding_db_import.sql
```

---

## Regex Approach (Optional)

Example of extracting fields from unstructured data:

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

![ERD Diagram](./ERD.jpg)

Relationships:
- `campaign.contact_id` → `contacts.contact_id`
- `campaign.category_id` → `category.category_id`
- `campaign.subcategory_id` → `subcategory.subcategory_id`

---

## Usage Notes & Tips

- Update paths as needed.
- Edit schema for constraints like `PRIMARY KEY` or `FOREIGN KEY`.
- Optional tools like `schema_writer.ipynb` can automate parts of the process.

---

## Credits & Citations

1. **Author**: _[Your Name]_ for UT/edX/2U Data Analytics Bootcamp.
2. **Starter Code & Data**: Provided by **edX/2U**.
3. **ChatGPT**: Assisted in structuring this README.
4. **PostgreSQL Docs**: [postgresql.org/docs](https://www.postgresql.org/docs/)
5. **pandas Docs**: [pandas.pydata.org/docs](https://pandas.pydata.org/docs)

---

Thank you for exploring this Crowdfunding ETL project!