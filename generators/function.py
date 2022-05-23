def square ():
    for i in range(1,11):
        yield i**2
s = square()
for s1 in s :
    print(s1)

