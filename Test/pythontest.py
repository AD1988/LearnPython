import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s:'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log('WTF')
def func():
    print('test')

func()