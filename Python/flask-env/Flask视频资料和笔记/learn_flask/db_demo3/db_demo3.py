#encoding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# # 用户表
# create table users (
#     id int primary key autoincrement,
#     username varchar(100) not null
# )
# # 文章表
# create table article (
#     id int primary key autoincrement,
#     title varchar(100) not null,
#     content text not null
#     author_id int,
#     foreign key `author_id` references `users.id`
# )

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship('User',backref=db.backref('articles'))

db.create_all()


@app.route('/')
def index():
    # 想要添加一篇文章，因为文章必须依赖用户而存在，所以首先的话，先添加一个用户
    # user1 = User(username='zhiliao')
    # db.session.add(user1)
    # db.session.commit()

    # article = Article(title='aaa',content='bbb',author_id=1)
    # db.session.add(article)
    # db.session.commit()

    # 我要找文章标题为aaa的这个作者
    # artile = Article.query.filter(Article.title == 'aaa').first()
    # author_id = artile.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print 'username:%s' % user.username

    # article.author
    # author = User.query.filter(User.username=='zhiliao').first()
    # author.articles

    # article = Article(title='aaa',content='bbb')
    # article.author = User.query.filter(User.id == 1).first()
    # db.session.add(article)
    # db.session.commit()

    # 我要找文章标题为aaa的这个作者
    # artile = Article.query.filter(Article.title == 'aaa').first()
    # print 'username:%s' % artile.author.username

    # 我要找到zhiliao 这个用户写过的所有文章
    # article = Article(title='111',content='222',author_id=1)
    # db.session.add(article)
    # db.session.commit()
    user = User.query.filter(User.username == 'zhiliao').first()
    result = user.articles
    for article in result:
        print '-'*10
        print article.title

    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
