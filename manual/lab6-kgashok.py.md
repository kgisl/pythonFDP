
# Lab 6: find the maximum of a list of numbers. 

[TOC]

## Problem statement 

Implement a python program that finds the maximum in a list of numbers. The program must call a python function `getMaxNumber` that takes as argument a list of numbers (maximum of 10 integers). It must then return the maximum number in that list. 

	Sample Input1: [5]
	Sample Output1: 5
	
	Sample Input2: [1,2]
	Sample Output2: 2
	
	Sample Input3: [1,2,3,4]
	Sample Output3: 4


## Solution Key

```python 

#!/usr/bin/python
# -*- coding: utf-8 -*-


def getMaxNumber(numbers):
    """returns the maximum number in the list
....The sequence of steps in the algorithm is:
....#1 - initialize the maximum value
....#2 - Loop through the entries in the list
........#3 - If maxval is not set, update with number
........#3 - If maxval is less than number, update
....#4 - Return the max value
...."""

    maxval = None  # 1
    for num in numbers:  # 2
        if not maxval or maxval < num:  # 3
            maxval = num
    return maxval  # 4


def getListOfNumbers():
    """returns a list containing elements entered by user
....The sequence of steps in the algorithm is:
....#1 - initialize the list
....#2 - Start loop for maximum of 10 entries
........#3 - Get input from user. If not an number, break
........#4 - Append the number to the list
....#5 - Return the list containing numbers
...."""

    ilist = []  # 1
    for x in range(0, 10):  # 2
        try:  # 3
            userVal = input('Enter number ' + str(x) + ': ')
            ilist.append(int(userVal))  # 4
        except ValueError:
            break  # if user enters a non-integer

    return ilist  # 5


# Program starts here
userList = getListOfNumbers()
print ('List of numbers: ', userList)
maxNum = getMaxNumber(userList)
print ('The largest number is ', maxNum)

# Functional programming style
print ('The largest number is ', getMaxNumber(getListOfNumbers()))

```


## CloudCoder Exercise 

http://cloudcoder.kgisl.com/cloudcoder/#exercise?c=1,p=81 


## Viva Questions 

0. Both the functions `getMaxNumber` and `getListOfNumbers` are not **fruitful** functions. True or False? 
1. How will you find the minimum of the values in a list of numbers? What change will you make to the code? 
2. If the list is empty, what will be the value returned from the function? 
3. If the list happens to be empty, then `getMaxNumber` function must return the string `"N.A.".`. What changes will you make to the code? 
		
		Sample Input: []     
		Sample Output: "N.A." 

3. For Point 2, refactor the code that you have written using a ternary operator. 


## Bonus 1 
4. Suppose the user wanted the freedom not to be restricted to a maximum of 10 numbers, what change would you do to the code? 

## Bonus 2 
1. How will you rewrite the function `getMaxNumber()` using the in-built function `max` (https://docs.python.org/3/library/functions.html?highlight=max#max)? 
2. Can you reduce the function to a one-liner? 
3. Under what conditions will the one-liner function fail? 

## Bonus 3

1. How will you find out the 2nd largest number in the list of numbers? Take into consideration that the list may contain duplicate numbers as well. 


## Interview Grade 
If `n` is the size of the list, and `1 < k < n`, how will you find the `k`th largest number in the list of numbers? (a **#GTG** challenge, a Google interview question).
