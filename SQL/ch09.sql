------------- 預存程序 -------------
-- 建立預存程序(輸入一個國家的代碼(如"TWN")，接著會幫你列出該國所有的城市名)
DELIMITER $$

CREATE PROCEDURE GetCitiesByCountry(IN target_code CHAR(3))
BEGIN
    SELECT Name, District, Population 
    FROM city 
    WHERE CountryCode = target_code;
END $$

DELIMITER ;


-- 呼叫預存程序
CALL GetCitiesByCountry("TWN");



-- 查出某個城市的名稱，並計算它佔該國總人口的比例
DELIMITER $$

CREATE PROCEDURE GetCityPopulationRatioByName(IN target_city_name VARCHAR(35))
BEGIN
    -- 宣告內部變數
    DECLARE city_pop INT;
    DECLARE country_pop INT;
    DECLARE city_name VARCHAR(35);
    DECLARE country_code CHAR(3);

    -- 透過城市名稱取得資訊並存入變數
    SELECT Name, Population, CountryCode 
    INTO city_name, city_pop, country_code
    FROM city 
    WHERE Name = target_city_name;

    -- 取得該國的總人口並存入變數
    SELECT Population INTO country_pop 
    FROM country 
    WHERE Code = country_code;

    -- 輸出最終計算結果
    SELECT city_name AS `City`, 
           city_pop AS `City Pop`, 
           country_pop AS `Country Pop`,
           (city_pop / country_pop) * 100 AS `Ratio (%)`;
END $$

DELIMITER ;

-- 呼叫預存程序
CALL GetCityPopulationRatioByName("Taipei");
CALL GetCityPopulationRatioByName("New York");



-- 依據輸入的洲別與人口，統計該大洲有多少個城市超過指定人口
DELIMITER $$

CREATE PROCEDURE GetLargeCitiesByContinent(
    IN continent_name VARCHAR(20), 
    IN min_population INT
)
BEGIN
    -- 統計符合條件的城市數量
    SELECT co.Continent, 
           COUNT(ci.ID) AS "大城市數量",
           AVG(ci.Population) AS "平均人口"
    FROM city ci
    JOIN country co ON ci.CountryCode = co.Code
    WHERE co.Continent = continent_name 
      AND ci.Population > min_population
    GROUP BY co.Continent;
END $$

DELIMITER ;

-- 呼叫預存程序(查看亞洲人口超過500萬的城市統計)
CALL GetLargeCitiesByContinent("Asia", 5000000);



-- 查詢目前已有的預存程序
SELECT ROUTINE_SCHEMA, ROUTINE_NAME, ROUTINE_DEFINITION
FROM INFORMATION_SCHEMA.ROUTINES
WHERE ROUTINE_TYPE='PROCEDURE' AND ROUTINE_SCHEMA='world';



-- 刪除預存程序
DROP PROCEDURE GetCitiesByCountry



------------- 預存程序參數方向性 -------------
-- 建立計算打折價格
DELIMITER $$

CREATE PROCEDURE calc_discount(
    IN price INT, 
    IN rate DECIMAL(3,2), 
    OUT final_price INT
)
BEGIN
    SET final_price = price * rate; 
END $$

DELIMITER ;

-- 呼叫時要先準備好@my_result這個變數來接
CALL calc_discount(100, 0.8, @my_result);
SELECT CONCAT("打折後是: ", @my_result);



-- 建立查詢指定城市名、人口、所屬國家的預存程序
DELIMITER $$

CREATE PROCEDURE GetCityDetailsByName(
    IN target_name VARCHAR(35),  
    OUT c_name VARCHAR(35),      
    OUT c_pop INT,               
    OUT c_code CHAR(3)
)
BEGIN
    SELECT Name, Population, CountryCode 
    INTO c_name, c_pop, c_code
    FROM city 
    WHERE Name = target_name
    LIMIT 1;
END $$

DELIMITER ;


-- 呼叫時拿三個籃子去接
CALL GetCityDetailsByName('Taipei', @name, @pop, @code);
SELECT @name, @pop, @code;



-- 計算num*2+10的結果後再存回num
DELIMITER $$

