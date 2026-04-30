------------- 資料匯入 -------------
source C:\Users\student\Desktop\World.sql

------------- 查詢有多少個資料庫 -------------
show databases; 

------------- 資料匯出 -------------
1. 匯出指定資料庫
mysqldump -u root -p world > E:\backup_world.sql
2. 匯出全部資料庫
mysqldump -u root -p --all-databases > E:\all_databases.sql
3. 匯出指定表格
mysqldump -u root -p world city > E:\city_only.sql

------------- 查詢資料表名稱是否區分大小寫 -------------
SHOW VARIABLES LIKE 'lower_case_table_names';

------------- 離開資料庫 -------------
EXIT
quit
\q

------------- 查詢連線人數上限 -------------
SHOW VARIABLES LIKE 'max_connections';

------------- 查詢當前連線人數 -------------
SHOW PROCESSLIST;

------------- 查詢客戶端臨時連接埠 -------------
SELECT CONNECTION_ID();


------------- 建立帳號 -------------
CREATE USER 'marine'@'localhost' IDENTIFIED BY '12345678';

------------- 賦予權限 -------------
GRANT 操作權限 ON 資料庫.資料表 TO '帳號'@'ip';

1. 給予全部資料庫、表格所有權限
GRANT all ON *.* TO 'marine'@'localhost';
2. 給予指定資料庫查詢權限
GRANT SELECT ON world.* TO 'marine'@'localhost';
3. 給予指定資料表查詢權限
GRANT SELECT ON world.city TO 'marine'@'localhost';

------------- 重新載入，確保設定立即套用 -------------
FLUSH PRIVILEGES;

------------- 查詢權限 -------------
SHOW GRANTS FOR '帳號'@'ip'; 

SHOW GRANTS FOR 'gigi'@'localhost';

------------- 特定帳號自行修改密碼 -------------
SET PASSWORD = PASSWORD('新密碼');

------------- 修改權限 -------------
REVOKE 操作權限 ON 資料庫.資料表 FROM '帳號'@'ip';

REVOKE INSERT ON *.* FROM 'gigi'@'localhost';

------------- 修改密碼 -------------
ALTER USER '帳號'@'ip' IDENTIFIED BY '密碼';

ALTER USER 'gigi'@'localhost' IDENTIFIED BY '98765';

------------- 查詢帳號 -------------
SELECT user,host FROM mysql.user;

------------- 刪除帳號 -------------
DROP USER IF EXISTS '帳號'@'ip';

------------- 查詢資料庫支援的字元集 -------------
1. 查詢預設字元集
SHOW CHARACTER SET;

2. 查詢所有字元集
SHOW COLLATION;

3. 查詢指定字元集所支援的排序規則
SHOW COLLATION LIKE 'latin1%';

------------- 資料庫伺服器預設字元集與字元排序 -------------
SELECT @@character_set_server, @@collation_server;

------------- 資料庫預設字元集與字元排序 -------------
SELECT @@character_set_database, @@collation_database;

------------- 整數型態範例 -------------
-- 創建表格
CREATE TABLE example_table (
    n1 TINYINT(1) UNSIGNED ZEROFILL NULL,
    n2 TINYINT(2) UNSIGNED ZEROFILL NULL,
    n3 TINYINT(3) UNSIGNED ZEROFILL NULL,
    n4 TINYINT(4) UNSIGNED ZEROFILL NULL,
    n5 TINYINT(5) UNSIGNED ZEROFILL NULL
);

-- 插入資料
INSERT INTO int_test VALUES(1, 123, 47, 255, 81);
INSERT INTO int_test VALUES(1.2, 2.3, 3.4, 4.5, 5.6);

------------- 浮點型態範例 -------------
-- 創建表格
CREATE TABLE float_test (
    f FLOAT(5,2) UNSIGNED ZEROFILL NULL,
    f2 DOUBLE(7,3) UNSIGNED ZEROFILL NULL,
    f3 DECIMAL(9,5) UNSIGNED ZEROFILL NULL
);

-- 插入資料
INSERT INTO float_test (f, f2, f3) VALUES (1.234567, 1.234567, 1.234567);
INSERT INTO float_test (f) VALUES (1234.56);

