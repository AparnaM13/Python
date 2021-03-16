#Sort dictionary in ascending and descending order
import operator
d={0:8,1:5,2:6,3:9,4:4,5:0}
asc=sorted(d.items(),key=operator.itemgetter(1))
print("Ascending order:",asc)
dec=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("Descending order:",dec)