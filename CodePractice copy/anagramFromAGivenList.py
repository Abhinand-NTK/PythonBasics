# word_list = ["listen", "silent", "enlist", "inlets", "banana", "anaban"]

# ascii = [sum(ord(char) for char in string)  for string in word_list]

# counts = [ascii.count(one) for one in ascii]

# print(ascii)
# print(counts)
# print(max(counts))

word_list = ["listen", "silent", "enlist", "inlets", "banana", "anaban"]

# ascii_values = [sum(ord(word) for word in string) for string in word_list]

# count_values = [ascii_values.count(one) for one in  ascii_values]

# print(word_list[ascii_values.index(max(ascii_values))])

# print(max(count_values))


word_list = [sum(ord(char) for char in String) for String in word_list]
count_values = [word_list.count(item) for item in word_list]
print(max(count_values))