# # data = [
# #     ('HR', 'Alice', 50000),
# #     ('HR', 'Bob', 60000),
# #     ('Tech', 'Charlie', 120000),
# #     ('Tech', 'Dave', 110000),
# #     ('Tech', 'Eve', 115000)
# # ]
# #
# # departments = []
# # for i in data:
# #    if i[0] not in departments:
# #        departments.append(i[0])
# #
#
# sentences = [
#     "The quick brown fox jumps over the lazy dog",
#     "The dog barked loudly",
#     "Foxes are quick and clever",
#     "Lazy days are the best days"
# ]
#
# word_to_sentence_indices = {}
#
# for index, sentence in enumerate(sentences):
#     words = set(sentence.lower().split())  # use set to avoid duplicate indices for the same word in a sentence
#     for word in words:
#         if word not in word_to_sentence_indices:
#             word_to_sentence_indices[word] = []
#         word_to_sentence_indices[word].append(index)
#
# print(word_to_sentence_indices)
#

def group_words_by_length(words):
    length_dict = {}
    for word in words:
        length = len(word)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(word)
    return length_dict

words = ["apple", "bat", "banana", "cat", "dog", "elephant", "ant"]
result = group_words_by_length(words)

print(result)

def merge_dicts_max_value(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] = max(merged[key], value)
        else:
            merged[key] = value
    return merged

dict_a = {'a': 5, 'b': 3, 'c': 10}
dict_b = {'b': 7, 'c': 8, 'd': 2}

result = merge_dicts_max_value(dict_a, dict_b)
print(result)
