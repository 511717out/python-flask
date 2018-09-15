# coding:utf-8
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'username': u'王瑞',
        'gender': u'男',
        'age': u'18'
    }
    # 第一种方法直接在后面写
    # return render_template('index.html', username=u'王瑞', 'gender': u'男',)
    # 第二种方法：用字典
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
