try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Not a valid number")
else:
    print("You entered:", num)
finally:
    print("This will always execute, regardless of exceptions.")
p