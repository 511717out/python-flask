### MySQL学习：

#### 登录和退出的几种方式：

1. 登录：
    * mysql -u用户名 -p     (回车然后输入密码)
    * mysql -u用户名 -p密码 (密码跟在-p的后面：密码是明文显示出来的mysql会提示此种登录方式不安全)
2. 退出：
    * exit
    * quit
    * ctrl+c
#### 修改命令提示符
1. 连接客户端时通过参数指定：
    -uroot -proot --prompt 提示符
2. 连接客户端后，通过prompt命令修改
    1. 命令提示符常用参数：
    * \D:完整日期
    * \d:当前数据库
    * \h:服务器名称
    * \u:当前用户名
3. MySQL常用命令
    * select version();显示当前版本
    * select now();显示当前日期时间
    * select user();显示当前用户
    * DELIMITER 修改默认的分隔符
4. 开启输出日志
    * \T 保存路径 保存的文件名
    * \t 退出输出日志


#### 数据库的操作(DDL)

##### 1. 创建数据库
1. 完整示例：'CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name [[DEFAULT]CHARACTER SET[=]charset_name]'
    1. 这两种简单的方式创建数据库的方法都可以：实例中的 | 代表着它或者它都可以任选一个就行
        * CREATE DATABASE 数据库名称
        * CREATE SCHEMA 数据库名称
    2. 数据库会越来越多，创建数据库前先验证数据库存不存在，如果数据库名称不存在我们再来创建，这样可以避免数据库重名带来的麻烦
        * CREATE DATABASE IF NOT EXISTS 数据库名称
    3. 查看上一步命令所产生的警告：
        * SHOW WARNINGS;
    4. 创建数据库，并在创建之前检查数据库是否存在，并指定此数据库的默认字符集编码格式
        * 创建数据库时指定数据库字符集编码'DEFAULT CHARACTER SET = 'GBK';'
        * CREATE DATABASE IF NOT EXISTS 数据库名称 DEFAULT CHARACTER SET = '编码格式'
##### 2. 查看当前服务器下的数据库列表
1. 完整示例：SHOW {DATABASES|SCHEMAS}
    * SHOW DATABASES;
    * SHOW SCHEMAS;
2. 查看指定数据库的定义：
    * SHOW CREATE {DATABASE|SCHEMA} db_name
3. 修改指定数据库的编码方式
    * ALTER {DATABASE|SCHEMA} db_name [DEFAULT] CHARACTER SET [=] charset_name
4. 打开指定数据库
    * USE db_name
5. 得到当前打开的数据库的名称
    * SELECT DATABASE() | SCHEMA()
6. 删除指定的数据库，如果数据库存在在删除
    * DROP {DATABASE|SCHEMA} [IF EXISTS] db_name

##### 如何查看mysql的存储引擎

1. 查看mysql支持的存储引擎：

    'SHOW ENGINES\G'

2. 查看显示支持的存储引擎信息：

    'SHOW VARIABLES LIKE 'have%' '

3. 查看默认的存储引擎：

    'SHOW VARIABLES LIKE 'storage_engine' '


##### 如何查看数据库中的数据表以及表结构
1. 查看数据库下的数据表
    SHOW TABLES