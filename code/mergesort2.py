from heapq import merge
import random
from itertools import zip_longest

# http://j.mp/zipLongest


def mergesort(alist, verbose=False):
    def merge(A, B):
        return [
            (A if A[0] < B[0] else B).pop(0)
            for _ in A + B if len(A) and len(B)
        ] + A + B

    series = [[i] for i in alist]

    while len(series) > 1:
        print("\n", series)
        isl = iter(series)
        series = [
            merge(a, b) if b else a
            for a, b in zip_longest(isl, isl)
        ]
    return series[0]


array = [random.randrange(-40, 40)
         for _ in range(1111)
         ]
print("input", array)
print(mergesort(array))


def mergesort2(w):
    if len(w) < 2:
        return w
    else:
        mid = len(w) // 2
        return merge(mergesort(w[:mid]),
                     mergesort(w[mid:]))
