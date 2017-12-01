
# Useful links to explore

- See some beautiful Python poems - https://www.reddit.com/r/programming/comments/26dyh/ask_reddit_whats_the_most_beautiful_piece_of/c26ny9/
-  j.mp/python4Months   - and http://blog.agupieware.com/2014/01/benchmarks-teach-yourself-python-in.html 
-  https://www.reddit.com/r/programming/wiki/faq
- http://bit.ly/beginnerPython - easy video tutorials including for unittesting - http://j.mp/unittestVideo
- https://danieltakeshi.github.io/2013/07/05/ten-things-python-programmers-should-know/
- https://www.quora.com/What-are-the-most-important-topics-to-learn-in-Python/answer/Janarthanan-S-1?srid=ul6v
- https://www.quora.com/What-is-an-ideal-checklist-to-learn-Python-in-30-days/answer/Janarthanan-S-1?srid=ul6v - explore Python in 30 days 
- http://docs.python-guide.org/en/latest/intro/learning/ 
- https://stackoverflow.com/questions/2439638/in-what-order-should-the-python-concepts-be-explained-to-absolute-beginners 
- https://bitbucket.org/gregmalcolm/python_koans or https://github.com/gregmalcolm/python_koans - 289 koans to enlightenment! 
- http://j.mp/pythonKoanVideo 
- http://www.learnpython.org/ 
- https://www.quora.com/How-does-Quincy-Larson-suggest-I-learn-to-code/answer/Quincy-Larson 
   - https://www.quora.com/What-is-a-step-by-step-procedure-to-become-a-GitHub-open-source-developer-for-a-complete-newbie-What-are-the-prerequisite-courses-I-should-take-and-how-should-I-choose-the-best-project-Also-please-suggest-some-projects-in-C++-Java/answer/Quincy-Larson 
	   - https://github.com/search?l=Python&q=label%3Afirst-timers-only&state=open&type=Issues 
- https://www.quora.com/What-are-commonly-asked-Python-interview-questions
- https://medium.com/@sebastienphl/a-practical-guide-to-learning-the-basics-of-web-programming-79961f3f3baa 