CREATE PROCEDURE DoubleAndAddTen(INOUT num INT)
BEGIN
    SET num = (num * 2) + 10;
END $$

DELIMITER ;


-- 先設定一個變數=5
SET @my_val = 5;

-- 呼叫預存程序，傳入這個變數
CALL DoubleAndAddTen(@my_val);

-- 查看結果(5 * 2 + 10 = 20)
SELECT @my_val AS "結果";



-- 將城市名稱轉成國碼
DELIMITER $$

CREATE PROCEDURE ConvertCityToCode(INOUT city_info VARCHAR(50))
BEGIN
    -- 先判定表單中是否有這個城市名
    IF EXISTS (SELECT 1 FROM city WHERE Name = city_info) THEN
        
        -- 若有，才執行查詢並覆蓋
        SELECT CountryCode INTO city_info 
        FROM city 
        WHERE Name = city_info 
        LIMIT 1;
        
    ELSE
        -- 若無，可以選擇把變數清空或加上錯誤提示
        SET city_info = "Error: City Not Found";
        
    END IF;
END $$

DELIMITER ;


-- 先設定變數="Taipei"
SET @target = "Taipei";

-- 呼叫預存程序
CALL ConvertCityToCode(@target);

-- 變數的內容已經從"Taipei"變成"TWN"
SELECT @target AS "Country Code";



------------- 參數與變數的比較 -------------
-- 計算銀行利息
DELIMITER $$

CREATE PROCEDURE CalculateInterest(
    IN target_id INT,
    IN rate DECIMAL(5,2),
    OUT is_rich VARCHAR(10),
    INOUT balance DECIMAL(10,2)
)
BEGIN
    -- 宣告interest_amt，為內部的小工具，用來計算利息
    DECLARE interest_amt DECIMAL(10,2); 

    -- 計算利息
    SET interest_amt = balance * rate;

    -- 更新餘額
    SET balance = balance + interest_amt;

    -- 判定是否為有錢人
    IF balance > 1000000 THEN
        SET is_rich = "YES";
    ELSE
        SET is_rich = "NO";
    END IF;
END $$

DELIMITER ;



-- 設定@my_balance變數
SET @my_balance = 900000;

-- 呼叫預存程序(將顧客id、利率傳入，執行後會得到2個結果@rich, @my_balance)
CALL CalculateInterest(1, 0.2, @rich, @my_balance);

-- 查看結果
SELECT @rich AS "Is Rich?", @my_balance AS "Updated Balance";




------------- 使用者變數 -------------
-- 設定使用者變數
SET @my_continent = 'Asia';

SET @my_continent2 = 'Europe';

SET @my_region = 'Eastern Asia', @my_region2 = 'Middle Asia';


-- 查詢使用者變數
SELECT @my_continent, @my_continent2;

SELECT @my_region, @my_region2;


-- 用SELECT子句設定使用者變數
SELECT @my_gnp := 30000, @my_gnp2 := 5000;

SELECT @my_gnp, @my_gnp2;




SELECT @max_gnp := MAX(GNP), 
       @max_population := MAX(Population)
FROM   country;


-- 利用上面存好的變數@max_population 找出哪些國家的人口已達到世界最高記錄的70%以上
SELECT Name, Population, 
       (Population / @max_population) * 100 AS "百分比"
FROM country
WHERE Population > @max_population * 0.7;


-- 依員工薪水高低進行排序
SET @rank := 0;

SELECT ename, salary,
       @rank := @rank + 1 AS ranking
FROM emp
ORDER BY salary DESC;


-- 依員工薪水高低進行排序(改良版)
SET @rank := 0, @prev_salary := NULL;

SELECT 
    ename,
    salary,
    @rank := IF(@prev_salary = salary, @rank, @rank + 1) AS ranking,
	@prev_salary := salary
FROM emp
ORDER BY salary DESC;



------------- 函數 -------------
-- 建立查詢今日日期函數
DELIMITER $$

CREATE FUNCTION my_date()
RETURNS VARCHAR(64)
DETERMINISTIC
BEGIN
    DECLARE d, t, w VARCHAR(24);
	
    SET d = DATE_FORMAT(CURDATE(), '%Y/%m/%d');
    SET t = TIME_FORMAT(CURTIME(), '%H:%i:%s');
    SET w = DAYNAME(CURDATE());
	
    RETURN CONCAT( d, ' ', t, ' ', w );
