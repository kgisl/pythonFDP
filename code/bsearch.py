def binary_search(alist, token):
    '''function implements binary search algorithm using slicing

    @author kgashok
    @param alist is list of numbers to be searched
    @param token is the number to be find in the list

    @returns True if present, else False

    >>> binary_search([0, 1, 2, 3, 4], 2)
    True
    '''
    while alist:
        mid = len(alist) // 2
        midvalue = alist[mid]

        if token is midvalue:
            return True
        if token < midvalue:
            # for e.g. token is 3, and midvalue is 5
            # throw/slice away the upper half
            alist = alist[:mid]
        else:
            # if token is 7, and midvalue is 5
            # throw/slice away the lower half
            alist = alist[mid + 1:]

    return False
