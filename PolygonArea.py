# Mayolo Valencia
# From a set of input parameters this program displays
# a rectangle or square depending on the parameters
# also returns the area and its diagonal length
class Rectangle:
    
    # initialize the width and height of the rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # returns a description oif the width and height of the rectangle
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    # allows user to set width
    def set_width(self, width):
        self.width = width
    
    # allows user to set height
    def set_height(self, height):
        self.height = height
    
    # returns the area of the given arguments
    def get_area(self):
        return self.width * self.height
    
    # gets the perimeter of the given arguments
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    # gets the diagonal length
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    # makes a picture of the square but has set parameters
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        string = (("* " * self.width) + "\n") * self.height
        return string
    
    
    def get_amount_inside(self, shape):
        return int(self.get_area()/ shape.get_area())
    
                   
class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f'Square(side={self.width})'
    
    
    def set_side(self, side):
        self.width = side
        self.height = side
        
        
        
def main():
    
    rect = Rectangle(5, 10)
    print(rect.get_area())
    rect.set_width(10)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())
    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    
main()
