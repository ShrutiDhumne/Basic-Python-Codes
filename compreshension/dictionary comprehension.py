square = {num : num**2 for num in range(1,11)}
print(square)

string = 'i am happy'
w = {ch : string.count(ch) for ch in string}
print(w)

# if
eo = {i:('even' if i%2==0 else 'odd') for i in range (1,11)}
print(eo)