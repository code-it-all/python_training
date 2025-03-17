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

