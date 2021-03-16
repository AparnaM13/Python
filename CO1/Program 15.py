#Print out all colors from color-list1 not contained in color-list2
color1=input("Enter the first list of colors by comma : ")
color2=input("Enter the second list of colors by comma : ")
c1=set(color1.split(","))
c2=set(color2.split(","))
print("The difference is:",c1.difference(c2))
