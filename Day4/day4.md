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
**2.4.1 Function calls as part of complex expression**

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

**2.4.2. Functions are Objects:  Parentheses Invoke Functions**
- In Python, functions are treated as first-class objects, meaning they can be manipulated like any other data type (integers, strings, etc.). This has two key implications:

- Functions are Objects:
- - This means you can assign functions to variables, store them in data structures (like lists or dictionaries), and pass them as arguments to other functions.
Essentially, a function's name acts as a reference to the function object in memory.
- Parentheses Invoke Functions:
- - When you place parentheses () after a function's name (or a variable that references a function), you are telling Python to execute the code within that function.
If the function requires arguments, you place those arguments inside the parentheses.

### 2.5 Data Types
**Dynamic Typing Defined:**
- Python is a dynamically typed language. This means that the type of a variable is checked during runtime, as opposed to compile-time (like in statically typed languages such as C++ or Java).
You don't need to explicitly declare the data type of a variable before assigning a value to it.

**How it Works:**
- When you assign a value to a variable, Python automatically infers the data type based on the value itself.
- The same variable can hold values of different types at different points in the program. This flexibility is a key characteristic of dynamic typing.

**Advantages:**

- Flexibility: Dynamic typing allows for more flexible and concise code, as you don't need to worry about type declarations.
- Rapid Development: It can speed up development, as you can write code more quickly without the overhead of type checking.
- Ease of Use: It makes Python easier to learn and use, especially for beginners.

**Disadvantages:**
- Runtime Errors: Type-related errors may not be caught until runtime, which can make debugging more challenging.
- Performance: Dynamic typing can sometimes lead to slightly slower performance compared to statically typed languages, as type checking occurs during execution.
- Readability/Maintainability: In very large codebases, it can be harder to keep track of variable types, which can affect readability and maintainability.
- Type Checking Tools:
To mitigate the potential disadvantages, Python offers tools like mypy for optional static type checking. This allows you to add type annotations to your code and catch type errors before runtime.

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

### 2.7 Variables
**Objects in Memory:**
- In Python, everything is an object. This means that data, like integers, strings, lists, and functions, are all stored as objects in memory.
- Each object has:
A type (e.g., integer, string).
A value.
An identity (a unique memory address).
**Variable as References:**
- Variables in Python are not like boxes that hold values. Instead, they are more like labels or references that point to objects in memory.
- When you assign a value to a variable, you're essentially creating a reference from that variable to the object that represents that value.

**Memory Management:**
- Python uses automatic memory management, which includes:
- - Reference Counting: Python keeps track of how many references point to each object. When an object's reference count drops to zero, it means that no variables are pointing to it anymore.
- - Garbage Collection: Python also has a garbage collector that identifies and reclaims memory occupied by objects that are no longer in use, even if reference counts aren't zero (to handle circular references).

**Mutable vs. Immutable Objects:**
- Objects can be either mutable (changeable) or immutable (unchangeable).
- Immutable: Integers, floats, strings, and tuples are immutable. When you "change" an immutable object, you're actually creating a new object in memory.
- Mutable: Lists, dictionaries, and sets are mutable. You can change their values directly without creating new objects.

### 2.9 Choosing the right variable name

**Original**
```python
    l = [1, 5, 2, 8]
    m = max(l)
    n = min(l)
    print(m - n)
```

**Modified**
```python
    numbers = [1, 5, 2, 8]
    maximum_value = max(numbers)
    minimum_value = min(numbers)
    print(maximum_value - minimum_value)
```

**Why is total_price a better name than tp?**

**Clarity and Readability:**
- total_price clearly conveys the variable's purpose. Anyone reading the code can immediately understand that it represents the total cost of something.
tp is ambiguous. It could mean "total points," "test parameter," or any number of other things. This lack of clarity makes the code harder to understand.

**Maintainability:**
- When you or another developer revisits the code later, meaningful variable names make it much easier to understand the code's logic.
- With tp, you would have to spend time figuring out what it represents, especially in larger, more complex programs.

**Reduced Errors:**
- Meaningful names reduce the chances of errors. When variables have clear purposes, you're less likely to use them incorrectly.

**Collaboration:**
- If you're working on a team, using descriptive variable names is essential for effective collaboration. It ensures that everyone understands the code and can work together efficiently.

**Self-Documenting Code:**
Well-chosen variable names can make code self-documenting. This means that the code itself explains its purpose, reducing the need for extensive comments.

**Professionalism:**
Using good variable names is a sign of good coding practice and professionalism.


### 2.10 Statement and Expressions

**Expressions:**
- An expression is a combination of values, variables, operators, and function calls that evaluates to a single value.
- Expressions produce a result.
- Examples:
```python
    # 42 + 2 #(evaluates to 44)
    # x #(evaluates to the value of x)
    #len("hello")# (evaluates to 5)
    # x > 0 #(evaluates to True or False)
```
**Statements:**
- A statement is a complete instruction that performs an action.
- Statements do not necessarily produce a value. They perform operations or control the flow of the program.
- Examples: 
```python
   # x = 5 + 3 (assignment statement)
   # print(x) (print statement)
   # if x > 0: ... (conditional statement)
    #for i in range(10): ... (loop statement)
    #def my_function(): ...(function defination)
```

**Key Differences:**
- Expressions evaluate to a value, while statements perform an action.
- Expressions can be part of statements, but statements are not part of expressions.

```python
x = 5 + 3
print(x)
```
- 5+3:
This is an **expression**. It evaluates to the value 8.
- x = 5 + 3:
This is a **statement**. It's an assignment statement that assigns the result of the expression 5 + 3 to the variable x.
- x:
Within the print statement, x is an **expression**, that evaluates to the value that is stored within the x variable.
- print(x):
This is a **statement**. It's a print statement that displays the value of the variable x to the console.

### 2.11 Order of Operations

**PEMDAS**
- Also called BODMAS is an acronym that helps remember the order of operations in mathematical expressions. It dictates the sequence in which calculations should be performed to ensure consistent and correct results.

**In simpler terms:**
- Do what's in the parentheses first.
- Then, calculate exponents.
- Then, do multiplication and division (from left to right).
- Finally, do addition and subtraction (from left to right).

### 2.12 Reassignment

#### Developing Your Mental Model of How Python Evaluates

```python
items = [1, 2, 3]
print(items)
items = ["apple", "banana", "cherry"]
print(items)
```

