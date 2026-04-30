------------- SELECT敘述 -------------
SELECT ID, Name
FROM   city;

SELECT Name, ID
FROM   city;

SELECT ID, Name, District
FROM   city;


------------- 別名 -------------
SELECT ename, salary * 12 AS 'Annual Salary'
FROM   cmdev.emp;


------------- 數學運算 -------------
SELECT 13*5, 81/2, 81 DIV 2, 11%3, 11 MOD 3;


SELECT ename, salary, salary * 12,
       (salary * 12) + (salary DIV 2)
FROM   cmdev.emp;


SELECT ename, salary AS MonthSalary,
       salary * 12 AS AnnualSalary,
       (salary * 12) + (salary DIV 2) AnnualFullSalary
FROM   cmdev.emp;


------------- 註解 -------------
-- 這是單行註解

/*
此為多行註解
SELECT Name, ID
FROM   city
*/


------------- 為查詢結果排除重複 -------------
SELECT DISTINCT Continent 
FROM country;


SELECT DISTINCT Continent 
FROM country
ORDER BY Continent;


------------- 比較運算子 -------------
SELECT name, District, population
FROM city
WHERE name = 'Taipei';


SELECT ename, salary
FROM emp
WHERE deptno = 20;


SELECT ename, salary
FROM emp
WHERE deptno = NULL;


SELECT ename, salary
FROM emp
WHERE deptno <=> NULL;


-- 是否使用where子句的範例
SELECT dname, location
FROM dept;


SELECT deptno, dname, location
FROM dept
WHERE deptno < 20;


-- 查找日期
SELECT ename, job, salary
FROM   cmdev.emp
WHERE  hiredate = '1981-09-08';


SELECT ename, job, salary
FROM   cmdev.emp
WHERE  hiredate > '1981-09-08';


SELECT ename, job, salary
FROM   cmdev.emp
WHERE  hiredate < '1981-09-08';


------------- 查找NULL值 -------------
SELECT Name, LifeExpectancy
FROM   country
WHERE  LifeExpectancy = NULL;


SELECT Name, LifeExpectancy
FROM   country
WHERE  LifeExpectancy IS NULL;


SELECT Name, LifeExpectancy
FROM   country
WHERE  LifeExpectancy <=> NULL;


------------- 特定字串查詢 -------------
SELECT Name
FROM   city
WHERE  Name LIKE 'w';


SELECT Name
FROM   city
WHERE  Name LIKE 'w%';


SELECT Name
FROM   city
WHERE  Name LIKE 'w%';


SELECT Name
FROM   city
WHERE  Name LIKE '%w%';


SELECT Name
FROM   city
WHERE  Name LIKE 'w_____';


------------- BETWEEN/AND -------------
SELECT *
FROM   city
WHERE  Population BETWEEN 80000 AND 90000;


SELECT *
FROM emp
ORDER BY ename;


SELECT empno, ename, job, salary
FROM emp
WHERE ename BETWEEN "F" AND "M"
ORDER BY ename;


------------- IN -------------
SELECT *
FROM   city
WHERE  CountryCode = 'TWN' OR 
       CountryCode = 'USA' OR
       CountryCode = 'JPN' OR
       CountryCode = 'ITA' OR
       CountryCode = 'KOR';


SELECT *
FROM   city
WHERE  CountryCode IN ('TWN','USA','JPN','ITA','KOR');


------------- 邏輯運算子 -------------
-- NOT的用法
SELECT *
FROM   city
WHERE  NOT CountryCode = 'TWN';


-- AND的用法
SELECT *
FROM   city
WHERE  CountryCode = 'TWN' AND Population < 100000;


-- OR的用法
SELECT *
FROM   city
WHERE  CountryCode = 'TWN' OR CountryCode='USA';


-- 要留意邏輯運算子的優先順序
-- AND和OR在同一行時，AND會優先處理
SELECT Name, Continent, Population
FROM   country
WHERE  Continent='Europe' OR Continent='Africa' AND Population<10000;


-- 找出(洲別是歐洲或非洲)且人口小於10000的國家
SELECT Name, Continent, Population
FROM   country
WHERE  (Continent='Europe' OR Continent='Africa') AND Population<10000;


-- 找出(職位是經理OR薪水大於3000)且部門編號不是10的人
SELECT ename, job, salary, deptno
FROM emp
WHERE (job = "MANAGER" OR salary > 3000) AND NOT deptno = 10;


------------- 聚合函數 -------------
SELECT SUM(Population) PopSum, 
       AVG(Population) PopAvg,
       MAX(Population) PopMax, 
       Min(Population) PopMin,
       COUNT(*) Amount
FROM   country;

-- count()的用法
SELECT COUNT(*), COUNT(deptno), COUNT(DISTINCT deptno)
FROM emp;


------------- GROUP BY -------------
SELECT job, SUM(salary)
FROM emp
GROUP BY job;


SELECT   Continent,region, SUM(Population) PopSum
FROM     country
GROUP BY Continent;


SELECT   Continent,region, SUM(Population) PopSum
FROM     country
GROUP BY Continent, region;


SELECT   Continent,region, SUM(Population) PopSum
FROM     country
GROUP BY Continent, region WITH ROLLUP;


-- HAVING
SELECT   Region, SUM(Population)
FROM     country
WHERE    SUM(Population) > 100000000
GROUP BY Region;

SELECT   Region, SUM(Population)
FROM     country
GROUP BY Region
HAVING   SUM(Population) > 100000000;


------------- ORDER BY -------------
SELECT empno, ename, salary
FROM emp
ORDER BY ename;


SELECT empno, ename, salary
FROM emp
ORDER BY ename DESC;


SELECT   CountryCode, Name
FROM     city
ORDER BY CountryCode DESC, Name ASC;


SELECT empno, ename, salary, deptno
FROM emp
ORDER BY deptno, salary DESC;


SELECT   ename, salary * 12 AS AnnualSalary
FROM     cmdev.emp
ORDER BY salary * 12;


SELECT   ename, salary * 12 AS AnnualSalary
FROM     cmdev.emp
ORDER BY AnnualSalary;


SELECT   ename, salary * 12 AS AnnualSalary
FROM     cmdev.emp
ORDER BY 2;


------------- LIMIT -------------
SELECT empno, ename 
FROM   cmdev.emp 
LIMIT  10;

-- 跳過前3筆，開始取5筆資料
SELECT empno, ename 
FROM   cmdev.emp 
LIMIT  3, 5;

-- 跳過前5筆，開始取3筆資料
SELECT empno, ename 
FROM   cmdev.emp 
LIMIT  3 OFFSET 5;

