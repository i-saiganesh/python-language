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