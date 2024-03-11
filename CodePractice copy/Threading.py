import threading

# Define a function that will be executed by the thread
def print_numbers():
    for i in range(5):
        print(i)

# Create a thread object
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Thread execution complete")