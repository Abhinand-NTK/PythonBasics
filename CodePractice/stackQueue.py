# # Python program for implementation of stack

# # import maxsize from sys module
# # Used to return -infinite when stack is empty
# from sys import maxsize

# # Function to create a stack. It initializes size of stack as 0
# def createStack():
# 	stack = []
# 	return stack

# # Stack is empty when stack size is 0
# def isEmpty(stack):
# 	return len(stack) == 0

# # Function to add an item to stack. It increases size by 1
# def push(stack, item):
# 	stack.append(item)
# 	print(item , " pushed to stack ")

# # Function to remove an item from stack. It decreases size by 1
# def pop(stack):
# 	if (isEmpty(stack)):
# 		return str(-maxsize -1) # return minus infinite

# 	return stack.pop()

# # Function to return the top from stack without removing it
# def peek(stack):
# 	if (isEmpty(stack)):
# 		return str(-maxsize -1) # return minus infinite
# 	return stack[len(stack) - 1]

# # Driver program to test above functions
# stack = createStack()
# push(stack, 10)
# push(stack, 20)
# push(stack, 30)
# print(pop(stack) , " popped from stack")

class Stack:
    def __init__(self):
        self.stack = []

    def Push(self, element):
        return self.stack.append(element)

    def max_size(self):
        return self.stack.len()

    def is_empty(self):
        if len(self.stack) == 0:
            print("iam the monster")
            return True
        else:
            return f"Stack have elements  :- {self.stack}"

    def Pop(self):
        if self.is_empty():
            return "The stack is empty"
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty() == True:
            print(self.stack)
            return "The stack is empty"
        else:
            return self.stack[-1]
        
    def mid_element_of_stack(self):

        copy_stack = []
        for itmes in range(len(self.stack)):
            copy_stack.append(self.stack.pop())
        print(copy_stack)
        mid_element = copy_stack[(len(copy_stack)) // 2]
        for copy_items in range(len(copy_stack)):
            self.stack.append(copy_stack.pop())
        return mid_element
    


obj = Stack()
obj.Push(39)
obj.Push(23)
obj.Push(9)

print(obj.stack)
print(obj.peek())
print(obj.is_empty())
print(obj.mid_element_of_stack())
print(obj.stack)


def valid_paranthisis(elment):
    stack = []
    mapping = {"(":")","{":"}","[":"]"}

    for char in elment:
        if char in mapping:
            topelement = stack.pop() if stack else '#'
            if mapping[topelement] != char:
                return False
        else:
            stack.append(char)

    return  not stack

            
            
            
#Queue is usign the stack

class Stack_Using_Queue:

    def __init__(self):

        self.stack1 = []
        self.stack2 = []
    def push(self,element):
        self.stack1.append(element)

    def pop(self):
        self.peek()
        self.stack2.pop()


    def peek(self):
        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]
    
    def print_queue(self):
        
        print("The Queue is :--",f"{self.stack1 + self.stack2}")
    

obj = Stack_Using_Queue()
obj.push(7)
obj.push(6)
obj.push(3)
obj.push(4)
print(obj.print_queue())
obj.pop()
obj.pop()
obj.pop()
print(obj.print_queue())

from collections import deque

stack = deque()
stack.append(40)
stack.append(40)
stack.append(30)
stack.append(440)

print(stack)

stack.append(40)
stack.pop()
stack.pop()
stack.pop()
print(stack)

d = {'a':1,'b':2,'c':3}
data = d.get('d',0)
print(data)

    
