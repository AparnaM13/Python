#Create a list of colors from comma-separated color names entered by user.Display first and last colors
color=input("Enter the colors using comma: ")
list=color.split(",")
print(list)
print("First color is:",list[0])
print("Last color is:",list[-1])
