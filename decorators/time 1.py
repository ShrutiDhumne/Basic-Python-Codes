from functools import wraps
import time
def out_func(function):
    def infunc(*args,**kwrgs):
        t1 = time.time()
        ret = function()
        t2 = time.time()
        print(f"Time taken if {t2-t1}")
        return ret
    return infunc
@out_func
def print1(*args,**kwargs):
    for i in range(1,1001):
        print(i)

print1()


