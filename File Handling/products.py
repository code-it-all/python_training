input_file = "products.txt"
output_file = "products_sorted.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

header = lines[0].strip()  # First line as the header
products = [line.strip().split(",") for line in lines[1:]]  # Remaining lines as data

products.sort(key=lambda x: float(x[2]))  # Convert price to float for sorting

with open(output_file, "w") as file:
    file.write(header + "\n")  # Write the header
    for product in products:
        file.write(",".join(product) + "\n")  # Write each product record

print(f"Products sorted by price (ascending) and saved to {output_file}")
