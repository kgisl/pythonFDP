
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


def get_two_numbers():
    global a, b  
    a = input('Enter number: ')
    b = input('Enter number: ')
    a, b =  int (a), int (b)


# Program starts here
a = None  # initializing variables
b = None
get_two_numbers() # to get values from user 
gcdval = gcd(a, b) 
print ('The gcd is ', gcdval)

```


## CloudCoder Exercise 

http://cloudcoder.kgkite.ac.in/cloudcoder/#exercise?c=80,p=6941


## Related material 

- How to find the gcd of two numbers using prime factorization? http://j.mp/gcdPrime  
- Why 1 is the common factor? http://j.mp/gcdOne



## Viva Questions 

0. Show your manual workings for the ***gcd*** of 924 and 2562. 
1. What is the practical use of calculating the ***`gcd`*** of two numbers? 
1. If you have written the recursive solution of the Euclid algorithm, then write the iterative solution, and vice versa. 
2. How does the algorithm for the `gcd` of two numbers work? What is the name for this algorithm? Why is it so special? 
3. Why is the `global` keyword used in the function `getTwoNumbers`? 
4. Is the function `getTwoNumbers()` fruitful or not fruitful? 


## Bonus 1 
4. How will find the `gcd` of three integers? 

