# Illustrative programs of Tuples, Lists and Dictionaries

## Pre-requisites

- http://j.mp/insertVisual 
- http://j.mp/selectVisual
- http://j.mp/mergeVisual 


Different 
- SelectionSort 
    - TBD 
    - TBD 
- InsertionSort 
    - TBD 
   
- MergeSort 
    - List functions
	    - Looping through a list  - write code to iterate through the elements in a list
		    - Using indexing 
		    - Without using indexing 
		    - Using a `while` statement 
        -  pop() - what does it do? Does it accept any arguments?
            - does `alist.pop()` have the same effect as `alist.pop(0)`?
            - How to use `pop()` to remove the last element in the list? 
            - How to use `pop()` to remove the first element in the list?
            - Assume `alist` contains 4 elements `['one', 'two', 'three', 'four', 'zero']`. If you execute the following code, what will be the output? 
                       `alist.pop(0)`
                       `alist.pop()` 
                       `alist.pop(0)`
                     `print(alist[-1], alist[0])` 
             - If `ulist` is a non-zero list, what is the difference between `ulist[0]` versus `ulist.pop(0)`? 
            - Contrast between `del`, `pop` and `remove` effect on a list
            - Write a code snippet which operates on a list and prints every element in it. By the time it is done, the list must be empty. 
        - Merging 
	        - In how many ways can you append two lists?
	        -  What does the method `extend` perform for a list? 
      - Slicing 
        - Write the code statement to initialize a variable `middle` with  the index of the middle element of a list containing `n` elements.  
        - How to get the first 3 elements in the list and create another list out of those elements? 
        - How to get the last 3 elements in a list and create another list of of those elements?
        - How to get all the elements to the right of the midpoint of a list and place it in another list? 
        - Write a function `sliceInTwo` which accepts a list as argument. It should returns two lists that contain equal number of elements from the original list.
     - Misc 
         - Provide an example for using the ternary operator in Python
         - What is the most critical thing that is to be specified in a recursive call so that the program does not run forever? 
         - How do you swap two variables in the same statement? 
   
  - Histogram 
	  - Write a sample code snippet which uses list comprehension to create a list of numbers from 1 to 10 
      - Use the built-in **divmod**() function to divide 222 by 7 and unpack the quotient and remainder into a tuple, and print the tuple   
      - Create a list that contains all the keys in a dictionary. What is the code?
      - Create a list that contains all the values in a dictionary. What is the code?
      - Create a list of tuples from a dictionary that contains all the key:value pairs. 
          - Sort the tuples in the list based on its value in descending order
          - Write code for both the above. 
        
   
# SelectionSort 

http://j.mp/selectVisual 

## Algorithm

## Source code

```python
def selectsort(a):
  n = len(a) 
  for i in range(n):
    smallest = min(a[i:])
    index_of_smallest=a.index(smallest)
    a[i],a[index_of_smallest]=a[index_of_smallest],a[i]

  return a
```

# InsertionSort 

- http://j.mp/insertVisual 
- http://j.mp/interactInsert using `[10, 3, 2, 4, 0, 30, 1, 5, 15]`

## Algorithm

## Source code

```python
n=int(input("Enter the size of the list:"))
print("Enter the numbers:")
a=[int(input())for i in range(n)]
print("The list elements are: ",a)
for i in range(n):
    smallest= i 
    for j in range(i+1, len(a)): 
        if a[smallest] > a[j]: 
            smallest = j 
    a[i],a[smallest]=a[smallest],a[i]
print("The sorted list is:",a)
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
	- If size of list is 0 or 1, return (*since it is already sorted*)

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


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4ODA0NDQyMTcsLTE0ODU5ODEyMDUsMj
czMzk1OTQ3LC0xODk5NDY5MjYwLDE1ODkwNzY5MjQsODE1NjEy
MjQ1LC0zNDE3NjIxNDVdfQ==
-->