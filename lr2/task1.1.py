
class Rectangle:
    """
    Class Rectangle
    Takes 2 parameters: height and width of the rectangle
    Has 2 methods that return perimeter and area
    """

    def __init__(self, height=1, width=1):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, float):
            raise TypeError("Incorrect type length input")
        if not 0.0 <= height <= 20.0:
            raise ValueError("Incorrect value length input")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError("Incorrect type width input")
        if not 0.0 <= width <= 20.0:
            raise ValueError("Incorrect value width input")
        self.__width = width

    def perimeter(self):
        return 2 * (self.__height + self.__width)

    def area(self):
        return self.__width * self.__height


if __name__ == "__main__":
    obj = Rectangle()
    obj.width = 1.5
    obj.height = 2.0
    print(f"Height {obj.height}")
    print(f"Width {obj.width}")
    print(f"Perimeter {obj.perimeter()}")
    print(f"Area {obj.area()}")
