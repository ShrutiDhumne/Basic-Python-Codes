user = {
    'name': 'arya',
    'age': 11,
    'hobbies': ['dance', 'reading']
}

# to print all keys
for i in user:
    print(i)

for i in user.keys():
    print(i)

# to print values
for i in user.values():
    print(i)

for i in user:
    print(user[i])

# to print all items
u=user.items()
print(u)

for key,val in user.items():
    print(f"key element is {key} having value {val}")

for i in user.items():
    print(i)