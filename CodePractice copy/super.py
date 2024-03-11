class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calls the __init__ method of the Parent class
        self.age = age

child = Child("Alice", 10)
print(child.name)  # Output: Alice
print(child.age)   # Output: 10
