#Accept a file name from user and print extension of that
filename=input("Enter the filename:")
extension=filename.split(".")
print("Extension is",extension[-1])