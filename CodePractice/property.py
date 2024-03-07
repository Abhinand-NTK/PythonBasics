

class Test:
    def __init__(self):
        self.__abhi = 4

    def value(self):
        return self.__abhi
    def set(self,value):
        self.__abhi = value
        return "The value is updated"


obj  = Test()  
print(obj.value())
obj.__abhi = 3
print(obj.value())
obj.set(6)
print(obj.value())

# circle.py

class Circle:

    def __init__(self, radius):
        self._radius = radius

    @property 
    def radius(self):
        """The radius property."""
        print("Get radius")
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Delete radius")
        del self._radius

o = Circle(4)
print(o.radius())