#7. Check list are in same length,sum same,common elements
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
if len(list1)==len(list2):
    print('->List have same length')
else:
    print('->List is not in same length')
if sum(list1)==sum(list2):
    print('->Sums of list elements are equal')
else:
    print('->Sums of list elements are not equal')
flag=0
for i in list1:
    for j in list2:
        if i==j:
            flag+=1
            print(i)
if flag==0:
    print('->No common elements in both list')
else:
    print('is in both list')