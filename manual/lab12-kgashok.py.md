
# Lab 12: Find the most frequent words in a text read from a file

Write a Python program to compute the most frequently used words from the text file.

## Pre-Lab Questions 

1. There may not exist a file with the user provided filename(s) on the command line. In that case, a built-in [OS-level exception](https://docs.python.org/3/library/exceptions.html#os-exceptions) will be `raise`d when the program is executed. Write a Python function `open_file(filename)` that  handles the appropriate exception (https://docs.python.org/3/library/exceptions.html#FileNotFoundError) and re-`raise` the exception (allowing a caller to handle the exception as well). To help you get started, the basic code for `open_file` is already provided below. 

	```python
	def open_file(filename):
	    file = open(filename, 'r')
	    return file
	```


2. When such a function (`open_file()`) with the appropriate argument, it is good practice to have exception handling code in the calling code or function to handle the `OS_exception`. What would that exception handling code ideally look like? 


## Post-lab Questions





## Related Material

http://programmingzen.com/use-python-to-detect-the-most-frequent-words-in-a-file/

 