
# Lab 12a: File content sorter 

[TOC]

## Overall Instructions 

1. Update `KyG.id` file with your details
2. Read the instructions file
3. Ask your mentor plenty of questions
4. Modify the basic Python files to solve the problem statement


## Problem Statement 

### Sort a file of integers

Please read the question carefully - 
most errors are because you did not read the
instructions carefully. Make sure your
program produces the expected output,
and nothing else. Make sure that the
output is in a file called `output.txt`.
Do not use `C:\output.txt` or any other
such path. Similarly, make sure you
read the data from `input.txt` and not
from `C:\input.txt` or anything else. Do
not print anything to stdout. Do not
prompt the user to enter numbers. 

> Write a program which will read
> a bunch of integers from an input
> file, sort them, and print the sorted
> result to an output file.

You must read the input from `input.txt`
and you must write the output to `output.txt`. 
The input will contain one integer per line, 
and you’re expected to stop reading when 
you reach EOF. The output should also have
one integer per line.

## Warning 
Do not print anything else to 
`output.txt`. Do not print prompts like 
`“Please enter a number.”` The output should 
not contain anything other than the sorted 
integers, one per line.

If your input is something like this: 

```
	3 
	4 
	7 
	1 
	5 
```

The output should be

``` 
	1 
	3 
	4 
	5 
	7

```

## Important Notes
Please write your program in Python. 

You must be able to read the input from a 
file called `input.txt` in the current directory. 
You must be able to read the file in a format 
exactly as shown above - do not assume that any 
other information will be provided in the file 
or on standard input. You must write your output 
to a file called `output.txt` in the current directory. 

Do not write or print anything else into `output.txt`
other than the expected answer. Do print anything extra to
`stdout` or to the output file (if any). 

Read the instructions carefully. Most candidates fail 
because they did not follow the instructions exactly.

