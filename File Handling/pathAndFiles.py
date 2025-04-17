import os

directory = os.getcwd()
found_files = []
count = 0
for file in os.listdir(directory):
    if file.endswith('.txt') or file.endswith('.csv'):
        found_files.append(file)
        count+=1

for file in found_files:
    print(file)
print("Total number of text and csv files found : ", count)