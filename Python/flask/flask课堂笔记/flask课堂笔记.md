### flask基本讲解
'''

    # encoding: utf-8

    # 从flask这个框架中导入flask这个类
    from flask import Flask

    # 初始化一个flask对象
    # flask()
    # 需要传递一个参数__name__
    # 1.方便flask框架去寻找资源
    # 2.方便flask插件比如flask-Sqlalchemy出现错误的时候，去寻找问题所在的位置
    app = Flask(__name__)

    # @app.route是一个装饰器
    # @开头，并且在函数的上面，说明是装饰器
    # 这个装饰器的作用，是做一个URL与视图函数的映射
    # 127。0.0.1:5000/   -> 去请求hello——world这个函数，然后将结果返回给浏览器
    @app.route('/')
    def hello_world():
        return 'Hello World!'

    # 如果当前这个文件是作为入口程序运行，南无就执行app.run()
    if __name__ == '__main__':
        # 启动一个应用服务器来接收用户的请求
        # whlie True:
        #   listen()
        app.run()

'''

### debug模式
1. 在app.run()中传入一个关键字参数debug,app.run(debug=True),就设置当前项目为debug模式
2. debug模式的两大功能：
    * 当程序出现问题的时候，可以在页面中看到错误信息和出错的位置
    * 只要修改了项目中的Python文件，程序会自动加载，不需要手动重新启动服务器。

### 使用配置文件：
1. 新建一个config.py文件
2. 在主app文件中导入这个文件，并且配置到app中，示例代码如下：

        '''
           import config
           app.config.from_object(config)
        '''
3. 还有许多其他的参数，都是放在这个配置文件中，比如'SECRET_KEY'和'SQLALCHEMY'这些配置都是在这个文件中 


### URL传参数：
1. 参数的作用：可以在相同的URL，但是指定不同的参数，来加载 不同的数据。
2. 在flask中如何使用参数:

        '''
            @app.route('/article/<id>')
            def article(id):
                return u'您请求的参数是：%s' % id
        '''
    * 参数需要放在两个尖括号中
    * 视图函数中需要放和URL中同名的参数


