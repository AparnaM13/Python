str=input('Enter the string:')
new=str.split(" ")
a=new[0]
b=new[-1]
print('After swapping first character ',b[:1]+a[1:]+' '+a[:1]+b[1:])
