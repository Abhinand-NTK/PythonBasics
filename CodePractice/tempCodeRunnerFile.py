ascii_values = [sum(ord(word) for word in string) for string in word_list]

count_values = [ascii_values.count(one) for one in  ascii_values]

print(word_list[ascii_values.index(max(ascii_values))])

print(max(count_values))