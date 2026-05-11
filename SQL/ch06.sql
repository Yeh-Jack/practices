------------- INSERT INTO -------------
-- 插入單筆
INSERT INTO cmdev.dept VALUES (60, 'EDU', 'NEW YORK');


INSERT INTO cmdev.dept VALUES (70, 'MARKETING', DEFAULT);


INSERT INTO cmdev.dept VALUES (80, 'PURCHASING');


INSERT INTO cmdev.dept VALUES ('PURCHASING', 80, 'NEW YORK');


INSERT INTO cmdev.dept VALUES (70, 'PURCHASING', 'TAIPEI');


-- 主索引與IGNORE
INSERT INTO cmdev.dept
VALUES (50, 'MIS', DEFAULT);


INSERT IGNORE INTO cmdev.dept
VALUES (50, 'MIS', DEFAULT);


INSERT IGNORE INTO cmdev.dept
VALUES (500, 'MIS', DEFAULT);


-- 插入多筆
INSERT INTO cmdev.emp VALUES 
(8001, 'SIMON', 'MANAGER', 7369, '2001-02-03', 3300, NULL, 50),
(8002, 'JOHN', 'PROGRAMMER', 8001, '2002-01-01', 2300, NULL, 50),
(8003, 'GREEN', 'ENGINEER', 8001, '2003-05-01', 2000, NULL, 50);.


------------- REPLACE -------------
REPLACE INTO cmdev.dept VALUES (80, 'MIS', DEFAULT);


REPLACE INTO cmdev.dept VALUES (90, 'IT', 'TOKYO');


------------- UPDATE -------------
-- 查詢安全模式狀況
SHOW VARIABLES LIKE "sql_safe_updates";

-- 開啟安全模式
SET sql_safe_updates = 1;


UPDATE cmdev.emp
SET    salary = salary + 100;



UPDATE cmdev.emp
SET    salary = salary + 100
WHERE  salary < 1500


-- UPDATE + IGNORE
UPDATE cmdev.dept
SET    deptno = 50
WHERE  deptno = 30;


UPDATE IGNORE cmdev.dept
SET    deptno = 50
WHERE  deptno = 30;


UPDATE IGNORE cmdev.emp
SET    salary = 'HELLO', comm = 1000
WHERE  empno = 7369;

-- UPDATE + ORDER BY / LIMIT
UPDATE   cmdev.emp
SET      salary = salary + 100
ORDER BY salary


UPDATE   cmdev.emp
SET      salary = salary + 100
LIMIT    3


UPDATE   cmdev.emp
SET      salary = salary + 100
ORDER BY salary
LIMIT    3


UPDATE   cmdev.emp
SET      salary = salary + 100
ORDER BY salary DESC
LIMIT    3


------------- ON DUPLICATE KEY UPDATE -------------
-- 建立表格
CREATE TABLE page_views (
    page_id INT,
    view_date DATE,
    counter INT DEFAULT 1,
    PRIMARY KEY (page_id, view_date)
);

-- 新增資料
INSERT INTO page_views VALUES (101, "2026-03-10", 1)
ON DUPLICATE KEY UPDATE counter = counter + 1;


------------- UPDATE + 子查詢 -------------
UPDATE cmdev.emp
SET salary = salary * 1.1
WHERE deptno = (
    SELECT deptno
    FROM cmdev.dept
    WHERE dname = "RESEARCH"
);


------------- DELETE -------------
DELETE FROM cmdev.emp;


DELETE FROM  cmdev.emp
WHERE  salary < 1500;


DELETE FROM cmdev.emp
ORDER BY salary;


-- TRUNCATE + INSERT INTO
CREATE TABLE del_table_ex1(
	id INT NOT NULL auto_increment,
	NAME VARCHAR(20),
	PRIMARY KEY  (ID)
) AUTO_INCREMENT=996;


INSERT INTO del_table_ex1 (name) VALUES 
('marine'),
('gigi'),
('kaela'),
('gura'),
('iris');


TRUNCATE TABLE del_table_ex1;

INSERT INTO del_table_ex1 (name) VALUES ('anya');

SELECT * FROM del_table_ex1;


-- DELETE + INSERT INTO
CREATE TABLE del_table_ex2(
	id INT NOT NULL auto_increment,
	NAME VARCHAR(20),
	PRIMARY KEY  (ID)
) AUTO_INCREMENT=996;


INSERT INTO del_table_ex2 (name) VALUES 
('marine'),
('gigi'),
('kaela'),
('gura'),
('iris');


DELETE FROM del_table_ex2;

INSERT INTO del_table_ex2 (name) VALUES ('anya');

SELECT * FROM del_table_ex2;
