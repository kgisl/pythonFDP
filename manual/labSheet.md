
**Table of Contents**

* [Lab CheatSheet](#lab-cheatsheet)  
	* [Lab 1](#lab-1)  
	* [Lab 2](#lab-2)  
	* [Lab 3](#lab-3)  
	* [Lab 4](#lab-4)  
	* [Lab 5](#lab-5)  
	* [Lab 6](#lab-6)  
	* [Lab 7](#lab-7)  
	* [Lab 8](#lab-8)  
	* [Lab 9](#lab-9)  
		* [Alternative](#alternative)  
	* [Lab 10](#lab-10)  
	* [Lab 11](#lab-11)  
		* [Alternative](#alternative)  
	* [Lab 12](#lab-12)  


# Lab CheatSheet
The minimal code that is expected of the student for each of the lab is collated together in one place, for the benefit of the student, faculty and mentor. Practice problems around the base code will also need to be exercised during the labs. 


[TOC]

## Lab 1

_Algorithmic, Tuples, Modulo Arithmetic, Global Scope (vs) Local Scope, Indefinite looping (`while` keyword), `if-else` statement, Recursion_

```python
def gcd(number1, number2):
    while True:
	    if number2 != 0:
	        (number1, number2) = (number2, number1 % number2)
	    else:
		    break
    return number1

### Alternative
```python
def gcd(number1, number2):
    while number2:
	        (number1, number2) = (number2, number1 % number2)
    return number1
```


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


def gcd_r(a, b): 
	if b == 0: 
		return a
	return gcd_r(b, a % b)
	
```

## Lab 2
```python
def square_root(number):
    epsilon = 0.01
    k       = number
    guess   = k / 2.0
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (guess ** 2 - k) / (2 * guess)
    return guess
    
```

## Lab 3
```python
def expo(base, expo):
    ans = 1.0
    if type(base) == str or type(expo) == str:
        return "Invalid Input"
    elif expo >= 0:
        for i in range(1, expo + 1):
            ans = base*ans
    else:
        for i in range(expo, 0):
            ans = 1/base*ans
    return ans
```

## Lab 4
```python

def linear_search(myl, token):
    found = False
    for number in myl:
        if number == token:
            found = True
            break
    return found
```

### Alternative
```python
def linear_search(mylist, token):
    for elem in mylist:
        if elem is token:
            return True
    return False
```

### Alternative pythonic search
```python
def linear_search(mylist, token):
    return (token in mylist)        
```

```python
def binary_search(myl, token):
    found = False

    left  = 0
    right = len(myl)-1

    while left <= right and not found:
        mid = (right+left)//2
        if myl[mid] == token:
            found = True

        if myl[mid] > token:
            right = mid - 1
        else:
            left  = mid + 1       
    return found

```

### Alternative
```python
def bsearch(mylist, token):
    if not mylist:
        return False
    mid = len(mylist)//2    
    if mylist[mid] is token:
        return True
    elif mylist[mid] > token:
        return bsearch(mylist[:mid], token)
    else:
        return bsearch(mylist[mid+1:], token)
```


## Lab 5
```python

def generate_primes(min, max):
    primeList = []
    if type(min) == str or type(max) == str:
        return "Invalid Range"
    for num in range(min, max + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primeList.append(num)
    return primeList

```

### Alternative 
**using List comprehension**
```python
def generate_primes(min, max):    
    return [num for num in range(min, max + 1) if isPrime(num)]

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
```

## Lab 6

```python
def get_maxnumber(numbers):
    maxval = None  
    for num in numbers:  
        if not maxval or maxval < num:  
            maxval = num
    return maxval  
    
```

### Alternative
**using reduce function**
```python
from functools import reduce
def get_maxnumber(numbers):
    return reduce(max_of_two,numbers)

def max_of_two(x,y):
    return x if x > y else y
```    

**using lambda function**
```python
from functools import reduce
def get_maxnumber(numbers):
    return reduce(lambda x, y: x if x > y else y, numbers)
```    

## Lab 7 

```python

def remove_duplicates(L):
    result = []
    for elem in L:
        if elem not in res:
            res.append(elem)
    return result
	

```

### Alternative
```python
def remove_duplicates(L):
	return list(set(L))
```
Note: it returns the sorted list without duplicates.

## Lab 8 

```python

def selectsort(L): 
    for slot in range(len(L)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, slot + 1):
            if L[location] > L[positionOfMax]:
                positionOfMax = location

        temp             = L[slot]
        L[slot]          = L[positionOfMax]
        L[positionOfMax] = temp
    return L


def insertsort(L):

  for index in range(1, len(L)):
    key = L[index]
    j = index - 1

    while j >= 0 and (L[j] > key):
      L[j + 1] = L[j]
      j = j - 1
    L[j + 1] = key
  return L

```

## Lab 9

```python

def mergesort(numbers):
    if not numbers or len(numbers) == 1:
        return numbers
    else:
        mid = len(numbers)//2
        left = mergesort(numbers[:mid])
        right = mergesort(numbers[mid:])
        return merge(left, right)


def merge(left, right):
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged += [left.pop(0)]
        else:
            merged += [right.pop(0)]
    merged += left
    merged += right
    return merged
    
```

```python

import random

def quicksort(s):
  len_s = len(s)
  if len_s < 2:
    return s

  pivot = s[random.randrange(0, len_s)]

  L = [x for x in s if x < pivot]
  E = [x for x in s if x == pivot]
  G = [x for x in s if x > pivot]

  return quicksort(L) + E + quicksort(G)
```


### Alternative 
```python
from heapq import merge

def mergesort(w):
    if len(w)<2:
        return w
    else:
        mid = len(w) // 2
        return merge(mergesort(w[:mid]), mergesort(w[mid:]))
```


## Lab 10

```python

def format_matrix(matrix):
    return "\n".join((("{:<5}"*len(row)).format(*row))for row in matrix)
    
def matrixmulti(X, Y):
    result = [[0 for col in range(len(Y[0]))] for row in range(len(X))]

    if  len(X[0]) != len(Y):
        print ("Cannot multiply the matrices. Incorrect dimensions.")
        return

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    
    print(format_matrix(result))
    return result

```


## Lab 11

```python

def wordcount(input, sentence=False):
    delimit = " "
    numwords = len(input.strip().split())

    if sentence:
        delimit = "."
        tokens  = input.strip().split(delimit)
        numsentences = len([t for t in tokens if len(t) != 0])
        return (numwords, numsentences)
    return numwords


if __name__ == '__main__':
    import sys
    total = 0
    for arg in sys.argv[1:]:
        print (arg, end=", ")
        try:
            f = open(arg, 'r')
            text = f.read()
            print(wordcount(text, sentence=True))
            f.close()
        except:
            print("File not available!")

```

### Alternative 

```python
def wordcount(file=None):

    def countwords(f):
        return len(f.read().strip().split())

    import sys
    if file: 
        return countwords(open(file))
    return countwords(sys.stdin)
```


## Lab 12

```python

import string, sys

text = open(sys.argv[1], 'r').read()
text = text.lower()
for ch in string.punctuation:
    text = text.replace(ch, ' ')
	
counts = {}
for w in text.split():
    counts[w] = counts.get(w,0) + 1 
	
items = []
for w, c in counts.items():
    items.append((c, w))
items.sort()
items.reverse()

for i in range (5):
    c, w = items[i]
    print (w, c) 

```

### Alternative
```python
import sys
def frequent(f):
    words = f.read().strip().split()
    count = {}    
    maxCount = 0                               
    for word in words:
	count[word] = count.get(word, 0) + 1 
        if count[word] > maxCount:
            maxWord = word
            maxCount = count[word]                                   
    return maxWord, maxCount


file = sys.argv[1]
if file:
    word, frequency = frequent(open(file))
    print(file + ',', '"' + word + '"', frequency)   
```

Output:
```
python frequent.py file1.txt -> file1.txt, "the" 12
```
