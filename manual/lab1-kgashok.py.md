
# **** NOT EVEN Draft 1.0 ******

# Lab 1: Compute the gcd of two numbers. 

[TOC]

## Problem statement 

Write a Python program to compute the greatest common divisor (***gcd***) of two positive integers.

	Sample Input1: 0, 17
	Sample Output1: 17
	
	Sample Input2: 3, 10
	Sample Output2: 1
	
	Sample Input3: 44, 33
	Sample Output3: 11


## Solution Key

```python 


#!/usr/bin/python
# -*- coding: utf-8 -*-


def gcd(number1, number2):

    if number2 > number1:
        (number1, number2) = (number2, number1)

    if number1 % number2 == 0:
        return number2
    else:
        return 1

    return number1


def getTwoNumbers():
    global a, b
    a = int(input('Enter number: '))
    b = int(input('Enter number: '))


# Program starts here

a = None
b = None
getTwoNumbers()
gcdVal = gcd(a, b)
print ('The gcd is ', gcdVal)


```


## CloudCoder Exercise 

http://cloudcoder.kgkite.ac.in/cloudcoder/#exercise?c=80,p=6941


## Viva Questions 

0. What is the practical use of finding out the gcd of two numbers? 
1. What is the Euclid Algorithm for finding out the gcd of two numbers?
2. If you have written the recursive solution, then write the iterative solution, and vice versa. 
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
