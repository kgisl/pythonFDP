
# Lab 2:  Find the square root of a number (Newton’s method)

[TOC]

## Problem statement 

Implement a python program that determines the square root of a number using the Newton's method. 

	Sample Input1: 25
	Sample Output1: 5
	
	Sample Input2: 9
	Sample Output2: 3
	
	Sample Input3: 20
	Sample Output3: 4.47213595


## Solution Key

```python 

#!/usr/bin/python
# -*- coding: utf-8 -*-


def square_root(number):
    """returns the maximum number in the list
....The sequence of steps in the algorithm is:
....#1 - initialize the maximum value
....#2 - Loop through the entries in the list
........#3 - If maxval is not set, update with number
........#3 - If maxval is less than number, update
....#4 - Return the max value
...."""

	return number 


# Program starts here
number = input ("Input number: ") 
sqroot_number = square_root(number)
print ('The square root of ', number, 'is ', sqroot_number)


```


## CloudCoder Exercise 

TBD 


## Pre-Lab Questions 

0. What is the square root of 4? of 9? of 20?  (Use your calculator if you have to)
1. Manually work out the square root of 20 using the Newton method and show your workings. 


## Post-Lab Questions 
1. Both the functions `get_maxnumber` and `get_list_of_numbers` are not **fruitful** functions. True or False? 
1. How will you find the minimum of the values in a list of numbers? What change will you make to the code? 
2. If the list is empty, what will be the value returned from the function? 
3. If the list happens to be empty, then `get_maxnumber` function must return the string `"N.A.".`. What changes will you make to the code? 
		
		Sample Input: []     
		Sample Output: "N.A." 

3. For Point 2, refactor the code that you have written using a ternary operator. 


## Bonus 1 
4. Suppose the user wanted the freedom not to be restricted to a maximum of 10 numbers, what change would you do to the code? 

## Bonus 2 
1. How will you rewrite the function `get_maxnumber()` using the in-built function `max` (https://docs.python.org/3/library/functions.html?highlight=max#max)? 
2. Can you reduce the function to a one-liner? 
3. Under what conditions will the one-liner function fail? 

## Bonus 3

1. How will you find out the 2nd largest number in the list of numbers? Take into consideration that the list may contain duplicate numbers as well. 


## Interview Grade 
If `n` is the size of the list, and `1 < k < n`, how will you find the `k`th largest number in the list of numbers? (a **#GTG** challenge, a Google interview question).

