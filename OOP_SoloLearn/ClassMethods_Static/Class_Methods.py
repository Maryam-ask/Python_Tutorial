class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)
    # new_square is a class method and is called on the class, rather than on an instance of the class.
    # It returns a new object of the class cls.


square = Rectangle.new_square(5)