END $$

DELIMITER ;


-- 呼叫函數
SELECT my_date();



-- 建立判斷奇偶的函數
DELIMITER $$

CREATE FUNCTION is_even(n INT) RETURNS VARCHAR(4)
DETERMINISTIC
BEGIN
    IF n % 2 = 0 THEN
        RETURN 'Yes';
    ELSE
        RETURN 'No';
    END IF;
END$$

DELIMITER ;

-- 使用判斷奇偶的函數
SELECT is_even(10);
SELECT is_even(7); 



-- 建立階乘函數
DELIMITER $$

CREATE FUNCTION factorial(n INT) RETURNS BIGINT
DETERMINISTIC
BEGIN
    DECLARE result BIGINT DEFAULT 1;
    DECLARE i INT DEFAULT 1;

    WHILE i <= n DO
        SET result = result * i;
        SET i = i + 1;
    END WHILE;

    RETURN result;
END$$

DELIMITER ;

-- 呼叫階乘函數
SELECT factorial(5), factorial(7);


-- 建立稅率計算
DELIMITER $$

CREATE FUNCTION add_tax(price DECIMAL(10,2), tax_rate DECIMAL(5,2))
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    RETURN ROUND(price * (1 + tax_rate / 100), 2);
END$$

DELIMITER ;

-- 呼叫稅率計算
SELECT
    empno, ename, salary,
    add_tax(salary, 10) AS salary_with_tax
FROM
    emp;
	
	

-- 查詢函數
SELECT ROUTINE_SCHEMA, ROUTINE_NAME, ROUTINE_DEFINITION
FROM INFORMATION_SCHEMA.ROUTINES
WHERE ROUTINE_TYPE='FUNCTION' AND ROUTINE_SCHEMA='cmdev';



-- 刪除函數
DROP FUNCTION IF EXISTS my_date();




------------- 觸發程序 -------------
-- 建立存放薪資異動紀錄的表格
CREATE TABLE salary_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    empno INT,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    change_date DATETIME
);


-- 建立觸發程序
DELIMITER $$

CREATE TRIGGER emp_salary_update
AFTER UPDATE ON emp  -- 監聽emp表
FOR EACH ROW         -- 每一行受影響的資料都會執行一次
BEGIN
    -- 若薪資真正有變動時才記錄
    IF OLD.salary <> NEW.salary THEN
        INSERT INTO salary_log (empno, old_salary, new_salary, change_date)
        VALUES (OLD.empno, OLD.salary, NEW.salary, NOW());
    END IF;
END $$

DELIMITER ;


-- 修改員工SMITH(7369)的薪資 
UPDATE emp SET salary = 950.00 WHERE empno = 7369;

-- 查看日誌表，會發現觸發程序已經默默幫你寫好紀錄
SELECT * FROM salary_log;





-- 建立刪除資料時要寫入記錄的表格
CREATE TABLE emp_audit_delete (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    deleted_user VARCHAR(100),  -- 刪除人的帳號
    deleted_time DATETIME,      -- 刪除時間
    target_empno INT,           -- 刪了哪筆記錄 (員工編號)
    target_ename VARCHAR(50)    -- 刪了哪筆記錄 (員工姓名)
);


-- 建立觸發程序
DELIMITER $$

CREATE TRIGGER tr_emp_after_delete
AFTER DELETE ON emp
FOR EACH ROW
BEGIN
    INSERT INTO emp_audit_delete (deleted_user, deleted_time, target_empno, target_ename)
    VALUES (
        USER(),      -- 抓取當前登入的帳號
        NOW(),       -- 抓取當前的日期與時間
        OLD.empno,   -- 抓取剛被刪除的員工編號
        OLD.ename    -- 抓取剛被刪除的員工姓名
    );
END $$

DELIMITER ;


-- 假設我們要刪除編號為7369的員工
DELETE FROM emp WHERE empno = 7369;


-- 檢查日誌表，看看自動紀錄的內容
SELECT * FROM emp_audit_delete;




