import itertools

# http://j.mp/zipLongest


def mergesort(series):
    '''iterative mergesort implementation

    @author kgashok
    @param series is a sequence of unsorted elements

    @returns a list containing sorted elements

    Testable docstring? https://docs.python.org/2/library/doctest.html

    >>> mergesort([5, 4, 2, 8, 1, 3, 7, 6])
    [[5], [4], [2], [8], [1], [3], [7], [6]]
    [[4, 5], [2, 8], [1, 3], [6, 7]]
    [[2, 4, 5, 8], [1, 3, 6, 7]]
    [1, 2, 3, 4, 5, 6, 7, 8]
    '''
    def merge(A, B):
        merged = [
            (A if A[0] < B[0] else B).pop(0)
            for _ in A + B if len(A) and len(B)
        ] + A + B
        return merged

    iseries = iseries = [[i] for i in series]
    while len(iseries) > 1:
        # print("\n", iseries)
        print(iseries)
        ilist = iter(iseries)
        iseries = [merge(a, b) if b else a
                   for a, b in itertools.zip_longest(ilist, ilist)]

    return iseries[0]


print("1st test")
print(mergesort([5, 4, 2, 8, 1, 3, 7, 6]))
print("2nd test")
print(mergesort([1, 2, 3, 4, -1, -100, 290, 22, 5]))


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    pass
