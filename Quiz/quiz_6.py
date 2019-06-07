# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the method change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by *** and Eric Martin for COMP9021


from math import sqrt


class PointError(Exception):
    def __init__(self, message):
        self.message = message


class Point():
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif x is None or y is None:
            raise PointError('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y

    # Possibly define other methods


class TriangleError(Exception):
    def __init__(self, message):
        self.message = message


class Triangle():
    '''
    >>> p1 = Point(1, 2)
    >>> p2 = Point(4, 8)
    >>> p3 = Point(2, 4)
    >>> triangle = Triangle(point_1 = p1, point_2 = p2, point_3 = p3)
    Traceback (most recent call last):
    ...
    TriangleError: Incorrect input, triangle not created.

    >>> p3 = Point(3,5)
    >>> triangle = Triangle(point_1 = p1, point_2 = p2, point_3 = p3)
    >>> triangle.perimeter
    13.476032868131739
    >>> triangle.area
    1.5
    >>> p3 = Point(2,4)
    >>> triangle.change_point_or_points(point_3 = p3)
    Incorrect input, triangle not modified.
    >>> triangle.perimeter
    13.476032868131739
    >>> triangle.area
    1.5
    >>> p0 = Point(0,0)
    >>> p3 = Point(0,4)
    >>> triangle.change_point_or_points(point_3 = p3, point_1 = p0)
    >>> triangle.perimeter
    18.60112615949154
    >>> triangle.area
    8.0
    >>> triangle.change_point_or_points(point_2 = Point(4,0))
    >>> triangle.area
    8.0
    >>> triangle.change_point_or_points(point_3 = Point(4,0))
    Incorrect input, triangle not modified.
    >>> triangle.change_point_or_points(point_3 = Point(4,8))
    >>> triangle.area
    16.0
    >>> triangle.perimeter
    20.94427190999916
    '''



    def __init__(self, *, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self._compute_perimeter()
        self._compute_area()
        if self.area == 0:
            raise TriangleError('Incorrect input, triangle not created.')
        # Replace pass above with your code

    def change_point_or_points(self, *, point_1 = None,point_2 = None, point_3 = None):
        a, b, c = self.point_1, self.point_2, self.point_3
        if point_1 is not None:
            a = point_1
        if point_2 is not None:
            b = point_2
        if point_3 is not None:
            c = point_3
        if abs(((b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)) / 2) == 0:
            print('Incorrect input, triangle not modified.')
        else:
            self.point_1 = a
            self.point_2 = b
            self.point_3 = c
        self._compute_perimeter()
        self._compute_area()
        # Replace pass above with your code

    # Possibly define other methods
    def _compute_perimeter(self):
        self.perimeter = \
            sqrt((self.point_1.y - self.point_2.y) ** 2 + (self.point_2.x - self.point_1.x) ** 2) + \
            sqrt((self.point_3.y - self.point_2.y) ** 2 + (self.point_3.x - self.point_1.x) ** 2) + \
            sqrt((self.point_1.y - self.point_3.y) ** 2 + (self.point_2.x - self.point_3.x) ** 2)

    def _compute_area(self):
        self.area = \
            abs(((self.point_2.x - self.point_1.x) * (self.point_3.y - self.point_1.y) - \
                (self.point_3.x - self.point_1.x) * (self.point_2.y - self.point_1.y)) / 2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
