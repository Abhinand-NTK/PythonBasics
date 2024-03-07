my_tuple = (1, 2, 3, 4, 5)
my_iterator = iter(my_tuple)


# Retrieve and print each element from the iterator
while True:
    try:
        value = next(my_iterator)
        print(value)
    except StopIteration:
        break


class Sequecne:

    def __init__(self,s):
        self._index = 0 
        self._s = s


    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._s):
            return  self._s[self._index]
        else:
            raise StopIteration
        
