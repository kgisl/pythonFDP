
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

def removeDuplicates (mlist): 
	return mlist 

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
print ('List of elements: ', userList)
rList = removeDuplicates(userList)
print ('The list after removing duplicates ', rList)


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
