# # 1.
# for i in range(5):
#     print(i)
#
# # b) Runtime Error
# # x = 10 / 0
# # will raise a divide by zero exception
# try:
#     x = 10/0
# except ZeroDivisionError:
#     print("You cannot divide a number by zero")
#
# # c) Logic Error
# def calculate_area(radius):
#     return  3.14 * radius * radius
#
# print(calculate_area(10))

# 2.
# def process_data(data):
#     total = 0
#     try:
#         for item in data:
#             total += int(item)
#             # print(total)
#         return total / len(data)
#     except ValueError as e:
#         print("An Error Occurred: ", e)
#     except ZeroDivisionError:
#         print("You cannot divide a number by zero")
#
#
# print(process_data(['10', '20', '40', '30']))
# print(process_data(['10', '20', 'abc', '30']))


# # 3.
# import random
#
# def unreliable_function():
#     number = random.choice([0, 1, 2])
#     try:
#         return 10 / number
#     except ZeroDivisionError:
#         print("Dividing a number by zero is not possible!")
#
# for i in range(10):
#     print(unreliable_function())
#

# 4.
def calculate_discount(price, discount):
    discount = int(discount.strip('%'))
    discount_price = price * discount / 100
    try:
        return price - discount_price
    except ValueError:
        print("Invalid discount value")

print(calculate_discount(100, '10%'))