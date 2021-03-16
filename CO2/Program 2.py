#Generate fibonacci seriesof N terms
n=int(input('Enter the limit:'))
n1, n2 = 1,1
count=0
if n==1:
    print('Fibonacci series upto', n,'is')
    print(n1)
else:
    print('The fibonacci series is :')
    while count<n:
        print(n1)
        t=n1+n2
        n1=n2
        n2=t
        count+=1