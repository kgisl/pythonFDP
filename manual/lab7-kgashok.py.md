**Table of Contents**

* [Lab 7: Removing  all the duplicate elements in a list](#lab-7-removing--all-the-duplicate-elements-in-a-list)
	* [Problem statement](#problem-statement)
	* [Solution Key](#solution-key)
	* [CloudCoder Exercise](#cloudcoder-exercise)
	* [Pre-Lab Questions](#pre-lab-questions)
	* [Post-Lab Questions](#post-lab-questions)
	* [Bonus 1](#bonus-1)
	* [Bonus 2](#bonus-2)
	* [Interview grade](#interview-grade)
	* [Related Links](#related-links)
	* [Predict the output  of Snippet1](#predict-the-output--of-snippet1)
	* [Predict the output of Snippet2](#predict-the-output-of-snippet2)
	* [Analyze Snippet1 vs Snippet2](#analyze-snippet1-vs-snippet2)




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
    tokens = {}
    for elem in mlist:
        tokens[elem] = 1

    return list(tokens.keys())


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

0. If a list contains `[1, 2, 3, 'python', 3, 4, 'python1', 'python', 5]`, what would the list look like after all the duplicates are removed?
1. If a list contains `[5, 5, 5, 5, 5, 6, [1, 2, 6], [1, 2, 6]]`, what would the list contain after all the duplicates are removed?
2. What is the method available to remove an element from a list?
3. How will you get a list of all the `keys` that are present in a dictionary (which basically contains a key:value pair)?
4. How will get a list of all the `values` that are present in a dictionary?
5. What is the python code for building a dictionary out of 3 tuples? For e.g.
	> ("jan", 31)
	> ("feb", 28) and
	> ("mar", 31) `

7. What is the value of `L` after you run the code below?

> ![Imgur](http://i.imgur.com/3WRTL5N.png)



## Post-Lab Questions

0. Rewrite the code to use only `lists` and not a `dictionary`. Or vice versa. Provide analysis to whether the eventual output is `stable` or `unstable`.
1. You are not allowed to use another data structure to remove duplicates. That is, remove the duplicates in-place. Is this possible?
2. How will you find the common elements that exist in two different lists?
3. Write a program to calculate the product of all the integers that are available in a list. For e.g. if `alist = [2, 3, 5, 8]`, then `product(alist) = 240`
4. Find the `gcd` of two integers using the prime factorization method.  Review video at http://j.mp/whatIsPrime and http://j.mp/gcdPrime. Use the function you developed in `Lab 5` to complete this. Here's an outline for the function that you will need to develop:

		def gcd(n1, n2):
		    prime_factors_of_n1 = prime_factors(n1)
		    prime_factors_of_n2 = prime_factors(n2)
		    common_prime_factors = \
		        intersect_list(prime_factors_of_n1, prime_factors_of_n2)

		    product_of_common_prime_factors = product(common_prime_factors)
		    return product_of_common_prime_factors


## Bonus 1

1. You are asked to remove all the duplicate occurrences of only one specific element in the list. Write a function for this.
2. Count the number of number of distinct characters that occur more than once in the string. Read the problem statement and solve on CC - http://j.mp/countDuplicates
3. Write a program that will analyze whether a string is an isogram, pangram or a partial perfect pangram. Also if the string contains duplicates, count the number of duplicate characters that are there in the string.
	 - And how about checking whether two words are their respective anagrams? And if not, how many changes are needed to make them?

## Bonus 2

1. There is probably a one-line Pythonic solution for almost every complicated problem out there. That is also the case for this lab exercise. Can you figure it out?
2. There is even a shorter one liner if you use another powerful Python data type. Can you figure it out?
3. Between 1 and 2, which solution is more preferable? And why?


## Interview grade

Calculate the `gcd` for a list of integers using the prime factorization method. The method is well described in the video at http://j.mp/gcdPrime - use lists as part of the solution.

## Related Links

https://goo.gl/v7ephq
http://j.mp/removeDuplicates


## Predict the output  of Snippet1

```python

mylist = [1, 5, 1, 2, 3, 4, 2, 7, 4, 6]
if mylist:
    mylist.sort()
    last = mylist[-1]
    for i in range(len(mylist)-2, -1, -1):
      if last == mylist[i]:
          del mylist[i]
      else:
          last = mylist[i]

print(mylist)
```

## Predict the output of Snippet2

```python

u = [1, 5, 1, 2, 3, 4, 2, 7, 4, 6]
for x in s:
    if x not in u:
        u.append(x)
print (u)
```

## Analyze Snippet1 vs Snippet2

0. Both `mylist` and `u` are identical lists. True or False?
1. At the end of execution of their respective codes, `mylist` from `Snippet1` and `u` from `Snippet2` will always be of the same size, as long as they both start off by being equal. True or False?
2. At the end of execution of their respective codes, `mylist` and `u` will have the same contents, in the same order. True or False?
