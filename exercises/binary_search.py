def binary1(l1,key1):
    c = len(l1)//2
    i = 0
    j = int(len(l1)-1)
    while (i<j):
        if int(l1[c])==int(key1):
            return c
        elif int(key1) > int(l1[i]):
            i =c+1
        else:
            j =c-1
        c = (i+j)//2
    return 0

list1 = input("Enter sorted numbers seprated by space : ").split()
print(list1)
key1 = input("enter the element you want to search : ")
if binary1(list1,key1)== 0 :
    print("Element not found !!! ")
else :
    print("Element found !!!")


