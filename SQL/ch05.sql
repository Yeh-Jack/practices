------------- INNER JOIN -------------
SELECT country.Code, country.Capital, city.Name
FROM   country, city
WHERE  country.Capital = city.ID;


SELECT Code, Capital, city.Name
FROM   country, city
WHERE  Capital = ID;


SELECT Code, Capital, Name
FROM   country, city
WHERE  Capital = ID;

-- 表格別名
SELECT country.name, 
	   country.Population coPop,
	   city.Name, 
	   city.Population ciPop,
	   city.Population / country.Population * 100
FROM   country a, city b
WHERE  Capital = ID;


SELECT a.name, 
		a.Population coPop,
		b.Name, 
		b.Population ciPop,
		b.Population / a.Population * 100
FROM    country a, city b
WHERE   Capital = ID;

-- INNER JOIN.... ON的用法
SELECT a.name, a.Population coPop,
       b.Name, b.Population ciPop,
       b.Population / a.Population * 100
FROM   country a INNER JOIN city b ON Capital = ID
LIMIT 10;


-- USING的範例
SELECT empno, ename, dname
FROM   cmdev.emp e INNER JOIN cmdev.dept d USING (deptno);


------------- LEFT OUTER JOIN -------------
-- emp為主、dept為輔
SELECT empno, ename, e.deptno, d.dname
FROM   cmdev.emp e LEFT OUTER JOIN cmdev.dept d
       ON e.deptno = d.deptno;
	   
-- emp為輔、dept為主
SELECT empno, ename, e.deptno, d.dname
FROM   cmdev.emp e RIGHT OUTER JOIN cmdev.dept d
       ON e.deptno = d.deptno;


------------- UNION -------------
SELECT e.ename, e.deptno, d.deptno, d.dname
FROM emp AS e
LEFT JOIN dept AS d ON e.deptno = d.deptno

UNION

SELECT e.ename, e.deptno, d.deptno, d.dname
FROM emp AS e
RIGHT JOIN dept AS d ON e.deptno = d.deptno;


SELECT e.ename, e.deptno , d.deptno , d.dname
FROM emp AS e
LEFT JOIN dept AS d ON e.deptno = d.deptno

UNION

SELECT e.ename, e.deptno, d.deptno, d.dname
FROM emp AS e
RIGHT JOIN dept AS d ON e.deptno = d.deptno;


SELECT Region, Name, Population
FROM   world.country
WHERE  Region = 'Southeast Asia' AND Population < 2000000
UNION
SELECT Region, Name, Population
FROM   world.country
WHERE  Region = 'Eastern Asia' AND Population < 1000000
UNION
SELECT ename, job, salary
FROM   cmdev.emp
WHERE  salary < 1000;


SELECT Region, Name, Population
FROM   world.country
WHERE  Region = 'Southeast Asia' AND Population < 2000000
UNION
SELECT Region, Name, Population
FROM   world.country
WHERE  Region = 'Eastern Asia' AND Population < 1000000
UNION
SELECT ename, job, salary, comm
FROM   cmdev.emp
WHERE  salary < 1000;


------------- CROSS JOIN -------------
-- 建立班級表
CREATE TABLE classes (
    classname VARCHAR(10)
);

-- 建立成員表
CREATE TABLE members (
    name VARCHAR(10)
);

-- 插入圖片中的資料
INSERT INTO classes VALUES ("A班"), ("B班"), ("C班");
INSERT INTO members VALUES ("marine"), ("gigi"), ("kaela"), ("vivi");


SELECT c.classname, m.name
FROM classes AS c CROSS JOIN members AS m;

SELECT c.classname, m.name
FROM classes AS c, members AS m;


------------- JOIN統整 -------------
-- 建立第一張表tablea
CREATE TABLE table_a (
    id INT,
    name VARCHAR(20),
    age INT
);

-- 插入資料
INSERT INTO table_a (id, name, age) VALUES (1, "peter", 35),	 (2, "sara", 21), (3, "maria", 29);


