#20. From a list, create a list removing even no.s
l=int(input('Enter length of list: '))
print('Enter list elements:')
list1=[]
for i in range(l):
    x=int(input())
    list1.append(x)
print('Given list: ', list1)
for x in list1:
    if x%2==0:
        list1.remove(x)
print('List of odd nos ',list1)