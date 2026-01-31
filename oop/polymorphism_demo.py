class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.141592653589793 * self.radius * self.radius