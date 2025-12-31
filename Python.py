# --- FIRST PYTHON PROGRAM ---
print("this is a python program")

# --- DATA TYPES ---

# Strings
name_string = "Sai Ganesh"
print(f"My name is : {name_string}")

# Integers
age_int = 19
print(f"I am {age_int} years old.")

# Float
gpa = 9.99
print(f"My gpa is {gpa}")

# Boolean
is_student = True  
if is_student:
    print("You are a student")
else:
    print("You are not a student")

# --- TYPECASTING ---
# Converting one data type to another

name = "sai"
num = 7.8
age = 22

# Converting integer to float
age = float(age) 
print(f"Converted age to float: {age}")

# To Print the data type, we use type():
print(f"The data type of 'name' is: {type(name)}")

#Accept user input
name = input("What's your name buddy?? :")
weight = int(input("How much do you weigh?? :"))
height = float(input("Height?? :"))
print("So,You are"+name+".")
print("You weigh "+str(weight)+"Kgs")
print("Your height"+str(height)+"cms")

#Math Functions
import math

pi = 3.14
x = 1
y = 2
z = 3

# round() → Rounds a number to the nearest integer
print(round(pi))

# math.ceil() → Rounds a number UP to the nearest integer
print(math.ceil(pi))

# math.floor() → Rounds a number DOWN to the nearest integer
print(math.floor(pi))

# abs() → Returns the absolute (positive) value of a number
print(abs(pi))

# pow() → Raises a number to the power of another number
print(pow(pi, 2))

# math.sqrt() → Returns the square root of a number
print(math.sqrt(420))

# max() → Returns the largest value among the given arguments
print(max(x, y, z))

# min() → Returns the smallest value among the given arguments
print(min(x, y, z))