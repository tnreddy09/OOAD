class Shape:

    def __init__(self, name):
        self.name = name
        self.area = 0

    def get_area(self):
        return self.area

    def display_shape(self):
        print("Hey, I'm a {} My area is {}".format(self.name, self.area))


class Circle(Shape):
    """
        Class circle inherits Shape
    """

    def __init__(self, radius):
        super(Circle, self).__init__("Circle")
        self.radius = radius

    def set_area(self):
        self.area = 3.14 * self.radius * self.radius


class Rectangle(Shape):
    """
        Class circle inherits Shape
    """

    def __init__(self, length, breadth):
        super(Rectangle, self).__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def set_area(self):
        self.area = self.length * self.breadth


class Square(Shape):
    """
        Class circle inherits Shape
    """

    def __init__(self, side):
        super(Square, self).__init__("Square")
        self.side = side

    def set_area(self):
        self.area = self.side * self.side
