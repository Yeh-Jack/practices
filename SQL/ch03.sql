------------- 查詢資料庫的儲存位置 -------------
SHOW VARIABLES LIKE 'datadir';

------------- 創建資料庫 -------------
CREATE DATABASE IF NOT EXISTS test_mydb
    CHARACTER SET "utf8mb4"
    COLLATE "utf8mb4_unicode_ci";
	
------------- 查詢伺服器預設字元集與排序規則 -------------	
SELECT @@character_set_server, @@collation_server;

------------- 查詢特定資料庫預設字元集與排序規則 -------------	
SELECT @@character_set_database, @@collation_database;

SHOW CREATE DATABASE 資料庫名;

------------- 查詢系統資訊表 -------------
SELECT SCHEMA_NAME, DEFAULT_CHARACTER_SET_NAME, DEFAULT_COLLATION_NAME 
FROM information_schema.SCHEMATA;

------------- 修改資料庫 -------------
ALTER DATABASE test_mydb
    CHARACTER SET "big5"
    COLLATE "big5_chinese_ci";
	
------------- 刪除資料庫 -------------	
DROP DATABASE IF EXISTS test_mydb;


------------- 切換資料庫 -------------
USE 資料庫名;

------------- 查詢目前擁有的表格 -------------
SHOW TABLES;

SHOW TABLES FROM 資料庫名;

SHOW TABLES FROM world LIKE '%y';


------------- 建立表格 -------------
CREATE TABLE 員工 (
   身份證字號 CHAR(10)   NOT NULL PRIMARY KEY,
   姓名       VARCHAR(12) NOT NULL,
   城市       VARCHAR(5)  DEFAULT '台北',
   街道       VARCHAR(30),
   電話       CHAR(12),
   薪水       DECIMAL,
   保險       DECIMAL,
   扣稅       DECIMAL
);

-- 給欄位設定註解
CREATE TABLE employee (
    id_card CHAR(10) NOT NULL PRIMARY KEY COMMENT "身份證字號",
    name VARCHAR(12) NOT NULL COMMENT "姓名",
    city VARCHAR(5) DEFAULT "台北" COMMENT "城市"
);

-- 查詢表格的註解
SHOW FULL COLUMNS FROM employee;

-- 表格欄位有不一樣的字元集
CREATE TABLE addressbook (
  name      VARCHAR(20) CHARACTER SET big5,
  tel       VARCHAR(20),
  address   VARCHAR(80),
  birthdate DATE
) ENGINE = InnoDB
  CHARACTER SET = utf8
  COLLATE = utf8_unicode_ci;
  
------------- 查詢系統有哪些儲存引擎 -------------
SHOW ENGINES;

------------- NOT NULL -------------
CREATE TABLE addressbook1 (
  name      VARCHAR(20) NOT NULL,
  tel       VARCHAR(20) NULL,
  address   VARCHAR(80),
  birthdate DATE
);

INSERT INTO addressbook1 (name) VALUES ('Simon Johnson');

INSERT INTO addressbook (address) VALUES ('Taipei');

------------- DEFAULT -------------
CREATE TABLE addressbook2 (
  name      VARCHAR(20) NOT NULL,
  tel       VARCHAR(20),
  address   VARCHAR(80) DEFAULT 'Taipei',
  birthdate DATE
);

INSERT INTO addressbook2 (name) VALUES ('marine');


------------- TIMESTAMP與預設值 -------------
-- 建立表格
CREATE TABLE tstable (
  ts timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  ts2 timestamp NOT NULL default '0000-00-00 00:00:00',
  area varchar(20) NOT NULL,
  temp int(11) NOT NULL
);

-- 新增資料
INSERT INTO tstable (area, temp) VALUES ('NORTH', 25),
										('CENTRAL', 28),
										('SOUTH', 30);

-- 修改資料
UPDATE tstable SET temp = 32 WHERE area = 'South';


-- 修改sql_mode，將日期設定成可以輸入0000-00-00
SELECT @@GLOBAL.sql_mode, @@SESSION.sql_mode;

SET SESSION sql_mode = 'ONLY_FULL_GROUP_BY,IGNORE_SPACE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


--建立表格
CREATE TABLE timestamp_test (
  created timestamp default CURRENT_TIMESTAMP,
  updated timestamp on update CURRENT_TIMESTAMP,
  area varchar(20) NOT NULL,
  temp int(11) NOT NULL
);
INSERT INTO timestamp_test (area, temp) VALUES ('NORTH', 25),
										('CENTRAL', 28),
										('SOUTH', 30);

