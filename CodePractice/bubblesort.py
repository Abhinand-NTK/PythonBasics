input_str = input("Enter the elements after a comma :-")

ls = list(map(int,input_str.split(',')))
for i in range(len(ls)):
    for j in range(len(ls)-1-i):    
        if ls[j] > ls[j+1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]


print("The list is after sorting is :--",ls)