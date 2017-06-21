
# Lab 12: Find the most frequent words in a text read from a file

Write a Python program to compute the most frequently used words from the text file.

## Example 

	python frequent.py file1.txt -> file1.txt, "the" 12


## Pre-Lab Questions 

1. There may not exist a file with the user provided filename(s) on the command line. In that case, a built-in [OS-level exception](https://docs.python.org/3/library/exceptions.html#os-exceptions) will be `raise`d when the program is executed. Write a Python function `open_file(filename)` that  handles the appropriate exception (https://docs.python.org/3/library/exceptions.html#FileNotFoundError) and re-`raise` the exception (allowing a caller to handle the exception as well). To help you get started, the basic code for `open_file` is already provided below. 

	```python
	def open_file(filename):
	    file = open(filename, 'r')
		return file
	```


2. When such a function `open_file()`is called with the appropriate argument, it is recommended coding practice to have exception handling code in the calling code or function to handle `OS_exceptions`. What would that exception handling code be for handling the specific exception which was raised in the previous question?

3. What is the difference between a text file and a binary file? 

4. Imagine that the user specifies a filename, and a file exists with the same name but it happens to be a binary file and not a text file. If the program tries to read a binary file when it is expecting a text file, other exceptions will occur. What additional exception handling code would you add to handle **all other types** of exceptions that may arise, including the binary file scenario? 


## Post-lab Questions





## Related Material

http://programmingzen.com/use-python-to-detect-the-most-frequent-words-in-a-file/

 