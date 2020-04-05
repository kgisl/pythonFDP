

# Notes for Unit 2 - Illustrative programs


## Program 1


## Source Code 

```python
print("Enter two values to swap")
a = int(input())
b = int(input())

# using a temporary variable
print("Swapping using temporary variable...")
t = a
a = b
b = t

print("Value of a is {a} and\nValue of b is {b}".format(a=a, b=b))

# using XOR operator, eliminating the need for 3rd variable
print("Swapping using XOR operator...")
a = a ^ b
b = a ^ b
a = a ^ b

print("Value of a is {a} and\nValue of b is {b}".format(a=a, b=b))


def swap_func():
    global a, b
    print("swap_func function called")
    a, b = b, a


swap_func()  # go back to their original values
print("Value of a is {a} and\nValue of b is {b}".format(a=a, b=b))

```
## Sample Output
![out2](https://i.imgur.com/jOTVwC3.jpg)


## Demo 
run  `python3 swap.py` in [https://repl.it/@ashokb/unit-2-illustrative-programs](https://repl.it/@ashokb/unit-2-illustrative-programs)


## Program2


## Source Code 

```python
def circulate(a, b, c):
    i = 3
    while i:
        t = a
        a = b
        b = c
        c = t
        print(a, b, c)
        i -= 1

print("Enter 3 values")
a, b, c = input().split()
print()
circulate(a, b, c)

def circulate_list(alist):
    i = len(alist)
    while i:
        first = alist.pop(0)
        alist.append(first)
        print(*alist, sep=", ")
        i -= 1

alist = input("enter multiple values\n").split()
print()
circulate_list(alist)

```

## Sample Output

![out2](https://i.imgur.com/iSSVEUi.jpg)


## Demo 
run  `python3 circulate.py` in [https://repl.it/@ashokb/unit-2-illustrative-programs](https://repl.it/@ashokb/unit-2-illustrative-programs)



## Program 3 


|Question                                                                                                                                                                                                                                                                                                                  |Answer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|<p><strong>Coordinate Geometry Terms</strong></p><p><br></p><p>Coordinate Geometry Definition - It is one of the branches of geometry where the position of a point is defined using coordinates.</p><p><br></p><p>What are the Coordinates?	</p><p><br></p>                                                              |<p><span style="color: rgb(238, 236, 246); background-color: rgb(40, 45, 88);">What are the Coordinates?</span></p><p><br></p><p><span style="color: rgb(238, 236, 246); background-color: rgb(40, 45, 88);"><span class="ql-cursor">﻿</span>Coordinates are a set of values which helps to show the exact position of a point in the coordinate plane.</span></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|<p>Coordinate Plane Meaning	- A coordinate plane is a 2D plane which is formed by the intersection of two perpendicular lines known as the x-axis and y-axis.</p><p><br></p><p>What is the <strong>Distance Formula</strong>?</p>                                                                                         |<p><span style="background-color: rgb(40, 45, 88); color: rgb(238, 236, 246);">What is the </span><span style="color: rgb(226, 148, 20); background-color: rgb(40, 45, 88);">Distance Formula</span><span style="background-color: rgb(40, 45, 88); color: rgb(238, 236, 246);">?</span></p><p><br></p><p><span style="background-color: rgb(40, 45, 88); color: rgb(238, 236, 246);"><span class="ql-cursor">﻿</span></span>It is used to find the distance between two points situated in <strong>A(x1,y1)</strong> and <strong>B(x2,y2)</strong></p><p><br></p>                                                                                                                                                                                                                                                                                             |
|<p>What is the most logical way to represent a cartesian point in Python?</p><p><br></p><p>A. Use two variables, for e.g.  x1 and y1  or x2 and y2 </p><p>B. Use a single tuple variable</p><p>C. <strong>None</strong> of the above</p>                                                                                  |<p><strong>Choice B. </strong></p><p><strong>Tuple</strong> is the logical way of representing a point in Python.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|<p>What is the <a href="https://en.wikipedia.org/wiki/Syntax_(programming_languages)" rel="noopener noreferrer" target="_blank">syntax</a> for defining a point <code>(3, 4)</code> as a tuple in Python? </p><p><br></p><p>A. <code>(3, 4)</code></p><p>B. <code>tuple(3, 4)</code></p><p>C. Both the above are valid</p>|<p><strong>Choice C. </strong></p><p><br></p><p><strong>﻿(3, 4) </strong>and<strong> tuple(3, 4) </strong>are equivalent to each other.</p><p><br></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|<p>How can you deconstruct a <strong>tuple</strong> that represents a point?</p><p><br></p>                                                                                                                                                                                                                               |<p>How do you deconstruct a tuple? </p><p><br></p><p>If</p><p><code>pointA = (6, 8) # construction</code></p><p><br></p><p>then</p><p><code>x1, y1 = pointA # deconstruction</code></p><p><code>print(x1, y1)   # 6, 8 </code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|<p><code>x1, y1, x2, y2 = (1, 2, 3, 4)</code></p><p><br></p><p>What is the value of <code>x1</code> and <code>y2</code>?</p>                                                                                                                                                                                              |<pre class="ql-syntax" spellcheck="false">1 and 4. </pre>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|<p>What is the distance between (4, 0) and (0, 0)?</p><p><br></p><p><img src="https://memcode-production.s3.us-west-2.amazonaws.com/1585923947937" width="230"></p>                                                                                                                                                       |<p><strong>4</strong></p><p><br></p><p><code class="ql-font-monospace" style="background-color: rgb(49, 56, 114); color: rgb(208, 204, 238);">d = (x1 - x2)</code></p><p><code class="ql-font-monospace" style="background-color: rgb(49, 56, 114); color: rgb(208, 204, 238);">  = 4 - 0 </code></p><p><code class="ql-font-monospace" style="background-color: rgb(49, 56, 114); color: rgb(208, 204, 238);">  = 4 </code></p>                                                                                                                                                                                                                                                                                                                                                                                                                               |
|<p>What is the distance between (4, 3) and (4, 0)?</p><p><br></p><p><br></p><p><img src="https://memcode-production.s3.us-west-2.amazonaws.com/1585924803590" width="238" style="cursor: nwse-resize;"></p>                                                                                                               |<p><strong>3</strong></p><p><br></p><p><code>d = (x1 - x2) + (y1 - y2) </code></p><p><code>  = (4 - 4) + (3 - 0) </code></p><p><code>  = 0 + 3</code></p><p><code>  = 3</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|<p>What is the distance between (4, 3) and (0, 0)?</p><p><br></p><p><img src="https://memcode-production.s3.us-west-2.amazonaws.com/1585924993650" width="248" style="cursor: nwse-resize;"></p>                                                                                                                          |<p>Using previous formula, we get </p><p><br></p><p><code style="background-color: rgb(49, 56, 114); color: rgb(208, 204, 238);">d = (x1 - x2) + (y1 - y2) </code></p><p><code style="background-color: rgb(49, 56, 114); color: rgb(208, 204, 238);">  = (4 - 0) + (3 - 0) </code></p><p><code style="background-color: rgb(49, 56, 114); color: rgb(208, 204, 238);">  = 4 + 3</code></p><p><code style="background-color: rgb(49, 56, 114); color: rgb(208, 204, 238);">  = 7</code></p><p><br></p><p>But we know from <a href="https://www.mathsisfun.com/algebra/distance-2-points.html" rel="noopener noreferrer" target="_blank">https://www.mathsisfun.com/algebra/distance-2-points.html</a> </p><p><br></p><p><img src="https://memcode-production.s3.us-west-2.amazonaws.com/1585925436666" width="290" style="cursor: nwse-resize;"></p><p><br></p>|
|<p>If (x1 - x2) + (y1 - y2) is giving a higher value than what is correct,</p><p><br></p><p>What can the <strong>distance formula</strong> be? </p>                                                                                                                                                                       |<p>Why not square the x component and square the y component, and then reduce it down by using square root?</p><p><br></p><p>The distance formula is as follows:</p><p><br></p><p><img src="https://memcode-production.s3.us-west-2.amazonaws.com/1585939313392"></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|<p>What is the distance between <strong>(2, -1)</strong> and <strong>(5, 3)</strong>?</p>                                                                                                                                                                                                                                 |<p><img src="https://memcode-production.s3.us-west-2.amazonaws.com/1585926241096" width="276" style="cursor: nwse-resize;"></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|<p>Are you confident of writing the code for <strong>Distance between Two Points? </strong></p><p><br></p><p><strong><span class="ql-cursor">﻿</span></strong></p>                                                                                                                                                        |<p>Test yourself at <a href="http://j.mp/twoPoints" rel="noopener noreferrer" target="_blank">http://j.mp/twoPointsCC</a></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |


## Source Code 

```python
from math import sqrt


def distance_between(pointA, pointB):
    x1, y1 = pointA
    x2, y2 = pointB

    distx = x1 - x2
    disty = y1 - y2

    return sqrt(distx**2 + disty**2)


# main program
# tuple packing allows for assigning
# multiple inputs in one statement
print("Enter coordinates for Point A")
pointA = int(input()), int(input())

print("Enter coordinates for Point B")
pointB = int(input()), int(input())

print("distance between {0} and {1} is {2}"
    .format(pointA, pointB, distance_between(pointA, pointB))
)
```

## Sample Output

![out3](https://i.imgur.com/jGNMaNN.jpg)


## Demo 
run  `python3 distance.py` in [https://repl.it/@ashokb/unit-2-illustrative-programs](https://repl.it/@ashokb/unit-2-illustrative-programs)


## Teaching Assets

|item | link | remarks | 
|------|------|---------|
|Video capture |http://j.mp/distanceThisVideo | demonstrates how to use Memcode and CyberDojo and Slides
| Memcode cards | [https://www.memcode.com/courses/2288/](https://www.memcode.com/courses/2288/review) | useful for classroom and personal review |
| CyberDojo link | [http://cyberdojo1.kgfsl.com/kata/edit/Tx2Vqt](http://cyberdojo1.kgfsl.com/kata/edit/Tx2Vqt) | The super simple testing framework for capturing incremental coding sessions
| Google Slides | [PDF version](https://github.com/kgisl/pythonFDP/blob/master/units/Unit%202%20-%20illustrative%20programs.pdf) | Or PPTx file is better?
| Auto-generated documentation | [distance_between](https://github.com/kgisl/pythonFDP/blob/master/docs/README.md#distance_between) doctstring documentation | consolidates all docstrings in one place (docs/README.md) in the repo 




## Bonus Material

### Swap

There are actually 4 ways to do it. Please find all of them. 
[https://www.geeksforgeeks.org/python-program-to-swap-two-variables/](https://www.geeksforgeeks.org/python-program-to-swap-two-variables/)


