def bs(l1):
    a = len(l1)
    for i in range(a):
        for j in range(0,a - i - 1):
            if int(l1[j]) > int(l1[j + 1]):
                l1[j], l1[j + 1] = l1[j + 1], l1[j]
    return l1

list1 = input("Enter the numbers to sort : ").split(",")
print(bs(list1))