- Learn by Doing (#6) - #6 Learn by doing: practice your programming skills and build real projects as soon as possible. 
	- https://medium.com/@sebastienphl/a-practical-guide-to-learning-the-basics-of-web-programming-79961f3f3baa
		 - http://pythonpracticeprojects.com/ 
		 - http://javascriptissexy.com/how-to-learn-javascript-properly/ 








**Table of Contents**

* [Important Concepts](#important-concepts)  
	* [0. Types and their attributes (aka methods, Unit 3)](#0-types-and-their-attributes-aka-methods-unit-3)  
	* [1. Differentiate between parameters and arguments (Unit 3)](#1-differentiate-between-parameters-and-arguments-unit-3)  
		* [Argument Definition](#argument-definition)  
		* [Parameter Definition](#parameter-definition)  
	* [2. Explain Immutability with reference to the various data types in Python. (Unit 3)](#2-explain-immutability-with-reference-to-the-various-data-types-in-python-unit-3)  
		* [Everything is an Object](#everything-is-an-object)  
		* [What is ID?](#what-is-id)  
		* [What is value?](#what-is-value)  
		* [Immutable and Mutable](#immutable-and-mutable)  
	* [3. What is list comprehension and what is the main benefit? Describe with an example. (Unit 4)](#3-what-is-list-comprehension-and-what-is-the-main-benefit-describe-with-an-example-unit-4)  
	* [4. Slicing as an Object](#4-slicing-as-an-object)  
	* [5. If Python is interpreted, what are .pyc files?](#5-if-python-is-interpreted-what-are-pyc-files)  
	* [6. A String is a recursive data structure. True or False?](#6-a-string-is-a-recursive-data-structure-true-or-false)  
	* [7. The XOR trick, grokked, finally!](#7-the-xor-trick-grokked-finally)  
		* [Credits](#credits)  
	* [8. Packages and Modules](#8-packages-and-modules)  
	* [9. How to maintain a sorted list?](#9-how-to-maintain-a-sorted-list)  
* [Misc](#misc)  
	* [Important Links](#important-links)  
	* [The best 3 books](#the-best-3-books)  
	* [Learn by Example](#learn-by-example)  
		* [What standard libraries to learn in Python?](#what-standard-libraries-to-learn-in-python)  



# Important Concepts

[TOC]


## 0.0 Iterables 

In Python, there are iterables and there are non-iterables. Which of the following is not an iterable? 

  - `'abcdef'`
  - `range(100)` 
  - `[1, 2, 3, 4, 55, 100]` 
  - `[('a', 1), ('b', 2), ('c', 33)]` 
  - `(('a'), ('b'), ('c'), ('a', 1), ('b', 2), ('c', 33))`
  - `zip(string.ascii_lowercase, range(26))`
  - `adict.keys()`  where `adict` is a Python dictionary variable 
  - `adict.values()` where `adict` is a Python dictionary variable 
  - `{'a': 1, 'b': 2, 'c':3}`
  - `set(string.ascii_lowercase)`
  - `[[1, 2], [3], [4, 5, 6], [0]]`



## 0.1 Types and their attributes (aka methods, Unit 3)

There are 4 main types in Python (string, tuples, list and dictionary). And across all of them, there are about 25 important attributes (methods) that help process/modify them. They are tabulated as follows: 


|Type | Attributes | 
|:------|:-------|
|`__builtins__` | **`int`**, **`str`**, **`tuple`**, **`list`**, **`dict`**, **`len`**, **`sorted`**, **`del`** 
|` <class 'str'>`|`capitalize`, 1 **`count`**, `endswith`, 2 **`find`**, `format`, `index`, `isalnum`, 3 **`isalpha`**, `isdecimal`, `isdigit`, `islower`, `isnumeric`, `isspace`, `istitle`, `isupper`, 4 **`join`**, `ljust`, `lower`, `lstrip`, `replace`, 5 **`rfind`**, `rindex`, `rjust`, 6 **`split`**, `splitlines`, `startswith`, 7 **`strip`**, `swapcase`, `title`, `upper`, `zfill` |
|` <class 'tuple'>`|8 **`count`**, `index` |
|` <class 'list'>`|9 **`append`**, `clear`, `copy`, 10 **`count`**, 11 **`extend`**, `index`, 12 **`insert`**, 13 **`pop`**, 14 **`remove`**, 15 **`reverse`**, 16 **`sort`** |
|` <class 'dict'>`|`clear`, `copy`, `fromkeys`, 17 **`get`**, 18 **`items`**, 19 **`keys`**, 20 **`pop`**, `popitem`, `setdefault`, 21 **`update`**, 22 **`values`** |
|` <_io.TextIOWrapper name='file1.txt' mode='r+' encoding='UTF-8'>`|23 **`close`**, `fileno`, `flush`, 24 **`mode`**, `name`, 25 **`read`**, `readline`, `readlines`, `seek`, 26 **`write`**, `writelines` |
   

## 1. Differentiate between parameters and arguments (Unit 3)

http://j.mp/argsVsParams - the official Python guide does not do justice. It is best to read this article here - http://stupidpythonideas.blogspot.in/2013/08/arguments-and-parameters.html


![faqArg](https://cdn.rawgit.com/kgisl/pythonFDP/7d9a152b/img/ArgumentsVsParameters.jpeg)


### Argument Definition 

https://docs.python.org/3/glossary.html#term-argument
![argument](https://cdn.rawgit.com/kgisl/pythonFDP/7d9a152b/img/argumentGlossary.jpeg)

### Parameter Definition 

https://docs.python.org/3/glossary.html#term-parameter
![parameter](https://cdn.rawgit.com/kgisl/pythonFDP/7d9a152b/img/parameterGlossary.jpeg)

What is the difference between arguments and parameters?

Parameters are defined by the names that appear in a function definition, whereas arguments are the values actually passed to a function when calling it. Parameters define what types of arguments a function can accept. For example, given the
function definition: 

```python
def func (foo, bar=None, **kwargs)
	pass
```

`foo`, `bar` and `wargs` are parameters of `func` 

However, when calling func for example `func(42, bar=314, extra=somevar)` the values 42 314, and somevar are arguments.


**argument**
A value passed to a function (or method when calling the function. There are two kinds of arguments:

**keyword argument**:  an argument preceded by an identifier ( e.g. name in a function call). For example, 3 and 5 are both keyword arguments in the following calls to

	complex(real=3, imag=5)

**positional argument**: an argument that is not a keyword argument. Positional arguments in the following calls:
		
		complex (3, 5)

Arguments are assigned to the named local variables (aka _parameters_) in a function body. 

**parameters**
A named entity in a function (or method) definition that specifies an argument (or in some cases, arguments that the function can accept. There are five kinds of parameters. 


## 2. Explain Immutability with reference to the various data types in Python. (Unit 3)

### Everything is an Object 
![object](https://cdn.rawgit.com/kgisl/pythonFDP/e7ccde61/img/whatIsObject.png)

### What is ID?
![id](https://cdn.rawgit.com/kgisl/pythonFDP/e7ccde61/img/whatIsID.png)

### What is value? 
![value](https://cdn.rawgit.com/kgisl/pythonFDP/e7ccde61/img/whatIsValue.png)

### Immutable and Mutable 
![immutableP](https://cdn.rawgit.com/kgisl/pythonFDP/e7ccde61/img/pythonImmutable.png)
![mutableP](https://cdn.rawgit.com/kgisl/pythonFDP/e7ccde61/img/pythonMutable.png)

![mCode](https://cdn.rawgit.com/kgisl/pythonFDP/3a8caff1/img/mutableCode.png) ![mOutput](https://cdn.rawgit.com/kgisl/pythonFDP/3a8caff1/img/mutableOutput.png)

![immutableTable](https://cdn.rawgit.com/kgisl/pythonFDP/728f283e/img/mutablePython.png)




## 3. What is list comprehension and what is the main benefit? Describe with an example. (Unit 4)


**Main benefit**: Code is shorter and sometimes more clearer. 

![list_comprehension](https://cdn.rawgit.com/kgisl/pythonFDP/e3caa43d/img/explainListComprehension.png)

**Code Snippet** 
Lines `1-6` is equivalent to Lines `11-12` and equivalent to Line `17`.  

![listCode](https://cdn.rawgit.com/kgisl/pythonFDP/9e101ddd/img/listComprehensionCode.png)

**Output of Code Snippet**

![listOut](https://cdn.rawgit.com/kgisl/pythonFDP/020de846/img/listComprehensionOutput.jpg)


## 4. Slicing as an Object 
https://docs.python.org/3/library/functions.html#slice

![slice](https://cdn.rawgit.com/kgisl/pythonFDP/7502044e/img/slicingAsObject.png)


## 5. If Python is interpreted, what are .pyc files?

"...it reminded me that seemingly trivial questions may have rather deep answers.” http://bit.ly/deepAnswer  

## 6. A String is a recursive data structure. True or False? 

![stringRecursive](https://cdn.rawgit.com/kgisl/pythonFDP/a5233884/img/stringAsRecursive.jpg)

Credit: https://twitter.com/dbader_org/status/874653012374859776

Fun fact—Python `str` objects are **recursive** data structures: Each character in a string is a `str` of length 1 itself.

## 7. The XOR trick, grokked, finally! 

I have always wondered how the in-place `swap` worked using the XOR operation. The following **table** went a long way in helping clear up the magic in _my_ head. 

| arg 1 | arg 2   |	Result     |
|--------|--------|------------|
|A	     |B       |	C     |
|B	     |C	      | A     |   
|A	     |C	      | B     |

Therefore, 

```
a  = a ^ b   # c value in a 
b  = a ^ b   # b now contains a (since c ^ b -> a) 
a  = a ^ b   # a now contains b (since c ^ a -> b)
```

### Credits

http://www.brunton-spall.co.uk/post/2010/09/07/interview-questions-xor-trick-and-why-you-should-j/


## 8. Packages and Modules 

> **tl;dr  package**: A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an __path__ attribute.

> **tl; dr2** Packages are modules too. They are just packaged up differently; they are formed by the combination of a directory plus `__init__.py` file. They are modules that can contain other modules. 

Any Python file is a [module][1], its name being the file's base name without the `.py` extension. A [package][2] is a collection of Python modules: while a module is a single Python file, a package is a directory of Python modules containing an additional `__init__.py` file, to distinguish a package from a directory that just happens to contain a bunch of Python scripts. Packages can be nested to any depth, provided that the corresponding directories contain their own `__init__.py` file.

The distinction between module and package seems to hold just at the file system level. When you import a module or a package, the corresponding object created by Python is always of type `module`. Note, however, when you import a package, only variables/functions/classes in the `__init__.py` file of that package are directly visible, *not* sub-packages or modules. As an example, consider the `xml` package in the Python standard library: its `xml` directory contains an `__init__.py` file and four sub-directories; the sub-directory `etree` contains an `__init__.py` file and, among others, an `ElementTree.py` file. See what happens when you try to interactively import package/modules:

    >>> import xml
    >>> type(xml)
    <type 'module'>
    >>> xml.etree.ElementTree
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'module' object has no attribute 'etree'
    >>> import xml.etree
    >>> type(xml.etree)
    <type 'module'>
    >>> xml.etree.ElementTree
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'module' object has no attribute 'ElementTree'
    >>> import xml.etree.ElementTree
    >>> type(xml.etree.ElementTree)
    <type 'module'>
    >>> xml.etree.ElementTree.parse
    <function parse at 0x00B135B0>

  [1]: http://docs.python.org/tutorial/modules.html
  [2]: http://docs.python.org/tutorial/modules.html#packages

## 9. How to maintain a sorted list? 
You need to maintain a list in sorted order without having to call `sort` each time an item is added to the list. How will you do this?

# Misc

## Important Links

http://www.pixelmonkey.org/2015/06/06/pybooks
https://www.safaribooksonline.com/library/view/python-in-a/9781491913833/

http://python-guide-pt-br.readthedocs.io/en/latest/intro/learning/

The best programming practice book!
ByKevin Lon April 17, 2017
Format: Paperback
TL;DR: When it comes to programming practice, Elements of Programming interviews is the cream of the crop. If you are only going to buy one practice book, I would recommend this one above all the others. I have nothing but good things to say about the book, and can confidently say that no other product that offers as much depth as EoPI does.

The first thing you will notice about EoPI is that the level of detail is astounding; I was blown away by the sheer amount of effort that the authors put into it. The problem analysis is unparalleled, and goes far beyond basic algorithm/data structures knowledge. The solutions are easy to follow and explained very thoroughly. For example, if a problem has multiple solutions, the authors will walk you through each one and guide you towards the optimal solution. In addition to being a goldmine of commonly-asked problems, the book also offers many original problems that you wouldn't be able to find anywhere else; it is by far the most comprehensive practice resource out there. In terms of organization the book is extremely well structured, and even provides study plans for the reader to help with problem selection. Some of the problems in the book are much more difficult than what you would find in an actual interview. If you are able to comfortably solve the problems in this book, you should certainly have no problem with the real thing.

Before using this book I tried various other resources, particularly Cracking the Coding Interview and LeetCode. The former offered no depth whatsoever: mostly simple and overused problems (like what you would get in a technical phone screen). While the latter provided no shortage of challenging problems, I found it sometimes frustrating to use because of its unclear problem statements and its reliance on an auto-grader to compensate for lack of published solutions and guidance.

I have long been a fan of the series and I am delighted to see that a Python version has been released. I give Elements of Programming Interviews 5-stars because I think it is an essential practice resource. Honestly, it was a lot of fun to work through the book; it was much more pleasant than the usual practice problem grind. Even if you are not practicing for interviews at the time, I highly recommend checking it out. It is a great way to develop your problem solving ability and build confidence for future interviews.

https://www.amazon.com/dp/1537713949/ref=cm_wl_huc_continue

## The best 3 books

Python expertise awaits. Whether you are a pair of hackers building a prototype for a new startup; a 20-person team that is doing large-scale engineering with Python; or a thousand-person engineering department that is switching from Java/C++, your team will benefit greatly from copies of each of these!

- Python Essential Reference, 4e (Beazley)
- Fluent Python, 1e (Ramalho)
- Python Cookbook, 3e (Beazley, Jones)
- Bonus: Python Cookbook, 2e (Martelli, Ascher)

You’ll all be certified Pythonistas in no time. Welcome to the community, and Happy Hacking!

##  Learn by Example

https://doughellmann.com/blog/the-python-3-standard-library-by-example/ 

### What standard libraries to learn in Python? 

https://doughellmann.com/blog/the-python-3-standard-library-by-example/the-python-3-standard-library-by-example-table-of-contents/

http://my.safaribooksonline.com/book/programming/python/9780134291154 - book TOC 

