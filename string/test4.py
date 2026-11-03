palindrome = input("Enter the string: ")

reverse = palindrome[::-1]
print("reversed string",reverse)

if(palindrome == reverse):
    print('Entered string is palindrome')
else:
    print('Not a palindrome')