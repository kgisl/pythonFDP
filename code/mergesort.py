import itertools

# http://j.mp/zipLongest

def mergesort(series):
    def merge(A, B):
        merged = [
            (A if A[0] < B[0] else B).pop(0)
            for _ in A + B if len(A) and len(B)
        ] + A + B
        return merged

    iseries = iseries = [[i] for i in series]
    while len(iseries) > 1:
        print("\n", iseries)
        ilist = iter(iseries)
        iseries = [merge(a, b) if b else a
                   for a, b in itertools.zip_longest(ilist, ilist)]

    return iseries[0]


print(mergesort([1, 2, 3, 4, -1, -100, 290, 22, 5]))
