-- CSV LOCAL HARD-PATH IMPORTS:

-- (1)
COPY
    contacts
FROM
    '/Users/neelagarwal/Projects/DataClassRepos/Crowdfunding_ETL/Resources/Outputs/contacts.csv'
DELIMITER ',' CSV HEADER;

-- (2)
COPY
    category
FROM
    '/Users/neelagarwal/Projects/DataClassRepos/Crowdfunding_ETL/Resources/Outputs/category.csv'
DELIMITER ',' CSV HEADER;

-- (3)
COPY
    subcategory
FROM
    '/Users/neelagarwal/Projects/DataClassRepos/Crowdfunding_ETL/Resources/Outputs/subcategory.csv'
DELIMITER ',' CSV HEADER;

-- (4)
COPY
    campaign
FROM
    '/Users/neelagarwal/Projects/DataClassRepos/Crowdfunding_ETL/Resources/Outputs/campaign.csv'
DELIMITER ',' CSV HEADER;