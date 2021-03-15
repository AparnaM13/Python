#4.Count the occurence of each word in a line of text
s=input("Enter a string: ")
count=dict()
word=s.split()
for i in word:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)