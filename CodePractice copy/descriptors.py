class MyProperty:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class MyClass:
    my_attribute = MyProperty('my_attribute')

obj = MyClass()
obj.my_attribute = 42  # Calls __set__
print(obj.my_attribute)  # Calls __get__
del obj.my_attribute    # Calls __delete__
