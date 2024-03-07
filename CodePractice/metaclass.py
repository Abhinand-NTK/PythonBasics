#To create our custom metaclass, our custom metaclass has to inherit type metaclass and usually override – 

#__new__(): It’s a method which is called before __init__(). It creates the object and returns it. We can override this method to control how the objects are created.
#__init__(): This method just initialize the created object passed as a parameter
#We can create classes using the type() function directly. It can be called in following ways – 
#When called with only one argument, it returns the type. We have seen it before in the above examples.
#When called with three parameters, it creates a class. Following arguments are passed to it – 
#Class name
#Tuple having base classes inherited by class
#Class Dictionary: It serves as a local namespace for the class, populated with class methods and variables
#Consider this example –  

# https://www.geeksforgeeks.org/metaprogramming-metaclasses-python/


def test_method(self):
	print("This is Test class method!")

# creating a base class 
class Base:
	def myfun(self):
		print("This is inherited method!")

# Creating Test class dynamically using
# type() method directly
Test = type('Test', (Base, ), dict(x="atul", my_method=test_method))

# Print type of Test 
print("Type of Test class: ", type(Test))

# Creating instance of Test class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))

# calling inherited method
test_obj.myfun()

# calling Test class method
test_obj.my_method()

# printing variable
print(test_obj.x)


# Creating custom Metaclass

# To create our custom metaclass, our custom metaclass has to inherit type metaclass and usually override – 

# __new__(): It’s a method which is called before __init__(). It creates the object and returns it. We can override this method to control how the objects are created.
# __init__(): This method just initialize the created object passed as a parameter
# We can create classes using the type() function directly. It can be called in following ways – 

# When called with only one argument, it returns the type. We have seen it before in the above examples.
# When called with three parameters, it creates a class. Following arguments are passed to it – 
# Class name
# Tuple having base classes inherited by class
# Class Dictionary: It serves as a local namespace for the class, populated with class methods and variables
# Consider this example –  

def test_method(self):
	print("This is Test class method!")

# creating a base class 
class Base:
	def myfun(self):
		print("This is inherited method!")

# Creating Test class dynamically using
# type() method directly
Test = type('Test', (Base, ), dict(x="atul", my_method=test_method))

# Print type of Test 
print("Type of Test class: ", type(Test))

# Creating instance of Test class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))

# calling inherited method
test_obj.myfun()

# calling Test class method
test_obj.my_method()

# printing variable
print(test_obj.x)


class Meta(type):
    def __new__(cls, name, bases, dct):
        # Modify class attributes or add new ones
        dct['custom_attribute'] = 'This is a custom attribute added by the metaclass'
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

# Accessing the custom attribute added by the metaclass
print(MyClass.custom_attribute)  # Output: This is a custom attribute added by the metaclass
