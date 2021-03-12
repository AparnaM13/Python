#2.leap year
a=int(input('Enter current year:'))
b=int(input('Enter ending year:'))
print('Leap years are: ')
for i in range(a, b+1):
    if i%4==0 and i%100!=0 or i%400==0:
        print(i)