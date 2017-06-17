# Merge Sort

## Problem statement
Write a python program to sort the given list using `mergesort` algorithm
```code
Examples:
Input:[5,8,2]
Output:[2,5,8]

Input:[6,2,8,4,3,7,5,1]
Output:[1,2,3,4,5,6,7,8]

Input=[6,-2,8,4,-3,7,-5,1]
Output=[-5,-3,-2,1,4,6,7,8]

Input=[6,-2,"8.8",4.4,-3,7.5,-5,1]
Output="Invalid input"

Input=23
Output="Invalid input"
```
## Pseudo code
```
merge_sort(num)
	return divide(num)

divide(num)
	if num is empty or len(num) is 1:
		return num
	mid = len(num)/2
	left = divide(num[:mid])
	right = divide(num[mid:])
	merge(left,right)


merge(left,right)
	merged_list = [ ]
	while left and right are not empty:
		if left[0] <  right[0]:
			Pop left[0] and add it to merged_list
		else:
			Pop right[0] and add it to merged_list
	Append  remaining left and right to merged_list
```

## Solution key

```python
def mergesort(numbers):
    # check for the empty list or the list with single element
    if not numbers or len(numbers) == 1:
        return numbers
    # recursive splitting (Divide)
    else:
        mid = len(numbers)//2
        left = mergesort(numbers[:mid])
        right = mergesort(numbers[mid:])
        return merge(left, right)


def merge(left, right):
    # left and right are the sorted lists to be merged
    # The merged list after sorting
    merged = []
    # Loop till left or right becomes empty
    while left and right:
        # remove the minimum of left[0] and right[0]
        # and add it to the merged list
        if left[0] < right[0]:
            merged += [left.pop(0)]
        else:
            merged += [right.pop(0)]
    # add the remaining elements of left, if any
    merged += left
    # add the remaining elements of right, if any
    merged += right
    return merged

```


## CloudCoder exercises
[To be updated]


## Related material
Merge sort -  http://bit.ly/KG_mergesort

## Pre-Lab Questions

1. How do you get the number of elements in the list
2. Merge two lists [2,4,3] and [7,5,6]
3. Consider `left` and `right` lists of size 1. Merge them in a sorted order.
```
Example:
left = [12]  right = [3]
merged = [3,12]
```
4. Now consider the two sorted lists of unspecified size. Merge them in a sorted order.
```
Example:
left = [12,45]  right = [3,17]
merged = [3,12,17,45]
```
4b. Merge two sorted lists `[2,6,7]` and `[3,5,8]` in the sorted order

5. Divide the list `num` into `left` and `right` halves.
```
Example:
num = [6,2,8,4,3,7,5,1]
left = [6,2,8,4]  right = [3,7,5,1]
```
6. Recursively divide, till the partition size is 1
```
Example:
num = [12,3,45,17,15]
left = [12,3]
        left = [12]
        right = [3]
right = [17, 15]
        left = [17]
        right = [15]
```
7. What are the first two elements to be merged from the input list [6,2,8,4,3,7,5,1] in the mergesort
8. Validate whether given input is of `list` type.
9. Validate whether all the elements in the input are of `int` type.
10. Validate whether given list is empty

## Post-Lab Questions
1. Modify the program to validate whether given input is a valid list.
2. Modify the code to sort the list of string elements.
```
example:
input=['python','c','c++','java']
expected output=['c','c++','python','java']
```

## Bonus
1. What is the worst case complexity for merge sort algorithm?


## Interview Grade
1. Why quicksort is better than mergesort?
2. Is there a way to implement a hybrid sort (which uses MergeSort and InsertionSort)? What is the algorithm for this?

## CyberDojo session
- CD extrenal Link : http://cyberdojo1.kgfsl.com/kata/edit/B006BC6DA0?avatar=bee  
- CD local Link : http://10.100.8.8/kata/edit/B006BC6DA0?avatar=bee

## Test cases
```python
from mergesort import mergesort
import unittest
import random

class Test_mergesort(unittest.TestCase):

    def test_one_number(self):
        print("test 1")
        expected=[5]
        actual=mergesort([5])
        self.assertEqual(expected,actual)

    def test_two_numbers(self):
        print("test 2")
        expected=[2,5]
        actual=mergesort([5,2])
        self.assertEqual(expected,actual)   

    def test_three_numbers_ordered_right(self):
        print("test 3")
        expected=[2,5,8]
        input=[5,2,8]
        actual=mergesort(input)
        self.assertEqual(expected,actual)       

    def test_three_numbers_unordered(self):
        print("test 4")
        expected=[2,5,8]
        actual=mergesort([5,8,2])
        self.assertEqual(expected,actual) 

    def test_bigger_list(self):
        print("test 5")
        input=[6,2,8,4,3,7,5,1]
        expected=[1,2,3,4,5,6,7,8]
        actual=mergesort(input)
        self.assertEqual(expected,actual)          


    def test_empty(self):
        print("test 6")
        input=[]
        expected=[]
        actual=mergesort(input)
        self.assertEqual(expected,actual)          
    

    def test_negative_numbers(self):
        print("test 7")
        input=[6,-2,8,4,-3,7,-5,1]
        expected=[-5,-3,-2,1,4,6,7,8]
        actual=mergesort(input)
        self.assertEqual(expected,actual)          

    def test_float(self):
        print("test 8")
        input=[6,-2,8.8,4.4,-3,7.5,-5,1]
        expected=[-5,-3,-2,1,4.4,6,7.5,8.8]
        actual=mergesort(input)
        self.assertEqual(expected,actual)          

    def test_non_number(self):
        print("test 9")
        input=[6,-2,"8.8",4.4,-3,7.5,-5,1]
        expected="Invalid input"
        actual=mergesort(input)
        self.assertEqual(expected,actual)          

    def test_non_list(self):
        print("test 10")
        input=23
        expected="Invalid input"
        actual=mergesort(input)
        self.assertEqual(expected,actual) 

    def test_random(self):
        print("Random test input")
        input=[random.uniform(1,10) for _ in range(10)]
        expected=sorted(input)
        actual=mergesort(input)  
        self.assertEqual(expected,actual) 

if __name__ == '__main__':
    unittest.main()
```

## Answer key for validating the input

```python
def mergesort(numbers):
    # Top level function to validate the input once
    if not is_valid(numbers):
        return "Invalid input"
    # Original `mergedsort` function is renamed as `split`    
    return split(numbers) 
    
def is_valid(numbers):
    if(type(numbers) != list):
        return False
    for elem in numbers:
        if not isinstance(elem, int) and not isinstance(elem, float):
            return False
    return True
```
