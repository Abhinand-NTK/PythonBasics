#Binery Search

# ls = input("Enter the elements in the list after a comma :-").split(',')
# key = str(input("Enter the key value :--"))
# low = 0
# ls.sort() 
# high = len(ls)-1


# while low <= high:
#     mid = (low + high) // 2
#     if ls[mid] == key:
#         print("The element is found at postion in the ",mid + 1)
#         break
#     elif ls[mid] < key:
#         low = mid + 1
#     else:
#         high = mid - 1



elements = list(map(int, input("Enter the elements one after another separated by commas: ").split(',')))
key = int(input("Enter the key element to search: "))
elements.sort()
low = 0
heigh = len(elements) - 1

while low <= heigh:
    mid = (low + heigh) // 2  # Calculate mid inside the loop
    if elements[mid] == key:
        print(f"The element is present in the list at position {mid}.")
        break  # Add break to exit the loop once element is found
    elif elements[mid] < key:
        low = mid + 1
    else:
        heigh = mid - 1  # Fix the update for heigh variable
else:
    print("The element is not present in the list.")

