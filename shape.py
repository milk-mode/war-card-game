class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):

        self.radius=radius
    def area(self):
        return "{:.2f}".format(3.14*(self.radius**2))
    def perimeter(self):
        return "{:.2f}".format(2*3.14*self.radius)

class Rectangle(Shape):
    def __init__(self, length,width):
        self.length=length
        self.width=width
    def area(self):
        return "{:.2f}".format(self.length*self.width)
    def perimeter(self):
        return "{:.2f}".format(2*(self.length+self.width))
    
circle =Circle(10)
rectangle=Rectangle(10,20)

print('circle area: {}'.format(circle.area()))
print('circle perimeter: {}'.format(circle.perimeter()))
print('Rectangle area: {}'.format(rectangle.area()))
print('Rectangle perimeter: {}'.format(rectangle.perimeter()))
