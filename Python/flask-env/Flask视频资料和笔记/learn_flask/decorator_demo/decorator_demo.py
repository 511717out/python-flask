#encoding: utf-8

from functools import wraps

# 装饰器实际上就是一个函数
# 有两个特别之处
# 1. 参数是一个函数
# 2. 返回值是一个函数


# 在打印run之前，先要打印一个hello world
# 在所有的函数执行之前，都要打印一个hello world


# 1. 装饰器使用是通过@符号，放在函数的上面
# 2. 装饰器中定义的函数，要使用*args,**kwargs两对兄弟的组合。并且在这个函数中执行原始函数的时候也要把*args,**kwargs传进去。
# 3. 需要使用functools.wraps在装饰器中的函数上把传进来的这个函数进行一个包裹，这样就不会丢失原来的函数的__name__等属性。

def my_log(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        print 'hello world'
        func(*args,**kwargs)

    return wrapper

@my_log
def run():
    print 'run'

# run = my_log(run) = wrapper
#
# run.__name__代表的是run这个函数的名称
print '-'*10
print run.__name__
print '-'*10
#
# wrapper()
#
# print 'hello world'
# func() = print 'run'

@my_log
def add(a,b):
    c = a + b
    print u'结果是：%s' % c

# add(1,2)

# run()

add(1,2)