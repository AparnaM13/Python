#Accept an integer n and compute n+nn+nnn
n=int(input("Enter a number:"))
temp=str(n)
t1=int(temp+temp)
t2=int(temp+temp+temp)
tem=n+int(t1)+int(t2)
print("The value is:",tem)