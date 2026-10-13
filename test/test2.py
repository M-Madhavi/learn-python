i=int(input("Enter a number: "))

if(i<0):
    print('the number is negative',i)
elif(i==0):
    print("the number is 0",i)
else:
    print("the number is positive",i)


num =int(input("Enter a number"))

if(num%2 == 0):
    print('entered number is even',num)
else:
    print("entered number is odd",num)



#match
day = int(input("Enter a number between 1 and 7: "))

match day:
    case 1:
        print("Day is monday")
    case 2:
        print("Day is tuesday")
    case 3:
        print("Day is wednesday")
    case 4:
        print("Day is thrusday")
    case 5:
        print("Day is friday")
    case 6:
        print("Day is saturday")
    case _:
        print("today is sunday!!")

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
operator = input("enter operator: ")

match operator:
    case '-':
        print(num1+num2)
    case '/':
        print (num1/num2)
    case '+':
        print(num1+num2)
    case '*':
        print(num1*num2)
