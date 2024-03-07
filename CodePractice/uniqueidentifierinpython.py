x = 7 # here the x is the identifier that is using to store the value
y = x
print(id(x))
print(id(y)) # The output of it is the uniqueidentifier for the value 7 it is the memory location 


a = 10
b = 10
print(id(a) == id(b)) 
print(id(a)) 
print(id(b)) 

# the below is the diffence of the allocation of memory address for the mutable and the immutable objects

x = 23
y = 23
z = [1, 2, 3]
w = [1, 2, 3]

print(id(x))  # Output: Unique identifier for integer object x
print(id(y))  # Output: Same as above (same value, same memory location)
print(id(z))  # Output: Unique identifier for list object z
print(id(w))  # Output: Unique identifier for list object w here the value identifier is diffent for each cause it is mutable
# the same is for the dict also


c = 444545
d = 444545

print(id(c),id(d))