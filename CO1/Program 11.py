#11. Biggest of three numbers
print('Enter 3 numbers:')
a=input()
b=input()
c=input()
if a>b:
    if a>c:
        print('Largest number is ', a)
    else:
        print('Largest number is ', c)
else:
    if b>c:
        print('Largest number is ', b)
    else:
        print('Largest number is ', c)