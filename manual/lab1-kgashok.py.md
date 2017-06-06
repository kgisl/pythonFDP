
# Lab 1: Compute the gcd of two numbers 

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
    while b:
        (a, b) = (b, a % b)
    return a


def get_twonumbers():
    global a, b  
    a = input('Enter number: ')
    b = input('Enter number: ')
    a, b =  int (a), int (b)


# Program starts here
a = None  # initializing variables
b = None
get_twonumbers() # to get values from user 
gcdval = gcd(a, b) 
print ('The gcd is ', gcdval)

```


## CloudCoder Exercise 

http://cloudcoder.kgkite.ac.in/cloudcoder/#exercise?c=80,p=6941


## Related material 

- How to find the gcd of two numbers using prime factorization? http://j.mp/gcdPrime  
- Why 1 is the common factor? http://j.mp/gcdOne



## Pre-Lab Questions 

0. Show your manual workings for the ***gcd*** of 924 and 2562. 
1. What is the practical use of calculating the ***`gcd`*** of two numbers? 
2. If you have written the recursive solution of the Euclid algorithm, then write the iterative solution, and vice versa. 
3. How does the algorithm for the `gcd` of two numbers work? What is the name for this algorithm? Why is it so special? 
4. Why is the `global` keyword used in the function `get_twonumbers`? 
5. Is the function `get_twonumbers()` fruitful or not fruitful? 

## Post-lab Questions

0. What if `a` or/and `b` are negative integers? How will you need to modify the logic of the program? 

## Bonus 1 
4. How will find the `gcd` of three integers? 

## Related Material 

### PPT Slides showing the Recursive Calls 
 http://j.mp/gcdDemo 

### Recursion vs Iteration

![recursionImage](http://i.imgur.com/vXBg7rb.png)