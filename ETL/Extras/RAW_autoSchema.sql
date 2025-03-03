-- Schema Creation and Validation
DROP TABLE IF EXISTS contacts CASCADE;
DROP TABLE IF EXISTS category CASCADE;
DROP TABLE IF EXISTS subcategory CASCADE;
DROP TABLE IF EXISTS campaign CASCADE;

CREATE TABLE contacts (
    contact_id INT
    ,first_name VARCHAR(12) NOT NULL
    ,last_name VARCHAR(13) NOT NULL
    ,email VARCHAR(42) NOT NULL
);

SELECT * FROM contacts;

CREATE TABLE category (
    category_id CHAR(4)
    ,category VARCHAR(12) NOT NULL
);

SELECT * FROM category;

CREATE TABLE subcategory (
    subcategory_id VARCHAR(8)
    ,subcategory VARCHAR(17) NOT NULL
);

SELECT * FROM subcategory;

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

SELECT * FROM campaign;


-- CSV Import Validation
SELECT * FROM contacts;
SELECT * FROM category;
SELECT * FROM subcategory;
SELECT * FROM campaign;

