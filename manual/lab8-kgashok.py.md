# Lab 8: Sorting
Sort the given list using selection sort and insertion sort. 

## Select vs Insert vs Merge vs Quick

- In `selectsort`, the position of the update is pre-determined, starting from the end of the list. We then go **select** the maximum value among the unsorted elements of the list, and swap it with the element in the pre-determined location.
- In `insertsort`, given a key, a copy of a pre-determined element in the list, we  **insert** it at the appropriate location after comparing it with the unsorted elements of the list.
- In `mergesort`, a divide-and-conquer partitioning algorithm (which more often requires extra memory), the input array is divided in two halves, calls itself recursively for the two halves and then merges the two sorted halves. The `merge()` function is used for merging two halves.
- In `quicksort`, also a divide-and-conquer partitioning algorithm (lends itself to be efficiently implemented *in-place* without extra memory), the choice of the pivot element determines how the elements get partitioned, and calls itself recursively for the two partitions. 


## Solution Key 

```python

def selectsort(L): 
    # start filling from the end of the list
    for slot in range(len(L)-1, 0, -1):
        positionOfMax = 0
        # find the position of the maximum value
        for location in range(1, slot + 1):
            if L[location] > L[positionOfMax]:
                positionOfMax = location

        # swap the slot with the maximum value
        temp             = L[slot]
        L[slot]          = L[positionOfMax]
        L[positionOfMax] = temp
        print(L) 
        
    return L


def insertsort(L):

  # scan every element to determined where it must be inserted
  # Location 0 constitutes a "sorted" list already. So begin from 1
  for index in range(1, len(L)):
    key = L[index]
    # start with the immediate previous element
    j = index - 1

    # determine which 'j' it should be at
    # meanwhile, keep shifting elements to the right
    while j >= 0 and (L[j] > key):
      L[j + 1] = L[j]
      j = j - 1
      print(L)
    # end of inner while loop 

    # update the list with the current element in consideration
    L[j + 1] = key
  # end of outer for loop
  return L
  
alist = [54,26,93,17,77,31,44,55,20]
selectsort(alist)
print(alist)
alist = [54,26,93,17,77,31,44,55,20]
insertsort(alist)
print(alist)

```

### Simplest insert sort 
First see the video and then code!  http://j.mp/insertSortVideo

```python
def ins_sort(k):
    for i in range(1,len(k)):   
        j = i                   
        while j > 0 and k[j] < k[j-1]: 
            k[j], k[j-1] = k[j-1], k[j] 
            j=j-1 
    return k
```

## Related Material 

- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
- http://bit.ly/insertVisualizer - insertSort in the visualizer 

3-problem series for learning/teaching insertsort

- Part 1- https://www.hackerrank.com/challenges/insertionsort1
- Part 2 - https://www.hackerrank.com/challenges/insertionsort2
- Part 3 - https://www.hackerrank.com/challenges/correctness-invariant  (fix the bug)




## Recursive SelectionSort 

```python
# https://code.activestate.com/recipes/576917-functional-selection-sort/#c1 

import operator 
def selectsortr(l):
    if not l: return []
    idx, v = min(enumerate(l), key=operator.itemgetter(1))
    print(v, l[:idx], l[idx+1:])
    return [v] + selectsortr(l[:idx] + l[idx + 1:])
```

## Recursive InsertSort

```python
import bisect

def insertion_sort(L):
    print(L)
    if len(L) == 1:  
        return L
    else:
        candidate = L.pop()
        bisect.insort(insertion_sort(L), candidate)
        return L
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
  