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
from PIL import Image, ImageOps
image = Image.open("C:/Users/LENOVO/PycharmProjects/tuts/Iterations/images/image.jpg")
inverted_image = ImageOps.invert(image)
inverted_image.save("C:/Users/LENOVO/PycharmProjects/tuts/Iterations/images/inverted_image.jpg")
