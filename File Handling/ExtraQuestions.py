# # import os
# #
# # # open a file and display the lines and of notes.txt
# # #
# # # with open("notes.txt", "r") as file:
# # #     line = file.readlines()
# # #
# # # for i in line:
# # #     print(i)
# #
# #
# # # count the number of lines in poem.txt
# # with open("poem.txt", "r") as file:
# #     file_lines = file.readlines()
# #     print(f"number of lines : {len(file_lines)}")
# #
# # # write to a file
# # with open("writing.txt", "w") as file:
# #     file.write("\nThis is task line")
# #     file.write("\nThis is another line")
# #     file.write("\nThis is yet another line")
# #     file.write("\nwhy a new task")
# #     file.write("\nThis is task")
# #
# # # append to file
# # with open("writing.txt", "a") as file:
# #     file.write("\nThisssss is an appenddddddd to existing filee.")
# #
# #
# # # check if a file exist
# # print(os.path.exists("data.txt"))
# #
# # Remove blank lines
# # with open("poem.txt", "r+") as file:
# #     file_lines = file.readlines()
# #
# # # print(file_lines)
# # for i in file_lines:
# #     if i == "\n":
# #         file_lines.remove(i)
# # print(file_lines)
#
#
# # find and replace
# target ="Python"
# replaced = "PYTHON"
# with open("article.txt", 'r') as file:
#     lines = file.readlines()
#     # print(lines)
# for i in lines:
#     words = i.split()
#     for word in words:
#         if word == target:
#             word = "PYTHON"
#         # print(word)
#         with open("updated_article.txt", "a")as f:
#             f.write(word + " ")
# print("file updated")

# uppercase writer
# with open("article.txt", "r") as file:
#     lines = file.readlines()
# for i in lines:
#     words = i.split()
#     for word in words:
#         with open("Allcaps.txt", "a") as f:
#             f.write(word.upper()+ " ")
# print("File updated")

# with open("students.txt", "r") as file:
#     with open("report.txt", "w") as f:
#         f.write("Name,Marks,Status\n")
#         for line in file:
#             name, marks = line.strip().split(",")
#             status = "Pass" if int(marks) >= 50 else "Fail"
#             f.write(f"{name},{marks},{status}\n")
#
# reverse file lines
with open("article.txt", "r") as file:
    lines = file.readlines()
lines.reverse()

with open("reversed.txt", "a") as f:
     f.writelines(str(lines))
print("File updated")