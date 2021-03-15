#3.a)Generate a positive list of integers
l=[-1,2,-3,4,5,0,-6]
for i in l:
    x=[i for i in l if i>=0]
print('Given list is:', l)
print('List of positive integers:', x)

#3.b)List of square numbers from a given list
for i in l:
    y=[j**2 for j in l]
print('List of squares of element', y)

#3.c)For a list of vowels selected from a given word
v=['a','e','i','o','u']
c=input('Enter a word:')
z=[k for k in c if k in v]
print('List of vowels in a given word:', z)

#4. c)List of ordinal value of each element of word
o=[ord(q) for q in c]
print('list of ordinal values in given word:', o)