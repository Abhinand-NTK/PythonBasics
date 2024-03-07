## The below the code is an ex For the nonlocal keyword used in the python 
## it can only used in the nexted structures cant use for the local and the global variables

def foo():
	name = "geek" # Our local variable

	def bar():
		nonlocal name		 # Reference name in the upper scope
		name = 'GeeksForGeeks' # Overwrite this variable
		print(name)
		
	# Calling inner function
	bar()
	
	# Printing local variable
	print(name)

foo()
