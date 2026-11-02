name = 'your name'
print(name[0],name[-1],len(name))

str1='hello'
str2='world'

print(str1+" "+str2)
print(str1,str2)


text = 'Python Programming'

print(text[0:6])
print(text[12:])
print(text[-6:])

# skip character
print(text[0:len(text):2])
print(text[::2])

# reverse string using slicing

print(text[::-1])

strmethods = '   hey test the array methods   '
check = '123abc'
print(check.isalnum())

print(strmethods.strip())
print(strmethods.title())
print(strmethods.count('o'))
