
# Source code
```python

################################
# Program No 0
# simple program for histogram 
#  - without functions
#  - prompting user for the input 
#
#################################
# Build a histogram
from collections import defaultdict
counters = defaultdict(int)
input_list = []
entries = int(input("Number of entries? "))
for _ in range(entries):
  userval = int(input("Enter value:"))
  input_list.append(userval)
  counters[userval] += 1

if input_list:
  print("Input values", input_list)
  histogram = sorted(counters.items())
  print("Histogram", histogram)
  print("Visualize the histogram")
  for i in range(len(histogram)): 
    print (f'{histogram[i][0]:2}', '*'*histogram[i][1]) 
else:
  print("No values available to build histogram")

################################
# Program No 1
# using dictionary to build the histogram
#   - using a randomizer for input
#   - functionally decomposing the logic 
#
#################################
# Build a histogram

import random
# build a random list 
# returns a list containing numbers 1 <= v <= maxval
# the list will contain n elements where
#   mincount < n < maxcount 
def random_list(mincount, maxcount, maxval, minval=1): 
  size = random.randint(mincount, maxcount)
  alist = []
  for _ in range(size):
    alist.append(random.randrange(minval, maxval+1))		
  return alist

arlist = random_list(50, 120, 20, -10)
print("A random list", arlist)


# returns a list containig tuples with 
# value and frequency, aka a histogram
from collections import defaultdict
def generate_histogram(arlist):
  counters = defaultdict(int) #inits value to 0
  for number in arlist:
	  counters[number] += 1

  histogram = sorted(counters.items())
  return histogram

histo = generate_histogram(arlist)
print("A histogram with", histo)

print("Visualizing the histogram")
for i in range(len(histo)): 
  print (f'{histo[i][0]:2}', '*'*histo[i][1])


################################
# Program No 2
# without using dictionary
# 
#################################

# returns a list of tuples with value and frequency
def generate_histogram2(arlist):
  counters = [0] * (1+max(arlist)) # non-zero values

  for number in arlist:
    try:
      counters[number] += 1
    except:
      print(f'**** Error with {number}!')
      print(f'--- in {histo} with {len(histo)}')

  histogram = [(i,n) 
	  for i, n in enumerate(counters) if n
	]
  return histogram

arlist = random_list(50, 120, 20) # positive integers
print("A random list", arlist)

histo = generate_histogram2(arlist)
print("A histogram with", histo)

print("Visualizing the histogram")
for i in range(len(histo)):
  print (f'{histo[i][0]:2}', '*'*histo[i][1])

```

# Assignment
1. How many distinct programs are there in the above code? 
2. What is the main advantage of Program 1 over Program 2?
3. What is the main advantage of Program 2 over Program 1? 
4. Modify Program 1 to display an ordered histogram. 

[//]: http://bit.ly/histoThis 

# Misc

```python
###########################
#
# from Charulatha PDF
#
###########################
def histogram(items):
	for n in items:
		output = ''
		times = n
		while(times > 0):
			output += '@'
			times = times - 1
		print(output)

histogram([2, 3, 6, 5])
```

1. Provide commentary on the above program source code
2. Why not use this code for teaching? 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjU4MTM2NTgsNTAzMzQ0NDUwLDgwNjEwNz
EzNiw4NTc5MzgxNTIsLTgzNDA5MDU3NCwtNzQzMDM3MzI4LC05
NjM2NTY0MzIsLTg2MzE5NjgzNiwtMTI0MTQ3OTUwOCw1ODkzND
MxOTBdfQ==
-->