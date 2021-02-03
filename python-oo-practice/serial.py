"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """ self.start will store the increment start value
            self.original will reference the original start value.
        """ 
        self.start = start 
        self.original = start 

    def __repr__(self):
        print(f'<SerialGenerator start={self.start}>')

    def generate(self):
        """ Increment self.start by 1 then return it. """
        self.start += 1
        return self.start - 1

    def reset(self):
        """ Reset self.start to its original value, which is stored in self.original """
        self.start = self.original

serial = SerialGenerator(100)
serial.__repr__()
print(serial.generate())
print(serial.generate())
print(serial.generate())
serial.reset()
print(serial.generate())

