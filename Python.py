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
print("So,You are "+name+".")
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

#String Indexing and Slicing , START:STOP:STEP
#Indexing-Acessing Characters-One or More at a Time
name = "sai ganesh s"
letter = name[2:10]
is_letter = name[:6]
also_letter = name[4:]
#STOP in Indexing
hi_letter = name[1:5:2]
oyy_letter = name[::3]
hey_letter = name[::-2]
#SLICING-Cutting the characters off
mail = "mailto:ganesh@fake.in"
slice = slice(7,-3)

print(letter)
print(is_letter)
print(also_letter)
print(hi_letter)
print(oyy_letter)
print(hey_letter)
print(mail[slice])

#IF,ELSE,ELIF STATEMENTS

age = int(input("Nee vayasu entha?? : "))
if age >=18:
    print("Nuv Magadu ra Bujji!")
elif age<0:
    print("BaneExtralu...")
elif 13<= age <=17:
    print("Niku Untadhi!")
else:
    print("Pillara Meerantha!")

#LOGICAL OPERATORS: and, or , not
money = int(input("Entha Dabbulu Unnayi : $"))

if money >= 0 and not (money > 2000):
    print("Parledu , Unnayi anthey...")
elif money > 2000 and not (money >= 10000):
    print("Meerante Unnollu Bayya...")
elif money >= 10000:
    print("Koteswarudu ra Mee nanna!")
#OR WASN'T USED HERE BUT IT CAN BE USED LIKE THIS:
if money < 0 or money > 100000:
    print("Invalid amount")

#While Loop-A while loop keeps running a block of code as long as a condition is true.(Unlimited Attempts)
name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

#For Loop-The numbers start from 100 goes till 500 , Increments by 3 times each
for i in range(100,500,3):
  print(i)
#for loop using strings
for i in "Ganesh":
  print(i)
  
#Happy New Year : 10,9,...,1 , Happy New Year
import time 
for i in range(10,0,-1):
 print(i)
 time.sleep(1)
print("HAPPY NEW YEAR")