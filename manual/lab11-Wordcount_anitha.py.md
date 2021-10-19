# Lab 11: Programs that take command line arguments (word count)

[TOC]

## Problem statement

Write a Python program to count the number of words passed in command line arguments.

    Sample Input1: Hi, Hello, Hi
    Sample Output1: {'Hi': 2, 'Hello': 1}

    Sample Input2: abc,123,def,abc
    Sample Output2: {'abc': 2, 123:1,'def': 1}

    Sample Input3: @@@,python,FDP,@@@,FDP,FDP
    Sample Output3:{@@@ :2,'python': 1,'FDP': 3}

## Solution Key

```python

#'Method 1
def wordcountFun(words):
    wordcount={}
    for word in words.split(' '):
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    print (wordcount)
    return wordcount

# Method 2
def wordcountFun1(words):
    wordcount={}
    new=words.lower()
    for word in new.split(' '):
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    print (wordcount)
    return wordcount

# Method 3
def wordcountFun2(words):
    wordcount={}
    for word in words.split(','):
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    print (wordcount)
    return wordcount

```

## CloudCoder Exercise

## Related material

## Pre-Lab Questions

## Post-lab Questions

## Bonus 1

## Related Material

### PPT Slides showing the Recursive Calls

### Recursion vs Iteration

### CD Link : http://10.100.8.8/kata/edit/D5502D90C6?avatar=bat
