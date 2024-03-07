

n = 'aba'
mid = len(n)//2
left = n[0:mid]
right = n[-1:mid - len(n) :-1]
print(left,right)
if left == right:
    print("it is an palidrome")