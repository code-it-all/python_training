# pipelines in python
# Finding the longest pipeline and return maximum threshold time
# Given pipeline
pipelines = [
    ("Data Ingestion", 30),
    ("preprocessing", 45),
    ("Model Training", 120),
    ("Evaluation", 20),
]
threshold = 40

# # to find the longest pipeline we are using the time given with the corresponding pipelines above
long_pipeline = max(pipelines, key=lambda x: x[1])   # the lambda function will access the time of pipelines

# identify the pipeline which are exceding the threshold value given with corresponding pipelines
exceding_pipeline = [pipeline for pipeline in pipelines if pipeline[1] > threshold]
#
print("Longest pipeline : ", long_pipeline)
print("List of pipelines exceeding threshold : ", exceding_pipeline)


from pyexpat.errors import messages

import re
#
logs = """ ERROR 404: Not Found
# INFO: Connection established
# ERROR 500: Internal Server Error
# ERROR 404: Not found"""
#
pattern = r"ERROR (\d+)"
#using regex where \d matches any digit, + matches one or more digits and () capturing group that extracts the numeric
# value

error_codes = set(re.findall(pattern, logs))
# #re.findall() will scan the text and extracts only the error codes form matching log entries
# # since we use (\d+) as capturing group only numbers are returned.
# # set() returns unique values
print(error_codes)
#
config_string = """ host=localhost
# port = 5432
# username=user1
# password=secret
# debug=true"""
#
config_dict = {}
for line in config_string.strip().split('\n'):
    if "=" in line:
        key, value = line.split("=")
        config_dict[key] = value

print(config_dict)

# data cleaner to list all the hashtags used in a string
post = "Loving the new #python course! #coding #python #skills"
post = post.split()
hashtags = []
for word in post:
    if word.startswith("#"):
        hashtags.append(word)

print(set(hashtags))   #set() is used to extract the unique values only
#
#
secret_message = "hweollrolwd"
#
new_list = [secret_message[s] for s in range(0, len(secret_message), 2)]
print(new_list)
other_list = [secret_message[s] for s in range( len(secret_message)) if s%2 != 0]
print(other_list)
new_list[3] = other_list[2] + other_list[3] + " "+ other_list[0] + other_list[1] + 'r'
#
# print(''.join(new_list))
#
# inventory = [
#     ("Apples", 50),
#     ("Bananas", 100),
#     ("Oranges", 70),
# ]
#
# maximum_item = max(inventory, key = lambda x: x[1])
# print(maximum_item[0])
#
# survey_data = "5,7,2,6,9,1,45"
# survey_data_int = list(map(int, survey_data.split(",")))
# max_value = max(survey_data_int)
# min_value = min(survey_data_int)
# print(f"Max Score : {max_value} Min Score : {min_value}")
# print()
# # print(survey_data_int)
#
# user = ['Alice' ,'Bob' ,'Charlie']
# roles = ('admin' ,'user' ,'guest')
#
# access_roles = {}
# for i,j in zip(user,roles):    #zip function allows to combine multiple iterables into iterator of tuples
#     access_roles[i] = j
#
# print(access_roles)
#
# messages = "My account is locked, please help!"
# category = "low"
# if len(messages) > 5:
#     category = "medium"
# elif len(messages) > 10:
#     category = "high"
#
# print(category)
#
# # find the product with longest word length
# products = ["Laptop", "Smartphone", "TV", "Wireless Headphones"]
# longest_product = max(products, key=len)
# print(longest_product)
#
# # extract last 10 readings and find the average
# sensor_readings = [12, 15, 14, 16, 20, 22, 21, 23, 25, 30, 28, 27]
# sum = 0
# # print(len(sensor_readings))
# sensor_readings = sensor_readings[-10:]
# for i in sensor_readings:
#     sum+= i
# print("Average is : ", sum/10)
#
# # reverse the given list
# transactions = [50, -150, 200, -300, 100]
# print("Reverse of Transactions : ", transactions[::-1])
#
# # Format logs with timestamps
# logs = ["System Boot", "Network Connected", "User Login"]
# timestamps = ["08:00:01", "08:00:05", "08:00:09"]
# formated_data = []
# for i,j in zip(logs,timestamps):
#     formated_data.append(f"{j} : {i}")
# print(formated_data)
#
# # pattern generator
# symbol = "* "
# count = 5
# print(symbol*count)
#
# # count the occurence of target keyword
# text = "The product is excellent, absolutely excellent!"
# target = "excellent"
# count = text.count(target)
# print(f"'{target}' count : {count}")
#
#
# # find the index of first occurence of target word
# log = "INFO: All system go. ERROR: Failed to start service."
# target = "ERROR"
# index = log.find(target)
# print(f"'{target}' index : {index}")
#
#
# # parse csv into list
# csv_data = "Alice,25,Engineer\nBob,30,Doctor\nCharlie,22,Artist"
# csv_data = csv_data.split("\n")
# csv_data = [data.split(',') for data in csv_data ]
# print(csv_data)
#
# # username generator generate usernames form full names
# names = ["Alice Wonderland", "Bob Builder", "Charlie Chaplin"]
# surnames = []
# first_name = []
# for name in names:
#     first_name.append(name.split()[0][0])
# for name in names:
#     surnames.append(name.split()[1])
# user_name = []
# for i,j in zip(first_name,surnames):
#     user_name.append(i+j)
# print(user_name)

# count messages per user from chat logs
chat_logs = [
    "Alice: Hi!",
    "Bob: Hello!",
    "Alice: How are you?",
    "Bob: I’m good, thanks!"
]

user_messages = {}
for log in chat_logs:
    user, message = log.split(": ")
    if user not in user_messages:
        user_messages[user] = 1
    else:
        user_messages[user] += 1
print(user_messages)
result = ", ".join(f"{user} : {count} messages" for user, count in user_messages.items())

# find the pattern from the given string and compress the data
string_to_compress = "ababababmnmnmnmn"
def pattern_in_string(string_pattern):
    new_string = ""
    count = 1

    for i in range(len(string_pattern)):
        if string_pattern[i] not in new_string:
            new_string += string_pattern[i]
            print(new_string)
            count = 0
        if string_pattern[i] == new_string[-1]:
            count += 1
    return new_string, count


result, count = pattern_in_string(string_to_compress)
print(f"Pattern : '{result}' repeated {count} times")
