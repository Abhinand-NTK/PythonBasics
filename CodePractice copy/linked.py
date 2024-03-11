

# class Node:

#     def __init__(self,data):

#         self.data = data
#         self.next = None

# class LinkidList:

#     def __init__(self):
#         self.head = None
    
#     def add_begin(self,data):

#         newnode = Node(data)
#         newnode.next = self.head
#         self.head = newnode
    
#     def add_end(self,data):

#         if self.head is None:
#             newnode = Node(data)
#             self.head = newnode

#         else:

#             n = self.head
#             while n.next is not None:
#                 n = n.next
#             newnode = Node(data)
#             n.next = newnode
#     def add_after_value(self,value,data):

#         prev = self.head    
#         current = self.head.next
#         while current is not None:
#             if prev.data == value:
#                 newnode = Node(data)
#                 prev.next = newnode
#                 newnode.next = current
#             current = current.next
#             prev = current
#     def add_before(self,data,value):

#         if self.head is None:
#             newnode = Node(data)
#             newnode.next = self.head
#             self.head = newnode
#         else:
#             if self.head.data ==  value:
#                 newnode = Node(data)
#                 newnode.next = self.head
#                 self.head = newnode
            

#             else:
#                 while current is not None:
#                     if current.data == value:
#                         newnode = Node(data)
#                         prev.next = newnode
#                         newnode.next = current
#                     current = current.next
#                     prev = current

#     def pop(self):
#         n=self.head
#         while n.next.next is not None:
#             n = n.next
#         n.next = None
#     def delete_after_a_value(self,value):
#         if self.head is None:
#             return
#         else:
#             if self.head.data == value:
#                 self.head = None
#             else:
#                 current = self.head.next
#                 prev = self.head
#                 while current is not None:
#                     if prev.data == value:
#                         prev.next = current.next
#                         break  
#                     current = current.next
#                     prev = prev.next

#     def reverse(self):
#         prev = None
#         current = self.head
#         while current is not None:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head = prev

        
#     def print(self):

#         n = self.head
#         while n is not None:
#             print(n.data,end=',')
#             n = n.next

# l = LinkidList()
# l.add_end(1)
# l.add_end(2)
# l.add_end(4)
# l.add_end(5)
# l.add_after_value(1,12)
# l.add_before(12,1)
# l.pop()
# l.pop()
# l.delete_after_a_value(1)
# l.reverse()

# l.print()


class Node:

    def __init__(self,data):
        self.next = None
        self.data = data

class LinkedList:

    def __init__(self):

        self.head = None
    
    def add_begin(self,data):
        
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def add_end(self,data):

        if self.head is None:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
        else:
            n = self.head
            while n.next is not None:
                print("Work")
                n = n.next
            newnode = Node(data)
            n.next = newnode
    def print(self):
        n = self.head
        while n is not None:
            print(n.data,end=',')
            n = n.next



l = LinkedList()
             
l.add_begin(1)
l.add_begin(3)
l.add_begin(5)
l.add_begin(5)

l.add_end(3)
l.add_end(5)
l.add_end(3)
l.add_end(7)
l.add_end(43)


l.print()



class Node:
    def __init__(self,value):
        self.next = None
        self.data = value


class LinkedList:

    def __init__(self):
        self.head = None

    def add_begin(self,value):

        newnode = Node(value)
        newnode.next = self.head 
        self.head = newnode
    

    def add_end(self,value):

        if self.head is None:
            newnode = Node(value)
            self.head  = newnode
            return
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            
            newnode  = Node(value)
            n.next = newnode
            # newnode.next = n

    def search(self,value):

        n = self.head
        while n.next is not None:
            if n.data == value:
                return f"The value {value}  is  present in the linked list"
            n = n.next
    
    def add_after_a_Element(self,element,value):
        n = self.head
        while n.next is not None:
            if n.data == element:
                newnode = Node(value)
                newnode.next = n.next
                n.next = newnode 
                return
            n = n.next   
        return "The element is not in the Linked list"
            
    def add_Before_the_element(self,element,value):

        prev = self.head
        current = self.head.next

        while current is not None:
            if current.data == element:
                newnode = Node(value)
                newnode.next = current
                prev.next = newnode
            current = current.next
    def print(self):
        n = self.head
        while n is not None:
            print(n.data,end="=>")
            n = n.next

    def sorting(self):
        sorted_list = []
        current = self.head
        while current is not None:
            min_element = current.data
            temp = current.next
            while temp is not None:
                if temp.data < min_element:
                    min_element = temp.data
                temp = temp.next
            sorted_list.append(min_element)
            current = current.next
        return sorted_list

                    


li = LinkedList()

li.add_begin(49)
li.add_begin(69)
li.add_begin(449)
li.add_end(45549)

li.add_after_a_Element(49,34)
li.add_Before_the_element(49,34)


li.print()
print(li.sorting())
