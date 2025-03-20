## Sequences in Python

### 5.1 Introduction
**Sequences**

In Python, a sequence is like a collection or list of items arranged in a specific order. These items can be numbers, 
letters, words, or other objects. Each item is accessible via its index.

Main types of sequences in python are:

1. **Lists:**

- A list is a collection that can store different types of items (like numbers and strings) and allows you to change them.

Example:
```python
my_list = [1, 2, 3, "hello"]
print(my_list)
```

2. **Tuples:**

- A tuple is like a list, but you cannot change the items once you've created it.

Example:
```python
my_tuple = (1, 2, 3, "world")
print(my_tuple)
```

3.**Strings:**

- A string is a sequence of characters (letters, numbers, or symbols) and is used to work with text.

Example:
```python
my_string = "Python"
print(my_string)
```
4. **Bytes and Bytearrays:**

- These are used to work with binary data (like files or images). Bytes are immutable (cannot be changed), while bytearrays are mutable (can be changed).

### 5.2 Strings, Lists and Tuples

#### 5.2.1 Strings
- Arrays of bytes representing unicode characters, Images, Videos.
- A single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.
- Strings in Python are immutable. This means that they cannot be changed after they are created.


**Creating a string**
1. Single word/line string : can be created using either single('') or double ("")  quotes.
Example - 
```python
str1 = "Hello"
str2 = "World"
print(str1, str2)
```

2. Multi-line String: If we need to span multiple lines then we can use triple quotes (''') or (""")
Example: 
```python
str_example = """ Hello World!
This is an example of multiple line string.
We are in python training."""

print(str_example)
```

**Accessing Strings**
- Strings in Python are sequences of characters, so we can access individual characters using indexing. 
- Strings are indexed starting from 0 and -1 from end. This allows us to retrieve specific characters from the string.
- **Note:** Accessing an index out of range will cause an IndexError. Only integers are allowed as indices and using a float or other types will result in a TypeError.
Example: 
```python
s = "Vrishti Sharma"
print(s[6]) # i
print(s[2])  #s
print(s[-2])  #m
print(s[-7])  #h
```

**String Slicing**
- Slicing is a way to extract portion of a string by specifying the start and end indexes. 
- The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).

Example:
```python
s = "Vrishti Sharma" 
print(s[:4])  #Vris
print(s[3: ]) #shti Sharma
print(s[5:8]) # ti
print(s[::-1]) #amrah ithsirV
```

**Deleting a String**
- In Python, it is not possible to delete individual characters from a string since strings are immutable. However, we can delete an entire string variable using the del keyword.

Example:
```python
s = "Hello world"
del s

```
**Note:** After deleting the string using del and if we try to access s then it will result in a NameError because the variable no longer exists.

String Methods:
- capatalize()
- casefold()
- center()
- count()
- endswith()
- find()
- format()
- index()
- isalnum(), isalpha(), isdigit(), islower(), ismumeric(), ipsupper()
- lower(),
- join()
- split()

#### Lists in python
- A **list** is a built-in dynamic sized array (automatically grows and shrinks). 
- We can store all types of items (including another list) in a list. A list may contain mixed type of items, this is 
possible because a list mainly stores references at contiguous locations and actual items maybe stored at different locations.
- List can contain duplicate items.
- List in Python are Mutable. Hence, we can modify, replace or delete the items.
- List are ordered. It maintain the order of elements based on how they are added.
- Accessing items in List can be done directly using their position (index), starting from 0.

**Note:** Lists Store References, Not Values
- Each element in a list is not stored directly inside the list structure. 
- Instead, the list stores references (pointers) to the actual objects in memory. Example (from the image representation).

**Creating a list**

1. Using square brackets:
example:
```python
a = [1,2, 3,4]
b = ['apple', 'banana', 'cherry']

print(a)
print(b)
```
2. Using list() Constructor
example:
```python
a = list((1, 2, 4, "abc", "36.09"))
print(a)
```

3. Repeating elements
example:
```python
a = [9] * 5
b = [0] * 7
print(a)
print(b)
```

**Adding Elements into List**
We can add elements to a list using the following methods:

- append(): Adds an element at the end of the list.
- extend(): Adds multiple elements to the end of the list.
- insert(): Adds an element at a specific position.

**Removing Elements from List**
We can remove elements from a list using:

- remove(): Removes the first occurrence of an element.
- pop(): Removes the element at a specific index or the last element if no index is specified.
- del statement: Deletes an element at a specified index.

**List methods**
- append()
- copy()
- clear()
- count()
- extend()
- index()
- insert()
- pop()
- remove()
- reverse()
- sort()

### Strings in python

A string is a sequence of characters. Python treats anything inside quotes as a string. This includes letters, numbers, and symbols. Python has no character data type so single character is a string of length 1.

Example:
```python
s = "vrishti sharma"
print(s[1])
s1 = s+ s[0]
print(s1)
```