# @property = Decorator used to define method as property (it can be accessed like an attribute)
#             Benefit: Add additional logic when read, write, or delete attributes
#             Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width  #using underscore _width makes attributes protected
        self._height = height #these attributes are meant to be used internally, inside the class

    @property
    def width(self):
        return f"{self._width: .1f}cm"

    @property
    def height(self):
        return f"{self._height: .1f}cm"

    @width.setter  # in this we adding our additional logic
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")


    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
        

rectangle = Rectangle(3, 4)

rectangle.width = 5
rectangle.height = 6

print(rectangle._width)
print(rectangle._height)

del rectangle.width
del rectangle.height