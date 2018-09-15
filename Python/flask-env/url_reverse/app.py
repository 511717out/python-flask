# coding:utf-8
from flask import Flask,url_for

app = Flask(__name__)


@app.route('/')
def index():
    print url_for('my_list')
    print url_for('article',id='abc')
    return 'Hello World'

@app.route('/list/')
def my_list():
    return 'list'

@app.route('/article/<id>/')
def article(id):
    return u'您请求的id是：%s' % id

if __name__ == '__main__':
    app.run(debug=True)


'''
    1. 什么叫做反转URL：从视图函数到URL的转换叫做反转URL
    2. 反转URL的用处：
        * 在页面重定向的时候，会使用URL反转。
        * 在模板中也会使用URL反转。
        * 代码实例：

'''