-- 修改資料
UPDATE timestamp_test SET temp = 32 WHERE area = 'South';

------------- 建立CHECK條件約束 -------------
-- 建立表格
CREATE TABLE orders (
    order_id     INT NOT NULL AUTO_INCREMENT PRIMARY KEY,		-- 訂單編號
    total_amount DECIMAL(10, 2) NOT NULL,						-- 訂單總價
    paid_amount  DECIMAL(10, 2) DEFAULT 0,						-- 已付金額
    
    CONSTRAINT total_amount_check CHECK (total_amount > 0),		-- 強制規定：訂單總價必須大於0才能寫入
    CONSTRAINT paid_amount_check  CHECK (paid_amount >= 0)		-- 強制規定：付款金額不可為負數
);

-- 完整填寫所有欄位
INSERT INTO orders (total_amount, paid_amount) VALUES (1500.50, 1500.50);

-- 只填寫總價
INSERT INTO orders (total_amount) VALUES (2800.00);

-- 一次插入多筆資料
INSERT INTO orders (total_amount, paid_amount) 
		VALUES (500.00, 0.00),
			   (120.75, 120.75),
			   (999.00, 500.00);

-- 錯誤範例(觸發CHECK)
INSERT INTO orders (total_amount) VALUES (-100);


------------- 修改表格名稱 -------------
-- 一次修改一個
ALTER TABLE addressbook RENAME TO address_book;

-- 一次修改多個
RENAME TABLE old_table1 TO new_table1,
             old_table2 TO new_table2,
             old_table3 TO new_table3;
			 
-- 把表格從資料庫A移動到資料庫B
RENAME TABLE test.towndata TO testdb.towndata;
RENAME TABLE test.timestamp_test TO world.timestamp_test_backup;
RENAME TABLE world.timestamp_test_backup TO test.timestamp_test;

------------- 新增欄位 -------------
-- 建立表格
CREATE TABLE mytable(
	n1 INT,
	n2 INT,
	n3 INT);

-- 新增一欄apple(整數型態)	
ALTER TABLE mytable ADD apple int;

-- 新增一欄banana，位置指定為第一個
ALTER TABLE mytable ADD banana int FIRST;

-- 新增一欄kiwi，位置指定在n2之後
ALTER TABLE mytable ADD kiwi int AFTER n2;

-- 一次新增多欄
ALTER TABLE mytable ADD (peach int, grape int);


------------- 刪除欄位 -------------
ALTER TABLE mytable DROP banana;


------------- 修改欄位 -------------
-- 把apple欄位改成tinyint、無負號、自動補零
ALTER TABLE mytable MODIFY apple TINYINT(5) UNSIGNED ZEROFILL;
INSERT INTO mytable (apple) VALUES (7);

-- 把grape更名為mongo、DEFAULT=0、位置移至n3之前
ALTER TABLE mytable CHANGE grape mongo int(11) DEFAULT 0 AFTER kiwi;


------------- 刪除表格 -------------
TRUNCATE TABLE mytable;

DROP TABLE mytable;


------------- 查詢表格資訊 -------------
SELECT TABLE_SCHEMA, TABLE_NAME, ENGINE, TABLE_ROWS,
       AUTO_INCREMENT,TABLE_COLLATION
FROM   information_schema.TABLES
WHERE  TABLE_SCHEMA = 'world';


SHOW CREATE TABLE 表格名;


------------- 用其他表格建立新表格 -------------
CREATE TABLE cityoftaiwan
SELECT Name, Population
FROM   world.city
WHERE  CountryCode='TWN';

-- 調整欄位屬性
CREATE TABLE cityoftaiwan2(
	NAME varchar(30),
	population INT UNSIGNED)
SELECT Name, Population
FROM   world.city
WHERE  CountryCode='TWN';

-- 調整欄位屬性 + 新增一欄
CREATE TABLE cityoftaiwan3(
	NAME varchar(30),
	population INT UNSIGNED,
	Description VARCHAR(50))
SELECT Name, Population
FROM   world.city
WHERE  CountryCode='TWN';


------------- 建立暫存表 -------------
CREATE TEMPORARY TABLE tmp_table
SELECT Name, Population
FROM   world.city
WHERE  CountryCode='TWN';


-- 修改暫存表
ALTER TABLE tmp_table RENAME tmp_cityoftaiwan;

use test;
select avg(updated)
  from timestamp_test;
  