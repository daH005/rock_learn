class GeometricFigure:

    def area(self):
        pass


class Rectangle(GeometricFigure):

    def __init__(self, w, h):
        self._w = w
        self._h = h

    def area(self):
        return self._w * self._h


class Circle(GeometricFigure):

    def __init__(self, r):
        self._r = r

    def area(self):
        return 3.14 * self._r**2


class Rhombus(GeometricFigure):

    def __init__(self, d1, d2):
        self._d1 = d1
        self._d2 = d2

    def area(self):
        return 0.5 * self._d1 * self._d2


if __name__ == '__main__':
    rectangle = Rectangle(5, 5)
    print(rectangle.area())

    circle = Circle(3)
    print(circle.area())

    rhombus = Rhombus(3, 3)
    print(rhombus.area())
