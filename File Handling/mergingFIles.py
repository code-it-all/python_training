with open("Chapter1.txt", "r") as file1:
    data_from_file1 = file1.read()
with open("Chapter2.txt", "r") as file2:
    data_from_file2 = file2.read()
with open("Chapter3.txt", "r") as file3:
    data_from_file3 = file3.read()
with open("Book.txt" , "w") as output_file:
    output_file.write(data_from_file1+ " \n\n")
    output_file.write(data_from_file2+ " \n\n")
    output_file.write(data_from_file3+"\n\n")
print("book created successfully!")
