#Add 'ing' at the end of a given string.If it already ends with 'ing',then add 'ly'
string=input("Enter a string : ")
if(len(string)>2):
    if string[-3:]=='ing':
        string+='ly'
    else:
        string+='ing'
print(string)