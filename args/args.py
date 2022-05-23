def total1(*args):
    sum  = 0
    for num in args:
        sum += num
    return sum
print(total1(1,2,3,4))