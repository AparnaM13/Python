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
f=0
for i in list1:
    for j in list2:
        if i==j:
            f+=1
            print(i,end=',')
if(f==0):
    print("No common elements")
else:
    print("is in both list")
