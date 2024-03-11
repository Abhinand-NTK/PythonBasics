arry = [4,46,4,73,7,3,5,5]

def arry_to_chunk(arr,n):
   return [arr[item:item+n]for item in range(0,len(arr),n)]


print(arry_to_chunk(arry,3))