#Count the number of characters in a string
str = input("Enter a string: ")
count = 0
for i in str:
    if i.isalpha():
        count += 1

print("Number of charecters in "+str+" is: ", count)