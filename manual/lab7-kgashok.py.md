
# Lab 7: Removing  all the duplicate elements in a list

[TOC]

## Problem statement 

Write a python program that removes all the duplicate elements in a list. 

	Sample Input0: [1, 2, 3, 4]
	Sample Output0: [1, 2, 3, 4]

	Sample Input1: [1, 2, 3, 4, 4]
	Sample Output1: [1, 2, 3]

	Sample Input2: [5, 5, 5, 5]
	Sample Output2: []

	Sample Input3: [11, 22, 33, 44, 22]
	Sample Output3: [11, 33, 44]


## Solution Key

```python 

#!/usr/bin/python
# -*- coding: utf-8 -*-


def remove_duplicates(mlist):
    return mlist


def get_list_of_elements():
    """returns a list containing elements entered by user
....The sequence of steps in the algorithm is:
....#1 - initialize the list
....#2 - Start loop for maximum of 10 entries
........#3 - Get input from user. If null, break
........#4 - Append the element to the list
....#5 - Return the list containing elements
...."""

    ilist = []  # 1
    for x in range(0, 10):  # 2
        element = input('Enter element ' + str(x) + ': ')
        if element:
            ilist.append(element)  # 4
        else:
            break  # 3
    return ilist  # 5


# Program starts here

elist = get_list_of_elements()
print ('List of elements: ', elist)
nlist = remove_duplicates(elist)
print ('The list after removing duplicates ', nlist)


```


## CloudCoder Exercise 

TBD 

## Pre-Lab Questions 

0. What is the method available to remove an element from a list? 
1. How will you get a list of all the keys that are present in a dictionary? 
2. How will get a list of all the values that are present in a dictionary? 


## Post-Lab Questions 

0. You are asked to remove all the duplicate occurrences of only one specific element in the list. Write a function for this. 

## Bonus 1 

## Bonus 2 

## Bonus 3

## Interview Grade 

1. There is probably a one-line Pythonic solution for almost every complicated problem out there. That is also the case for this lab exercise. Can you figure it out? 
