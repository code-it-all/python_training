import os
from datetime import datetime

source_file = "data.txt"
current_date = datetime.now().strftime("%Y-%m-%d")
backup_folder = "backup"
destination_file = os.path.join(backup_folder, f"data_backup_{current_date}")
os.makedirs(backup_folder, exist_ok=True)

with open(source_file, "r") as source:
    with open(destination_file,"w") as destination:
        for line in source:
            destination.write(line)

print(f"Backup created: {destination_file}")



formatted_file = "formatted_text.txt"

# Read the file
with open("raw_text.txt", "r") as source:
    lines = source.readlines()

formatted_lines = [line.strip().replace("\t", "  ") for line in lines]

with open(formatted_file, "w") as formatted:
    formatted.write("\n".join(formatted_lines))

print(f"Formatted text saved in {formatted_file}")
