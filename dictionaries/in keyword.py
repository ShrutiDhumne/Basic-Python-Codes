user = {
    'name':'arya',
    'age':11,
    'hobbies':['dance','reading']
}
print(user)

# for keys
if 'name' in user:
    print('present')
else:
    print('absent')

# for values
if 'arya' in user.values():
    print('present')
else:
    print('absent')



