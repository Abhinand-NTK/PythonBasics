int_Str = input("Enter the inputs after a comma :")
ls = list(map(int,int_Str.split(',')))

for i in range(1,len(ls)):
    key = ls[i]
    j = i - 1
    while j >= 0 and key < ls[j]:
        ls[j+1] = ls[j]
        j -= 1
    ls[j+1] = key

print("The array is sorted after :- ",ls)


# ls = [345,5,71,2,7,2,772,56,6456]

# def merge_sort(ls):

#     if len(ls)<=1:
#         return ls

#     mid  = len(ls) // 2
#     left = ls[:mid]
#     right = ls[mid:]

#     return Merge(merge_sort(left),merge_sort(right))



# def Merge(left,right):

#     sorted  = []

#     while left and right:
#         if left[0] >= right[0]:
#             sorted.append(right.pop(0))
#         else:     
#             sorted.append(left.pop(0)) 

#     return sorted + left + right


# print(merge_sort(ls))

elements = input("Enter the elements").split(',')
elements = list(map(int,elements))

for i in range(1,len(elements)):

    key = elements[i]

    j = i - 1

    while j >= 0 and key > elements[j]:
        elements[j+1] = elements[j]
        j = j - 1
    elements[j+1] = key

print("Sorted array is :-",elements)
