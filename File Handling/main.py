
def top_student(data):
    if int(data[1]) >=  80:
        return print(f'{data[0]} got top score of {data[1]}')


with open('students.txt','r') as file:
    data = file.read()


data = data.split('\n')
length_data = len(data)
new_data = []
for i in data:
    new_data.append(i.split(','))

print(new_data)
sum_data = 0
for i in new_data:
    sum_data += int(i[1])
average = sum_data/length_data
print(average)
print(top_student(new_data))

