# for loop to print numbers from 1 to 10
# for i in range(1,11):
#     print(i)
#
#
# # WAP that count vowels in a string
# def count_vowels(string):
#     vowels = 'aeiou'
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels("hello"))
#
# # Calculate the sum of squares from 1 to 100
# sum_of_squares = 0
# for i in range(1,101):
#     sum_of_squares += i*i
# print(f"sum of squares upto 100 : {sum_of_squares}")
#
# # Create a multiplication table up to 10 X 10.
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} X {j} = {i*j}")

# Use pil to invert the colors of an image.
# from PIL import Image, ImageOps
# image = Image.open("C:/Users/LENOVO/PycharmProjects/tuts/Iterations/images/image.jpg")
# inverted_image = ImageOps.invert(image)
# inverted_image.save("C:/Users/LENOVO/PycharmProjects/tuts/Iterations/images/inverted_image.jpg")

# to print the string values
str_to_check = "hello world! @*^abc"
new_str = ""
for char in str_to_check:
    if char.isalpha() or char.isspace():
        new_str += char
print(new_str)


# find the binary value of the given number then find the number of on bits i.e 1 in that binary number
num = 321
binary_value = ""
count = 0
while num > 0:
    binary_value = str(num % 2) + binary_value
    num = num // 2
for i in binary_value:
    if i == "1":
        count += 1
print(count)

# waf to print the multiplication of 2 matrix
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for i in range(len(matrix1)):
    result.append([])
    for j in range(len(matrix2[0])):
        total = 0
        for k in range(len(matrix2)):
            total += matrix1[i][k] * matrix2[k][j]
            result[i].append(total)
print(result)
