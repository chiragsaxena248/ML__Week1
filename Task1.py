# Create a basic “About Me” program that takes user input (name, age, location, interest) and prints a personalized intro paragraph.

name =  input("Enter your name : ")
age = int(input("Enter your age :"))
location = input("Enter your address :")
interest = input("Enter your interest :")

print("About me !")
print("My name is", name, "and I am", age, "years old. I belong to", location, ", and my interest is in", interest,".")