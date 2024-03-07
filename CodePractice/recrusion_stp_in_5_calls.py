def recursive_function(counter):
    # Base case: Stop recursion when counter reaches 5
    if counter == 5:
        print("Reached the limit of 5 calls.")
        return
    
    print("Recursive call #", counter)
    
    # Make the recursive call with an incremented counter
    recursive_function(counter + 1)

# Start the recursion with an initial counter of 1
recursive_function(1)


def r(count):
    if count == 5:
        return print("The limit reached")
    print("The call No:-",count)
    r(count+1)
r(1)