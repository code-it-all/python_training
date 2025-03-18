## ADVANCED DEBUGGING ASSIGNMENT

1.**Error classification**
```python
# syntax error semicolon missing
for i in range(5):
    print(i)

# b) Runtime Error
# x = 10 / 0
# will raise a divide by zero exception
try:
    x = 10/0
except ZeroDivisionError:
    print("You cannot divide a number by zero")

# c) Logic Error
def calculate_area(radius):
    return  3.14 * radius * radius  #formula for calculating are of circle is 3.14 * r * r

print(calculate_area(10))   #function call was missing
```

2.**Debugging Complex Functions**

```python
def process_data(data):
    total = 0
    for item in data:
        total += int(item)  # This may throw an error if item is not convertible to int
    return total / len(data)  # Handle division by zero error

print(process_data(['10', '20', 'abc', '30']))
```

Solution:
```python
def process_data(data):
    total = 0
    try:
        for item in data:
            total += int(item)
            # print(total)
        return total / len(data)
    except ValueError as e:
        print("An Error Occurred: ", e)
    except ZeroDivisionError:
        print("You cannot divide a number by zero")


print(process_data(['10', '20', '40', '30']))
print(process_data(['10', '20', 'abc', '30']))

```


3. **Advanced Debugging Challenge**
```python
import random

def unreliable_function():
    number = random.choice([0, 1, 2])
    return 10 / number #divide by zero exception will be raised

for i in range(10):
    print(unreliable_function())
```

Solution:
```python
import random

def unreliable_function():
    number = random.choice([0, 1, 2])
    try:
        return 10 / number
    except ZeroDivisionError:
        print("Dividing a number by zero is not possible!")

for i in range(10):
    print(unreliable_function())
```

4. **Writing Debug-Friendly Code**
```python
def calculate_discount(price, discount):
    return price - (price * discount / 100)

print(calculate_discount(100, '10%'))
```
Solution
```python
def calculate_discount(price, discount):
    discount = int(discount.strip('%'))
    discount_price = price * discount / 100
    try:
        return price - discount_price
    except ValueError:
        print("Invalid discount value")

print(calculate_discount(100, '10%'))
```

5.**Rubber Duck Debugging**
```python
numbers = [1, 2, 3, 4, 5]
result = 1
for num in numbers:
    result *= num
print("Product:", result)  #no changes required
```
Explanation
- numbers = [1, 2, 3, 4, 5]: A list named numbers is created, containing the integers 1 through 5.
- result = 1: A variable named result is initialized to 1. This is the initial value for the product.
- for num in numbers: A for loop iterates through each element in the numbers list. In each iteration, the current element is assigned to the variable num.
- result *= num: In each iteration, the result variable is multiplied by the current value of num. This effectively calculates the product of all the numbers in the list.
- print("Product:", result): After the loop finishes, the final value of result is printed to the console.



6. **Advanced Challenge: Debug a Multithreaded Program**
```python
import threading

counter = 0
def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  # Expected: 200000
```
Solution:
```python
import threading

counter = 0
def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = [threading.Thread(increment()) for _ in range(2)]  #increment function called
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Counter:", counter)  # 200000
```

7.**Activity: Debug with breakpoints**

code to be debugged:
```python
def divide(a, b):
    result = a / b
    return result

a = 10
b = 0
print(divide(a, b))
```
Explanation:

-This code defines a function divide that takes two arguments, a and b, and returns the result of a / b. 
However, when b is 0, it will raise a ZeroDivisionError.

Solution
```python
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"  
    else:
        result = a / b
        return result

a = 10
b = 0
print(divide(a, b))

```

8.**Memory Leaks and performance Debugging**

```python
import time

def inefficient_function():
    result = []
    for i in range(100000):
        result.append(i * 2)
    time.sleep(2)
    return result

print(len(inefficient_function()))
```
Problems with above code:

- Large List Creation: Creating a list of 100,000 integers consumes memory.
- Time.sleep: the time.sleep(2) pauses the program for 2 seconds, and depending on the use case, this delay could be unecessary.
- Simple Operation: the multiplication of i*2 is a very simple operation. If the goal was to simply create a range of even numbers, there are more efficient ways of doing so.

Possible solution to improve efficiency
```python
result = [i*2 for i in range(100000)]
print(len(result))
```

9. **Unexpected None**

```python
def add(a, b):
    result = a + b
print(add(3, 4))
```

Explanation:
- The above code never returns any value.
- The print() statement doesn't receive any value hence it prints none.
- 'result' is a local variable created but never used.

Solution:
```python
def add(a, b):
    result = a + b
    return result

print(add(3, 4))
```

10. **Salient Failure**

```python
try:
    result = 10 / 0
except:
    pass
print("No error detected!")
```
Explanation:
- We need to define the error with the except keyword for error handling.
- The pass keyword in except block will simply pass the control flow to next step , resulting in no error raising.

Solution: 
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print('You cannot divide any number with zero!')
```