def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    mid = len(ls) //2
    left = ls[:mid]
    right = ls[mid:]

    return merge(merge_sort(left),merge_sort(right))

def merge(left,right):

    result = []
    while left and right:
        if left[0] >= right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    return result + left + right

arr = [345,5,71,2,7,2,772,56,6456]      

result = merge_sort(arr)

print("The sorted array is the :-",result)