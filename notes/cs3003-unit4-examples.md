# Illustrative programs of Tuples, Lists and Dictionaries

## Pre-requisites

- http://j.mp/insertVisual   
- http://j.mp/selectVisual  
- http://j.mp/mergeVisual    
- http://bit.ly/histogramVisual    
- [https://www.toptal.com/developers/sorting-algorithms](https://www.toptal.com/developers/sorting-algorithms)

## Recommended sequence
  - InsertSort -> SelectionSort -> MergeSort -> Histogram
   
# InsertionSort 

## Pre-requisites
- http://j.mp/insertVisual 
- http://j.mp/interactInsert using `[10, 3, 2, 4, 0, 30, 1, 5, 15]`
 -  `pop()` - what does it do? Does it accept any arguments? What does `push()` do? Does it accept an argument as well?
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
  - `insert()` - what does this do? How many arguments does it accept? 
	  - write the equivalent of `append()` function using `insert()` 
	  - When `pop` method exists, why is there no `push` method? Define a suitable list operation `push`that would be perform the role of a list `push` method if it were to exist. 

What will the following snippets do? 
```python
alist = list(range(10))
for i in range(len(alist)):
	val = alist.pop()
	print(val, end=" ")
```

```python
alist = list(range(10))
for i in range(len(alist)):
	val = alist.pop(0)
	print(val, end =" ")
```

```python
alist = list(range(10))
for i in range(len(alist)):
	val = alist.pop(i)
	print(val, end = " ")

```


## Algorithm

- In `insertsort`, given a key, a copy of a pre-determined element in the list, we  **insert** it at the appropriate location after comparing it with the unsorted elements of the list.

		mark first element as sorted
		for each unsorted element X
			'extract' the element X as 'key'
			insert key at the relevant index so list remains sorted
		return sorted list 

More detailed pseudo-code: 

	mark first element as sorted
	for each unsorted element X
	  extract the element X
	  for j = lastSortedIndex (position -1) down to 0
	    if current element j > X
	      decrement j by 1 
	    else break loop and insert X here
    return sorted list
   
	   
## Source code 

```python
def insertsort(alist):
    n = len(alist)
    # STEP 0 - iterate through the list
    for idx in range(1, n):
        # STEP 1 - element to insert 
        # j, value = idx, alist.pop(idx)
        j, value = idx, alist[idx]

        # STEP 2 - decide where to insert 
        sorted_already = alist[:idx]
        while j > 0 and value < sorted_already[j-1]:
            j -= 1
        # STEP 3 - insert it in the relevant index
        # alist.insert(j, value)
        if j != idx: 
            alist[j+1:idx+1] = alist[j:idx]
            alist[j] = value
            print('intermediary:', alist)
        return alist
```

The following code can be used to test the above code:
```python
# Test case using random shuffle
from random import shuffle 
alist = list(range(10))
shuffle(alist)

print("Unsorted", alist)
print("Sorted", insertsort(alist))
```

![insert1](http://j.mp/insert1PNG)
![insert2](http://j.mp/insert2PNG)
![insert3](http://j.mp/insert3PNG)

Practice insertionsort at http://j.mp/insertionSortCC 
 - The million insert challenge http://j.mp/millionInsert 


# SelectionSort 

## Pre-requisites
 - http://j.mp/selectVisual 
 - http://j.mp/interactSelect using `[10, 3, 2, 4, 0, 30, 1, 5, 15]`
  - Which built-in function helps find the minimum element in a list? 
	  - What happens when the built-in function is provided with a null list?
	  - If you cannot use `min`, write the code for finding the minimum value in a list
   - What is the method of a list that returns the index for an element in the list? 
	   - What is the difference between `find` and `index`? 
 - how do you iterate over all the elements in a list, except the last one? Write the python code to do this 
  - What is the value of `[1, 2, 3, 4][0:]` and `[1, 2, 3, 4][1:]` and `[1, 2, 3, 4][2:]`?
  - What is the built-in function which is used to find the minimum value of a list of numbers? Create a list containing 10 random numbers. Write the python code to find the minimum value in the list.
  - What is the list method to find out the index of a value in a list? 
	  - How many arguments does the method accept? 
	  - What is the second argument for? 
  - What are the ways you can swap the value in two variables? 
	  - What is the most pythonic way to do this? 
  - Find the minimum value in a list and the index of the minimum value. Write a list comprehension as part of the code that returns both values in a tuple. 
   - Write code for swapping two variables without using a temporary variable. If it is not a one line statement, try refactoring whatever you have into one single statement. 


## In-class Demo
- [http://j.mp/compareSort](http://j.mp/compareSort)

## Algorithm

- In `selectsort`, the position of the update is pre-determined, starting from the beginning of the list. We then go **select** the maximum value among the unsorted elements of the list, and swap it with the element in the pre-determined location.

Here's an example: 
![select](http://bit.ly/select2PNG)

		repeat (numOfElements - 1) times
			for each of the unsorted elements
			select the minimum value among them
			swap minimum with first unsorted position

## Source code

### Version 1
```python
def selectionsort(alist):
    n = len(alist)
    # STEP 0 - iterate through the list
    for i in range(n-1):
        min_i = i 
        # STEP 1 - update mini_i with index 
        # of min value in unsorted alist[i+1:]
        for j in range(i+1, n): 
            if alist[j] < alist[min_i]: 
                min_i = j
        # STEP 2 - swap it with element at index 'i'
        if min_i != i:
            alist[i], alist[min_i] = alist[min_i], alist[i]
    return alist
```

### Version 2 
```python
def selectsort(alist):
    n = len(alist) 
    # STEP 0 - iterate through the list
    for i in range(n-1):
        # STEP 1 - find the index of the minimum
        unsorted = alist[i:]
        smallest = min(unsorted)
        min_i = alist.index(smallest, i)
        # STEP 2 - swap if required 
        if min_i != i:
            alist[i],alist[min_i] = alist[min_i], alist[i]
            print("intermediary", alist)
    return alist

```

### Version 3
 - uses  `slicing`,  `tuples` and `list comprehension` to make the code very efficient and eminently readable.  

```python
def selectsort(alist):
    n = len(alist)
    for i in range(n-1):
        unsorted = alist[i:]
        (minval, min_idx) = min((v, i) \
            for i, v in enumerate(unsorted))
        alist[i], alist[min_idx+i] = alist[min_idx+i], alist[i]
        print("intermediary", alist)
    return alist

tlist = [85, 69, 12, 12, 54, 36, 45, 5]
print("unsorted", tlist)
print("sorted:", selectsort(tlist))
```

### Bonus 
Can you improve on the **basic selection sort**? How about grabbing the maximum value during every iteration and using it? 

Practice selection sort at http://j.mp/selectionSortCC 


# MergeSort

## tl;dr![tldr](http://bit.ly/tamilMerge)
The key thing is to slice into almost two equal halves. That's the **crux**!

## Pre-requisites

   - List functions
     - Looping through a list  - write code to iterate through the elements in a list
	    - Using indexing 
	    - Without using indexing 
	    - Using a `while` statement 
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
    - Ultimate challenge 
      - http://j.mp/sortApply 

 
## In-class demo
[MergeSort Color](http://j.mp/mergeVisual)


## Visualization
Notice that at each level we divide the array into two halves until we get bunch of single element arrays. This is the divide  portion of the divide and conquer  method. Then, we start merging and sorting the smaller arrays in a series of steps which is the conquer  portion of divide and conquer.

![mergeGIF](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)

## Merge example 

0. Use a 4-element array to explain mergesort - why should it be 8 and so confusing upfront? 
1.  With reference to below diagram, how many lists are there in Row 4? 
2. Until what row is **Divide** happening? 
3. From which row onwards **Conquer** has begun? 

![mergeExample](http://bit.ly/mergeExample2)


- InsertSort and SelectionSort are examples of **comparison** sorts
- However, MergeSort, is an example of the **Divide-and-Conquer** algorithm sorts

  - **Divide** means portioning the n-element array to be sorted into two sub-arrays of n/2 elements. If A is an array containing zero or one element, then it is already sorted. However, if there are more elements in the array, divide A into two sub-arrays, A1 and A2, each containing about half of the elements of A. 
  - **Conquer** means sorting the two sub-arrays recursively using merge sort. Combine means merging the two sorted sub-arrays of size n/2 to produce the sorted array of n elements.


## Algorithm

Means what it sounds like. A divide and conquer algorithm breaks up a problem into smaller sub-problems and solves those, putting the solutions to the sub-problems together to come up with the solution to the total problem.

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
assert (merge([1, 2, 3], [4, 5, 10]) == \
	[1, 2, 3, 4, 5, 10])
alist = [6, 2, 1, 5, 8, 7, 4, 3]
print(mergesort(alist))
# [1, 2, 3, 4, 5, 6, 7, 8]
```


# Histogram 

![histo](http://j.mp/histoPNG)

- http://bit.ly/histogramVisual

## Pre-requisites

  - Histogram 
	  - Write a sample code snippet which uses list comprehension to create a list of numbers from 1 to 10 
      - Use the built-in **divmod**() function to divide 222 by 7 and unpack the quotient and remainder into a tuple, and print the tuple   
      - Create a list that contains all the keys in a dictionary. What is the code?
      - Create a list that contains all the values in a dictionary. What is the code?
      - Create a list of tuples from a dictionary that contains all the key:value pairs. 
          - Sort the tuples in the list based on its value in descending order
          - Write code for both the above. 
     - Can a string be a key in a dictionary? Can a list like `[1, 2, 3]` be a key in a dictionary? Why not? 
     - Can an integer be a key in the dictionary? Can a tuple like `(5, 10)` be a key in a dictionary? Why not? 
   
      - Create a histogram with tuples that represent bins (interval specified by low and high values) of sufficient width and see the typical double peaks that occur in random data  

## Algorithm 

- We build a histogram using a dictionary where the keys of the dictionary will be the letters in the string and the associated values for each key will be the number of times that the letter appeared.

- What about a letter that does not appear in the string? It will never be placed in the dictionary. By assumption, any key that is not in the dictionary has a count of 0.

1.  Define the function to require one parameter, the string.
2.  Create an empty dictionary of counts.
3.  Iterate through the characters of the string, one character at a time.

## Source Code 

## Version 1 

```python
################################
# Program No 1
# using dictionary to build the histogram
#   - using a randomizer for input
#   - functionally decomposing the logic 
#
#################################
# Build a histogram

import random
# build a random list 
# returns a list containing numbers 1 <= n <= maxval
# the list will contain n elements where
#   mincount < n < maxcount 
def random_list(mincount, maxcount, maxval, minval=1): 
  size = random.randint(mincount, maxcount)
  alist = []
  for _ in range(size):
    alist.append(random.randrange(minval, maxval+1))		
  return alist

arlist = random_list(50, 120, 20, -10)
print("A random list", arlist)


# returns a list containing tuples with 
# value and frequency, aka a histogram
from collections import defaultdict
def generate_histogram(arlist):
  counters = defaultdict(int) #inits value to 0
  for number in arlist:
	  counters[number] += 1

  histogram = sorted(counters.items())
  return histogram

histo = generate_histogram(arlist)
print("A histogram with", histo)

print("Visualizing the histogram")
for i in range(len(histo)): 
  print (f'{histo[i][0]:2}', '@'*histo[i][1])

```

## Version 2 

A histogram contains bins (lower bound, upper bound), and statistical values are dropped into these bins. Eventually, the histogram is visualized based on the bin counts. This type of histogram is what is used in more statistical analysis. 

```python
################################
# Program No 5
# using tuple as key in a dictionary 
# to build bins of values for 
# visualization 
#
# Refer https://datavizcatalogue.com/methods/histogram.html 
#
#################################
# Build a histogram

import random
# build a random list 
# returns a list containing numbers 1 <= n <= maxval
# the list will contain n elements where
#   mincount < n < maxcount 
def random_list(mincount, maxcount, maxval, minval=1): 
  size = random.randint(mincount, maxcount)
  alist = []
  for _ in range(size):
    alist.append(random.randrange(minval, maxval+1))		
  return alist

maxval, minval = 100, 10
arlist = random_list(40, 200, maxval, minval)
#print("A random list", arlist)

# returns a list containing tuples with 
# value and frequency, aka a histogram
from collections import defaultdict
def generate_histogram(arlist):
  counters = defaultdict(int) #inits value to 0

  bincount = 10
  binwidth = (maxval-minval)/bincount
  #minval = min(arlist)
  #maxval = max(arlist)
  points = [p for p in range(minval, maxval+1, int(binwidth))]
  
  bins = [(start, end-1) if end != maxval else (start, end) \
          for (start, end) in zip(points, points[1:])
  ]
	#bins.append(points[-1])
  
  for number in arlist:
    for start, end in bins: 
      if start <= number <= end: 
        counters[(start, end)] += 1

  return counters 

histo = generate_histogram(arlist)
print("A histogram with", histo.items())

print("Visualizing the histogram")
for bin in histo.items(): 
  print (f'{str(bin[0]):>10}', '@'*bin[1])

# Ordered histogram 
o_histogram = sorted(
	[(v, k) for k, v in histo.items()], reverse=True
)

print("Visualizing the ordered histogram")
for bin in o_histogram:
  print (f'{str(bin[1]):>10}', '@'*bin[0])
```

## Complexity Analysis

This needs to be expanded - or even required? 
	- Rajasekaran to discuss 

http://bit.ly/complexThis

# Epilogue 
_A speech at the end of a play that serves as a comment on or a conclusion to what has happened._

**InsertionSort**, **SelectionSort** and **MergeSort** algorithms were covered in detail, primarily using a **Show-And-Tell** approach which is most intuitive.  Also, the approach is very effective in engaging students of diverse learning capabilities. 

A comparison screenshot of the three sorts in action in "verbose" mode is presented below. The screenshot helps differentiate the three sorting algorithms when they process the same unsorted list as a test case. The ***curious*** student will want to trace how the unsorted list becomes a sorted one in each of the three cases. 

## Verbose Compare
![verbose](http://bit.ly/sortVerbose)

## Python Pseudo Code Compare

  - insertionsort : get a key and **insert** it into *sorted* sublist
  - selectionsort : **select** minimum value and swap into *sorted* sublist 
  - mergesort :  divide and **merge** (_conquer_) of *sorted* sublists

![sortCode](http://bit.ly/sortCompared2)

## Helper functions
Three helper functions (`insort`, `min_index` and `merge`) were written and used in the respective sorting implementation. 

These helper functions are very effective in capturing the core of each of the algorithm. Also, they help in presenting the algorithm in an incremental fashion, reducing the cognitive load on the student. 


```python
def  insort(alist, key, j):  
    '''insort inserts 'key' into the sorted alist[:j]
    so that it remains sorted 
    'j' is the current index of 'key' in alist 
    '''  
    while j > 0 and alist[j-1] > key: 
        alist[j] = alist[j-1] 
        j -= 1 
    alist[j] = key
```
http://j.mp/insortCC 

```python
def min_index(alist, i):
    '''function returns the index of the
    minimum value in the sublist alist[i:] 
    '''
    n = len(alist) 
    min_i = i 
    for j in range(i+1, n): 
        if alist[j] < alist[min_i]: 
            min_i = j
    return min_i
```
- *How can you refactor the above function to have only one line of code?*
- *If `i` is not provided, how will you default it to an appropriate value?* 

http://j.mp/indexMinCC

```python
def  merge(A, B): 
    '''
    merge generates a new sorted list containing
    all elements contained in both sorted lists
    '''
    C =  []
    while A and B:
        smaller = (A if A[0]  < B[0]  else B).pop(0)
        C.append(smaller)  
    # pick up the residual elements in A or B 
    return C + A + B
```
http://j.mp/mergeListCC and http://j.mp/unionListCC

```python
def divideTwo(alist):
    mid = len(alist)//2
    return alist[:mid], alist[mid:]
    
```
http://j.mp/divideTwo - divide a list into two halves


## Other related exercises


- http://j.mp/butFirstCC and http://j.mp/butLastCC - iterate over a list
- http://j.mp/rightShiftCC - right shift exactly by one position
- http://j.mp/swapListCC - swap elements in a list
- http://j.mp/enumListCC  - manually code out the enumerate function 


## GIF galore 

Which one is which? 

## Sort 1
![gifSelect]()
## Sort 2 
![gifInsert]()
## Sort 3 
![gifMerge]()


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM3NDYxMzEyNywtMTgzMDczMDIyMSwtOT
Y5ODMwOTMsLTE5NTU5MDcyMTcsMTA1OTIwNjc0LC0xNjM1MjQ5
NzQsNzI5MzE2MTQ4LC0xMTk1MTIzMDgsLTEzOTMyNjEzNjEsLT
QyOTcxMzU3NiwtMzk5NzE4MTk3LDkyNzkxNzI5NCw5NTU2OTQz
ODEsLTY3MjI5MTAwNywxNzY0NzE3NjU5LDE2NDMxOTczOTgsMT
U4NTQ2NjUyMCwtMjAzMDkyODQ2OSwtMTkzMzcwMzE4LC0xMzg0
MjUwNDgwXX0=
-->