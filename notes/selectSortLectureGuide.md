

# SelectSort 

# Context setting 
Unit 4 -> Lists, Tuples and Dictionaries -> Illustrative Programs
  - It is very important to use a data type in a real-world case, to understand its true value and benefit. 
  - We are covering three types of sorts 
	 - **Comparison** Algorithms - Insertion Sort and Selection Sort 
	 - **Divide and Conquer** Algorithms - Merge Sort, Quick Sort
  
 - We have already seen the power of Lists when we covered  **InsertionSort** 
	 - Select a `value` from the unsorted sub-list
	 - Decide where to **insert** it in the already_sorted sub-list
	 - Right shift all the values and then insert the `value`

# Agenda 
- Over the next 20 minutes, we shall see how lists can be used to implement **SelectionSort**

- **SHOW and TELL**  - Show Example, And Tell Theory 
	- versus Tell Theory, Show Example 
	- a more effective style to create engagement 
		- VERY VERY effective when you students participate
		- Even more effective when students KNOW something already

# Pre-req quiz 
	- Are you ready?
		- Do you know something already 
		- Known to Unknown

  - how do you iterate over all the elements in a list, except the last one? Write the python code to do this 
  - What is the value of `[1, 2, 3, 4][0:]` and `[1, 2, 3, 4][1:]` and `[1, 2, 3, 4][2:]`?
  - What is the built-in function which is used to find the minimum value of a list of numbers? Create a list containing 10 random numbers. Write the python code to find the minimum value in the list.
  - What is the list method to find out the index of a value in a list? 
	  - How many arguments does the method accept? 
	  - What is the second argument for? 
  - What are the ways you can swap the value in two variables? 
	  - What is the most pythonic way to do this? 
		  - Word count - Python beats Java, like crazy! 

Show of hands as to many of you students reviewed all the above questions and have answers written down in your notebooks? 
	- best practice of a engineering student is to come prepared for the class. You must spend at least 2 hours reviewing the material taught in class, and preparing for the class 

## Interactive Coding

## Stage - 1
1. Example of list containing `[1, 2, 3, 5, 6, 4]` 
	2. Already sorted list, except the number 4 

2. **Select** the minimum value in all of the unsorted list 
	3. `1` is the minimum - place it in index `0` 
	4. `2` is the minimum - place it in index `1` 
	5. `3` is the minimum - place it in index `2` 
	6. `4` is the minimum - prepare to swap with 5 
		7. `[1, 2, 3, 4, 6, 5]` 
	7. `5` is the minimum - prepare to swap with 6 
		8. `[1, 2, 3, 4, 5, 6]`

3. If necessary (`i != min_i`) swap the minimum value from the unsorted sublist with the element in the sorted sub-list

---

## Stage 2
4. Define an iteration through the list, and do this for every element in the list 
5. Initialize the right variables and execute the code
6. Place the entire code inside inside a function definition and call it `selectionsort` 

![select](http://bit.ly/select2PNG)

## Selection Sort Description 

-   In  `selectsort`, the position of the update is pre-determined, starting from the beginning of the list. We then go  **select**  the maximum value among the unsorted elements of the list, and swap it with the element in the pre-determined location.

## Pseudo Code 

Have seen the example, it becomes very easy to define the pseudo code for SelectionSort 

	repeat (numOfElements - 1) times 
		for each of the unsorted elements 
		select the minimum value among them
		swap minimum with first unsorted position
	
The Python code to implement the pseudo code above:

```python 
  def  selectsort(alist): 
    n =  len(alist)
	for i in  range(n-1):
	  unsorted = alist[i:] 
	  smallest =  min(unsorted) 
	  min_i = alist.index(smallest, i)
	  alist[i],alist[min_i]  = alist[min_i], alist[i]  
	  print("intermediary", alist)  return alist
```

## Part 1.5 

Can you improve on the above logic? How can you do it? Please discuss with your immediate neighbour. 
	- if you know how to code it, write down the code in Python as well 
	- Go back and improve the pseudo code as well 







## Part 2 
   - OPTIONAL - generate a list containing tuples, where each tuple contains both the element and the index of the element in the list 
   - OPTIONAL - use a built-in function to find out the tuple containing the least value in the list

## A more efficient Selection Sort 

-   uses  `tuples`  and  `list comprehension`  to make the code very efficient and eminently readable.

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


## Summary
1. We reviewed SelectionSort in a "manual mode" 
2. We arrived at the pseudo code 
3. We wrote the equivalent code for SelectionSort 

In reflection, **SelectionSort** is just the opposite of **InsertionSort**. The worst case complexity of this SelectionSort is `O(n^2)`

## Last 2 Minute 

 - respond to Questions from Students 
	 - review the relevant Question Paper snippets
	 - Ask 1 or more students questions from Pre-requisites
  
  - Ask them to review http://j.mp/mergeVisual for the coming class 



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY1NDU1Mzg5MiwtMTUxMDIzMzM3MSwxMD
k2NTQ1MzQ0XX0=
-->