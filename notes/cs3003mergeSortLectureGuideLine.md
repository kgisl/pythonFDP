# Merge Sort Lecture Guideline

# Context setting 
Unit 4 -> Lists, Tuples and Dictionaries -> Illustrative Programs
  - It is very important to use a data type in a real-world case, to understand its true value and benefit. 
  - We are covering three types of sorts 
	 - **Comparison** Algorithms - Insertion Sort and Selection Sort 
	 - **Divide and Conquer** Algorithms - Merge Sort, Quick Sort
  
# Agenda 
- Over the next 20 minutes, we shall see how lists can be used to implement **Merge Sort**

# Pre-req quiz 
- Are you ready?
	- Known to Unknown
- Best practice of a engineering student is to come prepared for the class. 
	- You must spend at least 2 hours reviewing the material taught in class, and preparing for the class 
 - Quiz 
	 -  44+ MCQ in Online Socrative portal 
		- Immediate feedback
	- Paper based 
			- Show of hands? How many completed it? Attempted it?

## Interactive Coding

## Stage - 1
 - How to divide a sorted list into equal halves? 
 - How to mere the list back into original form? 
 - How to form odd and even lists?
	 -  And then merge them together to get sorted numbers from 1 to 8? 

---

## Stage 2

  - How to merge (combine) sorted list? 
  - How to merge odd number list and even number list? 
  - Use PythonAnywhere.com to zoom in and out of a `mergesort` verbose run 

Notice that at each level we divide the array into two halves until we get bunch of single element arrays. This is the divide  portion of the divide and conquer  method. Then, we start merging and sorting the smaller arrays in a series of steps which is the conquer  portion of divide and conquer.

![merge](http://bit.ly/mergeVerbose)


## Merge Sort Description 

tl;dr![tldr](http://bit.ly/tamilMerge)


- InsertSort and SelectionSort are examples of **comparison** sorts
- However, MergeSort, is an example of the **Divide-and-Conquer** algorithm sorts

  - **Divide** means portioning the n-element array to be sorted into two sub-arrays of n/2 elements. If A is an array containing zero or one element, then it is already sorted. However, if there are more elements in the array, divide A into two sub-arrays, A1 and A2, each containing about half of the elements of A. 
  - **Conquer** means sorting the two sub-arrays recursively using merge sort. Combine means merging the two sorted sub-arrays of size n/2 to produce the sorted array of n elements.

## Algorithm

- In `mergesort`, a divide-and-conquer partitioning algorithm (which more often requires extra memory), the input array is divided in two halves, calls itself recursively for the two halves and then merges the two sorted halves. The `merge()` function is used for merging two halves.

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

## Source code

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
  return C + A + B

def mergesort(ulist): 
  if len(ulist) <= 1: 
    return ulist

  mid = len(ulist)//2

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

## Part 2 
_Break Activity for the 20th min_ which also helps students review what was covered until now. 
- Lead with the question: **Can you improve on the above logic?** How can you do it? Please discuss with your immediate neighbour. 
	- Refer to the last question of the Pre-requisite Quiz
		- Ask your faculty for more clues 


## Summary
1. We incrementally developed MergeSort in a "demo mode" 
2. We arrived at the pseudo code 
3. We wrote the equivalent code for SelectionSort 

The beauty of MergeSort is that regardless of the list and how badly it is sorted, O(n) is `nlog(n)` which is favourable among almost most sorting algorithms.  

## Last 2 Minute 

 - respond to Questions from Students 
	 - review the relevant Question Paper snippets
	 - Ask 1 or more students questions from Pre-requisites
  
 - Review Pre-requisites for Histogram (next class) 



<!--stackedit_data:
eyJoaXN0b3J5IjpbNTk0ODUyMDc3LDE0ODMxMjYzNzFdfQ==
-->