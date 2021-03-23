#Sort dictionary in ascending and descending order

d={
    "car":1,
    "bike":6,
    "train":2
}
l=list(d.items())
l.sort()
nl=dict(l)
print("Ascending order is,",nl)
l1=list(d.items())
l1.sort(reverse=True)
nl1=dict(l1)
print("Descending order is,",nl1)