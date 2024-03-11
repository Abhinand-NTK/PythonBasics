# List of dictionaries
my_list = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}]

# Sort the list based on the 'age' key in each dictionary
sorted_list = sorted(my_list, key=lambda x: x['age'])

# Print the sorted list
print(sorted_list)


# List of dictionaries
my_list = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 35}]

# Manually sort the list based on the 'age' key in each dictionary using bubble sort
n = len(my_list)
for i in range(n):
    for j in range(0, n-i-1):
        if my_list[j]['age'] > my_list[j+1]['age']:
            # Swap the dictionaries
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

# Print the sorted list
print(my_list)
