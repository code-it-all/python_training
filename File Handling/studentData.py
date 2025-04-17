import json

# Input and output file names
input_file = "students.txt"
output_file = "students.json"

# Read the text file and process data
with open(input_file, "r") as file:
    lines = file.readlines()

# Extract the header and data rows
header = lines[0].strip().split(",")  # First line as the header
students = [dict(zip(header, line.strip().split(","))) for line in lines[1:]]  # List of dictionaries

# Write the data to a JSON file
with open(output_file, "w") as json_file:
    json.dump(students, json_file, indent=4)

print(f"Data converted to JSON and saved in {output_file}")
