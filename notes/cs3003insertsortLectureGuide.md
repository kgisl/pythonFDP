
# Insertion Sort 
_Lecture outline_

# Context setting 
Unit 4 -> Lists, Tuples and Dictionaries -> Illustrative Programs
  - It is very important to use a data type in a real-world case, to understand its true value and benefit. 
  - We are covering three types of sorts 
	 - **Comparison** Algorithms - Insertion Sort and Selection Sort 
	 - **Divide and Conquer** Algorithms - Merge Sort, Quick Sort
  

# Agenda 
- Over the next 20 minutes, we shall see how lists can be used to implement **InsertionSort**

- **SHOW and TELL**  - Show Example, And Tell Theory 
	- versus Tell Theory, Show Example 
	- a more effective style to create engagement 
		- VERY VERY effective when you students participate
		- Even more effective when students KNOW something already

# Pre-req quiz 
	- Are you ready?
		- Do you know something already 
		- Known to Unknown

![index](http://j.mp/indexList)

 - What is the code to iterate over all the elements in a list?
 - What is the code to iterate over all the elements in a list, starting from the 2nd element in the list? 
 - If `al= [11, 12, 13, 14, 15]`, and `al[2] = 15` are executed, what will be `al` contain? 
 - If you have more time, http://j.mp/insertTDD
 - Finish the http://bit.ly/insortCC

Show of hands as to many of you students reviewed all the above questions and have answers written down in your notebooks? 
	- best practice of a engineering student is to come prepared for the class. You must spend at least 2 hours reviewing the material taught in class, and preparing for the class 

## Use a Pack of Cards
http://j.mp/compareSort - the first 35 seconds of the video 

## Interactive Coding

## Stage 1
  - Manual sorting, like you were to sort a list of cards
	  - use a custom built `insort` function

---

## Stage 2
4. Define an iteration through the list, and do this for every element in the list 
5. Initialize the right variables and execute the code
6. Place the entire code inside inside a function definition and call it `insertionsort` 

![insert](http://bit.ly/insertionSortPNG)

## Insertion Sort Description 

-  In `insertionsort`, given a **key**, a copy of a pre-determined element in the list, we  **insert** it at the appropriate location after comparing it with the unsorted elements of the list. We do this repeatedly for all the elements in the list.


![insert1](http://j.mp/insert1PNG)
![insert2](http://j.mp/insert2PNG)
![insert3](http://j.mp/insert3PNG)



## Pseudo Code 

Have seen the example, it becomes very easy to define the pseudo code for InsertionSort 

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
   
	
## Source Code
The Python code to implement the pseudo code above:


```python
def insertionsort(alist): 
    '''insertionsort algorithm implemented 
    using insort function 
    ''' 
    for i in range(1, len(alist)): 
        key = alist[i]
        insort(alist, key, i)
        print("inter", alist)
    return alist

def insort(alist, key, j): 
    '''insort inserts 'key' into the 
    sorted alist[:j] so that it remains sorted 
    'j' is the current index of 'key' in alist 
    ''' 
    while j > 0 and alist[j-1] > key: 
        alist[j] = alist[j-1] 
        j -= 1 
    alist[j] = key
```

The following code can be used to test the above code:
```python
# Test case using random shuffle
from random import shuffle 
alist = list(range(11, 19))
shuffle(alist)
print("Unsorted", alist)
print("Sorted", insertionsort(alist))
```

## Summary
1. We incrementally developed InsertionSort in a "manual mode" 
2. We arrived at the pseudo code 
3. We wrote the equivalent code for InsertionSort 


## Last 2 Minute 

 - respond to Questions from Students 
	 - review the relevant Question Paper snippets
	 - Ask 1 or more students questions from Pre-requisites
  
 - Practice insertionsort at http://j.mp/insertionSortCC   
 - Review http://j.mp/selectVisual for the next class 

## Program File for Demo

Modify this file as you deem fit to demonstrate on PythonAnywhere.com or on the mu editor
  - http://j.mp/insertPAW
  - This is the script I use in my sample video http://bit.ly/insertVideo


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMDkwOTU3OTAsMjMzNzY0MzU3LDQ2OT
Q1NjU1OSwtMzEwNjMyNzQ5LDEzNTA4NjIyMTksLTU0MzY4NTg3
MSwxOTEzOTUwNywtMTMyMzI4Njg2N119
-->