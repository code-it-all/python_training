#2.2 Write a program that: Assigns different values to variables. Prints the type of each variable. also defines the datatypes in 2.5
val1 = 45
val2 = 45.67
val3 = "Hello"
val4 = True
print(type(val1), type(val2), type(val3), type(val4))

# 2.3.1 Python script that demonstrate : addition, subtraction. multiplication. modulo and division
a = 7
b = 2

# addition
print ('Sum: ', a + b)

# subtraction
print ('Subtraction: ', a - b)

# multiplication
print ('Multiplication: ', a * b)

# division
print ('Division: ', a / b)

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)

# a to the power b
print ('Power: ', a ** b)

# 2.3.3 Logical operators
# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False


# Type conversion functions
num = '123'
converted_num = int(num)
print(converted_num, type(converted_num))

float_num = 3.14
converted_str = str(float_num)
print(converted_str, type(converted_str))

string_num = "45.67"
converted_float = float(string_num)
print(converted_float, type(converted_float))

integer_num = 789
converted_string = str(integer_num)
print(converted_string, type(converted_string))

float_to_int = int(3.99)
print(float_to_int, type(float_to_int))

int_to_float = float(5)
print(int_to_float, type(int_to_float))

# Function calls as part of complex expression
x = 10
y = 3
result = float(x / y)  # Combining division and type conversion
print(result)

string_value = "hello"
length_plus_five = len(string_value) + 5 # using len() inside an expression.
print(length_plus_five)

value = -7
absolute_plus_two = abs(value) + 2 # using abs() in an expression
print(absolute_plus_two)

list1 = [1,2,3]
list2 = [4,5,6]
combined_length = len(list1) + len(list2) # using len() multiple times in one expression.
print(combined_length)

# 2.4.2 functions are objects

def say_something(message):
  return message

message_function = say_something
output = message_function("This is a message.")
print(output)

def uppercase_string(input_string):
    return input_string.upper()

upper_func = uppercase_string
upper_letter = upper_func("hello")
print(upper_letter)

# 2.7 Variables
# Integer example (immutable)
x = 10
print("x:", x, "id(x):", id(x)) #x: 10 id(x): 140710373164232

# String example (immutable)
name = "Alice"
print("name:", name, "id(name):", id(name))   #name: Alice id(name): 1837710473712

# List example (mutable)
my_list = [1, 2, 3]
print("my_list:", my_list, "id(my_list):", id(my_list))  #my_list: [1, 2, 3] id(my_list): 1837710175104

#Dictionary example (mutable)
my_dict = {"a":1, "b":2}
print("my_dict:", my_dict, "id(my_dict):", id(my_dict))     #my_dict: {'a': 1, 'b': 2} id(my_dict): 1837710172160

# 2.8 variable names and keywords

# Exercise: Using reserved keywords as variable names

# Attempting to use 'if' as a variable name:
# if = 10  # This will result in a SyntaxError

# Attempting to use 'for' as a variable name:
# for = "hello"  # This will also result in a SyntaxError

# Attempting to use 'while' as a variable name:
# while = True # SyntaxError

# Attempting to use 'True' as a variable name
# True = "test" # SyntaxError

# Fun Fact: Listing reserved keywords

import keyword
print(keyword.kwlist)

# The below list will be printed
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']