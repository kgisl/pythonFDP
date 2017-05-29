
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

    # Newton-Raphson for square root
    # Find x such that x**2 - 24 is within epsilon of 0

    epsilon = 0.01
    k       = number
    guess   = k / 2.0
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (guess ** 2 - k) / (2 * guess)
    print ('Square root of', k, 'is about', guess)
    return guess


# Program starts here

user_number = int(input('Input number: '))
sqroot_number = square_root(user_number)
print ('The square root of ', user_number, 'is ', sqroot_number)


```


## CloudCoder Exercise 

TBD 


## Pre-Lab Questions 

0. What is the `square root` of 4? of 9? of 20?  (Use your calculator if you have to)
1. Manually work out the `square root` of 20 using the Newton method and show your workings. 


## Post-Lab Questions 


## Bonus 1 

## Bonus 2 

## Bonus 3


## Interview Grade 

Add some code to the implementation of Newton-Raphson that keeps track of the number of iterations used to find the root. Use that code as part of a program that compares the efficiency of Newton-Raphson and bisection search. Please report which is more efficient. And by how much. 


## The Newton Method 

The most commonly used approximation algorithm is usually attributed to Isaac Newton. It is typically called Newton’s method, but is sometimes referred to as the Newton-Raphson method.15 It can be used to find the real roots of many functions, but we shall look at it only in the context of finding the real roots of a polynomial with one variable. The generalization to polynomials with multiple variables is straightforward both mathematically and algorithmically.

A polynomial with one variable (by convention, we will write the variable as x) is
either zero or the sum of a finite number of nonzero terms, e.g., `3x2 + 2x + 3`.

Each term, e.g., `3x2`, consists of a constant (the coefficient of the term, 3 in this case) multiplied by the variable (x in this case) raised to a nonnegative integer exponent (2 in this case). The exponent on a variable in a term is called the degree of that term. The degree of a polynomial is the largest degree of any single term. Some examples are, 3 (degree 0), 2.5x + 12 (degree 1), and 3x2 (degree 2). In contrast, 2/x and x0.5 are not polynomials. If `p` is a polynomial and `r` a real number, we will write `p(r)` to stand for the value of the polynomial when x = r. A root of the polynomial p is a solution to the equation p = 0, i.e., an r such that p(r) = 0. So, for example, the problem of finding an approximation to the square root of 24 can be formulated as finding an x such that x2 – 24 ≈ 0. Newton proved a theorem that implies that if a value, call it guess, is an approximation to a root of a polynomial, then `guess – p(guess)/p’(guess)`, where `p’` is the first derivative of `p`, is a better approximation.

For any constant k and any coefficient c, the first derivative of `cx2 + k` is `2cx`. For example, the first derivative of `x2 – k` is `2x`. Therefore, we know that we can improve on the current guess, call it `y`, by choosing as our next guess `y - (y2 - k)/2y`. This is called **successive approximation.** 

