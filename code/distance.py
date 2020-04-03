from math import sqrt


def distance_between(pointA, pointB):
    """calculate distance between two points
    
    Arguments:
    pointA -- first point
    pointB -- second point
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
