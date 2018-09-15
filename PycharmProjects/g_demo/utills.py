#coding:utf-8
from flask import g


def login_log():
    print u'当前登录用户是：%s' % g.username