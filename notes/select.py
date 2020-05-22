'''
File that is used on PythonAnywhere iPython console to do
a demo of the Comparison Sorting algorithm that makes
up the Selection Sort algorithm
'''
try:
    from colorama import Back, Fore, Style
except BaseException:
    print("No terminal colour output! Install colorama!")

from random import shuffle
from inspect import getsourcelines


def fprint(fname):
    '''
    In IPython, you have the very convenient "func"??
    which will inspect the source code (http://j.mp/inspectThis)

    My own function source code inspection function
    Filters out any print statements and input statements
    '''
    lines, count = getsourcelines(fname)
    print("----source code for", fname.__name__)
    clines = ""
    for line in lines:
        if fname.__name__ == "fprint" or \
            ("print" not in line and
             "input()" not in line and
             ".magic" not in line):
            clines = clines + line
    print(clines)


def selection_sort(collection):
    """Pure implementation of the selection sort algorithm in Python
    
    @param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    
    @return: the same collection ordered by ascending
    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> selection_sort([])
    []
    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        collection[least], collection[i] = (
            collection[i], collection[least]
        )
    return collection


def swap(alist, ai, bi):
    '''swap two elements in a list'''
    alist[ai], alist[bi] = alist[bi], alist[ai]
    return alist


def min_index(alist, i):
    n = len(alist)
    print(*enumerate(alist[i:], i))
    input()
    min_i = i
    for j in range(i + 1, n):
        if alist[j] < alist[min_i]:
            min_i = j
    try:
        print(
            Back.RED +
            "Found minimum {0} at {1}".format(
                alist[min_i],
                min_i))
        print(Style.RESET_ALL, end="")
    except BaseException:
        print("Found minimum {0} at {1}".format(alist[min_i], min_i))

    input()
    return min_i


def print_history(hlist):
    for i, h in enumerate(hlist):
        if i != 0:
            print("     ", h[:i], end="")
            print(Back.BLUE + str(h[i:]))
            print(Style.RESET_ALL, end="")
            #print("      {0}{1}".format(h[:i], h[i:]))
        else:
            print("      {0}".format(h))


def selectsort(alist):
    get_ipython().magic('clear ')
    hlist = []
    n = len(alist)
    for i in range(n - 1):
        try:
            print(Style.RESET_ALL, end="")
            print_history(hlist)
            print("inter", alist[:i], end="")
            print(Back.BLUE + str(alist[i:]))
            print(Style.RESET_ALL, end="")
            hlist.append(alist.copy())
        except BaseException:
            print("inter {0}{1}".format(alist[:i], alist[i:]))
        # find index of min value
        # in unsorted sublist alist[i+1:]
        min_i = min_index(alist, i)
        # swap it with element at index 'i'
        try:
            print(Back.GREEN +
                  "--> swapping {0} and {1}".format(alist[min_i], alist[i]))
            print(Style.RESET_ALL, end="")
        except BaseException:
            print("--> swapping {0} and {1}".format(alist[min_i], alist[i]))
        alist[min_i], alist[i] = alist[i], alist[min_i]
        input()

    print(alist)
    input()
    return alist


def selectsortf(alist):
    get_ipython().magic('clear ')
    n = len(alist)
    for i in range(n - 1):
        print("inter ", end="")
        print(Back.BLUE + alist[:i], end="")
        print(Style.RESET_ALL + alist[i:])
        #print("inter {0}{1}".format(alist[:i],alist[i:]))
        # find index of min value
        # in unsorted sublist alist[i+1:]
        min_i = min_index(alist, i)
        # swap it with element at index 'i'
        if min_i != i:
            print(Back.GREEN +
                  "--> swapping {0} and {1}".format(alist[min_i], alist[i]))
            alist[min_i], alist[i] = alist[i], alist[min_i]

            input()
            print(Style.RESET_ALL, end="")
    print(alist)
    input()
    print(Style.RESET_ALL, end="")
    return alist


def selectsortc(alist):
    n = len(alist)
    for i in range(n - 1):
        # find index of min value
        # in unsorted sublist alist[i+1:]
        min_i = min_index(alist, i)
        # swap it with element at index 'i'
        if min_i != i:
            alist[min_i], alist[i] = alist[i], alist[min_i]

    return alist


def selectsortd(alist):
    n = len(alist)
    for i in range(n - 1):
        # find index of min value
        # in unsorted sublist alist[i+1:]
        min_i = min_index(alist, i)
        # swap it with element at index 'i'
        alist[min_i], alist[i] = alist[i], alist[min_i]

    return alist


def min_index_c(alist, i):
    '''function returns the index of the
    minimum value in the sublist alist[i:]
    '''
    n = len(alist)
    min_i = i
    for j in range(i + 1, n):
        if alist[j] < alist[min_i]:
            min_i = j
    return min_i


# Interactive script starts below

get_ipython().magic('clear ')
al = list(range(11, 19))
while True:
    shuffle(al)
    print(al)
    choice = input("Okay?")
    if not choice or choice in 'nN':
        continue
    else:
        break

selectsort(al)
fprint(min_index)
input()
fprint(selectsortd)
input()

# Run Select Sort on the same sorted list
# Challenge students to come up with improvement
selectsort(al)
get_ipython().magic('psource selectsortd ')
input("\nDoes Anyone have the answer on how to improve SelectionSort?\n")
get_ipython().magic('clear ')
get_ipython().magic('psource min_index_c ')
input()
print("----")
get_ipython().magic('psource selectsortc ')
input()
