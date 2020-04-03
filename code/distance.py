from math import sqrt


def distance_between(pointA, pointB):
    """Computes the distance between two Point objects.

    @author kgashok
    
    @param pointA is a tuple  
    @param PointB is a tuple  
    """
    x1, y1 = pointA
    x2, y2 = pointB

    distx = x1 - x2
    disty = y1 - y2

    return sqrt(distx**2 + disty**2)


# main program
# tuple packing allows for assigning
# multiple inputs in one statement
pointA = int(input("Enter xcordinate for PointA ")), \
    int(input("Enter ycordinate for PointA "))

pointB = int(input("Enter xcordinate for PointB ")), \
    int(input("Enter ycordinate for PointB "))

print(distance_between(pointA, pointB))
