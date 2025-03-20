### Q1.
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


### Q2.
1. Mutability:
- Strings: Strings are immutable, meaning you cannot change their characters after they are created. If you need to modify a string, you must create a new one.
- Lists: Lists are mutable, meaning you can change their elements after they are created. You can add, remove, or modify elements within a list.
- Tuples: Tuples are immutable, like strings. Once a tuple is created, its elements cannot be changed.

2. Syntax:
- Strings: Strings are enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
- Lists: Lists are enclosed in square brackets ([ ]).
- Tuples: Tuples are enclosed in parentheses ( ( ) ).

3. Use Cases:
- Strings: Strings are used to represent text.
- Lists: Lists are used to store collections of items that may need to be modified. They are highly versatile and used in many situations.
- Tuples: Tuples are used to store collections of items that should not be changed. They are often used for:
    Storing related pieces of data, like coordinates (x, y).
    Returning multiple values from a function.
    Situations where data integrity is crucial.

4. Performance:
Because of their immutability, tuples are generally slightly faster and more memory-efficient than lists.


### Q3.

- Zero-Based Indexing: Python uses zero-based indexing, meaning the first element in a sequence has an index of 0, the second has an index of 1, and so on.
- Positive Indexing: Positive indices start from the beginning of the sequence.
- Negative Indexing: Negative indices start from the end of the sequence, with -1 representing the last element, -2 the second-to-last, and so on.
- Square Brackets: You access elements using square brackets [].
Example in main.py


### Q6
result of len([1, [2, 3], 4]) will be 3
This is because the element at index 1, will be counted as a single element instead of 2 elemnts.

### Q7.
Slicing:
- Slicing is a way to extract portion of a string by specifying the start and end indexes. 
- The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).
- There is an additional part in slicing for step value which is optional to define the next step value [start: end: step].

Example:
```python
s = "Vrishti Sharma" 
print(s[:4])  #Vris
print(s[3: ]) #shti Sharma
print(s[5:8]) # ti
print(s[::-1]) #amrah ithsirV
```
- Negative Indices: Slicing also supports negative indices, which count from the end of the sequence.
- Out-of-Bounds Slicing: Python handles out-of-bounds slice indices gracefully. If a slice index exceeds the sequence's length, Python adjusts the slice accordingly.
- Slicing creates a new object. It does not modify the original sequence.

### Q11.
Output of the following code:
```python
my_tuple = (1, 2, 3);
print(my_tuple[1:])
```
- The above code will throw a syntax error because of semicolon(;)
- After removing the semicolon the output will be:  (2, 3)

### Q12. Difference between list.append() and list.extend()

list.append():

- append() adds the entire argument as a single element.
- Regardless what the element is it is added as one object. in list.append()
- Length increase by 1.
- O(1) Time complexity.

list.extend()
- extend() iterates through the argument and adds each element individually.
- Accepts an iterable.
- length increase by number of elements added.
- Time complexity O(K).

