age = 29 # integer
balance = 100.50 # float
is_active = True # boolean
is_Admin = False # boolean
username = "john_doe" # string
favorite_color = ["red", "blue", "green"] # list
user_profile = {"age": age,"balance": balance,"is_active": is_active,"username": username,"favorite_color": favorite_color} # dictionary

print(type(age), type(balance), type(is_active), type(is_Admin), type(username), type(favorite_color), type(user_profile))


#Explicit Type Casting

# Type Casting
number_string = "42"
number = int(number_string) # int() converts a string to an integer
print(number_string, number)
print(type(number_string), type(number))

age = 25
age_string = str(age) # str() converts an integer to a string
print(age_string,age)
print(type(age_string),type(age))

number_float = float(number_string) # float() converts a string to a float
print(number_float)
print(type(number_float))

# conver to list
number_list = list(number_string)
print(number_list)
print(type(number_list))




# Implicit Type Casting

int_number = 5
float_number = 5.0
result = int_number + float_number #converts int_number int to float implicitly. int_number will become 5.0
print(result)
print(type(result))


#Constant Variables

PI = 3.14159
print(PI)
print(type(PI))

# We still can change the value of a constant variable. Python do not have true constant variables.

PI = 5
print(PI)
print(type(PI))
