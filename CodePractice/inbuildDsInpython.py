

ls = input("Enter the elements(seprarated by spacces) ::-")
result = ls.split()
print('The list is :-',result)

# The split function have two arguments such as the first is the seprator means 
# how we need to seprate the string and the second is the 
# maxsplit means how much contenet wee need 

txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(" ")

print(x)


txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 2)

print(x)

ls = [1,2,3,3]

# can add the elements in the backend
ls.append(5)
ls.append(4)

# can add the elements according to the index
ls.insert(3,6)
ls.insert(3,6)

# can add more elments through the backend using the extend
ls.extend([7,8,9])
print(ls)

ls.reverse()
print(ls)

ls = list(reversed(ls))

print(ls)

#reversing the string list using the slice oprations

print(ls[::-1])

# list comprehesion
# find the odd no from the above list

odd = [i for i in ls if i % 2 == 0]

odd_squre = [i*i for i in ls if i % 2 == 0]

print("The odd no is in the list are ::--",odd)

print("The odd_squre no is in the list are ::--",odd_squre)

l =[4,64,64,3,42,9,1,4]

import functools

print("The sum of the ls is ::--",functools.reduce(lambda a, b: a if a > b else b, l))

 
l1 = ["eat", "sleep", "repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)
 
# changing index and printing separately
for count, ele in enumerate(l1,100):
    print (count, ele)



print("The largest elemetn in the list ::--",functools.reduce(lambda a,b: a if a > b else b,l))

res = filter(lambda a : a % 2 == 0,l)
print('odd numbers ::-',list(res))

t =(1,2,3)
print(type(t))
print(t[0])

(a,b,c) = t
print(b)


test = [2,2,22,2,22,2,22]

se = set([2,2,22,2,22,2,22])
se.add(tuple(test))
print(se)