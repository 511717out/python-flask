#coding:utf-8
from flask import Flask,render_template,request,session,redirect,url_for,g
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
    print 'index'
    return 'index'


@app.route('/login/',methods=['GET','POST'])
def login():
    print 'login'
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhiliao' and password == '111111':
            session['username'] = 'zhiliao'
            return u'登录成功'
        else:
            return u'用户名或密码错误'


@app.route('/edit/')
def edit():
    if hasattr(g,'username'):
        return u'修改成功'
    else:
        return redirect(url_for('login'))

# before_requst:在请求之前执行的
# before_request:是在视图函数之前执行的
# before_request：这个函数只是一个装饰器，它可以把需要设置为钩子函数的代码放到视图函数之前执行


@app.before_request
def my_before_request():
    if session.get('username'):
        g.username = session.get('username')


if __name__ == '__main__':
    app.run(debug=True)
