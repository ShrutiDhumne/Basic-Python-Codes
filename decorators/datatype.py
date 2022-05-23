from functools import wraps
def out(n):
    def outer(function):
      def inner(*args,**kwargs):
        print("start")
        return function(*args,**kwargs)
    return inner()

@out(int)
def add(*args):
    i = 0
    for arg in args:
        i = i + arg
    print(i)
add(1,2,3,4)
