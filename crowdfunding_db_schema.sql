DROP TABLE IF EXISTS contacts CASCADE;
DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS subcategories CASCADE;
DROP TABLE IF EXISTS campaign CASCADE;

CREATE TABLE contacts (
    contact_id INT
    ,first_name VARCHAR(12) NOT NULL
    ,last_name VARCHAR(13) NOT NULL
    ,email VARCHAR(42) NOT NULL

    ,CONSTRAINT pk_contact_id PRIMARY KEY (contact_id)
);

CREATE TABLE category (
    category_id CHAR(4)
    ,category VARCHAR(12) NOT NULL

    ,CONSTRAINT pk_cat_id PRIMARY KEY (category_id)
);

CREATE TABLE subcategory (
    subcategory_id VARCHAR(8)
    ,subcategory VARCHAR(17) NOT NULL

    ,CONSTRAINT pk_subcat_id PRIMARY KEY (subcategory_id)
);

CREATE TABLE campaign (
    cf_id INT
    ,contact_id INT
    ,company_name VARCHAR(33) NOT NULL
    ,"description" VARCHAR(53)
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
    
    ,CONSTRAINT pk_cf_id PRIMARY KEY (cf_id)
    ,CONSTRAINT fk_contact_id FOREIGN KEY (contact_id) REFERENCES contacts(contact_id)
    ,CONSTRAINT fk_cat_id FOREIGN KEY (category_id) REFERENCES category(category_id)
    ,CONSTRAINT fk_subcat_id FOREIGN KEY (subcategory_id) REFERENCES subcategory(subcategory_id)
);