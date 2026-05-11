------------- 建立檢視表 -------------
CREATE VIEW CountryView AS
SELECT   Continent, Region, Code, Code2, Name
FROM     world.country
ORDER BY Continent, Region, Code;


CREATE VIEW CountryMaxGNP AS
SELECT Name, GNP
FROM   world.country
WHERE  (Region, GNP) IN ( SELECT   Region, MAX(GNP)
                          FROM     world.country
                          GROUP BY Region );
						  

				  

CREATE VIEW city_with_country_info AS
SELECT 
    city.ID, 
    city.Name AS cityName, 
    country.Name AS countryName, 
    country.Continent, 
    city.Population
FROM world.city
JOIN world.country ON city.CountryCode = country.Code;


CREATE VIEW dominant_official_languages AS
SELECT 
    country.Name AS 國家名, 
    countrylanguage.Language AS 官方語言, 
    countrylanguage.Percentage AS 佔比
FROM world.country
JOIN world.countrylanguage ON country.Code = countrylanguage.CountryCode
WHERE countrylanguage.IsOfficial = "T" 
  AND countrylanguage.Percentage > 50;


CREATE VIEW continentStats AS
SELECT 
    Continent, 
    COUNT(*) AS 國家總數, 
    SUM(Population) AS 總人口數, 
    AVG(LifeExpectancy) AS 平均壽命
FROM world.country
GROUP BY Continent;


------------- 查詢檢視表詳細內容 -------------
SELECT TABLE_SCHEMA, TABLE_NAME, VIEW_DEFINITION 
FROM information_schema.VIEWS 
WHERE TABLE_NAME = "CountryView";		


SHOW CREATE VIEW CountryView;


------------- 建立檢視表的注意事項 -------------
-- 不能重名
CREATE VIEW CountryView AS
SELECT   Continent, Region, Code, Code2, Name
FROM     world.country
ORDER BY Continent, Region, Code;


-- 來源不能用暫存表
CREATE TEMPORARY TABLE taiwan_tmp
SELECT NAME, population
FROM world.city
WHERE countrycode = 'TWN';

CREATE VIEW taiwan_data AS
SELECT NAME, population
FROM taiwan_tmp
WHERE population > 1000000;


-- 欄名不能重複
CREATE VIEW ScaleView AS
SELECT co.Name, 
       ci.Name, 
	   co.Population, 
	   ci.Population,
       ROUND(ci.Population / co.Population, 2) Scale
FROM   world.country co, world.city ci
WHERE  co.Code = ci.CountryCode;


CREATE VIEW ScaleView AS
SELECT co.Name AS CountryName, 
       ci.Name AS CityName,
       co.Population AS CountryPop, 
	   ci.Population AS CityPop,
       ROUND(ci.Population / co.Population, 2) Scale
FROM   world.country co, world.city ci
WHERE  co.Code = ci.CountryCode;


CREATE VIEW ScaleView 
(CountryName, CityName, CountryPop, CityPop, Scale)
AS
SELECT co.name, 
       ci.Name, 
	   co.Population, 
	   ci.Population,
       ROUND(ci.Population / co.Population, 2) Scale
FROM   world.country co, world.city ci
WHERE  co.Code = ci.CountryCode;


------------- 修改檢視表 -------------
CREATE VIEW CountryMaxGNP AS
SELECT Name, GNP
FROM   world.country
WHERE  (Region, GNP) IN ( SELECT   Region, MAX(GNP)
                          FROM     world.country
                          GROUP BY Region );


CREATE OR REPLACE VIEW CountryMaxGNP AS
SELECT Code, Name, GNP
FROM   world.country
WHERE  (Region, GNP) IN ( SELECT   Region, MAX(GNP)
                          FROM     world.country
                          GROUP BY Region );						  


ALTER VIEW CountryMaxGNP AS
SELECT Code, Name, GNP
FROM   world.country
WHERE  (Region, GNP) IN ( SELECT   Region, MAX(GNP)
                          FROM     world.country
                          GROUP BY Region );						  
						  

------------- 刪除檢視表 -------------
DROP VIEW IF EXISTS CountryMaxGNP, ScaleView;				  


------------- 檢視表的資料維護 -------------
-- 建立檢視表
CREATE VIEW EmpDept30View AS
SELECT empno, ename, job, manager, hiredate, salary, comm
FROM   cmdev.emp
WHERE  deptno = 30;


SELECT * FROM EmpDept30View;


-- 將員編7844的comm改為600
UPDATE EmpDept30View
SET    comm = 600
WHERE  empno = 7844;


SELECT empno,ename,salary,comm 
FROM EmpDept30View 
WHERE empno = 7844;


SELECT empno,ename,salary,comm 
FROM cmdev.emp 
WHERE empno = 7844;


-- 插入新資料
INSERT INTO EmpDept30View
VALUES (9001, 'SIMON', 'SALESMAN', 7698, 
        '2000-04-01', 1000, 250);
		
SELECT empno,ename,salary,comm
FROM EmpDept30View 
WHERE empno = 9001;


SELECT empno,ename,salary,comm,deptno
FROM cmdev.emp 
WHERE empno = 9001;


-- 刪除資料
DELETE FROM EmpDept30View WHERE empno = 9001;


SELECT empno,ename,salary,comm 
FROM EmpDept30View 
WHERE empno = 9001;


SELECT empno,ename,salary,comm,deptno 
FROM cmdev.emp 
WHERE empno = 9001;


------------- 檢查點 -------------
CREATE OR REPLACE VIEW EmpDept30View AS
SELECT empno, ename, job, manager, hiredate, salary, comm
FROM   cmdev.emp
WHERE  deptno = 30
WITH CHECK OPTION;


INSERT INTO EmpDept30View
VALUES (9002, 'MARY', 'SALESMAN', 7698,
        '2000-05-01', 1200, 150);
		
		
UPDATE EmpDept30View
SET    comm = 1200
WHERE  empno = 7844;		



CREATE TABLE t1(
	n INT
);

CREATE OR REPLACE VIEW v1 
AS
SELECT n
FROM t1
WHERE n > 10;

INSERT INTO v1 VALUES (5);


CREATE OR REPLACE VIEW v2 
AS
SELECT n
FROM v1
WITH CASCADED CHECK OPTION;


INSERT INTO v2 VALUES (5);


CREATE OR REPLACE VIEW v3 
AS
SELECT n
FROM v2
WHERE n < 20
WITH CASCADED CHECK OPTION;


INSERT INTO v3 VALUES (5);


INSERT INTO v3 VALUES (13);

SELECT "t1" AS table_name, n FROM t1
UNION
SELECT "v1" AS table_name, n FROM v1
UNION
SELECT "v2" AS table_name, n FROM v2
UNION
SELECT "v3" AS table_name, n FROM v3;


INSERT INTO v3 VALUES (26);


ALTER VIEW v2 AS
SELECT n
FROM v1 
WITH LOCAL CHECK OPTION;


INSERT INTO v2 VALUES (6);


SELECT "t1" AS table_name, n FROM t1
UNION
SELECT "v1" AS table_name, n FROM v1
UNION
SELECT "v2" AS table_name, n FROM v2;


INSERT INTO v3 VALUES (11);

SELECT n, GROUP_CONCAT(table_name) AS 出現位置
FROM (
    SELECT "t1" AS table_name, n FROM t1
    UNION ALL
    SELECT "v1", n FROM v1
    UNION ALL
    SELECT "v2", n FROM v2
    UNION ALL
    SELECT "v3", n FROM v3
) AS combined_data
GROUP BY n;