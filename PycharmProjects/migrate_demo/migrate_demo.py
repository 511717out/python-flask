#coding:utf-8

from flask import Flask
from exts import db
from models import Article
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


# 新建一个article模型，采用models分开模式
# flask-script方式


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
