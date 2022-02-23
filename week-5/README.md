## Assignment - Week 5

#### 要求二：建立資料庫和資料表

```
CREATE DATABASE `website`; -- 創建資料庫
USE `website`; -- 使用資料庫 

CREATE TABLE `member`( -- 創建表格 
    `id` BIGINT AUTO_INCREMENT, -- 獨立編號
    `name` VARCHAR(255) NOT NULL, -- 姓名
    `username` VARCHAR(255) NOT NULL, -- 帳戶名稱
    `password` VARCHAR(255) NOT NULL, -- 帳戶密碼
    `follower_count` INT NOT NULL DEFAULT 0, -- 追蹤者數量
    `time` DATETIME NOT NULL DEFAULT NOW(), -- 註冊時間
    PRIMARY KEY(`id`)
);
DESCRIBE `member`; -- 查看表格 
```
![CREATE DATABASE](/images/1.png)
![CREATE DATABASE](/images/2.png)

#### 要求三：SQL CRUD

```
-- 新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test
INSERT INTO `member`(`name`, `username`, `password`) VALUES('test', 'test', 'test');

-- 接著繼續新增至少 4 筆隨意的資料
-- SpongeBob / Patrick / Mr.Krabs / Sandy
-- `id` > `name` > `username` > `password` > `follower_count` > `time`
INSERT INTO `member`(`name`, `username`, `password`) VALUES('Bob', 'SpongeBob', '1111');
INSERT INTO `member`(`name`, `username`, `password`) VALUES('Star', 'Patrick', '2222');
INSERT INTO `member`(`name`, `username`, `password`) VALUES('Crab', 'Mr.Krabs', '3333');
INSERT INTO `member`(`name`, `username`, `password`) VALUES('Squirrel', 'Sandy', '4444');
-- DELETE FROM `member` WHERE `id` = 2;

-- 1. 取得所有在 member 資料表中的會員資料
SELECT * FROM `member`; 
-- 2. 取得所有在 member 資料表中的會員資料 > 按照 time 欄位，由近到遠排序
SELECT * 
FROM `member`
ORDER BY `time` DESC;
-- 3. 取得 member 資料表中第 2 ~ 4 共三筆資料 > 按照 time 欄位，由近到遠排序
--    ( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
SELECT *
FROM `member`
ORDER BY `time` DESC
LIMIT 1, 3;
-- 4. 指令取得欄位 username 是 test 的會員資料
SELECT *
FROM `member`
WHERE `username` = 'test';
-- 5. 取得欄位 username 是 test 且 欄位 password 也是 test 的資料
SELECT *
FROM `member`
WHERE `username` = 'test' AND `password` = 'test';

-- 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
UPDATE `member`
SET `name` = 'test2'
WHERE `username` = 'test';
```
![CREATE DATABASE](/images/3.png)
![CREATE DATABASE](/images/4.png)
![CREATE DATABASE](/images/5.png)
![CREATE DATABASE](/images/6.png)
![CREATE DATABASE](/images/7.png)
![CREATE DATABASE](/images/8.png)

#### 要求四：SQL Aggregate Functions

```
-- 1. 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
SELECT COUNT(*) FROM `member`;
-- 2. 取得 member 資料表中，所有會員 follower_count 欄位的總和。
-- SpongeBob(99385) / Patrick(161425) / Mr.Krabs(16082) / Sandy(34734) > sum = 311626
UPDATE `member`
SET `follower_count` = 161425
WHERE `username` = 'Patrick';
SELECT SUM(`follower_count`) FROM `member`;
-- 3. 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
SELECT AVG(`follower_count`) FROM `member`;
```
![CREATE DATABASE](/images/9.png)
![CREATE DATABASE](/images/10.png)

#### 要求五：SQL JOIN (Optional)

```
-- 1. 在資料庫中，建立新資料表，取名字為 message。
CREATE TABLE `massage`(
    `id` BIGINT AUTO_INCREMENT, -- 獨立編號
    `member_id` BIGINT NOT NULL, -- 留言者會員編號
    `content` VARCHAR(255) NOT NULL, -- 留言內容
    `time` DATETIME NOT NULL DEFAULT NOW(), -- 留言時間
    PRIMARY KEY(`id`),
    FOREIGN KEY(`member_id`) REFERENCES `member` (`id`) ON DELETE CASCADE
);

INSERT INTO `massage`(`member_id`, `content`) VALUES(1, 'first comment');
INSERT INTO `massage`(`member_id`, `content`) VALUES(1, 'second comment');

INSERT INTO `massage`(`member_id`, `content`) VALUES(4, 'hello SpongeBob'); 
-- 第30行 DELETE FROM `member` WHERE `id` = 2; 
-- `id` : 1,2,3,4,5 > 1,3,4,5,6

INSERT INTO `massage`(`member_id`, `content`) VALUES(1, 'third comment');

-- 2. 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
SELECT `member`.`name`, `massage`.`content`
FROM `member` RIGHT JOIN `massage`
ON `member`.`id` = `massage`.`member_id`;

-- 3. 取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
SELECT `member`.`name`, `massage`.`content`
FROM `member` RIGHT JOIN `massage`
ON `member`.`id` = `massage`.`member_id`
WHERE `member`.`username` = 'test';
```
![CREATE DATABASE](/images/11.png)
![CREATE DATABASE](/images/12.png)
![CREATE DATABASE](/images/13.png)
![CREATE DATABASE](/images/14.png)
![CREATE DATABASE](/images/15.png)
![CREATE DATABASE](/images/16.png)





