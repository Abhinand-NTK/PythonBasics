    # linked list head

class Node:
    """
    Class for Creating the new nodes for the list
    """
    # Node of the linked list

    def __init__(self, data):
        """
        Funtion for initilize the node 
        """
        self.data = data  # The time while when we create a object for the class we want to pass a data as the value of the node
        # The variable is using to store the ref("Means the memory location") of the next node
        self.next = None


class LinkedList:
    """
    Class for Declaraing the LinKedList
    """

    # Basically this is the class for creating the linked list means adding 
    # values ,deleting sorting all the performance want to perform here

    def __init__(self):
        """
        Funtion for intilize the list object means the head of the node
        """
        self.head = None


    def push(self,data):
        """
        Adding a node in the begining 
        """
        Newnode = Node(data) # created a object for the node class and make the
        Newnode.next = self.head
        self.head = Newnode

    def Append(self,data):
        """
        Function for adding the element in the backofthe list
        """
        Newnode =  Node(data)# Create a new node
        #Checking the selfnode is empty of not if empty we will add the node as the intial node 
        if self.head is None:
            self.head = Newnode
            return None # and return the Node
        last = self.head
        #Other Wise will consider head as the last node and will loop until the last node came to appear 
        while last.next:
            last = last.next
        last.next = Newnode # heance after finding the last node the while loop 
        # will exist means the last node next will be none
        # so we can assign the new object of the node in the last varible

    def Search(self,value):
        """
        Funtion for adding  a value in after a value in the linked list
        """

        current = self.head


        while current:
            print("I am while loop and working well",current.data,value)
            if current.data == value:
                return "The value is in the linked list"
            current = current.next

        return "The value is not in the list"


    def AddElementAfterGivenValue(self,value,data):
        """
        Funtion for adding a value after a given value
        """
        position = self.head

        while position:
            if position.data == value:
                new_node = Node(data)  # Create a new node with the given data
                new_node.next = position.next  # Set the new node's next to the next of the current node
                position.next = new_node  # Set the current node's next to the new node
                return  # Exit the function after adding the new node
            position = position.next

        return "The value is not in the list"  # Return a message if the given value is not found
          

    def print(self):
        """
        For printing the valuesn in the list
        """
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
    
    def print_nodes(self):
        """
        This function is added to provide a better understanding 
        of the objects of the Node class. When elements are inserted at the beginning,
        an object of the Node class is created, and it will have its own memory space along
        with two additional data points. The first one is the reference of the linked node, 
        and the other one is the value stored in the node. Run the code and check 
        the object reference value for more information.
        """
        temp = self.head
        while temp:
            print(f"Node: {temp}, Data: {temp.data}, Next: {temp.next}")
            temp = temp.next



link = LinkedList()


# link.push(1) 
# link.push(2) 
# link.push(3)

# link.print()
# link.print_nodes()


link.Append(1)
link.Append(2)
link.Append(3)

link.AddElementAfterGivenValue(2,5)


link.print()
link.print_nodes()

# print(link.Search(1))