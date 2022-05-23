#to get the square of first 10 numbers in list
square = [i**2 for i in range(1,11)]
print(square)

# to get negative numbers
negative = [-i for i in range(1,11)]
print(negative)

# to get first letters of string in list
# names=[]
# name = ['rohit','mohit','shm','ram','arayn']
# names = [names.append(i[0]) for i in name]
#
# # for i in name:
# #     names.append(i[0])
# print(names)

#using if statment to get even numbers
even1 = [i for i in range(1, 11) if(i%2==0)]
print(even1)

def num(l):
    return[str(i) for i in l if(type(i)==int or type(i)== float)]
print(num([1,2,3,4,'three','one',5.6]))

# if-else
num = [1,2,3,4,5,6,7,8,9,10]
new = [i**2 if(i%2==0) else i**3 for i in num]
print(new)

# nested list
nc = [[i for i in range(1,4)] for i in range(3)]
print(nc)