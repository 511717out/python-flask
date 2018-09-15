#coding:utf-8

from flask_script import Manager
from migrate_demo import app
from flask_migrate import Migrate,MigrateCommand
from exts import db
from models import Article

# init 初始化迁移环境
# migrate 生成迁移文件
# upgrade
# 数据库迁移一般分为两步
#
# 生成迁移的脚本
# 运行脚本，更改数据库
# 模型 -> 迁移文件 -> 表


manager = Manager(app)

# 1. 要使用flask——migrate，必须绑定app和db
migrate = Migrate(app,db)

# 2. 把MigrateCommand命令添加到manader中
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()