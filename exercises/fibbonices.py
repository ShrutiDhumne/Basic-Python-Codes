def fibbo(n):
    a,b = 0,1
    i=0
    if n==0:
        print(0)
    elif n==1:
        print(1)
    else:
        while i<n:
            c = a+b
            a,b = b,c
            print(a)
            i+=1


num = int(input("Enter the number : "))
fibbo(num)

