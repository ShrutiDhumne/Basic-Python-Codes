def fact(n):
    if n == 0 or n == 1:
        return n
    return n * fact(n-1)

num = int(input("Enter the number to find factorial : "))
print(f"Factioral of {num} is : {fact(num)}")