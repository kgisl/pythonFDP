# Illustrative programs of Tuples, Lists and Dictionaries

## Pre-requisites

- http://j.mp/insertVisual   
- http://j.mp/selectVisual  
- http://j.mp/mergeVisual    
- http://bit.ly/histogramVisual    
- [https://www.toptal.com/developers/sorting-algorithms](https://www.toptal.com/developers/sorting-algorithms)

   
# SelectionSort 

## Pre-requisites
 - http://j.mp/selectVisual 
 - http://j.mp/interactSelect using `[10, 3, 2, 4, 0, 30, 1, 5, 15]`

## In-class Demo
- [http://j.mp/compareSort](http://j.mp/compareSort)

## Algorithm

	repeat (numOfElements - 1) times
		for each of the unsorted elements
			select the minimum value among them
		swap minimum with first unsorted position

## Source code

```python
def selectsort(a):
  n = len(a) 
  for i in range(n-1):
    smallest = min(a[i:])
    index_of_smallest=a.index(smallest, i)
    a[i],a[index_of_smallest]=a[index_of_smallest],a[i]
  return a


```

# InsertionSort 

- http://j.mp/insertVisual 
- http://j.mp/interactInsert using `[10, 3, 2, 4, 0, 30, 1, 5, 15]`

## Algorithm
	mark first element as sorted
	for each unsorted element X
	  'extract' the element X as 'key'
	  insert key at the relevant index so list remains sorted
    return sorted list 

```python

from bisect import insort
def insertsort(alist):
	n = len(alist)
	for i in range(1, n):
        key = alist.pop()
        insort(alist, key, hi=i)
	return alist

alist = [32, 26, 15, 32, 48, 35, 47, 72]
print(insertsort(alist))
```
    
More detailed pseudo-code: 

	mark first element as sorted
	for each unsorted element X
	  extract the element X
	  for j = lastSortedIndex (position -1) down to 0
	    if current element j > X
	      decrement j by 1 
	    else break loop and insert X here
    return sorted list
   
	   
## Source code 2

```python
def insertsort(alist):
	n = len(alist)
    for i in range(1, n):
        key = alist.pop(i)
        # insort(alist, key, hi=i)
        j = i
        while j > 0 and alist[j-1] > key: 
            j -= 1
        alist.insert(j, key) 
        print(key, alist)
    return alist

alist = ['3', '2', '1', '5', '4', '7', '8', '6']
print(insertsort(alist))
```

# MergeSort



[MergeSort Color](http://mergeVisual)


Notice that at each level we divide the array into two halves until we get bunch of single element arrays. This is the divide  portion of the divide and conquer  method. Then, we start merging and sorting the smaller arrays in a series of steps which is the conquer  portion of divide and conquer.

![mergeGIF](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

## Merge example 

1. How many lists are there in Row 4? 
2. Until what row is **Divide** happening? 
3. From which row onwards **Conquer** has begun? 

![mergeExample](http://bit.ly/mergeExample2)


- InsertSort and SelectionSort are examples of **comparison** sorts
- However, MergeSort, is an example of the **Divide-and-Conquer** algorithm sorts

  - **Divide** means portioning the n-element array to be sorted into two sub-arrays of n/2 elements. If A is an array containing zero or one element, then it is already sorted. However, if there are more elements in the array, divide A into two sub-arrays, A1 and A2, each containing about half of the elements of A. 
  - **Conquer** means sorting the two sub-arrays recursively using merge sort. Combine means merging the two sorted sub-arrays of size n/2 to produce the sorted array of n elements.

## Algorithm
The basic steps in the recursive MergeSort Algorithm is as follows: 

	Func MERGESORT: 
	    input (unsorted list of elements)  `ulist` 
	    output (sorted list of elements)   `slist`

	- TERMINAL CASE: 
		- if size of list is 0 or 1, return (since it is sorted)
	- Split the unsorted list (`ulist`) into equal sublists: left sublist and right sublist 
	- Recursively call MergeSort on the left sublist (`leftA`) 
	- Recursively call MergeSort on the right sublist (`leftB`) 
	- Merge the sorted left and sorted right sublists to form one sorted list 
	- Return the sorted list (`slist`) 

## MergeSort implementation in Python

Visualize at http://tinyurl.com/visualMerge 

```python
# a helper function for the mergesort function
# function to merge already sorted lists
def merge(A, B): 
  C = []
  while A and B:
    candidate = (A if A[0] < B[0] else B).pop(0)
    C.append(candidate)

  # pick up the residual elements in A or B	
  C += A + B
  return C

def mergesort(ulist): 
  if len(ulist) <= 1: 
    return ulist

  mid = int(len(ulist)/2)

  leftA    = ulist[:mid]
  rightB   = ulist[mid:]

  sortedA  = mergesort(leftA) 
  sortedB  = mergesort(rightB)
	
  slist = merge(sortedA, sortedB)
  return slist

# test cases
assert (merge([1, 2, 3], [4, 5, 10]) == [1, 2, 3, 4, 5, 10])
alist = [6, 2, 1, 5, 8, 7, 4, 3]
print(mergesort(alist))
# [1, 2, 3, 4, 5, 6, 7, 8]
```


## Histogram 

- http://bit.ly/histogramVisual


<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA0MjMyODk3OSw3ODg0NDgxMTEsLTMyMz
c4NDY3NCw2NTI4MTgyNTQsMTQyOTM3MzgxNywyMDg0NTg5NTY0
LDIxMzMyNDc4NTQsMzc1ODUwMTk0LDE2MDk0MzA3NjgsLTE5OD
czOTM5NTYsMjIwMjk5NTUsMTMxMzEzOTE5NywtMTU3NDMzNTYy
MiwtMTQ4NTk4MTIwNSwyNzMzOTU5NDcsLTE4OTk0NjkyNjAsMT
U4OTA3NjkyNCw4MTU2MTIyNDUsLTM0MTc2MjE0NV19
-->