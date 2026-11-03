string = 'hey, strings in python'
#         -22              .... -2-1

print(string[-2])
print(len(string))
print(string[-4]) # -4+length of the string = -4+22 = 18
print(string[18])

# slicing

print(string[0:6]) #goes from 0 to 5 -> hey, s
print(string[2:-1])# 2 to -1+22 = 21 same as [2:21] ->y, strings in pytho

# slicing with step

test = 'SOMERANDOMTEXTTOTEST'
print(len(test))

# print(test[0:10:n]) #skip n-1 characters

print(test[0:10:1])# skip 0 characters -> SOMERANDOM
print(test[0:10:3])# skip 2 characters(3-1) in between the string -> SENM

print(string[:4]) # replace the first empty number with 0->gets string from 0 to 3 indexes ->hey, -> [0:4]
print(string[1:]) # Replace the second empty number with length-1 -> skips the number of characters in first place and prints the remaining->ey, strings in python ->[1:len]

