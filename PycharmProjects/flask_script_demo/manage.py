# coding:utf-8

from flask_script import Manager
from flask_script_demo import app
from db_script import DBManager

manager = Manager(app)


# 数据库相关的操作，都放在一起

@manager.command
def runaerver():
    print '服务器跑起来了'

manager.add_command('db',DBManager)