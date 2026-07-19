# Variables
# Variable name must start with a letter or underscore, followed by letters, digits, or underscores
# Assigning a string value to a variable
greeting = "Hello, World!"

# Assigning a number value to a variable
user_age = 30

# Using the variables
print(greeting)
# Outputs: Hello, World!

print(f"The user is {user_age} years old.")
# Outputs: The user is 30 years old.


# Assign multiple values to multiple variables

x, y = 5, 10
print(x, y)
# Outputs: 5 10

# Assign single value to multiple variables
p = q = 5
print(p, q)
# Outputs: 5 5

# Variables with the input() function

username = input("Enter your username: ")
print("username",username)
password = input("Enter your password: ")
print(f"password is {password}")

# varaibles with operations/calculations
base_salary = 50000
bonus = 0.2
total_salary = base_salary + (base_salary * bonus)
print('bonus', base_salary * bonus)
print(f"{username} , your total salary is {total_salary} with a bonus of {bonus * 100}%")
