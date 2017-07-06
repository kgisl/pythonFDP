
# Lab CheatSheet

[//]: [TOC]

## Lab 1

```python
def gcd(number1, number2):
    while b:
        (a, b) = (b, a % b)
    return a
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
## Lab 5
```python

def prime(min, max):
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

## Lab 6

```python
def get_maxnumber(numbers):
    maxval = None  
    for num in numbers:  
        if not maxval or maxval < num:  
            maxval = num
    return maxval  
    
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

