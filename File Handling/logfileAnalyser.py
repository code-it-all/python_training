
with open("server.log", "r") as file:
    count = 0
    lines = file.readlines()
# print(lines)
with open("errors_only.log", 'a') as logs:
    for line in lines:
        if "ERROR" in line:
            logs.write(line)
    print("Errors Logged in file.")

