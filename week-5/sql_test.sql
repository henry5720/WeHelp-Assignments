CREATE DATABASE `sql_test`; -- 創建資料庫
SHOW DATABASES; -- 顯示資料庫 
DROP DATABASE `sql_test`; -- 刪除資料庫 

USE `sql_test`; -- 使用資料庫 
CREATE TABLE `student`( -- 創建表格 
	`student_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `major` VARCHAR(20),
    `score` INT
);

DESCRIBE `student`; -- 查看表格 
DROP TABLE `student`; -- 刪除表格 
ALTER TABLE `student` ADD gpa DECIMAL(3,2); -- 新增表格元素 
ALTER TABLE `student` DROP COLUMN gpa; -- 刪除表格元素 

SELECT * FROM `student`; -- 選擇全部資料(*)從表格(student)

INSERT INTO `student` VALUES(1, '小白', '英語', '50'); 
INSERT INTO `student` VALUES(2, '小黃', '生物', '90');
INSERT INTO `student` VALUES(3, '小綠', '歷史', '70');
INSERT INTO `student` VALUES(4, '小藍', '英語', '80');
INSERT INTO `student` VALUES(5, '小黑', '化學', '20');

SET SQL_SAFE_UPDATES=0; -- 關閉
UPDATE `student`
SET `major` = '生物'
WHERE `student_id` = 3;

DELETE FROM `student`
WHERE `score` <= 60;
SET SQL_SAFE_UPDATES=1; -- 結束後再開啟

-- 取得資料
SELECT * 
FROM `student` -- 選擇全部資料(*)從表格(student)
ORDER BY `score` ASC, `student_id` -- 以(score)排序 
-- 預設 ASC 由低到高 / DESC 由高到低
LIMIT 3 -- 限制回傳數量
WHERE `major` = '英語' OR `score` <> 70 -- 限制回傳條件 
WHERE `major` IN('歷史', '英語', '生物');

SELECT `name`, `major` FROM `student`;


-- A1.創建公司資料庫表格
CREATE TABLE `employee` (
	`emp_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `birth_date` DATE,
    `sex` VARCHAR(1),
    `salary` INT,
    `branch_id` INT,
    `sup_id` INT
);
DESCRIBE `employee`;

-- A2.創建部門表格 > 補上第一個表格(employee)的foreign key
CREATE TABLE `branch` (
	`branch_id` INT PRIMARY KEY,
    `branch_name` VARCHAR(20),
    `manager_id` INT,
    FOREIGN KEY (`manager_id`) REFERENCES `employee` (`emp_id`) ON DELETE SET NULL
);
DESCRIBE `branch`;

ALTER TABLE `employee`
ADD FOREIGN KEY (`branch_id`)
REFERENCES `branch` (`branch_id`)
ON DELETE SET NULL;

ALTER TABLE `employee`
ADD FOREIGN KEY (`sup_id`)
REFERENCES `employee` (`emp_id`)
ON DELETE SET NULL;

-- A3.創建客戶表格
CREATE TABLE `client` (
	`client_id` INT PRIMARY KEY,
    `client_name` VARCHAR(20),
    `phone` VARCHAR(20)
);
DESCRIBE `client`;

-- A4.創建合作表格
CREATE TABLE `works_with` (
	`emp_id` INT,
    `client_id` INT,
    `total_sales` INT,
    PRiMARY KEY (`emp_id`, `client_id`),
    FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`) ON DELETE CASCADE,
    FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`) ON DELETE CASCADE
);
DESCRIBE `works_with`


-- B1.新增員工資料
	INSERT INTO `employee` VALUES(206, '小黃', '1998-10-08', 'F', 50000, 1, NULL);
-- 出錯 > 創建時 FOREIGN KRY 未定義 

-- B2.先新增部門資料(manager_id 先設為 NULL) 
	INSERT INTO `branch` VALUES(1, '研發', NULL);
	INSERT INTO `branch` VALUES(2, '行政', NULL);
	INSERT INTO `branch` VALUES(3, '資訊', NULL);

