-- 创建maizi数据库
CREATE DATABASE IF NOT EXISTS `maizi` CHARACTER SET 'UTF8';

-- 打开数据库
USE `maizi`;

-- 创建学员表(user)
-- 编号 id
-- 用户名 username
-- 年龄 age
-- 性别 sex
-- 邮箱 email
-- 地址 addr
-- 生日 birth
-- 薪水 salary
-- 电话 tel
-- 是否结婚 married
-- 注意：当需要输入中文的时候，需要临时转换客户端的编码方式
-- SET NAMES GBK;
-- 字段注释 通过COMMENT 给字段添加注释


CREATE TABLE IF NOT EXISTS `user` (
id SMALLINT,
username VARCHAR(20),
age TINYINT,
sex ENUM('男','女','保密'),
email VARCHAR(50),
addr VARCHAR(200),
birth YEAR,
salary FLOAT(8,2),
tel INT,
married TINYINT(1) COMMENT '0代表未结婚，非0代表已婚'
)ENGINE=INNODB CHARSET=UTF8;



-- 创建课程表course
-- 编号cid
-- 课程名称courseName
-- 课程描述courseDesc
CREATE TABLE IF NOT EXISTS course(
    cid TINYINT,
    courseName VARCHAR(50),
    courseDesc VARCHAR(200)
);


-- 创建新闻分类表cms_cate
-- 编号，分类名称，分类描述
CREATE TABLE IF NOT EXISTS cms_cate(
    id TINYINT,
    cateName VARCHAR(50),
    cateDesc VARCHAR(200)
)ENGINE=MyISAM CHARSET=UTF8;


-- 创建新闻表cms_news
-- 编号，新闻标题，新闻内容，新闻发布时间，点击量，是否置顶
CREATE TABLE IF NOT EXISTS cms_news(
    id INT,
    title VARCHAR(50),
    content TEXT,
    pubTime INT,
    clickNum INT,
    isTop TINYINT(1) COMMENT '0代表不置顶，1代表置顶'
);

-- 查看cms_news表的表结构
DESC cms_news;
DESCRIBE cms_news;
SHOW COLUMNS FROM cms_news;


-- 测试整型
CREATE TABLE text1(
    num1 TINYINT,
    num2 SMALLINT,
    num3 MEDIUMINT,
    num4 INT,
    num5 BIGINT
);


-- 向表中插入记录INSERT tb1_name VALUE|VALUES(值,...)
INSERT text1 VALUES(-128,-32768,-8388608,-2147483648,-9223372036854775808);

-- 查询表中所有记录 SELECT * FROM tb1_name
SELECT * FROM text1;
-- 查询表中的某一个值
SELECT * FROM text1 WHERE num3=3.14;



-- 无符号UNSIGNED
CREATE TABLE text2(
    num1 TINYINT UNSIGNED,
    num2 TINYINT
);
-- 插入值 测试有符号无符号的区别
INSERT text2 VALUES(0,-12);
-- mysql> INSERT text2 VALUES(-10,-12);
-- ERROR 1264 (22003): Out of range value for column 'num1' at row 1


-- 零填充 ZEROFILL  加入零填充的时候自动无符号了
CREATE TABLE text3(
    num1 TINYINT ZEROFILL,
    num2 SMALLINT ZEROFILL,
    num3 MEDIUMINT ZEROFILL,
    num4 INT ZEROFILL,
    num5 BIGINT ZEROFILL
);
-- 插入数据
INSERT text3 VALUES(1,1,1,1,1);
-- 查询表中所有记录
SELECT * FROM text3;


-- 测试浮点类型
-- 定点数是以字符串形式存储的 精度比较高

CREATE TABLE text4(
    num1 FLOAT(6,2),
    num2 DOUBLE(6,2),
    num3 DECIMAL(6,2)
);
-- 表中插入数据
INSERT text4 VALUES(3.1415,3.1415,3.1415);
INSERT text4 VALUES(3.2495,3.2495,3.2495);

-- 查询表中的某一个值
SELECT * FROM text4 WHERE num3=3.14;