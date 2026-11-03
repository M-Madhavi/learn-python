text ="Coding in python is fun"
count = 0
vowels = ['a','e','i','o','u']
# for i in range(1,len(text)):
#     # print(text[i])
#     if(text[i] == 'a' or text[i] =='e' or text[i] =='i' or text[i] =='o' or text[i] =='u'):
#         count += 1
# print(count)

for char in text.lower():
    # print(char)
    if(char in vowels):
        count +=1
print(f"there are {count} vowels in the sentence")


