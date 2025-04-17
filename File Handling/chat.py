from datetime import datetime

log_file = "chat_log.txt"

with open(log_file, "w") as file:
    file.write("Chat History Log\n")
    file.write("----------------\n")

print("Chat started. Type 'exit' to end the session.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended. Log saved to 'chat_log.txt'.")
        break

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a") as file:
        file.write(f"[{timestamp}] You: {user_input}\n")
