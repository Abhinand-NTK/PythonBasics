# singletonmodiule can be implmented by different types of setups
# A singleton pattern can be implemented in three different ways. They are as follows:

# Module-level Singleton
# Classic Singleton
# Borg Singleton

# usecases of the singleton 

# Managing a database connection
# Global point access to writing log messages
# File Manager
# Print spooler

class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance

class SingletonChild(SingletonClass):
	pass

singleton = SingletonClass() 
child = SingletonChild()
print(child is singleton)

singleton.singl_variable = "Singleton Variable"
print(child.singl_variable)
