#
# # Q3.
# my_list = ['apple', 'banana', 'cherry', 'date']
#
# # Positive indexing
# print(my_list[0])  # Output: apple
# print(my_list[2])  # Output: cherry
#
# # Negative indexing
# print(my_list[-1]) # Output: date
# print(my_list[-3]) # Output: banana
#
# my_string = "Python"
#
# print(my_string[0])  # Output: P
# print(my_string[1])  # Output: y
# print(my_string[-1]) # Output: n
#
# # Q4. to access last chracter of a string
# str1 = "Hello world!"
# print(str1[-1])  # !
#
# # Q5 create a list of numbers and access the third element
# numbers = [1, 2, 3, 4, 5]
# print(numbers[2])   # 3
#
# # Q8 reverse a string using slicing
# string_example = "Hello World!"
# print(string_example[::-1])      #!dlroW olleH
#
# #Q9. To demonstrate list repetition
# a = [9] * 5    #[9, 9, 9, 9, 9]
# b = [0] * 7    #[0, 0, 0, 0, 0, 0, 0]
# print(a)
# print(b)
#
# # list concetination
# str1 = "Hello "
# str2 = "World!"
# print(str1 + str2)   #Hello World!
#
# # Q10 to count the occurrence of an element in a list
# list_example = [1,2,3,4,5,6,2,4,2,1,6,6,6,6,2]
# target = 2
# count = 0
# for i in list_example:
#     if i == target:
#         count += 1
# print(f"Number of times {target} occurred : {count}")   #number of times 2 occurred: 4
#
# # Q13 write a code to split "Learn python, step by step"
# str_to_split = "Learn python, step by step"
# print(str_to_split.split())      #['Learn', 'python', ',', 'step', 'by', 'step']
from operator import index
#
# # Q14 Join a list
# list_to_join = ['Python', 'is', 'fun']
# print(' '.join(list_to_join))   #Python is fun
#
# # Q15 find the index of 2 at the first occurence
# occurrence_check = [1, 2, 2, 3, 4, 2]
# print(occurrence_check.index(2))     #1
#
# # Q16 Check if string is palindrome or not
# Check_palindrome = "madam"
# new_string = Check_palindrome[::-1]
# if Check_palindrome == new_string:
#     print("Yes, it is a palindrome")
# else:
#     print("No, it is not a palindrome")
#
# # Q17 WAF to return the length of the longest word in a sentence.
#
# def long_word(sentence):
#     str_words = sentence.split()
#     # result = [i for i in str_words max(str_words, key = len)]
#     result = max(str_words, key=len)
#     return len(result)
#
#
# sen_to_check = "The quick brown fox jumps over the lazy dog"
# print(long_word(sen_to_check))
#
#
# # Q18. Nested list indexing demonstration.
#
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# # Inorder to access the element in the middle of the matrix we need to use indexing with 2 square brekets
# # first [] will transverse to the row and 2nd will access the element
# print(matrix[1][1])   #5
#
# # Q19 To convert a list of characters into a string.
# character_to_join = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# print(''.join(character_to_join))   #hello world

# Q20. Write a code to remove duplicate while preserving the order
# list_to_remove_duplicates = [1, 2, 3, 4, 5, 6, 2, 4, 2, 1, 6, 6, 6, 6]
# new_list = []
# for i in list_to_remove_duplicates:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# Q21. Write a function that takes a list of tuples and sort tuples by the second element of each tuple
# def sort_tuples(tuples):
#     elements = [list_of_tuple[1] for list_of_tuple in tuples]
#     # print(elements)
#     elements.sort()
#     new_list = []
#     for i in elements:
#         for j in tuples:
#             if i == j[1]:
#                 new_list.append(j)
#     return new_list
#
#
# list_of_tuples = [(1, 2), (3, 1), (5, 9), (7, 8)]
# print(sort_tuples(list_of_tuples))

