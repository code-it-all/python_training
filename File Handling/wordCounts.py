from collections import Counter

with open("story.txt", "r") as file:
    lines = file.read()
words = lines.split()
words_counted = Counter(words)
with open("frequency.txt", "w") as output:
    for word,count in words_counted.items():
        output.write(f"{word} : {count}\n")