-- 建立第二張表table_b
CREATE TABLE table_b (
    id INT,
    name VARCHAR(20),
    address VARCHAR(50)
);

-- 插入資料
INSERT INTO table_b (id, name, address) VALUES 
(1, "maria", "台北市"),
(2, "gigi", "高雄市"),
(3, "tom", "宜蘭市"),
(4, "peter", "台中市");


-- 建立第三張表table_c
CREATE TABLE table_c (
    id INT,
    name VARCHAR(20),
    phone VARCHAR(50)
);

-- 插入資料
INSERT INTO table_c (id, name, phone) VALUES
(1, "maria", "0955123456"),
(2, "kaela", "0930654321");


-- INNER JOIN
SELECT table_a.name, age, address
FROM table_a INNER JOIN table_b ON table_a.name = table_b.name;

-- LEFT OUTER JOIN
SELECT a.name, a.age, b.address
FROM table_a AS a LEFT JOIN table_b AS b ON a.name = b.name;

-- RIGHT OUTER JOIN
SELECT b.name, a.age, b.address
FROM table_a AS a RIGHT JOIN table_b AS b ON a.name = b.name;

-- LEFT OUTER JOIN 扣掉 INNER JOIN(左差集)
SELECT a.name, a.age, b.address
FROM table_a AS a
LEFT JOIN table_b AS b ON a.name = b.name
WHERE b.name IS NULL;

-- RIHGT OUTER JOIN 扣掉 INNER JOIN(右差集)
SELECT b.name, b.address, a.age
FROM table_a AS a
RIGHT JOIN table_b AS b ON a.name = b.name
WHERE a.name IS NULL;

-- UNION ALL(沒有去重)
SELECT a.name, a.age, b.address FROM table_a AS a LEFT JOIN table_b AS b ON a.name = b.name
UNION ALL
SELECT b.name, a.age, b.address FROM table_a AS a RIGHT JOIN table_b AS b ON a.name = b.name;

-- UNION(有去重)
SELECT a.name, a.age, b.address FROM table_a AS a LEFT JOIN table_b AS b ON a.name = b.name
UNION
SELECT b.name, a.age, b.address FROM table_a AS a RIGHT JOIN table_b AS b ON a.name = b.name;

-- UNION(對稱差集)
SELECT a.name, a.age, b.address FROM table_a AS a LEFT JOIN table_b AS b ON a.name = b.name WHERE b.name IS NULL
UNION
SELECT b.name, a.age, b.address FROM table_a AS a RIGHT JOIN table_b AS b ON a.name = b.name WHERE a.name IS NULL;

-- 三張表INNER JOIN
SELECT a.name, a.age, b.address, c.phone
FROM table_a a 
	INNER JOIN table_b b ON a.name = b.name
	INNER JOIN table_c c ON a.name = c.name;


------------- 子查詢 -------------
-- 薪資高於公司平均薪資
SELECT ename, salary
FROM emp
WHERE salary > (SELECT AVG(salary) FROM emp);

-- 人口數比美國人口多的國家
SELECT Code,name, Population
FROM   country
WHERE  Population > ( SELECT Population
                      FROM   country
                      WHERE  Code = 'USA' );
					  

-- 放在HAVING					  
SELECT deptno, AVG(salary) AS "平均薪資"
FROM emp
GROUP BY deptno
HAVING AVG(salary) > (SELECT AVG(salary) FROM emp);					  


-- 放在FROM
SELECT Name, Language, Population * Percentage
FROM   country, ( SELECT CountryCode, Language, Percentage
                  FROM   countrylanguage
                  WHERE  IsOfficial = 'T' ) officiallanguage
WHERE  Code = CountryCode;


-- 比較運算子
SELECT Name, GNP
FROM   country
WHERE  GNP = ( SELECT MAX(GNP)
               FROM   country );


SELECT Name, GNP
FROM   country
WHERE  GNP = ( SELECT Code, MAX(GNP)
               FROM   country );


