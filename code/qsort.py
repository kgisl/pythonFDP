def qsort_one_liner(array):
    '''function implements qsort algorithm in recursive mode

    @author kgashok
    @param array is list of numbers to be sorted

    @returns sorted array

    >>> qsort_one_liner([4, 3, 2, 3, 6, 0])
    [0, 2, 3, 3, 4, 6]
    '''
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
