name='check tests' #strings are immutable(cannot be changed)

# name[0] = 'm' # this is not possiple

a=len(name)
print(a)

print(name.upper(),name)
print(name.lower())
print(name.capitalize(),"  ",name.title())

text = '   hello python  '
print(text.strip())
print(text.lstrip())
print(text.rstrip())

print(text.find('t'))
print(text.replace('t','m'))

# split

fruits = 'Apples,Banana,Mangoes,Strawberries,Oranges'
print(fruits.split(','))

arr =  ['Apples', 'Banana', 'Mangoes', 'Strawberries', 'Oranges']
print(','.join(arr))

char = 'python123456'

print(char.isalpha())
print(char.isdigit())
print(char.isalnum())
print(char.isspace())