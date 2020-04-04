from math import sqrt


def distance_between(pointA, pointB):
    """Computes the distance between two Point objects.

    @author kgashok

    @param pointA is a tuple
    @param pointB is a tuple

    @return distance in float
    """
    x1, y1 = pointA
    x2, y2 = pointB

    distx = x1 - x2
    disty = y1 - y2

    return sqrt(distx**2 + disty**2)


# main program
# tuple packing allows for assigning
# multiple inputs in one statement
print("Enter coordinates for Point A")
pointA = int(input()), int(input())

print("Enter coordinates for Point B")
pointB = int(input()), int(input())

print("distance between points",
      distance_between(pointA, pointB)
      )
