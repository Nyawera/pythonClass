
from cmath import pi


class Circle:
    def __init__(self,radius):
        self.radius= radius
    def area_of_circle(self):    
        area = pi*self.radius**2
        return area


    def circumferance_of_circle(self):
        circumnferance = 2*pi*self.radius
        return circumnferance



class Square:
        def __init__(self,side):
            self.side= side

        def area_of_Square(self):
            area = self.side**2
            return area

        def parameter_of_Square(self):
         Parameter = 4*self.side
         return Parameter

class Rectangle:
    def __init__(self, width,length):
        self.width=width
        self.length= length


    def are_of_rectangle(self):
        area = self.width*self.length
        return area

        def parameter_of_rectangle(self):
            Parameter = 2*(self.width+length.width)
            return Parameter

class Sphere:
    def __init__(self,radius):
        self.radius=radius

    
    
    def area_of_Sphere(Self):
        surface_area= 4*pi* Self.radius * Self.radius
        return surface_area



    def volume(self):
        volume = (4/3)*self.radius*self.radius*self.radius
        return volume






     
           


            



