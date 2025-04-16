# #
# # def top_student(data):
# #     if int(data[1]) >=  80:
# #         return print(f'{data[0]} got top score of {data[1]}')
# #
# #
# # with open('students.txt','r') as file:
# #     data = file.read()
# #
# #
# # data = data.split('\n')
# # length_data = len(data)
# # new_data = []
# # for i in data:
# #     new_data.append(i.split(','))
# #
# # print(new_data)
# # sum_data = 0
# # for i in new_data:
# #     sum_data += int(i[1])
# # average = sum_data/length_data
# # print(average)
# # print(top_student(new_data))
# #
# import csv
#
# def add_student():
#     name = input("Enter name: ")
#     age = input("Enter age: ")
#     grade = input("Enter grade: ")
#
#     with open('students.csv', 'a', newline='') as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=['Name', 'Age', 'Grade'])
#         if csv_file.tell() == 0:  # Write header only if file is empty
#             writer.writeheader()
#         writer.writerow({'Name': name, 'Age': age, 'Grade': grade})
#
# def view_students():
#     try:
#         with open('students.csv', 'r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 print(row)
#     except FileNotFoundError:
#         print("No records found.")
#
# while True:
#     print("\n1. Add Student\n2. View Students\n3. Exit")
#     choice = input("Enter choice: ")
#     if choice == '1':
#         add_student()
#     elif choice == '2':
#         view_students()
#     elif choice == '3':
#         break
#     else:
#         print("Invalid choice.")
#
import ExtraQuestions