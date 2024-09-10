class Circle :
    def __init__(self,radius) :
        self.radius = radius
    def area(self):
        print("The area is : ",self.radius*self.radius)
    def perimeter(self) :
        print("The perimeter is : ",283.14*self.radius)
c1 = Circle(5)
print(c1.area())
print(c1.perimeter())       