-- B3.後新增員工資料
	INSERT INTO `employee` VALUES(206, '小黃', '1998-10-08', 'F', 50000, 1, NULL);
	INSERT INTO `employee` VALUES(207, '小綠', '1985-09-16', 'M', 29000, 2, 206);
	INSERT INTO `employee` VALUES(208, '小黑', '2000-12-19', 'M', 35000, 3, 206);
	INSERT INTO `employee` VALUES(209, '小白', '1997-01-22', 'F', 39000, 3, 207);
	INSERT INTO `employee` VALUES(210, '小蘭', '1925-11-10', 'F', 84000, 1, 207);

-- B4.跟新部門branch(manager_id)
	UPDATE `branch`
	SET `manager_id` = 208
	WHERE `branch_id` = 3;

-- B5.新增客戶資料
	INSERT INTO `client` VALUES(400, '阿狗', '2656496451');
	INSERT INTO `client` VALUES(401, '阿貓', '2656496451');
	INSERT INTO `client` VALUES(402, '旺來', '2656496451');
	INSERT INTO `client` VALUES(403, '露西', '2656496451');
	INSERT INTO `client` VALUES(404, '艾瑞克', '2656496451');

--  新增銷售金額
	INSERT INTO `works_with` VALUES(206, 400, '70000');
	INSERT INTO `works_with` VALUES(207, 401, '24000');
	INSERT INTO `works_with` VALUES(208, 402, '9800');
	INSERT INTO `works_with` VALUES(208, 403, '24000');
	INSERT INTO `works_with` VALUES(210, 404, '87940');


-- C. 練習
-- 1. 取得所有員工資料
SELECT * FROM `employee`;
-- 2.取得所有客戶資料
SELECT * FROM `client`;
-- 3.按薪水低到高取得員工資料
SELECT * FROM `employee`
ORDER BY `salary` ASC;
-- 4.取得薪水前3高的員工
SELECT * FROM `employee`
ORDER BY `salary` DESC
LIMIT 3;
-- 5.取得所有員工名字
SELECT `name` FROM `employee`;
-- 6.取得部門(不重複)
SELECT DISTINCT `branch_id` FROM `employee`;


-- D. aggregate function 聚合函數
-- 1.取得員工人數
SELECT COUNT(*) FROM `employee`;
-- 2.取得所有出生於 1970-01-01 之後的女性人數
SELECT COUNT(*) 
FROM `employee`
WHERE `birth_date` > '1970-01-01'
AND `sex` = 'F';
-- 3.取得所有員工的平均薪水 
SELECT AVG(`salary`) FROM `employee`;
-- 4.取得所有員工薪水的總和
SELECT SUM(`salary`) FROM `employee`;
-- 5.取得薪水最高的員工
SELECT MAX(`salary`) FROM `employee`; 


-- E. wildcards 萬用字原  % 代表多個字元, _ 代表一個字元
-- 1. 取得電話尾數451的客戶
SELECT * 
FROM `client` 
WHERE `phone` LIKE '%451';
-- 2.取得生日12月的員工 
SELECT * 
FROM `employee` 
WHERE `birth_date` LIKE '_____12%';


-- F. union 聯集
-- 1.員工名子 union 客戶名字 (a.搜尋數量一樣才能和 / b.資料型態也要一樣 ) 
SELECT `name` 
FROM `employee`
UNION 
SELECT `client_name` 
FROM `client`;


-- G. join 連接
INSERT INTO `branch` VALUES(4, '偷懶', NULL); 
-- 取得所有部門經理的名字 
SELECT `employee`.`emp_id`, `employee`.`name`, `branch`.`branch_name`
FROM `employee` LEFT JOIN `branch`
ON `employee`.`emp_id` = `branch`.`manager_id`;	


-- H. subquery 子查詢

-- 1.找出研發部門經理的名字
SELECT `name`
FROM `employee`
WhERE `emp_id` = (
	SELECT `manager_id` 
	FROM `branch`
	WHERE `branch_name` = '研發'
);

-- 2.找出單一客戶銷售金額超過50000的員工名字
SELECT `name`
FROM `employee`
WHERE `emp_id` IN(	-- 因為結果超過一筆不能用 = 
	SELECT `emp_id`
	FROM `works_with`
	WHERE `total_sales` > 50000 
);


