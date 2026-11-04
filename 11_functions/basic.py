def average(a,b,c):
    d= (a+b+c)/3.0
    return d

avg = average(4,5,6)
print(avg)


def add(a,b,plus=0): #params
    return a+b+plus #plus is default arg

sum = add(4,9,2)#args
print(sum)


c1= add(b=5,a=19) # keyword arguments
print("c1",c1)