user = {
    'name': 'arya',
    'age': 11,
    'hobbies': ['dance', 'reading']
}

more = {'class': '6th'}
user.update(more)
print(user)

# fromkeys method
# d = dict.fromkeys(("name","age","class"),"none")
# print(d)

# get method
# print(user.get('name'))
# print(user.get('names'))

# copy method
# user1 = user.copy()
# print(user)
# print(user1)

# popitem method  #it pops randomly
# p = user.popitem()
# print(p)
# print(user)

# pop method
p = user.pop('age')
print(p)
print(user)

