
for i in range(1,5):
    print("*" * i)

# sum=0
# j=0
# while j<=100:
#     print(j)
#     sum +=j
#     j +=1
# print(sum)

password = 'MadhuVi'
entered_password = input("Enter password")

while(entered_password != password):
    entered_password = input("Entered password is wrong! try again")
print("Correct password!!!")