-- 改良版的刪除資料時觸發程序
-- 建立影子資料表
CREATE TABLE emp_recovery_archive (
    archive_id INT AUTO_INCREMENT PRIMARY KEY,
    deleted_by VARCHAR(100), -- 紀錄刪除者的帳號
    deleted_at DATETIME,     -- 紀錄刪除時間
    -- 以下為emp表的結構
    empno INT,
    ename VARCHAR(16),
    job VARCHAR(16),
    manager INT,
    hiredate DATE,
    salary FLOAT(7,2),
    comm FLOAT(7,2),
    deptno INT
);


-- 建立觸發程序
DELIMITER $$

CREATE TRIGGER tr_emp_full_archive
AFTER DELETE ON emp
FOR EACH ROW
BEGIN
    INSERT INTO emp_recovery_archive (
        deleted_by, deleted_at,
        empno, ename, job, manager, hiredate, salary, comm, deptno
    )
    VALUES (
        USER(), NOW(),
        OLD.empno, OLD.ename, OLD.job, OLD.manager, OLD.hiredate, OLD.salary, OLD.comm, OLD.deptno
    );
END $$

DELIMITER ;


-- 假設我們要刪除編號為7369的員工
DELETE FROM emp WHERE empno = 7369;

-- 檢查日誌表，看看自動紀錄的內容
SELECT * FROM emp_recovery_archive;




-- 改良影子資料表，增加「動作」欄位
CREATE TABLE emp_recovery_archive (
    archive_id INT AUTO_INCREMENT PRIMARY KEY,
    deleted_by VARCHAR(100),
    deleted_at DATETIME,
    action VARCHAR(10),       -- 新增：紀錄是 "DELETE" 還是 "UPDATE"
    -- 以下為emp表的結構
    empno INT,
    ename VARCHAR(16),
    job VARCHAR(16),
    manager INT,
    hiredate DATE,
    salary FLOAT(7,2),
    comm FLOAT(7,2),
    deptno INT
);


-- 處理「刪除」的程序
DELIMITER $$

CREATE TRIGGER tr_emp_after_delete
AFTER DELETE ON emp
FOR EACH ROW
BEGIN
    INSERT INTO emp_recovery_archive (
        deleted_by, deleted_at, action,
        empno, ename, job, manager, hiredate, salary, comm, deptno
    )
    VALUES (
        USER(), NOW(), "DELETE", -- 標記為刪除
        OLD.empno, OLD.ename, OLD.job, OLD.manager, OLD.hiredate, OLD.salary, OLD.comm, OLD.deptno
    );
END $$

DELIMITER ;


-- 處理「異動」的程序
DELIMITER $$

CREATE TRIGGER tr_emp_after_update
AFTER UPDATE ON emp
FOR EACH ROW
BEGIN
    INSERT INTO emp_recovery_archive (
        deleted_by, deleted_at, action,
        empno, ename, job, manager, hiredate, salary, comm, deptno
    )
    VALUES (
        USER(), NOW(), "UPDATE", -- 標記為更新
        OLD.empno, OLD.ename, OLD.job, OLD.manager, OLD.hiredate, OLD.salary, OLD.comm, OLD.deptno
    );
END $$

DELIMITER ;


-- 假設我們要刪除編號為7902的員工
DELETE FROM emp WHERE empno = 7902;


-- 修改員工KING(7839)的comm
UPDATE emp SET comm = 310 WHERE empno = 7839;

-- 檢查日誌表，看看自動紀錄的內容
SELECT * FROM emp_recovery_archive;



-- 還原記錄
INSERT INTO emp (empno, ename, job, manager, hiredate, salary, comm, deptno)
SELECT empno, ename, job, manager, hiredate, salary, comm, deptno
FROM emp_recovery_archive
WHERE empno = 7902 AND action = "DELETE"
LIMIT 1;   -- 確保即便影子表有多筆紀錄，也只會還原一筆回去，避免主鍵衝突報錯


-- 確認資料是否有還原
SELECT * FROM emp WHERE empno = 7902;


-- 清理影子表(選擇性)
DELETE FROM emp_recovery_archive WHERE empno = 7902;



