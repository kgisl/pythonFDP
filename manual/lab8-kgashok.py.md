# Lab 8: Sorting
Sort the given list using selection sort and insertion sort. 


## Solution Key 

```python

def selectionSort(alist):
    # start filling from the end of the list
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        # find the position of the maximum value
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        # swap the fillslot with the maximum value
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):

  # scan every element to determined where it must be inserted
  for index in range(1, len(alist)):
  currentvalue = alist[index]
  # current location where it is situated
  location = index

  # determine which location it should be at 
  while location > 0:
    if alist[location - 1] > currentvalue:
        alist[location] = alist[location - 1]
        location = location - 1
    else:
      break
  # end of inner while loop 
   
  # update the list with the current element in consideration
  alist[location] = currentvalue
  # end of outer for loop

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

```

## Related Material 

- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html



## Recursive version of SelectionSort 

```python
def selsort(l):
    if not l: return []
    idx, v = min(enumerate(l), key=operator.itemgetter(1))
    return [v] + selsort(l[:idx] + l[idx + 1:])
```

## Recursive QuickSort 

http://mcsp.wartburg.edu/zelle/python/sigcse-workshop/mgp00064.html

```python 

def qsort(L): 
  if len (L) <= 1: return L

  return qsort([n for n in L[1:] if n < L[0]]) + \
    [L[0]] + \
    qsort([n for n in L[1:] if n >= L[0]])

```

or 
```python
def qsort(L):
  if len(L) <= 1: return L
    
  def subList(pivot, op):
    return [elem for elem in L[1:] if op(elem, pivot)]

  return qsort(subList(L[0], operator.lt)) + \
    [L[0]] + \
    qsort(subList(L[0], operator.ge))

```

or using `lambda` and `filter`

```python
from operator import ge as greater, lt as lesser

def qsort(L): 
  if len(L) <= 1: return L
  pivot   = L[0]
  sublist = lambda op: [*filter(lambda num: op(num, pivot), L[1:])]

  return qsort(sublist(lesser))+ [pivot] + qsort(sublist(greater))

print(qsort([3,1,4,2,5]) == [1,2,3,4,5])
```

and the most efficient: 

```python 

import random

def quicksort(s):
  len_s = len(s)
  if len_s < 2:
    return s

  pivot = s[random.randrange(0, len_s)]

  L = [x for x in s if x < pivot]
  E = [x for x in s if x == pivot]
  G = [x for x in s if x > pivot]

  return quicksort(L) + E + quicksort(G)

```

Improved version of `lambda` code (without using `filter`):
```python

from operator import ge, lt

def qsort(L, first=True):
  if len(L) <= 1: 
    return L

  L = L[:] if first else L  
  pivot = L.pop()
  sublist = lambda op: [n for n in L if op(n, pivot)]

  return [*qsort(sublist(lt), False), pivot, *qsort(sublist(ge), False)]

```

## Recursive MergeSort (in-place)

```python

def mergesort(nums):
  print ("nums:", nums)
  n = len(nums)
  if n > 1:
    # split into sublists
    m = n // 2
    nums1, nums2 = nums[:m], nums[m:]
    # recursively sort each piece 
    mergesort(nums1)
    mergesort(nums2)
    # merge the sorted pieces back into original list
    merge(nums1, nums2, nums)


def merge(lst1, lst2, lst3): 
  i1, i2, i3 = 0, 0, 0
  n1, n2 = len(lst1), len(lst2)

  print(lst1, lst2, lst3)
  while i1<n1 and i2<n2: 
    print(i1, i2, i3)
    if lst1[i1] < lst2[i2]: 
      lst3[i3] = lst1[i1]
      i1 = i1 + 1
    else:
      lst3[i3] = lst2[i2]
      i2 = i2  + 1
    i3 = i3 + 1 
    
  while i1 < n1: 
    lst3[i3] = lst1[i1]
    i1 = i1 + 1
    i3 = i3 + 1 
  while i2 < n2: 
    lst3[i3] = lst2[i2]
    i2 = i2 + 1
    i3 = i3 + 1 

  print("Interim (nums):", lst3)
```

### Test file

```python

from mergesort import mergesort
import unittest
import random

class Test_mergesort(unittest.TestCase):

    def test_simple_lists(self):
        alist = [1, 4, 5, 2, 4, 3, 10, 2, -4]
        
        expected = sorted(alist)
        mergesort(alist)
        self.assertEqual(expected, alist)


    def generate_random_list(self): 
        alist = []
        for i in range (10): 
            x = [random.randrange(-100, 101, 1)] * random.randrange(0, 6)
            alist.extend(x)
        
        random.shuffle(alist)    
        # print(sorted(alist))
        return alist

    def test_random_list(self):
        alist = self.generate_random_list()

        expected = sorted(alist)
        mergesort(alist)
        self.assertEqual(expected, alist)



if __name__ == '__main__':
    unittest.main()


```

## What exactly does this accomplish? 


```python 
  from threading import Timer
  l = [8, 2, 4, 6, 7, 1]
  for n in l:
      Timer(n, lambda x: print(x), [n]).start()
```
  