#Write lambda functions to find area of square,rectangle and triangle
a=int(input("Enter first side of triangle: "))
b=int(input("Enter second side of triangle: "))
c=int(input("Enter third side of triangle: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of triangle is : ",area)
a=int(input("Enter the side of square: "))
area=a*a
print("Area of square is: ",area)
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectengle: "))
area=a*b
print("Area of rectangle is: ",area)