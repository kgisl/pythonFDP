
# Important Concepts

[TOC]

## 1. Differentiate between parameters and arguments. 

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


## 2. Explain Immutability with reference to the various data types in Python. 

![immutable](https://cdn.rawgit.com/kgisl/pythonFDP/728f283e/img/mutablePython.png)


## 3. What is list comprehension and what is the main benefit? Describe with an example. 


**Main benefit**: Code is shorter and sometimes more clearer. 

![list_comprehension](https://cdn.rawgit.com/kgisl/pythonFDP/e3caa43d/img/explainListComprehension.png)

**Code Snippet** 
Lines `1-6` is equivalent to Lines `11-12` and equivalent to Line `17`.  

![listCode](https://cdn.rawgit.com/kgisl/pythonFDP/9e101ddd/img/listComprehensionCode.png)

**Output of Code Snippet**

![listOut](https://cdn.rawgit.com/kgisl/pythonFDP/020de846/img/listComprehensionOutput.jpg)