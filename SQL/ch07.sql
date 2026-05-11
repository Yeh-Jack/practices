use test;

------------- 複合索引 -------------
CREATE TABLE example_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    a INT NOT NULL,
    b INT NOT NULL,
    c INT NOT NULL,
    KEY idx_abc (a, b, c)
);


INSERT INTO example_table (id, a, b, c) VALUES
(1, 1, 2, 1),
(2, 1, 3, 2),
(3, 2, 1, 3),
(4, 2, 4, 4),
(5, 3, 2, 5),
(6, 5, 3, 2);


SHOW INDEX FROM example_table;


EXPLAIN 
SELECT * 
FROM example_table
WHERE a=1;

EXPLAIN 
SELECT * 
FROM example_table
WHERE b=1;

EXPLAIN 
SELECT * 
FROM example_table
WHERE a=5 AND b=3;

EXPLAIN 
SELECT * 
FROM example_table
WHERE a=5 AND b=3 AND c=2;

EXPLAIN 
SELECT * 
FROM example_table
WHERE a=2 AND c=3;

EXPLAIN 
SELECT * 
FROM example_table
WHERE a>1 AND b=4;


------------- 建立索引 -------------
CREATE TABLE addressbook (
  id        INT UNSIGNED PRIMARY KEY,  
  name      VARCHAR(20),
  tel       VARCHAR(20),
  address   VARCHAR(80),
  birthdate DATE,
  email     VARCHAR(36) UNIQUE KEY
);


CREATE TABLE addressbook2 (
  id        INT UNSIGNED,  
  name      VARCHAR(20),
  tel       VARCHAR(20),
  address   VARCHAR(80),
  birthdate DATE,
  email     VARCHAR(36),
  PRIMARY KEY (id),
  UNIQUE KEY (email)
);


------------- 查詢索引 -------------
DESC addressbook;

SHOW INDEX FROM addressbook;


------------- 修改表格時增加索引 -------------
CREATE TABLE addressbook3 (
  id        INT UNSIGNED,  
  name      VARCHAR(20),
  tel       VARCHAR(20),
  address   VARCHAR(80),
  birthdate DATE,
  email     VARCHAR(36)
);

ALTER TABLE addressbook3
ADD PRIMARY KEY (id);


ALTER TABLE addressbook3
ADD UNIQUE KEY (email);


ALTER TABLE addressbook3
ADD INDEX (address);


CREATE TABLE addressbook4 (
  id        INT UNSIGNED,  
  name      VARCHAR(20),
  tel       VARCHAR(20),
  address   VARCHAR(80),
  birthdate DATE,
  email     VARCHAR(36)
);

CREATE UNIQUE INDEX email_index 
ON addressbook4 (email);

CREATE INDEX name_index 
ON addressbook4 (name);


ALTER TABLE addressbook
ADD PRIMARY KEY (id);

ALTER TABLE addressbook
ADD UNIQUE KEY (email);


------------- 修改索引名稱 -------------
ALTER TABLE addressbook4 RENAME INDEX email_index TO idx_user_email;


------------- 刪除索引 -------------
ALTER TABLE addressbook2
DROP PRIMARY KEY,
DROP INDEX email;


ALTER TABLE addressbook4
DROP INDEX idx_user_email;


------------- AUTO_INCREMENT -------------
CREATE TABLE userData (
    id INT AUTO_INCREMENT,
    user_code VARCHAR(10),
    PRIMARY KEY (user_code),
    KEY (id)
);

INSERT INTO userData (user_code) VALUES ('A0001'),
										('A0002'),
										('A0003');


INSERT INTO userData VALUES (10, 'A0010');
INSERT INTO userData VALUES (0, 'A0000');
INSERT INTO userData VALUES (NULL, 'A0099');
INSERT INTO userData VALUES (8, 'A0008');


------------- 外部鍵 -------------
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50),
    PRIMARY KEY (customer_id)
);


CREATE TABLE orders (
    order_id INT AUTO_INCREMENT,
    order_date DATE,
    c_id INT,
    PRIMARY KEY (order_id),
    
    -- 設定外部鍵
    CONSTRAINT fk_customer_order 
    FOREIGN KEY (c_id) REFERENCES customers (customer_id)
    ON DELETE CASCADE
);


-- 查詢是否有設定外部鍵
SELECT 
    CONSTRAINT_NAME, 
    TABLE_NAME, 
    REFERENCED_TABLE_NAME, 
    COLUMN_NAME, 
    REFERENCED_COLUMN_NAME
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_NAME = "orders"


INSERT INTO customers (name) VALUES ('gigi'),('marine');

INSERT INTO orders (order_date, c_id) VALUES ("2026-03-20", 1);
INSERT INTO orders (order_date, c_id) VALUES ("2021-09-19", 99);


DELETE FROM customers WHERE customer_id=1;

