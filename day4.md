## Variable, Statements and Expression

### 2.2 Value and Data Types
1. _Value in Python:_
- A value is one of the basic things a program works with, like a letter or a number. 
You can print values in Python.
-  ```python
    print(101)
    print("Hello World")
     ```
   
2. _Data Types:_
- Numeric : int, float, complex
- Sequence Type : string, list, tuple
- Mapping Type : dict
- Boolean : bool
- Set Type : set, frozenset
- Binary Types : bytes, bytearray, memoryview

_If you are not sure what type a value has, use the type function to find out._
```python
    print(type(20))   #int
    print(type("Hello world!"))   #str
    print(type(3.14))   #float
```
### 2.3 Operators and Operands

**Operators**: Operators are special symbols that perform operations on variables and values.

1. **Arithmetic operators**: 
-  Arithmetic operators are symbols used to perform mathematical operations on numerical values.
-  Arithmetic operators include addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).

2.  **Comparision Operators**:
- Comparison operators compare two values/variables and return a boolean result: True or False. 
-  The comparison operators also called relational operators. 
- Some of the well known operators are "<" stands for less than, and ">" stands for greater than operator.
- operators :==, !=, >=, <=, <, >.

3. **Logical Operators**:
- Python logical operators are used to combine conditional statements, allowing you to perform operations based on multiple conditions.
- These Python operators, alongside arithmetic operators, are special symbols used to carry out computations on values and variables.
- Operators : and, or, not.


### 2.4 Function Calls
**Function calls as part of complex expression**

_How it Works:_

- Function Evaluation: When Python encounters a function call within an expression, it first evaluates the function. This means it executes the code inside the function and gets the return value.
- Substitution: The return value of the function is then substituted back into the expression in place of the function call.
 - Expression Evaluation: Finally, Python evaluates the rest of the expression, using the substituted return value.

_Examples_:
- Mathematical Operations:
- - result = abs(x) + pow(y, 2): Here, abs() and pow() are called, their return values are used in the addition operation, and the final result is assigned to result.
- - print(max(list_data) - min(list_data)): the max and min values are found, then subtracted, and the result is printed.
- String Manipulation:
 - - combined_string = "Hello, " + str(len("world")): The len() function's return value (an integer) is converted to a string using str() and then concatenated with another string.
- - Control Flow:
if len(my_list) > 0: ...: The len() function's return value is used in a conditional statement.


### 2.6 Type Conversion Functions 
**int():**

- This function converts a value to an integer.
- It can handle:
Strings that represent whole numbers (e.g., int("123")).
Floating-point numbers (e.g., int(3.14)), but it truncates the decimal part (it does not round).
If you try to convert a string that doesn't represent a valid integer (e.g., int("abc")), you'll get a ValueError.

**float():**

- This function converts a value to a floating-point number.
- It can handle:
Strings that represent numbers, including those with decimal points (e.g., float("3.14"), float("123")).
Integers (e.g., float(5)).

**str():**

- This function converts a value to a string.
- It can handle virtually any data type, including:
Integers (e.g., str(123)).
Floating-point numbers (e.g., str(3.14)), Lists, tuples, dictionaries, and other complex objects.

 
This is very useful for printing values, concatenating strings, and other tasks that require string representations of data.

### Variables
