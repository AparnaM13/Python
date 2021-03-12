#5.In a list of integers for values greater than 100, store over
n=int(input('Enter the number of elements:'))
a=[]
print('Enter the list elements:')
for i in range(n):
    x=int(input())
    if x>100:
        x='Over'
    a. append(x)
print(a)