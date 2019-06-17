'''
File that is used on PythonAnywhere iPython console to do
a demo of the Divide and Conquer concepts that make
up the Merge Sort algorithm
'''
from colorama import Fore, Back, Style
'''
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
'''

from inspect import getsource, getsourcelines

def fprint(fname):
    '''
    My own function source code inspection function
    Filters out any print statements and input statements
    '''
    lines, count = getsourcelines(fname)
    print("----source code for", fname.__name__)
    clines = ""
    for line in lines:
        if fname.__name__ == "fprint" or \
            ("print" not in line and \
            "input()" not in line):
            clines = clines + line
    print(clines)


def divideTwo(al):
  '''
  function which takes a list and returns two halves
  '''
  mid = len(al)//2
  print('  Using {0} and {1}'.format( "al[:"+str(mid)+"]","al["+str(mid)+":]"),)
  print(Back.RED + '  ...got {0} and {1}'.format(al[:mid], al[mid:]))
  print(Style.RESET_ALL, end="")
  return al[:mid], al[mid:]


def merge(A, B):
  '''
  merge generates a new sorted list containing
  all elements contained in both sorted lists
  '''
  print('     {0} and {1} merged into '.format(A,B))
  merged = [
    (A if A[0] < B[0] else B).pop(0)
    for _ in A+B if A and B
  ] + A + B
  print(Back.GREEN + "       --> ", merged)
  print(Style.RESET_ALL, end="")
  input()
  return merged


def mergesort(alist):
  '''sorts the list using the mergesort algorithm'''
  if (len(alist)) < 2:
    return alist

  left, right = divideTwo(alist)

  leftsorted  = mergesort(left)
  rightsorted = mergesort(right)

  return merge(leftsorted, rightsorted)

#-------------
oddstr = 'list(range(1, 11, 2))'
evenstr= 'list(range(2, 11, 2))'

get_ipython().magic('clear ')
print(oddstr)
input()
odd = eval(oddstr)
print("odd = ", odd)
input()
even = eval(evenstr)
print("even = ", even)
input()
print("odd + even = ", odd + even)
input()
print("executing merge(odd, even)...")
merge(odd, even)


#-------------
# Various lists to be initialized
from random import shuffle
al4 = list(range(1, 5))
ual4 = al4[:]
shuffle(ual4)

al8 = list(range(1, 9))
ual8 = al8[:]
shuffle(ual8)

get_ipython().magic('clear ')
print("al4", al4)
print("ual4", ual4)
print("al8", al8)
print("ual8", ual8)

input("Continue?...")
get_ipython().magic('clear ')

print("using al4", al4)
mergesort(al4)
input("Continue?...")
print("--------")
print("using unsorted", ual4)
mergesort(ual4)
input("Continue?...")
get_ipython().magic('clear ')
print("using al8", al8)
mergesort(al8)
input("Continue?...")
get_ipython().magic('clear ')
print("using unsorted", ual8)
mergesort(ual8)


input("Continue?...")
get_ipython().magic('clear ')
almostal8 = [2, 1, 4, 3, 6, 5, 8, 7]
print("Using almost_al8", almostal8)
mergesort(almostal8)
input("Continue?...")

