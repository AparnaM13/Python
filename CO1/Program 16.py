#Create a single string seperated with space from two strings by swapping the character at position 1
str=input('Enter the string:')
new=str.split(" ")
a=new[0]
b=new[-1]
print('After swapping first character ',b[:1]+a[1:]+' '+a[:1]+b[1:])
