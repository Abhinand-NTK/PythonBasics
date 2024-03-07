

# LinearSearch

n = int(input("Enter the no of elements :-"))
ls = list(input("Enter the elements in the list by separating by a comma::--").split(","))
key = str(input("Enter the key ::--"))
found = False
print(ls)
for i in range(n):
    if  ls[i] == key:
        found = True
        print("The element is found in the position in :--",i+1)
        break

if not found :
    print("The element is not found")