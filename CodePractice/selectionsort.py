# intStr = input("Enter the array after a comma :")
# ls = list(map(int,intStr.split(',')))

# for i in range(len(ls)):
#     min_index = i

#     for j in range(i+1,len(ls)):
#         if ls[min_index] > ls[j]:
#             min_index = j
#     ls[min_index],ls[i] = ls[i],ls[min_index]


# print("The elements are :-",ls)

ls = [46,767,783,8,36]

for i in range(len(ls)):
    min_index = i

    for j in range(i+1,len(ls)):
        if ls[min_index]>ls[j]:
            min_index = j
    ls[i],ls[min_index]=ls[min_index],ls[i]

print("The sorted array is :-",ls)
        