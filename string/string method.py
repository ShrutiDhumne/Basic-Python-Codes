name="ShRuTI"
print(len(name))
print(name.lower())
print(name.upper())
print(name.title())
print(name.count('u'))

# strip methods
a = "   shru  ti   "
print(a.lstrip())
print(a.rstrip())
print(a.strip())
print(a.replace(' ',''))
print(a.find('a'))

# center method

name1 = "Shruti"
print(name1.center(6+4,'&'))
print(name1.center(6+8,'*'))
print(name1.center(len(name)+1,'*'))
print(name1.center(7,'&'))

