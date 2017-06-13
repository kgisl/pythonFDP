
# Important Concepts

[TOC]

## 0. Types and their attributes (aka methods, Unit 3)

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

![faqArg](https://cdn.rawgit.com/kgisl/pythonFDP/7d9a152b/img/ArgumentsVsParameters.jpeg)

### Argument Definition 

![argument](https://cdn.rawgit.com/kgisl/pythonFDP/7d9a152b/img/argumentGlossary.jpeg)

### Parameter Definition 

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


# 4. If Python is interpreted, what are .pyc files?

http://j.mp/deepAnswer 

# 5. A String is a recursive data structure. True or False? 

![stringRecursive](https://cdn.rawgit.com/kgisl/pythonFDP/a5233884/img/stringAsRecursive.jpg)

Credit: https://twitter.com/dbader_org/status/874653012374859776

Fun fact—Python `str` objects are **recursive** data structures: Each character in a string is a `str` of length 1 itself.