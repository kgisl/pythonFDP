**Table of Contents**

* [Lab 8: Sorting](#lab-8-sorting)
	* [Select vs Insert vs Merge vs Quick](#select-vs-insert-vs-merge-vs-quick)
	* [Solution Key](#solution-key)
		* [Simplest insert sort](#simplest-insert-sort)
	* [Related Material](#related-material)
	* [Recursive SelectionSort](#recursive-selectionsort)
	* [Recursive InsertSort](#recursive-insertsort)
	* [Recursive QuickSort](#recursive-quicksort)
		* [Related Material](#related-material)
	* [Recursive MergeSort (in-place)](#recursive-mergesort-in-place)
		* [Unit test file](#unit-test-file)
	* [Recursive QuickSort, in-place](#recursive-quicksort-in-place)
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

'''
https://code.activestate.com/recipes/576917-functional-selection-sort/#c1 
'''

def selection_sortr(L):
    if not L: return [] # terminal case
    # select the minimum value and the index where it is located
    idx, v = min(enumerate(L), key=lambda e: e[1])
    #v, idx = min((v, i) for i, v in enumerate(L))

    print(v, L[:idx], L[idx+1:])
    return [v] + selection_sortr(L[:idx] + L[idx+1:])
    
```
**Output**
```
>> selection_sortr([1,56, 99, -1, 22, 99])
-1 [1, 56, 99] [22, 99]
1 [] [56, 99, 22, 99]
22 [56, 99] [99]
56 [] [99, 99]
99 [] [99]
99 [] []
=> [-1, 1, 22, 56, 99, 99]
```

## Recursive InsertSort

```python
import bisect
def insertion_sortr(L, nsorted=1):
    if nsorted >= len(L): return L  # terminal case
    key = L.pop() # pre-determined location
	# place key in sublist of 'nsorted' elements
	bisect.insort(L, key, hi=nsorted) 
	print(L)
    return insertion_sortr(L, nsorted + 1)
```
**Output**
```

insertion_sortr([1, 56, 99, -1, 22, 99])
99 [1, 56, 99, -1, 22]
22 [1, 99, 56, 99, -1]
-1 [1, 22, 99, 56, 99]
99 [-1, 1, 22, 99, 56]
56 [-1, 1, 22, 99, 99]
=> [-1, 1, 22, 56, 99, 99]
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

### Related Material 

http://bit.ly/quickSortVideoCD - a video explaining QuickSort incrementally in a CyberDojo session. 


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
  
  # avoid `extend`, since it will not do in-place 
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



### Unit test file

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

## Recursive QuickSort, in-place 

```python

def swap(arr,x,y):
    mem = arr[x]
    arr[x] = arr[y]
    arr[y] = mem
    

def qsort(ar,start,end):
    # base case
    if end-start <= 0:
        return ar
    # pivot
    pivot = ar[end]
    # init index for the next pivot
    # which is used in the next recursive qsort calls below
    ind = start
    # loop less final value (pivot)
    for i in range(start,end):
        elem = ar[i]
        if elem <= pivot:
            # move lesser elements to the left side
            swap(ar,i,ind)
            ind += 1
        else:
            # leave greater elements as-is
            pass
    swap(ar,ind,end) # swap in the pivot element
    print(ar)
    # left side contains pivot, and lesser elements
    ar = qsort(ar,start,ind-1)
    # right side contain greater elements than pivot
    ar = qsort(ar,ind+1,end)
    return ar
    
n = int(input())
ar = [int(x) for x in input().split()]
qsort(ar,0,n-1)

```

### Related Material

http://bit.ly/quickSortVideo



## What exactly does this accomplish? 


```python 
  from threading import Timer
  l = [8, 2, 4, 6, 7, 1]
  for n in l:
      Timer(n, lambda x: print(x), [n]).start()
```
  