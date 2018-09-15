#encoding: utf-8
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    class Person(object):
        name = u'黄勇'
        age = 18

    p = Person()

    context = {
        'username': u'知了课堂',
        'gender': u'男',
        'age': 18,
        'person': p,
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    return render_template('anthoer/index.html',**context)


if __name__ == '__main__':
    app.run(debug=True)
