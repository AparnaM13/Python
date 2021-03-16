#Count the number of characters in a string
string=input("Enter the string : ")
c=0
for i in range(0,len(string)):
    if(string[i]!=' '):
        c=c+1
print("Number of characters in the given string =",c)