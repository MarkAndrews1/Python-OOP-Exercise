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
        """Makes a new generator with start"""
        self.start = start
        self.next = start

    def __repr__(self):
        """Shows representation"""
        return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        """Returns the start plus one"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        '''Resets the start to the original number'''
        self.next = self.start
