-- Local CSV POSIX Path from Drive
-- Copied and Pasted from schema_writer.ipynb safely

-- (1)
COPY
    contacts
FROM
    '/Users/neelagarwal/Projects/DataClassRepos/Crowdfunding_ETL/Resources/Output/contacts.csv'
DELIMITER ',' CSV HEADER;

-- (2)
COPY
    category
FROM
    '/Users/neelagarwal/Projects/DataClassRepos/Crowdfunding_ETL/Resources/Output/category.csv'
DELIMITER ',' CSV HEADER;

-- (3)
COPY
    subcategory
FROM
    '/Users/neelagarwal/Projects/DataClassRepos/Crowdfunding_ETL/Resources/Output/subcategory.csv'
DELIMITER ',' CSV HEADER;

-- (4)
COPY
    campaign
FROM
    '/Users/neelagarwal/Projects/DataClassRepos/Crowdfunding_ETL/Resources/Output/campaign.csv'
DELIMITER ',' CSV HEADER;