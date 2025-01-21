class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculatePerimiter(self):
        return 2*3.14*self.radius
    
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return self.calculatePerimiter() + other
        return self.calculatePerimiter() + other.calculatePerimiter()

cir1 = Circle(2)
cir2 = Circle(2)

print(dir(Circle))