SELECT Name, GNP
FROM   country
WHERE  GNP = ( SELECT   MAX(GNP)
               FROM     country
               GROUP BY Continent );
			   

-- IN、 NOT IN
SELECT Name
FROM   country
WHERE  Code IN ('BRA','IDN','IND',
                'CHN','KOR','PAK');


SELECT Name
FROM   country
WHERE  Code IN ( SELECT CountryCode
                 FROM   city
                 WHERE  Population > 9000000 );

SELECT Name
FROM   country
WHERE  Code NOT IN ( SELECT CountryCode
                     FROM   city
                     WHERE  Population > 9000000 );				 


-- 邏輯運算子 ANY、ALL
CREATE TABLE IF NOT EXISTS innertable (
  n int(11) DEFAULT NULL
);


INSERT INTO innertable (n) VALUES
	(2),
	(3);


CREATE TABLE IF NOT EXISTS outertable (
  n int(11) DEFAULT NULL
);


INSERT INTO outertable (n) VALUES
	(1),
	(2),
	(3),
	(4),
	(5);


-- ALL(AND)的用法
SELECT * FROM outertable WHERE n = ALL (SELECT n FROM innertable);

SELECT * FROM outertable WHERE n <> ALL (SELECT n FROM innertable);

SELECT * FROM outertable WHERE n > ALL (SELECT n FROM innertable);

SELECT * FROM outertable WHERE n >= ALL (SELECT n FROM innertable);

SELECT * FROM outertable WHERE n < ALL (SELECT n FROM innertable);

SELECT * FROM outertable WHERE n <= ALL (SELECT n FROM innertable);

-- ANY(OR)的用法
SELECT * FROM outertable WHERE n = ANY (SELECT n FROM innertable);

SELECT * FROM outertable WHERE n <> ANY (SELECT n FROM innertable);

SELECT * FROM outertable WHERE n > ANY (SELECT n FROM innertable);

SELECT * FROM outertable WHERE n >= ANY (SELECT n FROM innertable);

SELECT * FROM outertable WHERE n < ANY (SELECT n FROM innertable);



SELECT a.Name AS "Country", 
       b.Name AS "CapitalCity", 
	   b.Population
FROM country AS a
INNER JOIN city AS b ON a.Capital = b.ID
WHERE b.Population > ALL (
                          SELECT Population 
                          FROM city 
                          WHERE countryCode IN (
												SELECT Code 
												FROM country 
												WHERE Region = "Southeast Asia")

);


步驟1，得到的結果有BRN、IDN、KHM、LAO、MMR、MYS、PHL、SGP、THA、TMP、VNM
SELECT Code 
FROM country 
WHERE Region = "Southeast Asia";




步驟2，得到9604900這個結果
SELECT  Population 
FROM    city 
WHERE   countryCode IN ('BRN','IDN','KHM','LAO','MMR','MYS','PHL','SGP','THA','TMP','VNM')
ORDER BY 1 DESC
LIMIT 3;


步驟3
以country為主 city為輔
找出以兩張表都有的城市人口數 > 步驟2的國家


-- 關聯子查詢
SELECT e1.ename, e1.salary, e1.deptno
FROM emp AS e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM emp AS e2
    WHERE e2.deptno = e1.deptno
);


-- 結果同上，但效率較高
SELECT e.ename, e.salary, e.deptno
FROM emp AS e
INNER JOIN (
    -- 先把各部門平均算好，這只會跑一次
    SELECT deptno, AVG(salary) AS avg_sal
    FROM emp
    GROUP BY deptno
) AS d_avg ON e.deptno = d_avg.deptno
WHERE e.salary > d_avg.avg_sal;



-- EXISTS
查找至少有一名員工的部門
SELECT d.dname
FROM dept AS d
WHERE EXISTS (
    SELECT 1
    FROM emp AS e
    WHERE e.deptno = d.deptno
);


SELECT d.dname
FROM dept AS d
WHERE EXISTS (
    SELECT "HELLO"
    FROM emp AS e
    WHERE e.deptno = d.deptno
);
