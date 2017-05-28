
# *** Draft 0.1 ***

# Lab 1: Compute the gcd of two numbers. 

[TOC]

## Problem statement 

Write a Python program to compute the greatest common divisor (***gcd***) of two positive integers.

	Sample Input1: 17, 17
	Sample Output1: 17
	
	Sample Input2: 0, 17
	Sample Output2: 17

	Sample Input3: 12, 17
	Sample Output3: 1 
		
	Sample Input3: 44, 33
	Sample Output3: 11



## Solution Key

```python 


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
    a = input('Enter number: ')
    b = input('Enter number: ')
	a, b =  int (a), int (b)


# Program starts here
a = None  # initializing variables
b = None
getTwoNumbers() # to get values from user 
gcdVal = gcd(a, b) 
print ('The gcd is ', gcdVal)


```


## CloudCoder Exercise 

http://cloudcoder.kgkite.ac.in/cloudcoder/#exercise?c=80,p=6941


## Viva Questions 

0. What is the practical use of calculating the `gcd` of two numbers? 
1. What is the Euclid Algorithm for finding out the `gcd` of two numbers?
2. If you have written the recursive solution, then write the iterative solution, and vice versa. 


## Bonus 1 
4. How will find the `gcd` of three integers? 

