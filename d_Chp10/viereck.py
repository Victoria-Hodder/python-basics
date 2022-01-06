class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


rectangle1 = Rectangle(5,4)
square1 = Square(4)

print(rectangle1.length)
print(rectangle1.area())
print(square1.area())
