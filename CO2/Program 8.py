#Accept a list of words and return length of longest word
a=input("Enter the list : ")
list=a.split(" ")
m=len(list[0])
for i in list:
    if(len(i)>m):
        m=len(i)
        t=i
print("Longest word is: ",t,"and its length is ",m)