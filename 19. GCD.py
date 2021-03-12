#19.Gcd of two numbers
n1=int(input('Enter first nunber: '))
n2=int(input('Enter second number: '))
a=n1
b=n2
while b!=0:
    t=b
    b=a%b
    a=t
gcd=a
print('Gcd of two numbers is ', gcd)