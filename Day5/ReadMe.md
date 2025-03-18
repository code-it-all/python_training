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

**Solution**:
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

**Solution**:
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
**solution**
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
print("Product:", result)
```