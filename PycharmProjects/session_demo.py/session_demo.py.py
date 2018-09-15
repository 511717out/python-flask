#coding:utf-8

from flask import Flask,session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


# 添加数据到session中
# 操作session的时候，跟操作字典是一样的
# SECRET_KEY

@app.route('/')
def hello_world():
    session['username'] = 'zhiliao'
    # 如果没有指定ｓｅｓｓｉｏｎ的过期时间，那么默认是浏览器关闭之后就自动结束
    # 古国设置ｓｅｓｓｉｏｎ的ｐｅｒｍａｎｅｎｔ属性为Ｔｒｕｅ，那么过期时间是３１天
    session.permanent = True
    return 'Hello World!'

@app.route('/get/')
def get():
    # session['username']
    # session.get('username')
    return session.get('username')

@app.route('/delete/')
def delete():
    print session.get('username')
    session.pop('username')
    print session.get('username')
    return 'success'

@app.route('/clear/')
def delete():
    print session.get('username')
    # 删除session中的所有的数据
    session.clear('username')
    print session.get('username')
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
