**Table of Contents**

* [Lab 8: Sorting](#lab-8-sorting)  
	* [Select vs Insert vs Merge vs Quick](#select-vs-insert-vs-merge-vs-quick)  
	* [Solution Key](#solution-key)  
		* [select sort](#select-sort)  
		* [insert  sort](#insert--sort)  
		* [merge sort](#merge-sort)  
		* [quick sort](#quick-sort)  
	* [Related Material](#related-material)  
	* [What exactly does this accomplish?](#what-exactly-does-this-accomplish)  


# Lab 8: Sorting
Sort the given list using selection sort and insertion sort. 

[TOC]

## Select vs Insert vs Merge vs Quick

- In `selectsort`, the position of the update is pre-determined, starting from the end of the list. We then go **select** the maximum value among the unsorted elements of the list, and swap it with the element in the pre-determined location.
- In `insertsort`, given a key, a copy of a pre-determined element in the list, we  **insert** it at the appropriate location after comparing it with the unsorted elements of the list.
- In `mergesort`, a divide-and-conquer partitioning algorithm (which more often requires extra memory), the input array is divided in two halves, calls itself recursively for the two halves and then merges the two sorted halves. The `merge()` function is used for merging two halves.
- In `quicksort`, also a divide-and-conquer partitioning algorithm (lends itself to be efficiently implemented *in-place* without extra memory), the choice of the pivot element determines how the elements get partitioned, and calls itself recursively for the two partitions. 


## Solution Key 

### select sort

```python
def selectsort(alist):
    for i in range(len(alist)):
        smallest, idx = min(
            (v, i) for i, v in enumerate(alist[i:]))
        alist[i], alist[idx+i] = alist[idx+i], alist[i]
    return alist
```
### insert  sort
```
import bisect
def insert_sort(alist):
    for i in range(len(alist)):
        key = alist.pop() 
        bisect.insort(alist, key, hi=i)
    return alist
```

### merge sort
```python
from itertools import zip_longest
def mergesort(alist, verbose=False):
    def merge(A, B):
        return [
            (A if A[0] < B[0] else B).pop(0)
            for _ in A + B if len(A) and len(B)
        ] + A + B

    series = [[i] for i in alist]
    while len(series) > 1:
        isl = iter(series)
        series = [
            merge(a, b) if b else a
            for a, b in zip_longest(isl, isl)
        ]
    return series[0]
```

### quick sort
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

`lambda` version: 
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

## Related Material 

http://bit.ly/quickSortVideoCD - a video explaining QuickSort incrementally in a CyberDojo session. 

http://bit.ly/quickSortVideo
 

## What exactly does this accomplish? 


```python 
  from threading import Timer
  l = [8, 2, 4, 6, 7, 1]
  for n in l:
      Timer(n, lambda x: print(x), [n]).start()
```
  
