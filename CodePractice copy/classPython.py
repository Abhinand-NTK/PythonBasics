class MyClass:

    class_attribute = "I am a class attribute"
    
    def __init__(self):
        self.instance_attribute = "I am an instance attribute"
    
    def instance_method(self):
        return "I am an instance method"

# Attribute references:
print(MyClass.class_attribute)      # Accessing a class attribute
obj = MyClass()
print(obj.instance_attribute)       # Accessing an instance attribute
print(obj.instance_method())        # Calling an instance method
print("dict",MyClass.__dict__)
print("dict",dir())


# Encapsulation 

class BankAccount:
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.__balance = balance

    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")
    
    def get_balance(self):
        return self.__balance
    
# Usage:
account = BankAccount("123456789", 1000)
account.withdraw(500)
print(account.get_balance())
print(account.account_no)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Usage:
rectangle = Rectangle(5, 4)
print(rectangle.area())  # Output: 20

circle = Circle(3)
print(circle.area())  # Output: 28.26
