-- Schema Creation and Validation
DROP TABLE IF EXISTS contacts CASCADE;
DROP TABLE IF EXISTS category CASCADE;
DROP TABLE IF EXISTS subcategory CASCADE;
DROP TABLE IF EXISTS campaign CASCADE;

CREATE TABLE contacts (
    contact_id INT
    ,first_name VARCHAR(20) NOT NULL
    ,last_name VARCHAR(20) NOT NULL
    ,email VARCHAR(50) NOT NULL
    ,CONSTRAINT pk_contact_id PRIMARY KEY (contact_id)
);

SELECT * FROM contacts;

CREATE TABLE category (
    category_id CHAR(4)
    ,category VARCHAR(12) NOT NULL
    ,CONSTRAINT pk_cat_id PRIMARY KEY (category_id)
);

SELECT * FROM category;

CREATE TABLE subcategory (
    subcategory_id VARCHAR(8)
    ,subcategory VARCHAR(17) NOT NULL
    ,CONSTRAINT pk_subcat_id PRIMARY KEY (subcategory_id)
);

SELECT * FROM subcategory;

CREATE TABLE campaign (
    cf_id INT
    ,contact_id INT 
    ,company_name VARCHAR(40) NOT NULL
    ,"description" VARCHAR(60) NOT NULL
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
    ,CONSTRAINT pk_cf_id PRIMARY KEY (cf_id)
    ,CONSTRAINT fk_contact_id FOREIGN KEY (contact_id) REFERENCES contacts(contact_id)
    ,CONSTRAINT fk_cat_id FOREIGN KEY (category_id) REFERENCES category(category_id)
    ,CONSTRAINT fk_subcat_id FOREIGN KEY (subcategory_id) REFERENCES subcategory(subcategory_id)
);

SELECT * FROM campaign;


-- CSV Import Validation
SELECT * FROM contacts;
SELECT * FROM category;
SELECT * FROM subcategory;
SELECT * FROM campaign;