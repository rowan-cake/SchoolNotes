from math import sqrt
from Q3 import distance


def triangleArea(x1,y1,x2,y2,x3,y3):
    """
    Effects: GEts area of triangle

    Paremeters: 
    Blah blah blah

    Returns: An area of a triangle
    """
    side1 = distance(x1,y1,x2,y2) 
    side2 = distance(x2,y2,x3,y3)
    side3 = distance(x3,y3,x1,y1)

    s = (side1+side2+side3)/2
    area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area
print("Enter three points for a triangle")
x1, y1 = map(float, input("(x1, y1):").split())
x2, y2 = map(float, input("(x2, y2):").split())
x3, y3 = map(float, input("(x3, y3):").split())

print("The area of the triangle is:", triangleArea(x1, y1, x2, y2, x3, y3))
