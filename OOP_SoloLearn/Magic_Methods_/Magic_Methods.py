class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        The __add__ method allows for the definition of a custom behavior for the + operator in our class.
        As you can see, it adds the corresponding attributes of the objects.
        Once it's defined, we can add two objects of the class together.
        :param other:
        :return: a new object, containing the result.
        """
        return Vector2D(self.x + other.x, self.y + other.y)


first = Vector2D(5, 7)
second = Vector2D(3, 9)

result = first + second
print(result.x)
print(result.y)