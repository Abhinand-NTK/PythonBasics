def partition(arr,low,heigh):

    pivot = arr[heigh]

    i = low - 1

    for j in range(low,heigh):

        if arr[j] <= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    print(arr)
    arr[i+1],arr[heigh]=arr[heigh],arr[i+1]
    return i + 1
def quicksort(arr,low,heigh):
    if low<heigh:
        pi = partition(arr,low,heigh)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,heigh)


arr = [4,53,46,75,854,75,5,37]

quicksort(arr,0,len(arr)-1)

print("The result after teh sortig is :--",arr)



def findPivotPos(arr,low,heigh):

    pivot = arr[heigh]

    i = low - 1

    for j in range(low,heigh):

        if arr[j] > pivot:
            i += 1
        arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[heigh] = arr[heigh],arr[i+1]

    return i + 1

def QuickSort(arr,low,heigh):

    if low > heigh:
        return arr
    
    pi =  findPivotPos(arr,low,heigh)

    quicksort(arr,pi+1,heigh)
    quicksort(arr,low,pi-1)
