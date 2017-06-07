
# Lab 12: Compute the most frequently used words from the text file.


## Problem statement 

Write a Python program to compute the most frequently used words from the text file.


sample input 0: the peacock is the beautiful bird...
sample output 0: the

sample input 1: sea shells is in the sea shore
sample output 1: sea

sample input 2: It is a quite easy program
sample output 2: There are no frequently used words
	


## Solution Key

```python 

def word_freq():
    max = 0 
    val = ''
    counter = {}
    f = open('animal.txt', 'r')
    contents = f.read()
    words = contents.split()
    for i in range(len(words)):
        words[i] = words[i].strip(',:.;')
        if words[i].lower() not in counter:
           counter[words[i].lower()] = 1
        else:
           counter[words[i].lower()] += 1
    for i in counter.keys():
        if counter[i] > max:
            max = counter[i]
            val = i
    return val

```


## CloudCoder Exercise 


## Related material 


## Viva Questions 


## Bonus 1 


## Related Material 



CD Material: http://10.100.8.8/kata/edit/AF5211CDC2?avatar=fox