------------- 字串型態範例 -------------
-- 創建表格
CREATE TABLE str_test(
	id INTEGER,
	val1 VARCHAR(4),
	val2 CHAR(4)
);

-- 插入資料
INSERT INTO str_test VALUES (1, 'a', 'a');
INSERT INTO str_test VALUES (2, 'a ', 'a ');
INSERT INTO str_test VALUES (3, 'a  ', 'a  ');

SELECT id, CONCAT(val1, '***') varcharcol, CONCAT(val2, '***') charcol
FROM str_test;

INSERT INTO str_test VALUES (4, 'hello world', 'hello world');

SELECT val1, LENGTH(val1), val2, LENGTH(val2)
FROM str_test;

------------- 日期型態範例 -------------
-- 創建表格
CREATE TABLE date_test (
  y4 year(4) DEFAULT NULL,
  d date DEFAULT NULL,
  t time DEFAULT NULL,
  dt datetime DEFAULT NULL,
  ts timestamp NULL DEFAULT NULL
);

-- 插入資料
INSERT INTO date_test (d) VALUES ('9000-1-1'),
								 ('900-1-1'),
								 ('90-1-1'),
								 ('9-1-1');

INSERT INTO date_test (d) VALUES ('69-1-1'),
								 ('70-1-1');

INSERT INTO date_test (t) VALUES ('200:30:30'),
								 ('-1:20:30');

INSERT INTO date_test (t) VALUES ('200:30:30'),
								 ('200:30'),
							     ('200');

------------- GLOBAL vs SESSION -------------		
SELECT @@GLOBAL.TIME_ZONE, @@SESSION.TIME_ZONE;

-- 創建表格
CREATE TABLE timezone_test (
    dt DATETIME,
    ts TIMESTAMP
);

-- 插入當前時間
INSERT INTO timezone_test VALUES (NOW(), NOW());

-- 修改GLOBAL或SESSION
SET time_zone = '+08:00';

-- 還原GLOBAL或SESSION
SET time_zone = 'SYSTEM';

------------- TIMESTAMP -------------
INSERT INTO timezone_test (ts) VALUES ('1970/01/01 08:00:01');

------------- ENUM -------------
-- 創建表格
CREATE TABLE enumtable (
  enumsize enum('XS','S','M','L','XL'),
  stringsize varchar(2)
);

-- 插入資料
INSERT INTO enumtable VALUES ('XS', 'XS'),
							 ('S', 'S'),
							 ('M', 'M'),
							 ('L', 'L'),
							 ('XL', 'XL');
							 
INSERT INTO enumtable (stringsize) VALUES('QQ');
INSERT INTO enumtable (enumsize) VALUES	('QQ');	

INSERT INTO enumtable (enumsize) VALUES (1), (3), (5);

-- 排序
SELECT * FROM enumtable ORDER BY enumsize;
SELECT * FROM enumtable ORDER BY stringsize;


------------- SET -------------
-- 創建表格
CREATE TABLE settable (
  workingday set('MON','TUE','WED','THU','FRI','SAT','SUN')
);

-- 插入資料
INSERT INTO settable VALUES ('MON,WED,FRI'),
							('TUE,THU'),
							('MON,TUE,WED,THU,FRI,SAT,SUN');
							
INSERT INTO settable VALUES ('MON,FRI'),
							('THU,THU');

INSERT INTO settable VALUES (0), (1), (4), (16);
INSERT INTO settable VALUES (21);


------------- ENUM與SET的排序 -------------
-- 創建表格
CREATE TABLE estable (
  enumsize enum('XS','S','M','L','XL') CHARACTER SET latin1 COLLATE latin1_general_ci,
  enumsize2 enum('XS','S','M','L','XL') CHARACTER SET latin1 COLLATE latin1_general_cs,
  workingday set('MON','TUE','WED','THU','FRI','SAT','SUN') CHARACTER SET latin1 COLLATE latin1_general_ci,
  workingday2 set('MON','TUE','WED','THU','FRI','SAT','SUN') CHARACTER SET latin1 COLLATE latin1_general_cs
);

-- 插入資料
INSERT INTO estable VALUES (1, 1, 21, 21),
						   ('M', 'M', 'MON', 'MON'),
						   ('m', 'M', 'mon', 'MON');