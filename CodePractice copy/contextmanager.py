# https://www.geeksforgeeks.org/context-manager-in-python/

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Example usage
with FileManager('example.txt', 'w') as file:
    file.write('Hello, world!')


from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()

# Example usage
with file_manager('example.txt', 'w') as file:
    file.write('Hello, world!')
