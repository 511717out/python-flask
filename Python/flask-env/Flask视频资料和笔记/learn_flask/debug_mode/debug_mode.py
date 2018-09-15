#encoding: utf-8

from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return '我是知了课堂'


if __name__ == '__main__':
    app.run()