-- 查看指定表格綁定幾個觸發程序
SHOW TRIGGERS LIKE "emp";


-- 刪除觸發程序
DROP TRIGGER IF EXISTS tr_emp_after_update;



------------- 預處理程序 -------------
-- 建立預處理程序
PREPARE my_country FROM
'SELECT Code, Name, GNP FROM country WHERE Code = ?';


-- 使用預處理程序
SET @my_code = 'USA';
EXECUTE my_country USING @my_code;


SET @my_code = 'JPN';
EXECUTE my_country USING @my_code;



-- 根據國家代碼查詢該國人口超過一定數量的城市
PREPARE find_big_city FROM "SELECT Name, District, Population 
                            FROM world.city 
							WHERE CountryCode = ? AND Population > ?";


-- 使用預處理程序
SET @country = "TWN";
SET @min_pop = 500000;
EXECUTE find_big_city USING @country, @min_pop;

SET @country = "JPN";
SET @min_pop = 2000000;
EXECUTE find_big_city USING @country, @min_pop;



-- 查詢特定部門中，職稱符合要求的員工姓名與薪資
PREPARE check_emp_salary FROM "SELECT ename, job, salary 
                               FROM cmdev.emp 
							   WHERE deptno = ? AND job = ?";
							   

-- 使用預處理程序SET @dno = 10;
SET @dno = 10;
SET @job_title = "MANAGER";							   
EXECUTE check_emp_salary USING @dno, @job_title;


-- 查詢目前伺服器上正在運行的預處理程序數量
SHOW GLOBAL STATUS LIKE "prepared_stmt_count";


-- 預處理程序的詳細清單
SELECT * FROM performance_schema.prepared_statements_instances;


-- 刪除預處理程序
DEALLOCATE PREPARE check_emp_salary;



------------- HANDLER -------------
-- 建立一個新增員工的預存程序，如果員工編號重複，則會出現警告訊息
DELIMITER $$

CREATE PROCEDURE add_new_emp(IN p_empno INT, IN p_ename VARCHAR(50), IN p_sal DECIMAL(10,2))
BEGIN
    -- 定義：若發生1062錯誤(Duplicate Entry)，執行CONTINUE並顯示訊息
    DECLARE CONTINUE HANDLER FOR 1062 
    BEGIN
        SELECT "發生錯誤：員工編號 " AS Error, p_empno AS ID, " 員工編號已存在，請使用其他編號。" AS Message;
    END;

    -- 執行新增動作
    INSERT INTO cmdev.emp (empno, ename, salary) VALUES (p_empno, p_ename, p_sal);

    -- 因為是CONTINUE，所以即使重複，這行還是會執行
    SELECT "程序執行完畢" AS Status;
END $$

DELIMITER ;


-- 執行預存程序
CALL add_new_emp(7369, "marine", 1500);
CALL add_new_emp(9001, "marine", 1500);




-- 建立查詢員工薪資的函數，若員工不存在則回傳-1
DELIMITER $$

CREATE FUNCTION get_emp_salary(p_empno INT) RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE v_sal DECIMAL(10,2) DEFAULT 0;
    
    -- 定義：如果找不到資料，將薪資設為-1作為標記
    DECLARE CONTINUE HANDLER FOR NOT FOUND 
        SET v_sal = -1;

    -- 執行查詢
    SELECT salary INTO v_sal FROM cmdev.emp WHERE empno = p_empno;

    RETURN v_sal;
END $$

DELIMITER ;



-- 執行函數
SELECT get_emp_salary(9999);





-- 建立觸發程序(檢查寫入的薪資是否合理)
DELIMITER $$

CREATE TRIGGER before_emp_insert
BEFORE INSERT ON cmdev.emp
FOR EACH ROW
BEGIN
	-- 自定義錯誤：若薪資為負時則顯示「薪資不可為負數」訊息
    IF NEW.salary < 0 THEN
        SIGNAL SQLSTATE "45000" SET MESSAGE_TEXT = "薪資不可為負數";
    END IF;
END $$

DELIMITER ;

-- 執行
INSERT INTO cmdev.emp (empno, ename, salary) VALUE (9001, 'marine', -200);
