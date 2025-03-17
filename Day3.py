# DAY 1
# return square of all the even number
# numbers = [23, 54,33, 89,52 , 84, 21, 782, 888]
# new_num = [x*x  for x in numbers if x%2 == 0]
# # for num in numbers:
# #     if num%2 == 0:
# #         new_num.append(num)
#
# print(new_num)


# return words wth len more than equal to 5
# words = ['hello', 'hi', 'world', 'yes', 'no']
# long_words = [word for word in words if len(word) >= 5]
# print(long_words)

# take a 2d array into a 1d array using list and list compri. then return the even values in array
# array_2d = [[1,2,3], [4,5,6], [6,7,8]]
# array_1d = [s*s for x in array_2d for s in x  if s%2 == 0]
# print(array_1d)

# print the reverse of words in an array
# words = ['hello', 'hi', 'world', 'yes', 'no']
#
# long_words = [word[: : -1] for word in words if len(word) >= 5]
# print(long_words)

# # print all possible sums in 2 arrays
# A = [2,4,7,9]
# B = [1, 3, 5, 8]
# sum_arrays = [x+y for x in A for y in B]
# print(sum_arrays)

# DAY 2
# return a list of even no using filter function
# list1 = [1, 2, 3, 4, 5,6]
# new_list = list(filter(lambda a: a%2 == 0, list1))
# print(new_list)

# list of names return the name which starts with a vowel
# vowels = 'a', 'e', 'i', 'o', 'u'   #will be considered as a tuple
# names = ['amy', 'john', 'pixy', 'eno']
# res = list(filter(lambda s: s[0] in vowels, names))
# print(res)
#
#
# # convert string integers into int within a list of string and integers
# list1 = ['hello', '22', 'world', '88']
# values = ' '.join(filter(lambda val : val.isdigit(), list1))  #will return integers space seperated
# # or
# # values = list(map(int, list(filter(lambda val : val.isdigit(), list1)))) will return list of integers
#
# print(values)


# input list of emails, output print the domain of emails
# emails = ['abc@gmail.com', 'xyz@yahoo.com', 'pqr@outlook.com']
# domains = list(map(lambda s : s.split('@'), emails))
# domains = [x[1] for x in domains]
# print(domains)


# in a list of integers find the average of every three numbers and return a new list
values = [1, 2, 3,4,5,6]
result = list(map( lambda i :sum( values[i : i+3]), range(len(values) - 2)))
print(result)