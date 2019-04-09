def qsort(array):
    return qsort([x for x in array[1:] if x < array[0]]) \
        + [array[0]] \
        + qsort([x for x in array[1:] if x >= array[0]]) if array \
        else []


def qsort(L):
    if not L:
        return []

    return qsort([n for n in L[1:] if n < L[0]]) \
        + [L[0]] \
        + qsort([n for n in L[1:] if n >= L[0]])
