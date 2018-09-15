#coding:utf-8
from flask import Flask,g,render_template,request
from utills import login_log

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhiliao' and password == '111111':
            # 就认为当前这个用户名和密码正确
            g.username = 'zhiliao'
            login_log()
            return u'恭喜登录成功'
        else:
            return u'您的用户名或密码错误！'



if __name__ == '__main__':
    app.run(debug=True)
