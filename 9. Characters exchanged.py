#9. Create a string from given string where first and last character exchanged
def stringch(str1):
    return str1[-1:]+str1[1:-1]+str1[:1]
print(stringch('abcd'))
print(stringch('1234'))