### 反转URL：
1. 什么叫做反转URL：从视图函数到URL的转换叫做反转URL
2. 反转URL的用处：
    * 在页面重定向的时候，会使用URL反转。
    * 在模板中也会使用URL反转。
    * 代码实例:

    '''
    
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

### 页面跳转和重定向
1. 用处：在用户访问一些需要登录的页面的时候，如果用户没有登录，那么可以让他重定向到登录的页面。
2. 代码实现：

    '''

        from flask import Flask, redirect, url_for

        app = Flask(__name__)


        @app.route('/')
        def index():
            # return redirect('/login/')
            login_url = url_for('login')
            return redirect(login_url)
            return u'这是首页'


        @app.route('/login/')
        def login():
            return u'这是登录页面'


        @app.route('/question/<is_login>')
        def question(is_login):
            if is_login == '1':
                return u'这是发布问答页面'
            else:
                return redirect(url_for('login'))


        if __name__ == '__main__':
            app.run(debug=True)

    '''


### Flask渲染Jinja2模板和传参
1. 如何渲染模板：
    * 模板放在'templates'文件夹下
    * 从'flask'种导入'render_template'函数。
    * 在视图函数中，使用'render_template'函数，渲染模板。注意：只需要填写模板的名字，不需要填写'tenplates'这个文件夹的路径。
2. 模板传参：
    * 如果只有一个或者少量的参数，直接在'render_template'函数中添加关键字就可以了。
    * 如果有多个参数的时候，那么可以先把所有的参数放在字典中，然后在'render_template'中，使用两个星号，把字典转换成关键参数传递进去，这样的代码更方便管理和使用。
3. 在模板中，如果要使用一个变量，语法是：'{{params}}'
4. 访问模型中的属性或者字典，可以通过'{{params.property}}'的形式，或者是使用'{{params['age']}}'。

### if判断
1. 语法：

    '''

        {% if xxx%}  # 开始
        {% else %}
        {% endif %}  # 结束语句

    '''
2. if的使用，可以和python中相差无几

### for循环遍历列表和字典：
1. 字典的遍历，语法'python'一样，可以使用'items()','keys()','values()','iteritems()','iterkeys','itervalues'。
    * 示例代码：

    '''

        {% for k,v in user.items() %}
            <p>{{ k }}: {{ v }}</p>
        {% endfor %}
    '''

2.列表的遍历：语法和'python'一样

    '''

        {% for website in websites %}
        <p>{{ website }}</p>
        {% endfor %}
    '''


### 过滤器
1. 介绍和语法：
    * 介绍：过滤器可以处理变量，把原始的变量经过处理后再展示出来，作用的对象是变量。
    * 语法：

    '''

        {{ avatar|default('xxx)}}
    '''
2. defailt过滤器：如果当前变量不存在，这时候可以指定默认值。
3. length过滤器：求列表或者字符串或者字典或者元祖的长度。


### 继承和block
1. 继承作用和语法：
    * 作用：可以吧一些公共的代码放在父模板中，避免每个模板写相同的代码，太麻烦。
    * 语法：

    '''

        {% extends 'base.html' %}
    '''
2. block实现：
    * 作用：可以让子模板实现一些自己的需求，父模板需要提前定义好。
    * 注意点：子模板中的代码必须放在block中
    * 代码：

    '''

         {% balock main %}
            <h1>这是首页<h1>
         {% endblock %}
    '''


### 加载静态文件
1. 语法：' url_for('static',filename='路径') '
2. 静态文件，flask会从'static'文件夹中来时寻找，所以不需要再写'static'这个路径了。
3. 可以加载css文件可以加载js文件还有image文件。



### MySQL
##### 安装
1. windows10直接在mysql官网下载64位的安装离线程序安装就可以了
2. Linux：


##### MySQL-python中间件的介绍与安装
1. 如果是在类Unix系统上，直接进入到虚拟环境，输入'sudo pip install mysql-python'.
2. windows上，需要在这里下载'https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python'
下载'MySQL_python-1.2.5-cp27-none-win_amd64.whl'然后在命令行中进入到'MySQL_python-1.2.5-cp27-none-win_amd64.whl'所在的目录，输入一下命令安装：

'''

    pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl
'''

##### flask-SQLAlchemy的介绍与安装
1. ORM：Obiect Relationship Mapping(模型关系映射)。
2. flask-SQLAlchemy是一套ORM框架。
3. ORM的好处：可以让我们操作数据库跟操作对象一样，非常方便。因为一个表就抽象成一个类，一条数据就抽象成该类的对象。
4. 安装'flask-SQLAlchemy'：
    '''

        sudo pip install flask-sqlalchemy
    '''

##### Flask-SQLAlchemy的使用：
1. 初始化和设置数据库信息：
    * 使用flask-sqlalchemy中的SQLAlchemy进行初始化：

    '''

        from flask_sqlalchemy import SQLAlchemy
        app = Flask(__name__)
        db = SQLAlchemy(app)
    '''
2. 设置配置信息：在'config.py'文件中添加一下配置信息：

    '''

        # dialect+driver：//username:password@host/database
        DIALECT = 'mysql'
        DRIVER = 'mysqldb'
        USERNAME = 'root'
        PASSWORD = 'root'
        HOST = '127.0.0.1'
        PORT = '3306'
        DATABASE = 'db_demo1'

        SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,
                                                    PORT,DATABASE)


        SQLALCHEMY_TRACK_MODIFICATIONS = False
    '''
3. 在主'app'文件中，添加配置文件

    '''

        app = Flask(__name__)
        app.config.from_object(config)
        db = SQLAlchemy(app)
    '''
4. 做测试，看有没有问题

    '''

        db.create_all()
    '''
    
    如果没有报错，说明配置没有问题，如果有错误可以根据错误进行修改。

##### 使用flask-SQLAlchemy创建模型与表的映射：
1. 模型需要继承自'db.Model',然后需要映射到表中的属性，必须写成'db.Column'的数据类型。
2. 数据类型：
    * 'db.Integer'代表的是整形
    * 'db.String'代表的是‘varchar’，需要指定最长的长度。
    * 'db.Text'代表的是text。
3. 其他参数：
    * 'primary_key':代表的是将这个字段设置为主键。
    * 'autoincrement':代表的是这个主键为自增长的。
    * 'nullable': 代表的是这个字段是否可以为空，默认为空，设置为False在数据库中值就不能为空了
4. 最后需要调用'db.create_all'来将模型创建到数据库中。

##### Flask-SQLAlchemy数据的增，删，改，查：
1. 增：

    '''

        # 增加
        article1 = Article(title='aaa',content='bbb')
        db.session.add(article1)
        # 事物
        db.session.commit()
    '''
2. 查：

    '''

        # 查
        # select * from article where article.title='aaa'
        article1 = Article.query.filter(Article.title == 'aaa').first()
        print 'title:%s' % article1.title
        print 'content:%s' % article1.content
    '''
3. 改：

    '''

        # 改
        # 1. 先把你要更改的数据查找出来
        article1 = Article.query.filter(Article.title == 'aaa').first()
        # 2. 把这条数据，你需要修改的地方进行修改
        article1.title = 'new title'
        # 3. 做事物的提交
        db.session.commit()
    '''
4. 删：

    '''

        # 删
        # 1. 把需要删除的数据查找出来
        article1 = Article.query.filter(Article.content == 'bbb').first()
        # 2. 把这条数据删除掉
        db.session.delete(article1)
        # 3. 做事物提交
        db.session.commit()
    '''

##### Flask-SQLAlchemy外键及其关系：
1. 外键：

    '''

        class User(db.Model):
            __tablename__ = 'user'
            id = db.Column(db.Integer,primary_key=True,autoincrement=True)
            username = db.Column(db.String(100),nullable=False)

        class Article(db.Model):
            __tablename__ = 'article'
            id = db.Column(db.Integer,primary_key=True,autoincrement=True)
            title = db.Column(db.String(100),nullable=False)
            content = db.Column(db.Text,nullable=False)
            author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

            author = db.relationship('User',backref=db.backref('articles'))

        db.create_all()
    '''
2. 'author = db.relationship('User',backref=db.backref('articles'))'解释：
    * 给'Article'这个模型添加一个'author'
        属性，可以访问这篇文章的作者的数据，像访问不同模型一样。
    * 'backref'是定义反向引用，可以通过'User.articles'访问这个模型所写的所有的文章。
3. 多对多：
    * 多对多的关系，要通过一个中间表进行关联。
    * 中间表，不能通过'class'的方式实现，只能通过'db.Table'的方式实现。
    * 设置关联：'tags = db.relationship('Tag',secondary=article_tag,backref=db.backref('articles'))'需要使用一个关键字参数'secondary=中间表'来进行关联。
    * 访问和数据添加可以通过一下方式进行操作：
        - 添加数据：
            '''

                article1 = Article(title='aaa')
                article2 = Article(title='bbb')

                tag1 = Tag(name='111')
                tag2 = Tag(name='222')

                article1.tags.append(tag1)
                article1.tags.append(tag2)

                article2.tags.append(tag1)
                article2.tags.append(tag2)

                db.session.add(article1)
                db.session.add(article2)

                db.session.add(tag1)
                db.session.add(tag2)

                db.session.commit()
            '''
        - 访问数据：
            '''

                article1 = Article.query.filter(Article.title == 'aaa').first()
                tags = article1.tags
                for tag in tags:
                    print tag.name
            '''


##### Flask-Script的介绍安装：
1. Flask-Script：Flask——Script的作用是可以通过命令行的形式来操作Flask。例如通过命令跑一个开发版本的服务器，设置数据库，定时任务等。
2. 安装：首先进入到虚拟环境中，然后'pip install flask-script'来进行安装。
3. 如果直接在主'manage.py'中写命令，那么终端就只需要'python manage.py command_name'就可以了。
4. 如果把一些命令集中在一个文件中，那么就需要在终端输入一个父命令，比如'python manage.py db init'。
5. 例子：
    '''

        from flask_script import Manager
        from flask_script_demo import app
        from db_script import DBManager

        manager = Manager(app)


        # 数据库相关的操作，都放在一起

        @manager.command
        def runaerver():
            print '服务器跑起来了'

        manager.add_command('db',DBManager)
    '''
6. 有子命令的例子：
    '''

        from flask_script import Manager

        DBManager = Manager()

        @DBManager.command
        def init():
            print '数据库初始化完成'

        @DBManager.command
        def migrate():
            print '数据表迁移成功'
    '''
##### 分开'models'以及解决循环引用：
1. 分开models的目的：为了让代码更加方便的管理。
2. 如何解决循环引用：把'db'放在一个单独的文件中，切断循环引用的线条就可以了。


##### Flask-Migrate的介绍与安装：
1. 介绍：因为采用'db.craete_all'子后期修改字段的时候，不会自动的映射到数据库中，必须删除表，然后重新运行'db.craete_all'才会重新映射，这样不符合我们的需求，因此flask-migrate就是为了解决这个问题，他可以在每次修改模型后，可以将修改的东西映射到数据库中。
2. 首先进入到你的虚拟环境中然后使用'pip install flask-migrate'进行安装就可以了。
3. 使用'falsk_migrate'必须借助'flask_scripts',这个包的'MigrateCommand'中包含了所有和数据库相关的命令。
4. 'flask_migrate'相关的命令：
    * 'python manage.py db init':初始化一个迁移脚本的环境，只需要执行一次。
    * 'python manage.py db migrate':将模型生成迁移文件，只要模型更改了，就需要执行一遍这个命令。

    * 'python manage.py db upgrade':将迁移文件真正的映射到数据库中。每次运行migrate命令后，就记得要运行这个命令。
5. 注意点：需要将你想要映射到数据库中的模型，都要导入到manage.py文件中，如果没有导入进去就不会映射到数据库中
6. 'manage.py'相关代码：

    '''

        from flask_script import Manager
        from migrate_demo import app
        from flask_migrate import Migrate,MigrateCommand
        from exts import db
        from models import Article

        # init 初始化迁移环境
        # migrate 生成迁移文件
        # upgrade
        # 数据库迁移一般分为两步
        #
        # 生成迁移的脚本
        # 运行脚本，更改数据库
        # 模型 -> 迁移文件 -> 表


        manager = Manager(app)

        # 1. 要使用flask——migrate，必须绑定app和db
        migrate = Migrate(app,db)

        # 2. 把MigrateCommand命令添加到manader中
        manager.add_command('db',MigrateCommand)


        if __name__ == '__main__':
            manager.run()
    '''

##### cookie:
1. 'cookie'出现的原因：在网站中，http是无状态的。也就是说即使第一次和服务器链接后并且登录成功后，第二次请求服务器依然不能知道当前请求的是那个用户。cookie的出现就是为了解决这个问题，第一次登录后服务器返回一些数据cookie给浏览器，然后浏览器保存在本地，当该用户发送第二次请求的时候，就会自动的把上次请求存储的cookie数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前的用户是哪个了。
2. 如果服务器返回了cookie给浏览器，南无浏览器下次在请求相同的服务器的时候，就会自动的把cookie发送给服务器，这个过程用户根本不需要管。
3. cookie是保存在浏览器中的，相对的是浏览器。


##### session:
1. session介绍：session和cookie的作用有点类似，都是为了存储用户相关的信息，不同的是，cookie是存储在本地浏览器，为session存储在服务器。存储在服务器的数据会更加安全，不容易被窃取，但存储在服务器也有一定的弊端，就是会占用服务器的资源，但现在服务器已经发展至今，一些session信息还是绰绰有余的。
2. 使用session的好处：
    * 敏感数据不是直接发送给浏览器，而是发送会一个session_id,服务器将session_id和敏感数据做一个映射存储在session（服务器上面）中，更加安全。
    * session可以设置过期时间，也从另外一方面，保证了用户的账号安全。

##### flask中的session工作机制：
1. flask中的session机制是：把敏感数据经过加密后放入session中，然后在把session存储到cookie中，下次请求的时候。再从浏览器发送过来的cookie中读取session，然后在从session中读取敏感数据，并进行解密，获取最终的用户数据。
2. flask的这种session机制，可以节省服务器的开销，因为把所有的信息都存储在客户端（浏览器）。
3. 安全是相对的，把session放到cookie中经过加密也是比较安全的，这点大家放心使用就可以了。

##### 操作session：
1. session的操作方式：
    * 使用session需要flask中导入session，以后所有和session相关的操作都是通过这个变量来的。
    * 使用session需要设置SECRET_KEY，用来作为加密用的。并且这个SECRET_KEY,如果每次服务器启动都变化的话，那么之前的ｓｅｓｓｉｏｎ就不能通过当前这个SECRET_KEY进行解密了。
    * 操作ｓｅｓｓｉｏｎ的时候，跟操作字典是一样的。
    * 添加ｓｅｓｓｉｏｎ：'session['username']'
    * 删除ｓｅｓｓｉｏｎ：session.pop('username')或者del session['username']
    * 清除所有ｓｅｓｓｉｏｎ：'session.clear()'
    * 获取ｓｅｓｓｉｏｎ：　'session.get(username)'
2. 设置ｓｅｓｓｉｏｎ的过期时间：
    * 如果没有指定ｓｅｓｓｉｏｎ的过期时间，那么默认是浏览器关闭之后就自动结束
    * 如果设置ｓｅｓｓｉｏｎ的ｐｅｒｍａｎｅｎｔ属性为Ｔｒｕｅ，那么过期时间是３１天
    * 可以通过给'app.config'设置'PERMANENT_SESSION_LIFETIME'来更改过期时间，这个值的数据类型是'datetime.timedelay'类型。

##### get请求post请求：
1. get请求：
    * 使用场景：如果只对服务器获取数据，并没有对服务器产生任何影响，那么这个时候使用get请求。
    * 传参：get请求传参是放在ＵＲＬ中的，并且是通过'?'的形式来指定key和value的。
2. post请求：
    * 使用场景：如果要对服务器产生影响，那么使用post请求。
    * post请求传参不是放在ＵＲＬ中的，是通过'from data'的形式发送给服务器的。


##### get和post请求获取参数：
1. get请求是通过'flask.request.args'来获取。
2. post请求是通过'flask.request.form'来获取
3. post请求在模板中要注意几点：
    * input标签中，要写name来标识value的key，方便后台获取。
    * 在写form表单的时候，要指定'method='post''并且要指定'action='/login/''。
4. 示例代码：
    '''

        <form action="{{ url_for('login') }}" method="post">
        <table>
            <tbody>
            <tr>
                <td>用户名：</td>
                <td><input type="text" placeholder="请输入用户名" name="username"></td>
            </tr>
                <tr>
                <td>密码：</td>
                <td><input type="text" placeholder="请输入密码" name="password"></td>
            　</tr>
                <tr>
                    <td></td>
                    <td><input type="submit" value="登录"></td>
                </tr>
            </tbody>
        </table>
    </form>
    '''


##### 保存全局变量的g属性：
g: global
1. g对象是专门保存用户的数据的
2. g对象在一次请求中的所有代码的地方，都是可以使用的。


##### 钩子函数（hook）
1. before_request:
    * 在请求之前执行的
    * 是在视图函数之前执行的
    * 这个函数只是一个装饰器，它可以把需要设置为钩子函数的代码放到视图函数执行之前来执行

2. context_processor:
    * 上下文处理器用该返回一个字典。字典中的key会在模板中当成变量来渲染。
    * 上下文处理器中返回的字典，在所有页面中都是可用的。
    * 被这个装饰器修饰的钩子函数，必须返回一个字典，即使为空也要返回。


##### 装饰器
1. 装饰器实际上就是一个函数，有两个特别之处
    1. 参数是一个函数
    2. 返回值是一个函数
2. 装饰器使用是通过@符号，放在函数上面
3. 装饰器中定义的函数，要使用*args,**kwargs两对兄弟的组合。并且在这个函数中执行原函数的时候也要把*args, **kwargs传进去。
4. 需要使用functiils.wraps在装饰器中的函数上把传进来的这个函数进行一个包裹，这样就不会丢失原来的函数__name__等属性
    * from functools import wraps