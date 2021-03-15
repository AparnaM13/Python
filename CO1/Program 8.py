#Get a string from an input string where all occurence of first character replaced with $ except first character
def stringch(str1):
    char=str1[6]
    str1=str1.replace(char,'$')
    str1=char+str1[1:]
    return str1
print(stringch('aeroplane'))