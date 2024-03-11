import os 

print(os.listdir())

for key, value in os.environ.items():
    print(f"{key}: {value}")



print("The type of the os in the python is :;--",type(os))