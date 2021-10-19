**Table of Contents**

- [Lab 1: Compute the gcd of two numbers](#lab-1-compute-the-gcd-of-two-numbers)
  - [Problem statement](#problem-statement)
  - [Solution Key](#solution-key)
  - [CloudCoder Exercise](#cloudcoder-exercise)
  - [Related material](#related-material)
  - [Pre-Lab Questions](#pre-lab-questions)
  - [Post-lab Questions](#post-lab-questions)
  - [Bonus 1](#bonus-1)
  - [Related Material](#related-material)
    - [PPT Slides showing the Recursive Calls](#ppt-slides-showing-the-recursive-calls)
    - [Recursion vs Iteration](#recursion-vs-iteration)
    - [Related Problems](#related-problems)

# Lab 1: Compute the gcd of two numbers

[TOC]

## Problem statement

Write a Python program to compute the greatest common divisor (**_gcd_**) of two positive integers.

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
    while True:
	    if number2 != 0:
	        (number1, number2) = (number2, number1 % number2)
	    else:
		    break
    return number1


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

0. Show your manual workings for the **_gcd_** of 924 and 2562.
1. What is the practical use of calculating the **_`gcd`_** of two numbers?
2. If you have written the recursive solution of the Euclid algorithm, then write the iterative solution, and vice versa.
3. How does the algorithm for the `gcd` of two numbers work? What is the name for this algorithm? Why is it so special?
4. Why is the `global` keyword used in the function `get_twonumbers`?
5. Is the function `get_twonumbers()` fruitful or not fruitful?
6. Define a function `is_valid_year` with parameter `year`. The function must return `True` if the value of `year` is between 1900 and 3000 (_inclusive_). Otherwise, it must return `False`.

## Post-lab Questions

0. What if `a` or/and `b` are negative integers? How will you modify the program to handle this? Clue: Use the `abs()` function.

## Bonus 1

0. How will find the `gcd` of three integers?
1. How do you calculate the number of days in a month?

## Related Material

### PPT Slides showing the Recursive Calls

http://j.mp/gcdDemo

### Recursion vs Iteration

![recursionImage](http://i.imgur.com/vXBg7rb.png)

```python
def gcd_r(a, b):
	if b == 0:
		return a
	return gcd_r(b, a % b)
```

### Related Problems

##### Days per month

```python
def is_valid(mnum):
    return 1 <= mnum <= 12


def is_multiple(n, d):
    return n % d == 0


def is_leap(year):
    """
    Whether a year is a leap year?
    The rules are as follows:
      - multiple of 4 and not of 100 or
      - multiple of 400
    """

    return (is_multiple(year, 4)
            and not is_multiple(year, 100)
            or is_multiple(year, 400))


# Number of days per month (except for February in leap years)
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def monthdays(year, month):
    if not is_valid(month):
        return -1

    ndays = mdays[month] + (month == 2 and is_leap(year))
    return ndays

```
