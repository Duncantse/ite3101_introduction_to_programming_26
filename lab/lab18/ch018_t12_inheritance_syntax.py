class Shape(object):
    """Makes shapes!"""

    def __init__(self, number_of_sides: int):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!

class Triangle(Shape):
    def __init__(self, side1: int , sede2: int, side3: int):
        self.side1 = side1
