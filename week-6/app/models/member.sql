CREATE DATABASE `website`; -- 創建資料庫
USE `website`; -- 使用資料庫 

CREATE TABLE `member`( -- 創建表格 
    `id` BIGINT AUTO_INCREMENT, -- 獨立編號
    `name` VARCHAR(255) NOT NULL, -- 姓名
    `username` VARCHAR(255) NOT NULL, -- 帳戶名稱
    `password` VARCHAR(255) NOT NULL, -- 帳戶密碼
    `time` DATETIME NOT NULL DEFAULT NOW(), -- 註冊時間
    PRIMARY KEY(`id`)
);
DESCRIBE `member`; -- 查看表格 

DELETE FROM `member`;
ALTER TABLE `member` AUTO_INCREMENT = 1;

-- 新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test
INSERT INTO `member`(`name`, `username`, `password`) VALUES('test', 'test', 'test');
INSERT INTO `member`(`name`, `username`, `password`) VALUES('Bob', 'SpongeBob', '1111');
INSERT INTO `member`(`name`, `username`, `password`) VALUES('Star', 'Patrick', '2222');
INSERT INTO `member`(`name`, `username`, `password`) VALUES('Crab', 'Mr.Krabs', '3333');
INSERT INTO `member`(`name`, `username`, `password`) VALUES('Squirrel', 'Sandy', '4444');
