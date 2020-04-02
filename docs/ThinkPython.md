
Think Python

### How to Think Like a Computer Scientist

```
Version 2.0.
```


Think Python

### How to Think Like a Computer Scientist

```
Version 2.0.
```
### Allen Downey

### Green Tea Press

```
Needham, Massachusetts
```

Copyright © 2012 Allen Downey.

Green Tea Press
9 Washburn Ave
Needham MA 02492

Permission is granted to copy, distribute, and/or modify this document under the terms of the
Creative Commons Attribution-NonCommercial 3.0 Unported License, which is available athttp:
//creativecommons.org/licenses/by- nc/3.0/.

The original form of this book is LATEX source code. Compiling this LATEX source has the effect of gen-
erating a device-independent representation of a textbook, which can be converted to other formats
and printed.

The LATEX source for this book is available fromhttp://www.thinkpython.com


# Preface

## The strange history of this book

In January 1999 I was preparing to teach an introductory programming class in Java. I had
taught it three times and I was getting frustrated. The failure rate in the class was too high
and, even for students who succeeded, the overall level of achievement was too low.

One of the problems I saw was the books. They were too big, with too much unnecessary
detail about Java, and not enough high-level guidance about how to program. And they all
suffered from the trap door effect: they would start out easy, proceed gradually, and then
somewhere around Chapter 5 the bottom would fall out. The students would get too much
new material, too fast, and I would spend the rest of the semester picking up the pieces.

Two weeks before the first day of classes, I decided to write my own book. My goals were:

- Keep it short. It is better for students to read 10 pages than not read 50 pages.
- Be careful with vocabulary. I tried to minimize the jargon and define each term at
    first use.
- Build gradually. To avoid trap doors, I took the most difficult topics and split them
    into a series of small steps.
- Focus on programming, not the programming language. I included the minimum
    useful subset of Java and left out the rest.

I needed a title, so on a whim I choseHow to Think Like a Computer Scientist.

My first version was rough, but it worked. Students did the reading, and they understood
enough that I could spend class time on the hard topics, the interesting topics and (most
important) letting the students practice.

I released the book under the GNU Free Documentation License, which allows users to
copy, modify, and distribute the book.

What happened next is the cool part. Jeff Elkner, a high school teacher in Virginia, adopted
my book and translated it into Python. He sent me a copy of his translation, and I had the
unusual experience of learning Python by reading my own book. As Green Tea Press, I
published the first Python version in 2001.

In 2003 I started teaching at Olin College and I got to teach Python for the first time. The
contrast with Java was striking. Students struggled less, learned more, worked on more
interesting projects, and generally had a lot more fun.


**vi Chapter 0. Preface**

Over the last nine years I continued to develop the book, correcting errors, improving some
of the examples and adding material, especially exercises.

The result is this book, now with the less grandiose titleThink Python. Some of the changes
are:

- I added a section about debugging at the end of each chapter. These sections present
    general techniques for finding and avoiding bugs, and warnings about Python pit-
    falls.
- I added more exercises, ranging from short tests of understanding to a few substantial
    projects. And I wrote solutions for most of them.
- I added a series of case studies—longer examples with exercises, solutions, and
    discussion. Some are based on Swampy, a suite of Python programs I wrote for
    use in my classes. Swampy, code examples, and some solutions are available from
    [http://thinkpython.com.](http://thinkpython.com.)
- I expanded the discussion of program development plans and basic design patterns.
- I added appendices about debugging, analysis of algorithms, and UML diagrams
    with Lumpy.

I hope you enjoy working with this book, and that it helps you learn to program and think,
at least a little bit, like a computer scientist.

Allen B. Downey
Needham MA

Allen Downey is a Professor of Computer Science at the Franklin W. Olin College of Engi-
neering.

### Acknowledgments

Many thanks to Jeff Elkner, who translated my Java book into Python, which got this
project started and introduced me to what has turned out to be my favorite language.

Thanks also to Chris Meyers, who contributed several sections toHow to Think Like a Com-
puter Scientist.

Thanks to the Free Software Foundation for developing the GNU Free Documentation Li-
cense, which helped make my collaboration with Jeff and Chris possible, and Creative
Commons for the license I am using now.

Thanks to the editors at Lulu who worked onHow to Think Like a Computer Scientist.

Thanks to all the students who worked with earlier versions of this book and all the con-
tributors (listed below) who sent in corrections and suggestions.


```
vii
```
### Contributor List

More than 100 sharp-eyed and thoughtful readers have sent in suggestions and corrections
over the past few years. Their contributions, and enthusiasm for this project, have been a
huge help.

If you have a suggestion or correction, please send email tofeedback@thinkpython.com.
If I make a change based on your feedback, I will add you to the contributor list (unless
you ask to be omitted).

If you include at least part of the sentence the error appears in, that makes it easy for me to
search. Page and section numbers are fine, too, but not quite as easy to work with. Thanks!

- Lloyd Hugh Allen sent in a correction to Section 8.4.
- Yvon Boulianne sent in a correction of a semantic error in Chapter 5.
- Fred Bremmer submitted a correction in Section 2.1.
- Jonah Cohen wrote the Perl scripts to convert the LaTeX source for this book into beautiful
    HTML.
- Michael Conlon sent in a grammar correction in Chapter 2 and an improvement in style in
    Chapter 1, and he initiated discussion on the technical aspects of interpreters.
- Benoit Girard sent in a correction to a humorous mistake in Section 5.6.
- Courtney Gleason and Katherine Smith wrotehorsebet.py, which was used as a case study
    in an earlier version of the book. Their program can now be found on the website.
- Lee Harr submitted more corrections than we have room to list here, and indeed he should be
    listed as one of the principal editors of the text.
- James Kaylin is a student using the text. He has submitted numerous corrections.
- David Kershaw fixed the brokencatTwicefunction in Section 3.10.
- Eddie Lam has sent in numerous corrections to Chapters 1, 2, and 3. He also fixed the Makefile
    so that it creates an index the first time it is run and helped us set up a versioning scheme.
- Man-Yong Lee sent in a correction to the example code in Section 2.4.
- David Mayo pointed out that the word “unconsciously" in Chapter 1 needed to be changed to
    “subconsciously".
- Chris McAloon sent in several corrections to Sections 3.9 and 3.10.
- Matthew J. Moelter has been a long-time contributor who sent in numerous corrections and
    suggestions to the book.
- Simon Dicon Montford reported a missing function definition and several typos in Chapter 3.
    He also found errors in theincrementfunction in Chapter 13.
- John Ouzts corrected the definition of “return value" in Chapter 3.
- Kevin Parks sent in valuable comments and suggestions as to how to improve the distribution
    of the book.
- David Pool sent in a typo in the glossary of Chapter 1, as well as kind words of encouragement.
- Michael Schmitt sent in a correction to the chapter on files and exceptions.


**viii Chapter 0. Preface**

- Robin Shaw pointed out an error in Section 13.1, where the printTime function was used in an
    example without being defined.
- Paul Sleigh found an error in Chapter 7 and a bug in Jonah Cohen’s Perl script that generates
    HTML from LaTeX.
- Craig T. Snydal is testing the text in a course at Drew University. He has contributed several
    valuable suggestions and corrections.
- Ian Thomas and his students are using the text in a programming course. They are the first ones
    to test the chapters in the latter half of the book, and they have made numerous corrections and
    suggestions.
- Keith Verheyden sent in a correction in Chapter 3.
- Peter Winstanley let us know about a longstanding error in our Latin in Chapter 3.
- Chris Wrobel made corrections to the code in the chapter on file I/O and exceptions.
- Moshe Zadka has made invaluable contributions to this project. In addition to writing the first
    draft of the chapter on Dictionaries, he provided continual guidance in the early stages of the
    book.
- Christoph Zwerschke sent several corrections and pedagogic suggestions, and explained the
    difference betweengleichandselbe.
- James Mayer sent us a whole slew of spelling and typographical errors, including two in the
    contributor list.
- Hayden McAfee caught a potentially confusing inconsistency between two examples.
- Angel Arnal is part of an international team of translators working on the Spanish version of
    the text. He has also found several errors in the English version.
- Tauhidul Hoque and Lex Berezhny created the illustrations in Chapter 1 and improved many
    of the other illustrations.
- Dr. Michele Alzetta caught an error in Chapter 8 and sent some interesting pedagogic com-
    ments and suggestions about Fibonacci and Old Maid.
- Andy Mitchell caught a typo in Chapter 1 and a broken example in Chapter 2.
- Kalin Harvey suggested a clarification in Chapter 7 and caught some typos.
- Christopher P. Smith caught several typos and helped us update the book for Python 2.2.
- David Hutchins caught a typo in the Foreword.
- Gregor Lingl is teaching Python at a high school in Vienna, Austria. He is working on a Ger-
    man translation of the book, and he caught a couple of bad errors in Chapter 5.
- Julie Peters caught a typo in the Preface.
- Florin Oprina sent in an improvement inmakeTime, a correction inprintTime, and a nice typo.
- D. J. Webre suggested a clarification in Chapter 3.
- Ken found a fistful of errors in Chapters 8, 9 and 11.
- Ivo Wever caught a typo in Chapter 5 and suggested a clarification in Chapter 3.
- Curtis Yanko suggested a clarification in Chapter 2.


```
ix
```
- Ben Logan sent in a number of typos and problems with translating the book into HTML.
- Jason Armstrong saw the missing word in Chapter 2.
- Louis Cordier noticed a spot in Chapter 16 where the code didn’t match the text.
- Brian Cain suggested several clarifications in Chapters 2 and 3.
- Rob Black sent in a passel of corrections, including some changes for Python 2.2.
- Jean-Philippe Rey at Ecole Centrale Paris sent a number of patches, including some updates
    for Python 2.2 and other thoughtful improvements.
- Jason Mader at George Washington University made a number of useful suggestions and cor-
    rections.
- Jan Gundtofte-Bruun reminded us that “a error” is an error.
- Abel David and Alexis Dinno reminded us that the plural of “matrix” is “matrices”, not “ma-
    trixes”. This error was in the book for years, but two readers with the same initials reported it
    on the same day. Weird.
- Charles Thayer encouraged us to get rid of the semi-colons we had put at the ends of some
    statements and to clean up our use of “argument” and “parameter”.
- Roger Sperberg pointed out a twisted piece of logic in Chapter 3.
- Sam Bull pointed out a confusing paragraph in Chapter 2.
- Andrew Cheung pointed out two instances of “use before def.”
- C. Corey Capel spotted the missing word in the Third Theorem of Debugging and a typo in
    Chapter 4.
- Alessandra helped clear up some Turtle confusion.
- Wim Champagne found a brain-o in a dictionary example.
- Douglas Wright pointed out a problem with floor division inarc.
- Jared Spindor found some jetsam at the end of a sentence.
- Lin Peiheng sent a number of very helpful suggestions.
- Ray Hagtvedt sent in two errors and a not-quite-error.
- Torsten Hübsch pointed out an inconsistency in Swampy.
- Inga Petuhhov corrected an example in Chapter 14.
- Arne Babenhauserheide sent several helpful corrections.
- Mark E. Casida is is good at spotting repeated words.
- Scott Tyler filled in a that was missing. And then sent in a heap of corrections.
- Gordon Shephard sent in several corrections, all in separate emails.
- Andrew Turnerspotted an error in Chapter 8.
- Adam Hobart fixed a problem with floor division inarc.


**x Chapter 0. Preface**

- Daryl Hammond and Sarah Zimmerman pointed out that I served upmath.pitoo early. And
    Zim spotted a typo.
- George Sass found a bug in a Debugging section.
- Brian Bingham suggested Exercise 11.10.
- Leah Engelbert-Fenton pointed out that I usedtupleas a variable name, contrary to my own
    advice. And then found a bunch of typos and a “use before def.”
- Joe Funke spotted a typo.
- Chao-chao Chen found an inconsistency in the Fibonacci example.
- Jeff Paine knows the difference between space and spam.
- Lubos Pintes sent in a typo.
- Gregg Lind and Abigail Heithoff suggested Exercise 14.4.
- Max Hailperin has sent in a number of corrections and suggestions. Max is one of the authors
    of the extraordinaryConcrete Abstractions, which you might want to read when you are done
    with this book.
- Chotipat Pornavalai found an error in an error message.
- Stanislaw Antol sent a list of very helpful suggestions.
- Eric Pashman sent a number of corrections for Chapters 4–11.
- Miguel Azevedo found some typos.
- Jianhua Liu sent in a long list of corrections.
- Nick King found a missing word.
- Martin Zuther sent a long list of suggestions.
- Adam Zimmerman found an inconsistency in my instance of an “instance” and several other
    errors.
- Ratnakar Tiwari suggested a footnote explaining degenerate triangles.
- Anurag Goel suggested another solution foris_abecedarianand sent some additional correc-
    tions. And he knows how to spell Jane Austen.
- Kelli Kratzer spotted one of the typos.
- Mark Griffiths pointed out a confusing example in Chapter 3.
- Roydan Ongie found an error in my Newton’s method.
- Patryk Wolowiec helped me with a problem in the HTML version.
- Mark Chonofsky told me about a new keyword in Python 3.
- Russell Coleman helped me with my geometry.
- Wei Huang spotted several typographical errors.
- Karen Barber spotted the the oldest typo in the book.


```
xi
```
- Nam Nguyen found a typo and pointed out that I used the Decorator pattern but didn’t men-
    tion it by name.
- Stéphane Morin sent in several corrections and suggestions.
- Paul Stoop corrected a typo inuses_only.
- Eric Bronner pointed out a confusion in the discussion of the order of operations.
- Alexandros Gezerlis set a new standard for the number and quality of suggestions he submit-
    ted. We are deeply grateful!
- Gray Thomas knows his right from his left.
- Giovanni Escobar Sosa sent a long list of corrections and suggestions.
- Alix Etienne fixed one of the URLs.
- Kuang He found a typo.
- Daniel Neilson corrected an error about the order of operations.
- Will McGinnis pointed out thatpolylinewas defined differently in two places.
- Swarup Sahoo spotted a missing semi-colon.
- Frank Hecker pointed out an exercise that was under-specified, and some broken links.
- Animesh B helped me clean up a confusing example.
- Martin Caspersen found two round-off errors.
- Gregor Ulm sent several corrections and suggestions.
- Dimitrios Tsirigkas suggested I clarify an exercise.
- Carlos Tafur sent a page of corrections and suggestions.
- Martin Nordsletten found a bug in an exercise solution.
- Lars O.D. Christensen found a broken reference.
- Victor Simeone found a typo.
- Sven Hoexter pointed out that a variable namedinputshadows a built-in function.
- Viet Le found a typo.
- Stephen Gregory pointed out the problem withcmpin Python 3.
- Matthew Shultz let me know about a broken link.
- Lokesh Kumar Makani let me know about some broken links and some changes in error mes-
    sages.
- Ishwar Bhat corrected my statement of Fermat’s last theorem.
- Brian McGhie suggested a clarification.
- Andrea Zanella translated the book into Italian, and sent a number of corrections along the
    way.


**xii Chapter 0. Preface**


## Contents








- 1 The way of the program Preface v
   - 1.1 The Python programming language
   - 1.2 What is a program?
   - 1.3 What is debugging?
   - 1.4 Formal and natural languages
   - 1.5 The first program
   - 1.6 Debugging
   - 1.7 Glossary
   - 1.8 Exercises
- 2 Variables, expressions and statements
   - 2.1 Values and types
   - 2.2 Variables
   - 2.3 Variable names and keywords
   - 2.4 Operators and operands
   - 2.5 Expressions and statements
   - 2.6 Interactive mode and script mode
   - 2.7 Order of operations
   - 2.8 String operations
   - 2.9 Comments
   - 2.10 Debugging
   - 2.11 Glossary
   - 2.12 Exercises
- 3 Functions xiv Contents
   - 3.1 Function calls
   - 3.2 Type conversion functions
   - 3.3 Math functions
   - 3.4 Composition
   - 3.5 Adding new functions
   - 3.6 Definitions and uses
   - 3.7 Flow of execution
   - 3.8 Parameters and arguments
   - 3.9 Variables and parameters are local
   - 3.10 Stack diagrams
   - 3.11 Fruitful functions and void functions
   - 3.12 Why functions?
   - 3.13 Importing withfrom
   - 3.14 Debugging
   - 3.15 Glossary
   - 3.16 Exercises
- 4 Case study: interface design
   - 4.1 TurtleWorld
   - 4.2 Simple repetition
   - 4.3 Exercises
   - 4.4 Encapsulation
   - 4.5 Generalization
   - 4.6 Interface design
   - 4.7 Refactoring
   - 4.8 A development plan
   - 4.9 docstring
   - 4.10 Debugging
   - 4.11 Glossary
   - 4.12 Exercises
- 5 Conditionals and recursion Contents xv
   - 5.1 Modulus operator
   - 5.2 Boolean expressions
   - 5.3 Logical operators
   - 5.4 Conditional execution
   - 5.5 Alternative execution
   - 5.6 Chained conditionals
   - 5.7 Nested conditionals
   - 5.8 Recursion
   - 5.9 Stack diagrams for recursive functions
   - 5.10 Infinite recursion
   - 5.11 Keyboard input
   - 5.12 Debugging
   - 5.13 Glossary
   - 5.14 Exercises
- 6 Fruitful functions
   - 6.1 Return values
   - 6.2 Incremental development
   - 6.3 Composition
   - 6.4 Boolean functions
   - 6.5 More recursion
   - 6.6 Leap of faith
   - 6.7 One more example
   - 6.8 Checking types
   - 6.9 Debugging
   - 6.10 Glossary
   - 6.11 Exercises
- 7 Iteration xvi Contents
   - 7.1 Multiple assignment
   - 7.2 Updating variables
   - 7.3 Thewhilestatement
   - 7.4 break
   - 7.5 Square roots
   - 7.6 Algorithms
   - 7.7 Debugging
   - 7.8 Glossary
   - 7.9 Exercises
- 8 Strings
   - 8.1 A string is a sequence
   - 8.2 len
   - 8.3 Traversal with aforloop
   - 8.4 String slices
   - 8.5 Strings are immutable
   - 8.6 Searching
   - 8.7 Looping and counting
   - 8.8 String methods
   - 8.9 Theinoperator
   - 8.10 String comparison
   - 8.11 Debugging
   - 8.12 Glossary
   - 8.13 Exercises
- 9 Case study: word play
   - 9.1 Reading word lists
   - 9.2 Exercises
   - 9.3 Search
   - 9.4 Looping with indices
   - 9.5 Debugging
   - 9.6 Glossary
   - 9.7 Exercises
- 10 Lists Contents xvii
   - 10.1 A list is a sequence
   - 10.2 Lists are mutable
   - 10.3 Traversing a list
   - 10.4 List operations
   - 10.5 List slices
   - 10.6 List methods
   - 10.7 Map, filter and reduce
   - 10.8 Deleting elements
   - 10.9 Lists and strings
   - 10.10 Objects and values
   - 10.11 Aliasing
   - 10.12 List arguments
   - 10.13 Debugging
   - 10.14 Glossary
   - 10.15 Exercises
- 11 Dictionaries
   - 11.1 Dictionary as a set of counters
   - 11.2 Looping and dictionaries
   - 11.3 Reverse lookup
   - 11.4 Dictionaries and lists
   - 11.5 Memos
   - 11.6 Global variables
   - 11.7 Long integers
   - 11.8 Debugging
   - 11.9 Glossary
   - 11.10 Exercises
- 12 Tuples xviii Contents
   - 12.1 Tuples are immutable
   - 12.2 Tuple assignment
   - 12.3 Tuples as return values
   - 12.4 Variable-length argument tuples
   - 12.5 Lists and tuples
   - 12.6 Dictionaries and tuples
   - 12.7 Comparing tuples
   - 12.8 Sequences of sequences
   - 12.9 Debugging
   - 12.10 Glossary
   - 12.11 Exercises
- 13 Case study: data structure selection
   - 13.1 Word frequency analysis
   - 13.2 Random numbers
   - 13.3 Word histogram
   - 13.4 Most common words
   - 13.5 Optional parameters
   - 13.6 Dictionary subtraction
   - 13.7 Random words
   - 13.8 Markov analysis
   - 13.9 Data structures
   - 13.10 Debugging
   - 13.11 Glossary
   - 13.12 Exercises
- 14 Files
   - 14.1 Persistence
   - 14.2 Reading and writing
   - 14.3 Format operator
   - 14.4 Filenames and paths
   - 14.5 Catching exceptions Contents xix
   - 14.6 Databases
   - 14.7 Pickling
   - 14.8 Pipes
   - 14.9 Writing modules
   - 14.10 Debugging
   - 14.11 Glossary
   - 14.12 Exercises
- 15 Classes and objects
   - 15.1 User-defined types
   - 15.2 Attributes
   - 15.3 Rectangles
   - 15.4 Instances as return values
   - 15.5 Objects are mutable
   - 15.6 Copying
   - 15.7 Debugging
   - 15.8 Glossary
   - 15.9 Exercises
- 16 Classes and functions
   - 16.1 Time
   - 16.2 Pure functions
   - 16.3 Modifiers
   - 16.4 Prototyping versus planning
   - 16.5 Debugging
   - 16.6 Glossary
   - 16.7 Exercises
- 17 Classes and methods xx Contents
   - 17.1 Object-oriented features
   - 17.2 Printing objects
   - 17.3 Another example
   - 17.4 A more complicated example
   - 17.5 The init method
   - 17.6 The__str__method
   - 17.7 Operator overloading
   - 17.8 Type-based dispatch
   - 17.9 Polymorphism
   - 17.10 Debugging
   - 17.11 Interface and implementation
   - 17.12 Glossary
   - 17.13 Exercises
- 18 Inheritance
   - 18.1 Card objects
   - 18.2 Class attributes
   - 18.3 Comparing cards
   - 18.4 Decks
   - 18.5 Printing the deck
   - 18.6 Add, remove, shuffle and sort
   - 18.7 Inheritance
   - 18.8 Class diagrams
   - 18.9 Debugging
   - 18.10 Data encapsulation
   - 18.11 Glossary
   - 18.12 Exercises


**Contents xxi**

**19 Case study: Tkinter 179**

```
19.1 GUI......................................... 179
```
```
19.2 Buttons and callbacks............................... 180
```
```
19.3 Canvas widgets.................................. 181
```
```
19.4 Coordinate sequences............................... 182
```
```
19.5 More widgets................................... 182
```
```
19.6 Packing widgets.................................. 183
```
```
19.7 Menus and Callables............................... 185
```
```
19.8 Binding....................................... 186
```
```
19.9 Debugging..................................... 188
```
```
19.10 Glossary...................................... 189
```
```
19.11 Exercises...................................... 190
```
**A Debugging 193**

```
A.1 Syntax errors.................................... 193
```
```
A.2 Runtime errors................................... 195
```
```
A.3 Semantic errors.................................. 198
```
**B Analysis of Algorithms 201**

```
B.1 Order of growth.................................. 202
```
```
B.2 Analysis of basic Python operations...................... 204
```
```
B.3 Analysis of search algorithms.......................... 205
```
```
B.4 Hashtables..................................... 206
```
**C Lumpy 211**

```
C.1 State diagram................................... 211
```
```
C.2 Stack diagram................................... 212
```
```
C.3 Object diagrams.................................. 213
```
```
C.4 Function and class objects............................ 215
```
```
C.5 Class Diagrams.................................. 216
```

**xxii Contents**


## Chapter 1

# The way of the program

The goal of this book is to teach you to think like a computer scientist. This way of think-
ing combines some of the best features of mathematics, engineering, and natural science.
Like mathematicians, computer scientists use formal languages to denote ideas (specifi-
cally computations). Like engineers, they design things, assembling components into sys-
tems and evaluating tradeoffs among alternatives. Like scientists, they observe the behav-
ior of complex systems, form hypotheses, and test predictions.

The single most important skill for a computer scientist is **problem solving**. Problem solv-
ing means the ability to formulate problems, think creatively about solutions, and express
a solution clearly and accurately. As it turns out, the process of learning to program is an
excellent opportunity to practice problem-solving skills. That’s why this chapter is called,
“The way of the program.”

On one level, you will be learning to program, a useful skill by itself. On another level, you
will use programming as a means to an end. As we go along, that end will become clearer.

### 1.1 The Python programming language

The programming language you will learn is Python. Python is an example of a **high-level
language** ; other high-level languages you might have heard of are C, C++, Perl, and Java.

There are also **low-level languages** , sometimes referred to as “machine languages” or “as-
sembly languages.” Loosely speaking, computers can only run programs written in low-
level languages. So programs written in a high-level language have to be processed before
they can run. This extra processing takes some time, which is a small disadvantage of
high-level languages.

The advantages are enormous. First, it is much easier to program in a high-level language.
Programs written in a high-level language take less time to write, they are shorter and
easier to read, and they are more likely to be correct. Second, high-level languages are
**portable** , meaning that they can run on different kinds of computers with few or no modi-
fications. Low-level programs can run on only one kind of computer and have to be rewrit-
ten to run on another.


**2 Chapter 1. The way of the program**

```
SOURCE
CODE
```
```
INTERPRETER OUTPUT
```
Figure 1.1: An interpreter processes the program a little at a time, alternately reading lines
and performing computations.

```
CODE
```
```
OBJECT EXECUTOR
CODE
```
```
SOURCE COMPILER OUTPUT
```
Figure 1.2: A compiler translates source code into object code, which is run by a hardware
executor.

Due to these advantages, almost all programs are written in high-level languages. Low-
level languages are used only for a few specialized applications.

Two kinds of programs process high-level languages into low-level languages: **interpreters**
and **compilers**. An interpreter reads a high-level program and executes it, meaning that it
does what the program says. It processes the program a little at a time, alternately reading
lines and performing computations. Figure 1.1 shows the structure of an interpreter.

A compiler reads the program and translates it completely before the program starts run-
ning. In this context, the high-level program is called the **source code** , and the translated
program is called the **object code** or the **executable**. Once a program is compiled, you
can execute it repeatedly without further translation. Figure 1.2 shows the structure of a
compiler.

Python is considered an interpreted language because Python programs are executed by an
interpreter. There are two ways to use the interpreter: **interactive mode** and **script mode**.
In interactive mode, you type Python programs and the interpreter displays the result:

>>> 1 + 1
2

The chevron,>>>, is the **prompt** the interpreter uses to indicate that it is ready. If you type
1 + 1, the interpreter replies 2.

Alternatively, you can store code in a file and use the interpreter to execute the contents of
the file, which is called a **script**. By convention, Python scripts have names that end with
.py.

To execute the script, you have to tell the interpreter the name of the file. If you have a
script nameddinsdale.pyand you are working in a UNIX command window, you type
python dinsdale.py. In other development environments, the details of executing scripts
are different. You can find instructions for your environment at the Python websitehttp:
//python.org.

Working in interactive mode is convenient for testing small pieces of code because you can
type and execute them immediately. But for anything more than a few lines, you should
save your code as a script so you can modify and execute it in the future.


**1.2. What is a program? 3**

### 1.2 What is a program?

A **program** is a sequence of instructions that specifies how to perform a computation. The
computation might be something mathematical, such as solving a system of equations or
finding the roots of a polynomial, but it can also be a symbolic computation, such as search-
ing and replacing text in a document or (strangely enough) compiling a program.

The details look different in different languages, but a few basic instructions appear in just
about every language:

**input:** Get data from the keyboard, a file, or some other device.

**output:** Display data on the screen or send data to a file or other device.

**math:** Perform basic mathematical operations like addition and multiplication.

**conditional execution:** Check for certain conditions and execute the appropriate code.

**repetition:** Perform some action repeatedly, usually with some variation.

Believe it or not, that’s pretty much all there is to it. Every program you’ve ever used,
no matter how complicated, is made up of instructions that look pretty much like these.
So you can think of programming as the process of breaking a large, complex task into
smaller and smaller subtasks until the subtasks are simple enough to be performed with
one of these basic instructions.

That may be a little vague, but we will come back to this topic when we talk about **algo-
rithms**.

### 1.3 What is debugging?

Programming is error-prone. For whimsical reasons, programming errors are called **bugs**
and the process of tracking them down is called **debugging**.

Three kinds of errors can occur in a program: syntax errors, runtime errors, and semantic
errors. It is useful to distinguish between them in order to track them down more quickly.

**1.3.1 Syntax errors**

Python can only execute a program if the syntax is correct; otherwise, the interpreter dis-
plays an error message. **Syntax** refers to the structure of a program and the rules about that
structure. For example, parentheses have to come in matching pairs, so(1 + 2)is legal,
but8)is a **syntax error**.

In English, readers can tolerate most syntax errors, which is why we can read the poetry
of e. e. cummings without spewing error messages. Python is not so forgiving. If there
is a single syntax error anywhere in your program, Python will display an error message
and quit, and you will not be able to run your program. During the first few weeks of your
programming career, you will probably spend a lot of time tracking down syntax errors.
As you gain experience, you will make fewer errors and find them faster.


**4 Chapter 1. The way of the program**

**1.3.2 Runtime errors**

The second type of error is a runtime error, so called because the error does not appear until
after the program has started running. These errors are also called **exceptions** because they
usually indicate that something exceptional (and bad) has happened.

Runtime errors are rare in the simple programs you will see in the first few chapters, so it
might be a while before you encounter one.

**1.3.3 Semantic errors**

The third type of error is the **semantic error**. If there is a semantic error in your program, it
will run successfully in the sense that the computer will not generate any error messages,
but it will not do the right thing. It will do something else. Specifically, it will do what you
told it to do.

The problem is that the program you wrote is not the program you wanted to write. The
meaning of the program (its semantics) is wrong. Identifying semantic errors can be tricky
because it requires you to work backward by looking at the output of the program and
trying to figure out what it is doing.

**1.3.4 Experimental debugging**

One of the most important skills you will acquire is debugging. Although it can be frus-
trating, debugging is one of the most intellectually rich, challenging, and interesting parts
of programming.

In some ways, debugging is like detective work. You are confronted with clues, and you
have to infer the processes and events that led to the results you see.

Debugging is also like an experimental science. Once you have an idea about what is going
wrong, you modify your program and try again. If your hypothesis was correct, then you
can predict the result of the modification, and you take a step closer to a working program.
If your hypothesis was wrong, you have to come up with a new one. As Sherlock Holmes
pointed out, “When you have eliminated the impossible, whatever remains, however im-
probable, must be the truth.” (A. Conan Doyle,The Sign of Four)

For some people, programming and debugging are the same thing. That is, programming
is the process of gradually debugging a program until it does what you want. The idea is
that you should start with a program that doessomethingand make small modifications,
debugging them as you go, so that you always have a working program.

For example, Linux is an operating system that contains thousands of lines of code, but
it started out as a simple program Linus Torvalds used to explore the Intel 80386 chip.
According to Larry Greenfield, “One of Linus’s earlier projects was a program that would
switch between printing AAAA and BBBB. This later evolved to Linux.” (The Linux Users’
GuideBeta Version 1).

Later chapters will make more suggestions about debugging and other programming prac-
tices.


**1.4. Formal and natural languages 5**

### 1.4 Formal and natural languages

**Natural languages** are the languages people speak, such as English, Spanish, and French.
They were not designed by people (although people try to impose some order on them);
they evolved naturally.

**Formal languages** are languages that are designed by people for specific applications. For
example, the notation that mathematicians use is a formal language that is particularly
good at denoting relationships among numbers and symbols. Chemists use a formal lan-
guage to represent the chemical structure of molecules. And most importantly:

```
Programming languages are formal languages that have been designed to
express computations.
```
Formal languages tend to have strict rules about syntax. For example, 3+ 3 = 6 is a
syntactically correct mathematical statement, but 3+ =3$6 is not. H 2 Ois a syntactically
correct chemical formula, but 2 Zzis not.

Syntax rules come in two flavors, pertaining to **tokens** and structure. Tokens are the basic
elements of the language, such as words, numbers, and chemical elements. One of the
problems with 3+ =3$6 is that $ is not a legal token in mathematics (at least as far as I
know). Similarly, 2 Zzis not legal because there is no element with the abbreviationZz.

The second type of syntax rule pertains to the structure of a statement; that is, the way the
tokens are arranged. The statement 3+ =3 is illegal because even though+and=are
legal tokens, you can’t have one right after the other. Similarly, in a chemical formula the
subscript comes after the element name, not before.
**Exercise 1.1.** Write a well-structured English sentence with invalid tokens in it. Then write an-
other sentence with all valid tokens but with invalid structure.

When you read a sentence in English or a statement in a formal language, you have to
figure out what the structure of the sentence is (although in a natural language you do this
subconsciously). This process is called **parsing**.

For example, when you hear the sentence, “The penny dropped,” you understand that
“the penny” is the subject and “dropped” is the predicate. Once you have parsed a sen-
tence, you can figure out what it means, or the semantics of the sentence. Assuming that
you know what a penny is and what it means to drop, you will understand the general
implication of this sentence.

Although formal and natural languages have many features in common—tokens, struc-
ture, syntax, and semantics—there are some differences:

**ambiguity:** Natural languages are full of ambiguity, which people deal with by using con-
textual clues and other information. Formal languages are designed to be nearly or
completely unambiguous, which means that any statement has exactly one meaning,
regardless of context.

**redundancy:** In order to make up for ambiguity and reduce misunderstandings, natural
languages employ lots of redundancy. As a result, they are often verbose. Formal
languages are less redundant and more concise.


**6 Chapter 1. The way of the program**

**literalness:** Natural languages are full of idiom and metaphor. If I say, “The penny
dropped,” there is probably no penny and nothing dropping (this idiom means that
someone realized something after a period of confusion). Formal languages mean
exactly what they say.

People who grow up speaking a natural language—everyone—often have a hard time ad-
justing to formal languages. In some ways, the difference between formal and natural
language is like the difference between poetry and prose, but more so:

**Poetry:** Words are used for their sounds as well as for their meaning, and the whole poem
together creates an effect or emotional response. Ambiguity is not only common but
often deliberate.

**Prose:** The literal meaning of words is more important, and the structure contributes more
meaning. Prose is more amenable to analysis than poetry but still often ambiguous.

**Programs:** The meaning of a computer program is unambiguous and literal, and can be
understood entirely by analysis of the tokens and structure.

Here are some suggestions for reading programs (and other formal languages). First, re-
member that formal languages are much more dense than natural languages, so it takes
longer to read them. Also, the structure is very important, so it is usually not a good idea
to read from top to bottom, left to right. Instead, learn to parse the program in your head,
identifying the tokens and interpreting the structure. Finally, the details matter. Small er-
rors in spelling and punctuation, which you can get away with in natural languages, can
make a big difference in a formal language.

### 1.5 The first program

Traditionally, the first program you write in a new language is called “Hello, World!” be-
cause all it does is display the words “Hello, World!”. In Python, it looks like this:

print 'Hello, World!'

This is an example of a **print statement** , which doesn’t actually print anything on paper. It
displays a value on the screen. In this case, the result is the words

Hello, World!

The quotation marks in the program mark the beginning and end of the text to be dis-
played; they don’t appear in the result.

In Python 3, the syntax for printing is slightly different:

print('Hello, World!')

The parentheses indicate thatprintis a function. We’ll get to functions in Chapter 3.

For the rest of this book, I’ll use the print statement. If you are using Python 3, you will
have to translate. But other than that, there are very few differences we have to worry
about.


**1.6. Debugging 7**

### 1.6 Debugging

It is a good idea to read this book in front of a computer so you can try out the examples as
you go. You can run most of the examples in interactive mode, but if you put the code in a
script, it is easier to try out variations.

Whenever you are experimenting with a new feature, you should try to make mistakes.
For example, in the “Hello, world!” program, what happens if you leave out one of the
quotation marks? What if you leave out both? What if you spellprintwrong?

This kind of experiment helps you remember what you read; it also helps with debugging,
because you get to know what the error messages mean. It is better to make mistakes now
and on purpose than later and accidentally.

Programming, and especially debugging, sometimes brings out strong emotions. If you
are struggling with a difficult bug, you might feel angry, despondent or embarrassed.

There is evidence that people naturally respond to computers as if they were people. When
they work well, we think of them as teammates, and when they are obstinate or rude, we
respond to them the same way we respond to rude, obstinate people (Reeves and Nass,
The Media Equation: How People Treat Computers, Television, and New Media Like Real People
and Places).

Preparing for these reactions might help you deal with them. One approach is to think of
the computer as an employee with certain strengths, like speed and precision, and partic-
ular weaknesses, like lack of empathy and inability to grasp the big picture.

Your job is to be a good manager: find ways to take advantage of the strengths and mitigate
the weaknesses. And find ways to use your emotions to engage with the problem, without
letting your reactions interfere with your ability to work effectively.

Learning to debug can be frustrating, but it is a valuable skill that is useful for many ac-
tivities beyond programming. At the end of each chapter there is a debugging section, like
this one, with my thoughts about debugging. I hope they help!

### 1.7 Glossary

**problem solving:** The process of formulating a problem, finding a solution, and express-
ing the solution.

**high-level language:** A programming language like Python that is designed to be easy for
humans to read and write.

**low-level language:** A programming language that is designed to be easy for a computer
to execute; also called “machine language” or “assembly language.”

**portability:** A property of a program that can run on more than one kind of computer.

**interpret:** To execute a program in a high-level language by translating it one line at a time.

**compile:** To translate a program written in a high-level language into a low-level language
all at once, in preparation for later execution.


**8 Chapter 1. The way of the program**

**source code:** A program in a high-level language before being compiled.

**object code:** The output of the compiler after it translates the program.

**executable:** Another name for object code that is ready to be executed.

**prompt:** Characters displayed by the interpreter to indicate that it is ready to take input
from the user.

**script:** A program stored in a file (usually one that will be interpreted).

**interactive mode:** A way of using the Python interpreter by typing commands and expres-
sions at the prompt.

**script mode:** A way of using the Python interpreter to read and execute statements in a
script.

**program:** A set of instructions that specifies a computation.

**algorithm:** A general process for solving a category of problems.

**bug:** An error in a program.

**debugging:** The process of finding and removing any of the three kinds of programming
errors.

**syntax:** The structure of a program.

**syntax error:** An error in a program that makes it impossible to parse (and therefore im-
possible to interpret).

**exception:** An error that is detected while the program is running.

**semantics:** The meaning of a program.

**semantic error:** An error in a program that makes it do something other than what the
programmer intended.

**natural language:** Any one of the languages that people speak that evolved naturally.

**formal language:** Any one of the languages that people have designed for specific pur-
poses, such as representing mathematical ideas or computer programs; all program-
ming languages are formal languages.

**token:** One of the basic elements of the syntactic structure of a program, analogous to a
word in a natural language.

**parse:** To examine a program and analyze the syntactic structure.

**print statement:** An instruction that causes the Python interpreter to display a value on
the screen.


**1.8. Exercises 9**

### 1.8 Exercises

**Exercise 1.2.** Use a web browser to go to the Python websitehttp: // python. org. This page
contains information about Python and links to Python-related pages, and it gives you the ability to
search the Python documentation.

For example, if you enterprintin the search window, the first link that appears is the documenta-
tion of theprintstatement. At this point, not all of it will make sense to you, but it is good to know
where it is.
**Exercise 1.3.** Start the Python interpreter and typehelp()to start the online help utility. Or you
can typehelp('print')to get information about theprintstatement.

If this example doesn’t work, you may need to install additional Python documentation or set an
environment variable; the details depend on your operating system and version of Python.
**Exercise 1.4.** Start the Python interpreter and use it as a calculator. Python’s syntax for math
operations is almost the same as standard mathematical notation. For example, the symbols+,-and
/denote addition, subtraction and division, as you would expect. The symbol for multiplication is
*.

If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What
is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).


**10 Chapter 1. The way of the program**


## Chapter 2

# Variables, expressions and

# statements

### 2.1 Values and types

A **value** is one of the basic things a program works with, like a letter or a number. The
values we have seen so far are 1 , 2 , and'Hello, World!'.

These values belong to different **types** : 2 is an integer, and'Hello, World!'is a **string** ,
so-called because it contains a “string” of letters. You (and the interpreter) can identify
strings because they are enclosed in quotation marks.

If you are not sure what type a value has, the interpreter can tell you.

>>> type('Hello, World!')
<type'str'>
>>> type(17)
<type'int'>

Not surprisingly, strings belong to the typestrand integers belong to the typeint. Less
obviously, numbers with a decimal point belong to a type calledfloat, because these num-
bers are represented in a format called **floating-point**.

>>> type(3.2)
<type'float'>

What about values like' 17 'and'3.2'? They look like numbers, but they are in quotation
marks like strings.

>>> type(' 17 ')
<type'str'>
>>> type('3.2')
<type'str'>

They’re strings.

When you type a large integer, you might be tempted to use commas between groups of
three digits, as in1,000,000. This is not a legal integer in Python, but it is legal:


**12 Chapter 2. Variables, expressions and statements**

```
message
n
pi
```
```
17
```
```
’And now for something completely different’
```
```
3.1415926535897932
```
```
Figure 2.1: State diagram.
```
#### >>> 1,000,000

#### (1, 0, 0)

Well, that’s not what we expected at all! Python interprets1,000,000as a comma-
separated sequence of integers. This is the first example we have seen of a semantic error:
the code runs without producing an error message, but it doesn’t do the “right” thing.

### 2.2 Variables

One of the most powerful features of a programming language is the ability to manipulate
**variables**. A variable is a name that refers to a value.

An **assignment statement** creates new variables and gives them values:

>>> message = 'And now for something completely different'
>>> n = 17
>>> pi = 3.1415926535897932

This example makes three assignments. The first assigns a string to a new variable named
message; the second gives the integer 17 ton; the third assigns the (approximate) value of
_π_ topi.

A common way to represent variables on paper is to write the name with an arrow pointing
to the variable’s value. This kind of figure is called a **state diagram** because it shows what
state each of the variables is in (think of it as the variable’s state of mind). Figure 2.1 shows
the result of the previous example.

The type of a variable is the type of the value it refers to.

>>> type(message)
<type 'str'>
>>> type(n)
<type 'int'>
>>> type(pi)
<type 'float'>

### 2.3 Variable names and keywords

Programmers generally choose names for their variables that are meaningful—they docu-
ment what the variable is used for.

Variable names can be arbitrarily long. They can contain both letters and numbers, but
they have to begin with a letter. It is legal to use uppercase letters, but it is a good idea to
begin variable names with a lowercase letter (you’ll see why later).


**2.4. Operators and operands 13**

The underscore character,_, can appear in a name. It is often used in names with multiple
words, such asmy_nameorairspeed_of_unladen_swallow.

If you give a variable an illegal name, you get a syntax error:

>>> 76trombones ='big parade'
SyntaxError: invalid syntax
>>> more@ = 1000000
SyntaxError: invalid syntax
>>> class ='Advanced Theoretical Zymurgy'
SyntaxError: invalid syntax

76trombonesis illegal because it does not begin with a letter.more@is illegal because it
contains an illegal character,@. But what’s wrong withclass?

It turns out thatclassis one of Python’s **keywords**. The interpreter uses keywords to
recognize the structure of the program, and they cannot be used as variable names.

Python 2 has 31 keywords:

and del from not while
as elif global or with
assert else if pass yield
break except import print
class exec in raise
continue finally is return
def for lambda try

In Python 3,execis no longer a keyword, butnonlocalis.

You might want to keep this list handy. If the interpreter complains about one of your
variable names and you don’t know why, see if it is on this list.

## 2.4 Operators and operands

**Operators** are special symbols that represent computations like addition and multiplica-
tion. The values the operator is applied to are called **operands**.

The operators `+,-,*,/` and `**`* perform addition, subtraction, multiplication, division and exponentiation, as in the following examples:

```20 + 32 hour - 1 hour* 60 + minute minute/60 5**2 (5+9)*(15-7)```

In some other languages, `^`is used for exponentiation, but in Python it is a bitwise operator called `XOR`. I won’t cover bitwise operators in this book, but you can read about them at
[http://wiki.python.org/moin/BitwiseOperators](http://wiki.python.org/moin/BitwiseOperators)

In Python 2, the division operator might not do what you expect:

>>> minute = 59
>>> minute/60
0

The value ofminuteis 59, and in conventional arithmetic 59 divided by 60 is 0.98333, not 0. The reason for the discrepancy is that Python is performing **floor division**. When both of the operands are integers, the result is also an integer; floor division chops off the fraction part, so in this example it rounds down to zero.


**14 Chapter 2. Variables, expressions and statements**

In Python 3, the result of this division is afloat. The new operator//performs floor
division.

If either of the operands is a floating-point number, Python performs floating-point divi-
sion, and the result is afloat:

>>> minute/60.0
0.98333333333333328

### 2.5 Expressions and statements

An **expression** is a combination of values, variables, and operators. A value all by itself
is considered an expression, and so is a variable, so the following are all legal expressions
(assuming that the variablexhas been assigned a value):

17
x
x + 17

A **statement** is a unit of code that the Python interpreter can execute. We have seen two
kinds of statement: print and assignment.

Technically an expression is also a statement, but it is probably simpler to think of them
as different things. The important difference is that an expression has a value; a statement
does not.

### 2.6 Interactive mode and script mode

One of the benefits of working with an interpreted language is that you can test bits of
code in interactive mode before you put them in a script. But there are differences between
interactive mode and script mode that can be confusing.

For example, if you are using Python as a calculator, you might type

>>> miles = 26.2
>>> miles * 1.61
42.182

The first line assigns a value tomiles, but it has no visible effect. The second line is an ex-
pression, so the interpreter evaluates it and displays the result. So we learn that a marathon
is about 42 kilometers.

But if you type the same code into a script and run it, you get no output at all. In script
mode an expression, all by itself, has no visible effect. Python actually evaluates the ex-
pression, but it doesn’t display the value unless you tell it to:

miles = 26.2
print miles * 1.61

This behavior can be confusing at first.

A script usually contains a sequence of statements. If there is more than one statement, the
results appear one at a time as the statements execute.

For example, the script


**2.7. Order of operations 15**

print 1
x = 2
print x

produces the output

1
2

The assignment statement produces no output.
**Exercise 2.1.** Type the following statements in the Python interpreter to see what they do:

5
x = 5
x + 1

Now put the same statements into a script and run it. What is the output? Modify the script by
transforming each expression into a print statement and then run it again.

### 2.7 Order of operations

When more than one operator appears in an expression, the order of evaluation depends
on the **rules of precedence**. For mathematical operators, Python follows mathematical
convention. The acronym **PEMDAS** is a useful way to remember the rules:

- **P** arentheses have the highest precedence and can be used to force an expression to
    evaluate in the order you want. Since expressions in parentheses are evaluated first,
    2 * (3-1)is 4, and(1+1)**(5-2)is 8. You can also use parentheses to make an
    expression easier to read, as in(minute * 100) / 60, even if it doesn’t change the
    result.
- **E** xponentiation has the next highest precedence, so2**1+1is 3, not 4, and3*1**3is
    3, not 27.
- **M** ultiplication and **D** ivision have the same precedence, which is higher than
    **A** ddition and **S** ubtraction, which also have the same precedence. So2*3-1is 5, not
    4, and6+4/2is 8, not 5.
- Operators with the same precedence are evaluated from left to right (except exponen-
    tiation). So in the expressiondegrees / 2 * pi, the division happens first and the
    result is multiplied bypi. To divide by 2 _π_ , you can use parentheses or writedegrees
    / 2 / pi.

I don’t work very hard to remember rules of precedence for other operators. If I can’t tell
by looking at the expression, I use parentheses to make it obvious.

### 2.8 String operations

In general, you can’t perform mathematical operations on strings, even if the strings look
like numbers, so the following are illegal:

' 2 '-' 1 ''eggs'/'easy''third'*'a charm'


**16 Chapter 2. Variables, expressions and statements**

The+operator works with strings, but it might not do what you expect: it performs **con-
catenation** , which means joining the strings by linking them end-to-end. For example:

first ='throat'
second ='warbler'
print first + second

The output of this program isthroatwarbler.

The*operator also works on strings; it performs repetition. For example,'Spam'*3is
'SpamSpamSpam'. If one of the operands is a string, the other has to be an integer.

This use of+and*makes sense by analogy with addition and multiplication. Just as4*3
is equivalent to4+4+4, we expect'Spam'*3to be the same as'Spam'+'Spam'+'Spam', and
it is. On the other hand, there is a significant way in which string concatenation and repe-
tition are different from integer addition and multiplication. Can you think of a property
that addition has that string concatenation does not?

### 2.9 Comments

As programs get bigger and more complicated, they get more difficult to read. Formal
languages are dense, and it is often difficult to look at a piece of code and figure out what
it is doing, or why.

For this reason, it is a good idea to add notes to your programs to explain in natural lan-
guage what the program is doing. These notes are called **comments** , and they start with
the#symbol:

# compute the percentage of the hour that has elapsed
percentage = (minute * 100) / 60

In this case, the comment appears on a line by itself. You can also put comments at the end
of a line:

percentage = (minute * 100) / 60 # percentage of an hour

Everything from the#to the end of the line is ignored—it has no effect on the program.

Comments are most useful when they document non-obvious features of the code. It is
reasonable to assume that the reader can figure outwhatthe code does; it is much more
useful to explainwhy.

This comment is redundant with the code and useless:

v = 5 # assign 5 to v

This comment contains useful information that is not in the code:

v = 5 # velocity in meters/second.

Good variable names can reduce the need for comments, but long names can make com-
plex expressions hard to read, so there is a tradeoff.

### 2.10 Debugging

At this point the syntax error you are most likely to make is an illegal variable name, like
classandyield, which are keywords, orodd~jobandUS$, which contain illegal charac-
ters.


**2.11. Glossary 17**

If you put a space in a variable name, Python thinks it is two operands without an operator:

>>> bad name = 5
SyntaxError: invalid syntax

For syntax errors, the error messages don’t help much. The most common messages are
SyntaxError: invalid syntaxandSyntaxError: invalid token, neither of which is
very informative.

The runtime error you are most likely to make is a “use before def;” that is, trying to use
a variable before you have assigned a value. This can happen if you spell a variable name
wrong:

>>> principal = 327.68
>>> interest = principle * rate
NameError: name'principle'is not defined

Variables names are case sensitive, soLaTeXis not the same aslatex.

At this point the most likely cause of a semantic error is the order of operations. For exam-
ple, to evaluate 21 _π_ , you might be tempted to write

>>> 1.0 / 2.0 * pi

But the division happens first, so you would get _π_ /2, which is not the same thing! There is
no way for Python to know what you meant to write, so in this case you don’t get an error
message; you just get the wrong answer.

### 2.11 Glossary

**value:** One of the basic units of data, like a number or string, that a program manipulates.

**type:** A category of values. The types we have seen so far are integers (typeint), floating-
point numbers (typefloat), and strings (typestr).

**integer:** A type that represents whole numbers.

**floating-point:** A type that represents numbers with fractional parts.

**string:** A type that represents sequences of characters.

**variable:** A name that refers to a value.

**statement:** A section of code that represents a command or action. So far, the statements
we have seen are assignments and print statements.

**assignment:** A statement that assigns a value to a variable.

**state diagram:** A graphical representation of a set of variables and the values they refer to.

**keyword:** A reserved word that is used by the compiler to parse a program; you cannot
use keywords likeif,def, andwhileas variable names.

**operator:** A special symbol that represents a simple computation like addition, multipli-
cation, or string concatenation.


**18 Chapter 2. Variables, expressions and statements**

**operand:** One of the values on which an operator operates.

**floor division:** The operation that divides two numbers and chops off the fraction part.

**expression:** A combination of variables, operators, and values that represents a single re-
sult value.

**evaluate:** To simplify an expression by performing the operations in order to yield a single
value.

**rules of precedence:** The set of rules governing the order in which expressions involving
multiple operators and operands are evaluated.

**concatenate:** To join two operands end-to-end.

**comment:** Information in a program that is meant for other programmers (or anyone read-
ing the source code) and has no effect on the execution of the program.

### 2.12 Exercises

**Exercise 2.2.** Assume that we execute the following assignment statements:

width = 17
height = 12.0
delimiter ='.'

For each of the following expressions, write the value of the expression and the type (of the value of
the expression).

```
1.width/2
```
```
2.width/2.0
```
```
3.height/3
```
```
4.1 + 2 * 5
```
```
5.delimiter * 5
```
Use the Python interpreter to check your answers.
**Exercise 2.3.** Practice using the Python interpreter as a calculator:

1. The volume of a sphere with radius r is^43 _π_ r^3. What is the volume of a sphere with radius 5?
    Hint: 392.7 is wrong!
2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
    $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
    60 copies?
3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
    tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?


## Chapter 3

# Functions

### 3.1 Function calls

In the context of programming, a **function** is a named sequence of statements that performs
a computation. When you define a function, you specify the name and the sequence of
statements. Later, you can “call” the function by name. We have already seen one example
of a **function call** :

>>> type(32)
<type'int'>

The name of the function istype. The expression in parentheses is called the **argument** of
the function. The result, for this function, is the type of the argument.

It is common to say that a function “takes” an argument and “returns” a result. The result
is called the **return value**.

### 3.2 Type conversion functions

Python provides built-in functions that convert values from one type to another. Theint
function takes any value and converts it to an integer, if it can, or complains otherwise:

>>> int(' 32 ')
32
>>> int('Hello')
ValueError: invalid literal for int(): Hello

intcan convert floating-point values to integers, but it doesn’t round off; it chops off the
fraction part:

>>> int(3.99999)
3
>>> int(-2.3)
-2

floatconverts integers and strings to floating-point numbers:


**20 Chapter 3. Functions**

>>> float(32)
32.0
>>> float('3.14159')
3.14159

Finally,strconverts its argument to a string:

>>> str(32)
' 32 '
>>> str(3.14159)
'3.14159'

### 3.3 Math functions

Python has a math module that provides most of the familiar mathematical functions. A
**module** is a file that contains a collection of related functions.

Before we can use the module, we have to import it:

>>> import math

This statement creates a **module object** named math. If you print the module object, you
get some information about it:

>>> print math
<module'math' (built-in)>

The module object contains the functions and variables defined in the module. To access
one of the functions, you have to specify the name of the module and the name of the
function, separated by a dot (also known as a period). This format is called **dot notation**.

>>> ratio = signal_power / noise_power
>>> decibels = 10 * math.log10(ratio)

>>> radians = 0.7
>>> height = math.sin(radians)

The first example useslog10to compute a signal-to-noise ratio in decibels (assuming that
signal_powerandnoise_powerare defined). The math module also provideslog, which
computes logarithms basee.

The second example finds the sine ofradians. The name of the variable is a hint thatsin
and the other trigonometric functions (cos,tan, etc.) take arguments in radians. To convert
from degrees to radians, divide by 360 and multiply by 2 _π_ :

>>> degrees = 45
>>> radians = degrees / 360.0 * 2 * math.pi
>>> math.sin(radians)
0.707106781187

The expressionmath.pigets the variablepifrom the math module. The value of this
variable is an approximation of _π_ , accurate to about 15 digits.

If you know your trigonometry, you can check the previous result by comparing it to the
square root of two divided by two:

>>> math.sqrt(2) / 2.0
0.707106781187


**3.4. Composition 21**

### 3.4 Composition

So far, we have looked at the elements of a program—variables, expressions, and
statements—in isolation, without talking about how to combine them.

One of the most useful features of programming languages is their ability to take small
building blocks and **compose** them. For example, the argument of a function can be any
kind of expression, including arithmetic operators:

x = math.sin(degrees / 360.0 * 2 * math.pi)

And even function calls:

x = math.exp(math.log(x+1))

Almost anywhere you can put a value, you can put an arbitrary expression, with one ex-
ception: the left side of an assignment statement has to be a variable name. Any other
expression on the left side is a syntax error (we will see exceptions to this rule later).

>>> minutes = hours * 60 # right
>>> hours * 60 = minutes # wrong!
SyntaxError: can't assign to operator

### 3.5 Adding new functions

So far, we have only been using the functions that come with Python, but it is also possible
to add new functions. A **function definition** specifies the name of a new function and the
sequence of statements that execute when the function is called.

Here is an example:

def print_lyrics():
print "I'm a lumberjack, and I'm okay."
print "I sleep all night and I work all day."

defis a keyword that indicates that this is a function definition. The name of the function
isprint_lyrics. The rules for function names are the same as for variable names: letters,
numbers and some punctuation marks are legal, but the first character can’t be a number.
You can’t use a keyword as the name of a function, and you should avoid having a variable
and a function with the same name.

The empty parentheses after the name indicate that this function doesn’t take any argu-
ments.

The first line of the function definition is called the **header** ; the rest is called the **body**.
The header has to end with a colon and the body has to be indented. By convention, the
indentation is always four spaces (see Section 3.14). The body can contain any number of
statements.

The strings in the print statements are enclosed in double quotes. Single quotes and double
quotes do the same thing; most people use single quotes except in cases like this where a
single quote (which is also an apostrophe) appears in the string.

If you type a function definition in interactive mode, the interpreter prints ellipses (...) to
let you know that the definition isn’t complete:


**22 Chapter 3. Functions**

>>> def print_lyrics():
... print "I'm a lumberjack, and I'm okay."
... print "I sleep all night and I work all day."

To end the function, you have to enter an empty line (this is not necessary in a script).

Defining a function creates a variable with the same name.

>>> print print_lyrics
<function print_lyrics at 0xb7e99e9c>
>>> type(print_lyrics)
<type 'function'>

The value ofprint_lyricsis a **function object** , which has type'function'.

The syntax for calling the new function is the same as for built-in functions:

>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.

Once you have defined a function, you can use it inside another function. For example, to
repeat the previous refrain, we could write a function calledrepeat_lyrics:

def repeat_lyrics():
print_lyrics()
print_lyrics()

And then callrepeat_lyrics:

>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.

But that’s not really how the song goes.

### 3.6 Definitions and uses

Pulling together the code fragments from the previous section, the whole program looks
like this:

def print_lyrics():
print "I'm a lumberjack, and I'm okay."
print "I sleep all night and I work all day."

def repeat_lyrics():
print_lyrics()
print_lyrics()

repeat_lyrics()

This program contains two function definitions:print_lyricsandrepeat_lyrics. Func-
tion definitions get executed just like other statements, but the effect is to create function
objects. The statements inside the function do not get executed until the function is called,
and the function definition generates no output.


**3.7. Flow of execution 23**

As you might expect, you have to create a function before you can execute it. In other
words, the function definition has to be executed before the first time it is called.
**Exercise 3.1.** Move the last line of this program to the top, so the function call appears before the
definitions. Run the program and see what error message you get.
**Exercise 3.2.** Move the function call back to the bottom and move the definition ofprint_lyrics
after the definition ofrepeat_lyrics. What happens when you run this program?

### 3.7 Flow of execution

In order to ensure that a function is defined before its first use, you have to know the order
in which statements are executed, which is called the **flow of execution**.

Execution always begins at the first statement of the program. Statements are executed one
at a time, in order from top to bottom.

Function definitions do not alter the flow of execution of the program, but remember that
statements inside the function are not executed until the function is called.

A function call is like a detour in the flow of execution. Instead of going to the next state-
ment, the flow jumps to the body of the function, executes all the statements there, and
then comes back to pick up where it left off.

That sounds simple enough, until you remember that one function can call another. While
in the middle of one function, the program might have to execute the statements in another
function. But while executing that new function, the program might have to execute yet
another function!

Fortunately, Python is good at keeping track of where it is, so each time a function com-
pletes, the program picks up where it left off in the function that called it. When it gets to
the end of the program, it terminates.

What’s the moral of this sordid tale? When you read a program, you don’t always want
to read from top to bottom. Sometimes it makes more sense if you follow the flow of
execution.

### 3.8 Parameters and arguments

Some of the built-in functions we have seen require arguments. For example, when you
callmath.sinyou pass a number as an argument. Some functions take more than one
argument:math.powtakes two, the base and the exponent.

Inside the function, the arguments are assigned to variables called **parameters**. Here is an
example of a user-defined function that takes an argument:

def print_twice(bruce):
print bruce
print bruce

This function assigns the argument to a parameter namedbruce. When the function is
called, it prints the value of the parameter (whatever it is) twice.

This function works with any value that can be printed.


**24 Chapter 3. Functions**

>>> print_twice('Spam')
Spam
Spam
>>> print_twice(17)
17
17
>>> print_twice(math.pi)
3.14159265359
3.14159265359

The same rules of composition that apply to built-in functions also apply to user-defined
functions, so we can use any kind of expression as an argument forprint_twice:

>>> print_twice('Spam'*4)
Spam Spam Spam Spam
Spam Spam Spam Spam
>>> print_twice(math.cos(math.pi))
-1.0
-1.0

The argument is evaluated before the function is called, so in the examples the expressions
'Spam'*4andmath.cos(math.pi)are only evaluated once.

You can also use a variable as an argument:

>>> michael = 'Eric, the half a bee.'
>>> print_twice(michael)
Eric, the half a bee.
Eric, the half a bee.

The name of the variable we pass as an argument (michael) has nothing to do with the
name of the parameter (bruce). It doesn’t matter what the value was called back home (in
the caller); here inprint_twice, we call everybodybruce.

### 3.9 Variables and parameters are local

When you create a variable inside a function, it is **local** , which means that it only exists
inside the function. For example:

def cat_twice(part1, part2):
cat = part1 + part2
print_twice(cat)

This function takes two arguments, concatenates them, and prints the result twice. Here is
an example that uses it:

>>> line1 ='Bing tiddle'
>>> line2 ='tiddle bang.'
>>> cat_twice(line1, line2)
Bing tiddle tiddle bang.
Bing tiddle tiddle bang.

Whencat_twiceterminates, the variablecatis destroyed. If we try to print it, we get an
exception:

>>> print cat
NameError: name 'cat'is not defined


**3.10. Stack diagrams 25**

```
line1
line2 ’tiddle bang.’
```
```
part1
part2
cat
```
```
bruce
```
```
’Bing tiddle ’
```
```
’Bing tiddle ’
’tiddle bang.’
’Bing tiddle tiddle bang.’
```
```
’Bing tiddle tiddle bang.’
```
```
<module>
```
```
cat_twice
```
```
print_twice
```
```
Figure 3.1: Stack diagram.
```
Parameters are also local. For example, outsideprint_twice, there is no such thing as
bruce.

### 3.10 Stack diagrams

To keep track of which variables can be used where, it is sometimes useful to draw a **stack
diagram**. Like state diagrams, stack diagrams show the value of each variable, but they
also show the function each variable belongs to.

Each function is represented by a **frame**. A frame is a box with the name of a function
beside it and the parameters and variables of the function inside it. The stack diagram for
the previous example is shown in Figure 3.1.

The frames are arranged in a stack that indicates which function called which, and so
on. In this example,print_twicewas called bycat_twice, andcat_twicewas called
by__main__, which is a special name for the topmost frame. When you create a variable
outside of any function, it belongs to__main__.

Each parameter refers to the same value as its corresponding argument. So,part1has the
same value asline1,part2has the same value asline2, andbrucehas the same value as
cat.

If an error occurs during a function call, Python prints the name of the function, and the
name of the function that called it, and the name of the function that calledthat, all the way
back to__main__.

For example, if you try to accesscatfrom withinprint_twice, you get aNameError:

Traceback (innermost last):
File "test.py", line 13, in __main__
cat_twice(line1, line2)
File "test.py", line 5, in cat_twice
print_twice(cat)
File "test.py", line 9, in print_twice
print cat
NameError: name'cat' is not defined

This list of functions is called a **traceback**. It tells you what program file the error occurred
in, and what line, and what functions were executing at the time. It also shows the line of
code that caused the error.


**26 Chapter 3. Functions**

The order of the functions in the traceback is the same as the order of the frames in the
stack diagram. The function that is currently running is at the bottom.

### 3.11 Fruitful functions and void functions

Some of the functions we are using, such as the math functions, yield results; for lack of a
better name, I call them **fruitful functions**. Other functions, likeprint_twice, perform an
action but don’t return a value. They are called **void functions**.

When you call a fruitful function, you almost always want to do something with the result;
for example, you might assign it to a variable or use it as part of an expression:

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

When you call a function in interactive mode, Python displays the result:

>>> math.sqrt(5)
2.2360679774997898

But in a script, if you call a fruitful function all by itself, the return value is lost forever!

math.sqrt(5)

This script computes the square root of 5, but since it doesn’t store or display the result, it
is not very useful.

Void functions might display something on the screen or have some other effect, but they
don’t have a return value. If you try to assign the result to a variable, you get a special
value calledNone.

>>> result = print_twice('Bing')
Bing
Bing
>>> print result
None

The valueNoneis not the same as the string'None'. It is a special value that has its own
type:

>>> print type(None)
<type 'NoneType'>

The functions we have written so far are all void. We will start writing fruitful functions in
a few chapters.

### 3.12 Why functions?

It may not be clear why it is worth the trouble to divide a program into functions. There
are several reasons:

- Creating a new function gives you an opportunity to name a group of statements,
    which makes your program easier to read and debug.
- Functions can make a program smaller by eliminating repetitive code. Later, if you
    make a change, you only have to make it in one place.


**3.13. Importing with** from **27**

- Dividing a long program into functions allows you to debug the parts one at a time
    and then assemble them into a working whole.
- Well-designed functions are often useful for many programs. Once you write and
    debug one, you can reuse it.

### 3.13 Importing withfrom

Python provides two ways to import modules; we have already seen one:

>>> import math
>>> print math
<module'math'(built-in)>
>>> print math.pi
3.14159265359

If you importmath, you get a module object namedmath. The module object contains
constants likepiand functions likesinandexp.

But if you try to accesspidirectly, you get an error.

>>> print pi
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name'pi'is not defined

As an alternative, you can import an object from a module like this:

>>> from math import pi

Now you can accesspidirectly, without dot notation.

>>> print pi
3.14159265359

Or you can use the star operator to importeverythingfrom the module:

>>> from math import *
>>> cos(pi)
-1.0

The advantage of importing everything from the math module is that your code can be
more concise. The disadvantage is that there might be conflicts between names defined in
different modules, or between a name from a module and one of your variables.

### 3.14 Debugging

If you are using a text editor to write your scripts, you might run into problems with spaces
and tabs. The best way to avoid these problems is to use spaces exclusively (no tabs). Most
text editors that know about Python do this by default, but some don’t.

Tabs and spaces are usually invisible, which makes them hard to debug, so try to find an
editor that manages indentation for you.

Also, don’t forget to save your program before you run it. Some development environ-
ments do this automatically, but some don’t. In that case the program you are looking at in
the text editor is not the same as the program you are running.


**28 Chapter 3. Functions**

Debugging can take a long time if you keep running the same, incorrect, program over and
over!

Make sure that the code you are looking at is the code you are running. If you’re not sure,
put something likeprint'hello'at the beginning of the program and run it again. If you
don’t seehello, you’re not running the right program!

### 3.15 Glossary

**function:** A named sequence of statements that performs some useful operation. Func-
tions may or may not take arguments and may or may not produce a result.

**function definition:** A statement that creates a new function, specifying its name, param-
eters, and the statements it executes.

**function object:** A value created by a function definition. The name of the function is a
variable that refers to a function object.

**header:** The first line of a function definition.

**body:** The sequence of statements inside a function definition.

**parameter:** A name used inside a function to refer to the value passed as an argument.

**function call:** A statement that executes a function. It consists of the function name fol-
lowed by an argument list.

**argument:** A value provided to a function when the function is called. This value is as-
signed to the corresponding parameter in the function.

**local variable:** A variable defined inside a function. A local variable can only be used
inside its function.

**return value:** The result of a function. If a function call is used as an expression, the return
value is the value of the expression.

**fruitful function:** A function that returns a value.

**void function:** A function that doesn’t return a value.

**module:** A file that contains a collection of related functions and other definitions.

**import statement:** A statement that reads a module file and creates a module object.

**module object:** A value created by animportstatement that provides access to the values
defined in a module.

**dot notation:** The syntax for calling a function in another module by specifying the mod-
ule name followed by a dot (period) and the function name.

**composition:** Using an expression as part of a larger expression, or a statement as part of
a larger statement.

**flow of execution:** The order in which statements are executed during a program run.


**3.16. Exercises 29**

**stack diagram:** A graphical representation of a stack of functions, their variables, and the
values they refer to.

**frame:** A box in a stack diagram that represents a function call. It contains the local vari-
ables and parameters of the function.

**traceback:** A list of the functions that are executing, printed when an exception occurs.

### 3.16 Exercises

**Exercise 3.3.** Python provides a built-in function calledlenthat returns the length of a string, so
the value oflen('allen')is 5.

Write a function namedright_justifythat takes a string namedsas a parameter and prints the
string with enough leading spaces so that the last letter of the string is in column 70 of the display.

>>> right_justify('allen')
allen
**Exercise 3.4.** A function object is a value you can assign to a variable or pass as an argument. For
example,do_twiceis a function that takes a function object as an argument and calls it twice:

def do_twice(f):
f()
f()

Here’s an example that usesdo_twiceto call a function namedprint_spamtwice.

def print_spam():
print'spam'

do_twice(print_spam)

1. Type this example into a script and test it.
2. Modifydo_twiceso that it takes two arguments, a function object and a value, and calls the
    function twice, passing the value as an argument.
3. Write a more general version ofprint_spam, calledprint_twice, that takes a string as a
    parameter and prints it twice.
4. Use the modified version ofdo_twiceto callprint_twicetwice, passing'spam'as an
    argument.
5. Define a new function calleddo_fourthat takes a function object and a value and calls the
    function four times, passing the value as a parameter. There should be only two statements in
    the body of this function, not four.

Solution:http: // thinkpython. com/ code/ do_ four. py.
**Exercise 3.5.** This exercise can be done using only the statements and other features we have learned
so far.

1. Write a function that draws a grid like the following:


**30 Chapter 3. Functions**

#### + - - - - + - - - - +

#### | | |

#### | | |

#### | | |

#### | | |

#### + - - - - + - - - - +

#### | | |

#### | | |

#### | | |

#### | | |

#### + - - - - + - - - - +

```
Hint: to print more than one value on a line, you can print a comma-separated sequence:
```
```
print '+', '-'
```
```
If the sequence ends with a comma, Python leaves the line unfinished, so the value printed
next appears on the same line.
```
```
print '+',
print '-'
```
```
The output of these statements is'+ -'.
Aprintstatement all by itself ends the current line and goes to the next line.
```
2. Write a function that draws a similar grid with four rows and four columns.

Solution: [http:](http:) // thinkpython. com/ code/ grid. py. Credit: This exercise is based on an
exercise in Oualline,Practical C Programming, Third Edition, O’Reilly Media, 1997.


## Chapter 4

# Case study: interface design

Code examples from this chapter are available fromhttp://thinkpython.com/code/
polygon.py.

### 4.1 TurtleWorld

To accompany this book, I have written a package called Swampy. You can download
Swampy fromhttp://thinkpython.com/swampy; follow the instructions there to install
Swampy on your system.

A **package** is a collection of modules; one of the modules in Swampy isTurtleWorld,
which provides a set of functions for drawing lines by steering turtles around the screen.

If Swampy is installed as a package on your system, you can importTurtleWorldlike this:

from swampy.TurtleWorld import *

If you downloaded the Swampy modules but did not install them as a package, you can ei-
ther work in the directory that contains the Swampy files, or add that directory to Python’s
search path. Then you can importTurtleWorldlike this:

from TurtleWorld import *

The details of the installation process and setting Python’s search path depend on your
system, so rather than include those details here, I will try to maintain current information
for several systems athttp://thinkpython.com/swampy

Create a file namedmypolygon.pyand type in the following code:

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

wait_for_user()


**32 Chapter 4. Case study: interface design**

The first line imports everything from theTurtleWorldmodule in theswampypackage.

The next lines create a TurtleWorld assigned toworldand a Turtle assigned tobob. Printing
bobyields something like:

<TurtleWorld.Turtle instance at 0xb7bfbf4c>

This means thatbobrefers to an **instance** of a Turtle as defined in moduleTurtleWorld.
In this context, “instance” means a member of a set; this Turtle is one of the set of possible
Turtles.

wait_for_usertells TurtleWorld to wait for the user to do something, although in this case
there’s not much for the user to do except close the window.

TurtleWorld provides several turtle-steering functions: fdandbkfor forward and back-
ward, andltandrtfor left and right turns. Also, each Turtle is holding a pen, which is
either down or up; if the pen is down, the Turtle leaves a trail when it moves. The functions
puandpdstand for “pen up” and “pen down.”

To draw a right angle, add these lines to the program (after creatingboband before calling
wait_for_user):

fd(bob, 100)
lt(bob)
fd(bob, 100)

The first line tellsbobto take 100 steps forward. The second line tells him to turn left.

When you run this program, you should seebobmove east and then north, leaving two
line segments behind.

Now modify the program to draw a square. Don’t go on until you’ve got it working!

### 4.2 Simple repetition

Chances are you wrote something like this (leaving out the code that creates TurtleWorld
and waits for the user):

fd(bob, 100)
lt(bob)

fd(bob, 100)
lt(bob)

fd(bob, 100)
lt(bob)

fd(bob, 100)

We can do the same thing more concisely with aforstatement. Add this example to
mypolygon.pyand run it again:

for i in range(4):
print 'Hello!'

You should see something like this:


**4.3. Exercises 33**

Hello!
Hello!
Hello!
Hello!

This is the simplest use of theforstatement; we will see more later. But that should be
enough to let you rewrite your square-drawing program. Don’t go on until you do.

Here is aforstatement that draws a square:

for i in range(4):
fd(bob, 100)
lt(bob)

The syntax of aforstatement is similar to a function definition. It has a header that ends
with a colon and an indented body. The body can contain any number of statements.

Aforstatement is sometimes called a **loop** because the flow of execution runs through the
body and then loops back to the top. In this case, it runs the body four times.

This version is actually a little different from the previous square-drawing code because it
makes another turn after drawing the last side of the square. The extra turn takes a little
more time, but it simplifies the code if we do the same thing every time through the loop.
This version also has the effect of leaving the turtle back in the starting position, facing in
the starting direction.

### 4.3 Exercises

The following is a series of exercises using TurtleWorld. They are meant to be fun, but they
have a point, too. While you are working on them, think about what the point is.

The following sections have solutions to the exercises, so don’t look until you have finished
(or at least tried).

1. Write a function calledsquarethat takes a parameter namedt, which is a turtle. It
    should use the turtle to draw a square.
    Write a function call that passesbobas an argument tosquare, and then run the
    program again.
2. Add another parameter, namedlength, tosquare. Modify the body so length of the
    sides islength, and then modify the function call to provide a second argument. Run
    the program again. Test your program with a range of values forlength.
3. The functionsltandrtmake 90-degree turns by default, but you can provide a
    second argument that specifies the number of degrees. For example,lt(bob, 45)
    turnsbob45 degrees to the left.
    Make a copy ofsquareand change the name topolygon. Add another parameter
    namednand modify the body so it draws an n-sided regular polygon. Hint: The
    exterior angles of an n-sided regular polygon are 360/ndegrees.
4. Write a function calledcirclethat takes a turtle,t, and radius,r, as parameters and
    that draws an approximate circle by invokingpolygonwith an appropriate length
    and number of sides. Test your function with a range of values ofr.


**34 Chapter 4. Case study: interface design**

```
Hint: figure out the circumference of the circle and make sure thatlength * n =
circumference.
Another hint: if bobis too slow for you, you can speed him up by changing
bob.delay, which is the time between moves, in seconds.bob.delay = 0.01ought
to get him moving.
```
5. Make a more general version ofcirclecalledarcthat takes an additional parameter
    angle, which determines what fraction of a circle to draw.angleis in units of degrees,
    so whenangle=360,arcshould draw a complete circle.

### 4.4 Encapsulation

The first exercise asks you to put your square-drawing code into a function definition and
then call the function, passing the turtle as a parameter. Here is a solution:

def square(t):
for i in range(4):
fd(t, 100)
lt(t)

square(bob)

The innermost statements,fdandltare indented twice to show that they are inside the
forloop, which is inside the function definition. The next line,square(bob), is flush with
the left margin, so that is the end of both theforloop and the function definition.

Inside the function,trefers to the same turtlebobrefers to, solt(t)has the same effect as
lt(bob). So why not call the parameterbob? The idea is thattcan be any turtle, not just
bob, so you could create a second turtle and pass it as an argument tosquare:

ray = Turtle()
square(ray)

Wrapping a piece of code up in a function is called **encapsulation**. One of the benefits of
encapsulation is that it attaches a name to the code, which serves as a kind of documenta-
tion. Another advantage is that if you re-use the code, it is more concise to call a function
twice than to copy and paste the body!

### 4.5 Generalization

The next step is to add alengthparameter tosquare. Here is a solution:

def square(t, length):
for i in range(4):
fd(t, length)
lt(t)

square(bob, 100)

Adding a parameter to a function is called **generalization** because it makes the function
more general: in the previous version, the square is always the same size; in this version it
can be any size.


**4.6. Interface design 35**

The next step is also a generalization. Instead of drawing squares,polygondraws regular
polygons with any number of sides. Here is a solution :rule

def polygon(t, n, length):
angle = 360.0 / n
for i in range(n):
fd(t, length)
lt(t, angle)

polygon(bob, 7, 70)

This draws a 7-sided polygon with side length 70. If you have more than a few numeric
arguments, it is easy to forget what they are, or what order they should be in. It is legal,
and sometimes helpful, to include the names of the parameters in the argument list:

polygon(bob, n=7, length=70)

These are called **keyword arguments** because they include the parameter names as “key-
words” (not to be confused with Python keywords likewhileanddef).

This syntax makes the program more readable. It is also a reminder about how arguments
and parameters work: when you call a function, the arguments are assigned to the param-
eters.

### 4.6 Interface design

The next step is to writecircle, which takes a radius,r, as a parameter. Here is a simple
solution that usespolygonto draw a 50-sided polygon:

def circle(t, r):
circumference = 2 * math.pi * r
n = 50
length = circumference / n
polygon(t, n, length)

The first line computes the circumference of a circle with radiusrusing the formula 2 _π_ r.
Since we usemath.pi, we have to importmath. By convention,importstatements are
usually at the beginning of the script.

nis the number of line segments in our approximation of a circle, solengthis the length
of each segment. Thus,polygondraws a 50-sides polygon that approximates a circle with
radiusr.

One limitation of this solution is thatnis a constant, which means that for very big circles,
the line segments are too long, and for small circles, we waste time drawing very small
segments. One solution would be to generalize the function by takingnas a parameter.
This would give the user (whoever callscircle) more control, but the interface would be
less clean.

The **interface** of a function is a summary of how it is used: what are the parameters? What
does the function do? And what is the return value? An interface is “clean” if it is “as
simple as possible, but not simpler. (Einstein)”

In this example,rbelongs in the interface because it specifies the circle to be drawn.nis
less appropriate because it pertains to the details ofhowthe circle should be rendered.


**36 Chapter 4. Case study: interface design**

Rather than clutter up the interface, it is better to choose an appropriate value ofndepend-
ing oncircumference:

def circle(t, r):
circumference = 2 * math.pi * r
n = int(circumference / 3) + 1
length = circumference / n
polygon(t, n, length)

Now the number of segments is (approximately)circumference/3, so the length of each
segment is (approximately) 3, which is small enough that the circles look good, but big
enough to be efficient, and appropriate for any size circle.

### 4.7 Refactoring

When I wrotecircle, I was able to re-usepolygonbecause a many-sided polygon is a good
approximation of a circle. Butarcis not as cooperative; we can’t usepolygonorcircleto
draw an arc.

One alternative is to start with a copy ofpolygonand transform it intoarc. The result
might look like this:

def arc(t, r, angle):
arc_length = 2 * math.pi * r * angle / 360
n = int(arc_length / 3) + 1
step_length = arc_length / n
step_angle = float(angle) / n

```
for i in range(n):
fd(t, step_length)
lt(t, step_angle)
```
The second half of this function looks likepolygon, but we can’t re-usepolygonwithout
changing the interface. We could generalizepolygonto take an angle as a third argument,
but thenpolygonwould no longer be an appropriate name! Instead, let’s call the more
general functionpolyline:

def polyline(t, n, length, angle):
for i in range(n):
fd(t, length)
lt(t, angle)

Now we can rewritepolygonandarcto usepolyline:

def polygon(t, n, length):
angle = 360.0 / n
polyline(t, n, length, angle)

def arc(t, r, angle):
arc_length = 2 * math.pi * r * angle / 360
n = int(arc_length / 3) + 1
step_length = arc_length / n
step_angle = float(angle) / n
polyline(t, n, step_length, step_angle)


**4.8. A development plan 37**

Finally, we can rewritecircleto usearc:

def circle(t, r):
arc(t, r, 360)

This process—rearranging a program to improve function interfaces and facilitate code re-
use—is called **refactoring**. In this case, we noticed that there was similar code inarcand
polygon, so we “factored it out” intopolyline.

If we had planned ahead, we might have writtenpolylinefirst and avoided refactoring,
but often you don’t know enough at the beginning of a project to design all the interfaces.
Once you start coding, you understand the problem better. Sometimes refactoring is a sign
that you have learned something.

### 4.8 A development plan

A **development plan** is a process for writing programs. The process we used in this case
study is “encapsulation and generalization.” The steps of this process are:

1. Start by writing a small program with no function definitions.
2. Once you get the program working, encapsulate it in a function and give it a name.
3. Generalize the function by adding appropriate parameters.
4. Repeat steps 1–3 until you have a set of working functions. Copy and paste working
    code to avoid retyping (and re-debugging).
5. Look for opportunities to improve the program by refactoring. For example, if you
    have similar code in several places, consider factoring it into an appropriately general
    function.

This process has some drawbacks—we will see alternatives later—but it can be useful if
you don’t know ahead of time how to divide the program into functions. This approach
lets you design as you go along.

### 4.9 docstring

A **docstring** is a string at the beginning of a function that explains the interface (“doc” is
short for “documentation”). Here is an example:

def polyline(t, n, length, angle):
"""Draws n line segments with the given length and
angle (in degrees) between them. t is a turtle.
"""
for i in range(n):
fd(t, length)
lt(t, angle)


**38 Chapter 4. Case study: interface design**

This docstring is a triple-quoted string, also known as a multiline string because the triple
quotes allow the string to span more than one line.

It is terse, but it contains the essential information someone would need to use this func-
tion. It explains concisely what the function does (without getting into the details of how
it does it). It explains what effect each parameter has on the behavior of the function and
what type each parameter should be (if it is not obvious).

Writing this kind of documentation is an important part of interface design. A well-
designed interface should be simple to explain; if you are having a hard time explaining
one of your functions, that might be a sign that the interface could be improved.

### 4.10 Debugging

An interface is like a contract between a function and a caller. The caller agrees to provide
certain parameters and the function agrees to do certain work.

For example,polylinerequires four arguments:thas to be a Turtle;nis the number of
line segments, so it has to be an integer;lengthshould be a positive number; andangle
has to be a number, which is understood to be in degrees.

These requirements are called **preconditions** because they are supposed to be true before
the function starts executing. Conversely, conditions at the end of the function are **post-
conditions**. Postconditions include the intended effect of the function (like drawing line
segments) and any side effects (like moving the Turtle or making other changes in the
World).

Preconditions are the responsibility of the caller. If the caller violates a (properly docu-
mented!) precondition and the function doesn’t work correctly, the bug is in the caller, not
the function.

### 4.11 Glossary

**instance:** A member of a set. The TurtleWorld in this chapter is a member of the set of
TurtleWorlds.

**loop:** A part of a program that can execute repeatedly.

**encapsulation:** The process of transforming a sequence of statements into a function defi-
nition.

**generalization:** The process of replacing something unnecessarily specific (like a number)
with something appropriately general (like a variable or parameter).

**keyword argument:** An argument that includes the name of the parameter as a “key-
word.”

**interface:** A description of how to use a function, including the name and descriptions of
the arguments and return value.

**refactoring:** The process of modifying a working program to improve function interfaces
and other qualities of the code.


**4.12. Exercises 39**

```
Figure 4.1: Turtle flowers.
```
```
Figure 4.2: Turtle pies.
```
**development plan:** A process for writing programs.

**docstring:** A string that appears in a function definition to document the function’s inter-
face.

**precondition:** A requirement that should be satisfied by the caller before a function starts.

**postcondition:** A requirement that should be satisfied by the function before it ends.

### 4.12 Exercises

**Exercise 4.1.** Download the code in this chapter from [http:](http:) // thinkpython. com/ code/
polygon. py.

1. Write appropriate docstrings forpolygon,arcandcircle.
2. Draw a stack diagram that shows the state of the program while executingcircle(bob,
    radius). You can do the arithmetic by hand or addprintstatements to the code.
3. The version ofarcin Section 4.7 is not very accurate because the linear approximation of the
    circle is always outside the true circle. As a result, the turtle ends up a few units away from
    the correct destination. My solution shows a way to reduce the effect of this error. Read the
    code and see if it makes sense to you. If you draw a diagram, you might see how it works.

**Exercise 4.2.** Write an appropriately general set of functions that can draw flowers as in Figure 4.1.

Solution: [http:](http:) // thinkpython. com/ code/ flower. py, also requires [http:](http:)
// thinkpython. com/ code/ polygon. py.
**Exercise 4.3.** Write an appropriately general set of functions that can draw shapes as in Figure 4.2.

Solution:http: // thinkpython. com/ code/ pie. py.


**40 Chapter 4. Case study: interface design**

**Exercise 4.4.** The letters of the alphabet can be constructed from a moderate number of basic ele-
ments, like vertical and horizontal lines and a few curves. Design a font that can be drawn with a
minimal number of basic elements and then write functions that draw letters of the alphabet.

You should write one function for each letter, with namesdraw_a,draw_b, etc., and put your
functions in a file namedletters.py. You can download a “turtle typewriter” fromhttp: //
thinkpython. com/ code/ typewriter. pyto help you test your code.

Solution: [http:](http:) // thinkpython. com/ code/ letters. py, also requires [http:](http:)
// thinkpython. com/ code/ polygon. py.
**Exercise 4.5.** Read about spirals athttp: // en. wikipedia. org/ wiki/ Spiral; then write
a program that draws an Archimedian spiral (or one of the other kinds). Solution: [http:](http:)
// thinkpython. com/ code/ spiral. py.


## Chapter 5

# Conditionals and recursion

### 5.1 Modulus operator

The **modulus operator** works on integers and yields the remainder when the first operand
is divided by the second. In Python, the modulus operator is a percent sign (%). The syntax
is the same as for other operators:

>>> quotient = 7 / 3
>>> print quotient
2
>>> remainder = 7 % 3
>>> print remainder
1

So 7 divided by 3 is 2 with 1 left over.

The modulus operator turns out to be surprisingly useful. For example, you can check
whether one number is divisible by another—ifx % yis zero, thenxis divisible byy.

Also, you can extract the right-most digit or digits from a number. For example,x % 10
yields the right-most digit ofx(in base 10). Similarlyx % 100yields the last two digits.

### 5.2 Boolean expressions

A **boolean expression** is an expression that is either true or false. The following examples
use the operator==, which compares two operands and producesTrueif they are equal
andFalseotherwise:

>>> 5 == 5
True
>>> 5 == 6
False

TrueandFalseare special values that belong to the typebool; they are not strings:

>>> type(True)
<type'bool'>
>>> type(False)
<type'bool'>


**42 Chapter 5. Conditionals and recursion**

The==operator is one of the **relational operators** ; the others are:

```
x != y # x is not equal to y
x > y # x is greater than y
x < y # x is less than y
x >= y # x is greater than or equal to y
x <= y # x is less than or equal to y
```
Although these operations are probably familiar to you, the Python symbols are different
from the mathematical symbols. A common error is to use a single equal sign (=) instead of
a double equal sign (==). Remember that=is an assignment operator and==is a relational
operator. There is no such thing as=<or=>.

### 5.3 Logical operators

There are three **logical operators** : and,or, andnot. The semantics (meaning) of these
operators is similar to their meaning in English. For example,x > 0 and x < 10is true
only ifxis greater than 0andless than 10.

n%2 == 0 or n%3 == 0is true ifeitherof the conditions is true, that is, if the number is
divisible by 2or3.

Finally, thenotoperator negates a boolean expression, sonot (x > y)is true ifx > yis
false, that is, ifxis less than or equal toy.

Strictly speaking, the operands of the logical operators should be boolean expressions, but
Python is not very strict. Any nonzero number is interpreted as “true.”

>>> 17 and True
True

This flexibility can be useful, but there are some subtleties to it that might be confusing.
You might want to avoid it (unless you know what you are doing).

### 5.4 Conditional execution

In order to write useful programs, we almost always need the ability to check conditions
and change the behavior of the program accordingly. **Conditional statements** give us this
ability. The simplest form is theifstatement:

if x > 0:
print 'x is positive'

The boolean expression afterifis called the **condition**. If it is true, then the indented
statement gets executed. If not, nothing happens.

ifstatements have the same structure as function definitions: a header followed by an
indented body. Statements like this are called **compound statements**.

There is no limit on the number of statements that can appear in the body, but there has to
be at least one. Occasionally, it is useful to have a body with no statements (usually as a
place keeper for code you haven’t written yet). In that case, you can use thepassstatement,
which does nothing.

if x < 0:
pass # need to handle negative values!


**5.5. Alternative execution 43**

### 5.5 Alternative execution

A second form of theifstatement is **alternative execution** , in which there are two possi-
bilities and the condition determines which one gets executed. The syntax looks like this:

if x%2 == 0:
print'x is even'
else:
print'x is odd'

If the remainder whenxis divided by 2 is 0, then we know thatxis even, and the program
displays a message to that effect. If the condition is false, the second set of statements is
executed. Since the condition must be true or false, exactly one of the alternatives will be
executed. The alternatives are called **branches** , because they are branches in the flow of
execution.

### 5.6 Chained conditionals

Sometimes there are more than two possibilities and we need more than two branches.
One way to express a computation like that is a **chained conditional** :

if x < y:
print'x is less than y'
elif x > y:
print'x is greater than y'
else:
print'x and y are equal'

elifis an abbreviation of “else if.” Again, exactly one branch will be executed. There is no
limit on the number ofelifstatements. If there is anelseclause, it has to be at the end,
but there doesn’t have to be one.

if choice =='a':
draw_a()
elif choice =='b':
draw_b()
elif choice =='c':
draw_c()

Each condition is checked in order. If the first is false, the next is checked, and so on. If one
of them is true, the corresponding branch executes, and the statement ends. Even if more
than one condition is true, only the first true branch executes.

### 5.7 Nested conditionals

One conditional can also be nested within another. We could have written the trichotomy
example like this:

if x == y:
print'x and y are equal'
else:
if x < y:


**44 Chapter 5. Conditionals and recursion**

```
print 'x is less than y'
else:
print 'x is greater than y'
```
The outer conditional contains two branches. The first branch contains a simple statement.
The second branch contains anotherifstatement, which has two branches of its own.
Those two branches are both simple statements, although they could have been conditional
statements as well.

Although the indentation of the statements makes the structure apparent, **nested condi-
tionals** become difficult to read very quickly. In general, it is a good idea to avoid them
when you can.

Logical operators often provide a way to simplify nested conditional statements. For ex-
ample, we can rewrite the following code using a single conditional:

if 0 < x:
if x < 10:
print 'x is a positive single-digit number.'

Theprintstatement is executed only if we make it past both conditionals, so we can get
the same effect with theandoperator:

if 0 < x and x < 10:
print 'x is a positive single-digit number.'

### 5.8 Recursion

It is legal for one function to call another; it is also legal for a function to call itself. It may
not be obvious why that is a good thing, but it turns out to be one of the most magical
things a program can do. For example, look at the following function:

def countdown(n):
if n <= 0:
print 'Blastoff!'
else:
print n
countdown(n-1)

Ifnis 0 or negative, it outputs the word, “Blastoff!” Otherwise, it outputsnand then calls
a function namedcountdown—itself—passingn-1as an argument.

What happens if we call this function like this?

>>> countdown(3)

The execution ofcountdownbegins withn=3, and sincenis greater than 0, it outputs the
value 3, and then calls itself...

```
The execution ofcountdownbegins withn=2, and sincenis greater than 0, it
outputs the value 2, and then calls itself...
The execution ofcountdownbegins withn=1, and sincenis greater
than 0, it outputs the value 1, and then calls itself...
The execution ofcountdownbegins withn=0, and sincenis
not greater than 0, it outputs the word, “Blastoff!” and then
returns.
```

**5.9. Stack diagrams for recursive functions 45**

```
Thecountdownthat gotn=1returns.
Thecountdownthat gotn=2returns.
```
Thecountdownthat gotn=3returns.

And then you’re back in__main__. So, the total output looks like this:

3
2
1
Blastoff!

A function that calls itself is **recursive** ; the process is called **recursion**.

As another example, we can write a function that prints a stringntimes.

def print_n(s, n):
if n <= 0:
return
print s
print_n(s, n-1)

Ifn <= 0thereturnstatement exits the function. The flow of execution immediately re-
turns to the caller, and the remaining lines of the function are not executed.

The rest of the function is similar tocountdown: ifnis greater than 0, it displayssand then
calls itself to displaysn−1 additional times. So the number of lines of output is1 + (n -
1), which adds up ton.

For simple examples like this, it is probably easier to use aforloop. But we will see
examples later that are hard to write with aforloop and easy to write with recursion, so it
is good to start early.

### 5.9 Stack diagrams for recursive functions

In Section 3.10, we used a stack diagram to represent the state of a program during a func-
tion call. The same kind of diagram can help interpret a recursive function.

Every time a function gets called, Python creates a new function frame, which contains the
function’s local variables and parameters. For a recursive function, there might be more
than one frame on the stack at the same time.

Figure 5.1 shows a stack diagram forcountdowncalled withn = 3.

As usual, the top of the stack is the frame for__main__. It is empty because we did not
create any variables in__main__or pass any arguments to it.

The fourcountdownframes have different values for the parametern. The bottom of the
stack, wheren=0, is called the **base case**. It does not make a recursive call, so there are no
more frames.
**Exercise 5.1.** Draw a stack diagram forprint_ncalled withs ='Hello'andn=2.
**Exercise 5.2.** Write a function calleddo_nthat takes a function object and a number,n, as argu-
ments, and that calls the given functionntimes.


**46 Chapter 5. Conditionals and recursion**

```
<module>
```
```
countdown
```
```
countdown
```
```
countdown
```
```
countdown
```
```
n 3
```
```
n 2
```
```
n 1
```
```
n 0
```
```
Figure 5.1: Stack diagram.
```
### 5.10 Infinite recursion

If a recursion never reaches a base case, it goes on making recursive calls forever, and the
program never terminates. This is known as **infinite recursion** , and it is generally not a
good idea. Here is a minimal program with an infinite recursion:

def recurse():
recurse()

In most programming environments, a program with infinite recursion does not really run
forever. Python reports an error message when the maximum recursion depth is reached:

```
File "<stdin>", line 2, in recurse
File "<stdin>", line 2, in recurse
File "<stdin>", line 2, in recurse
```
File "<stdin>", line 2, in recurse
RuntimeError: Maximum recursion depth exceeded

This traceback is a little bigger than the one we saw in the previous chapter. When the error
occurs, there are 1000recurseframes on the stack!

### 5.11 Keyboard input

The programs we have written so far are a bit rude in the sense that they accept no input
from the user. They just do the same thing every time.

Python 2 provides a built-in function calledraw_inputthat gets input from the keyboard.
In Python 3, it is calledinput. When this function is called, the program stops and waits for
the user to type something. When the user pressesReturnorEnter, the program resumes
andraw_inputreturns what the user typed as a string.

>>> text = raw_input()
What are you waiting for?
>>> print text
What are you waiting for?


**5.12. Debugging 47**

Before getting input from the user, it is a good idea to print a prompt telling the user what
to input.raw_inputcan take a prompt as an argument:

>>> name = raw_input('What...is your name?\n')
What...is your name?
Arthur, King of the Britons!
>>> print name
Arthur, King of the Britons!

The sequence\nat the end of the prompt represents a **newline** , which is a special character
that causes a line break. That’s why the user’s input appears below the prompt.

If you expect the user to type an integer, you can try to convert the return value toint:

>>> prompt ='What...is the airspeed velocity of an unladen swallow?\n'
>>> speed = raw_input(prompt)
What...is the airspeed velocity of an unladen swallow?
17
>>> int(speed)
17

But if the user types something other than a string of digits, you get an error:

>>> speed = raw_input(prompt)
What...is the airspeed velocity of an unladen swallow?
What do you mean, an African or a European swallow?
>>> int(speed)
ValueError: invalid literal for int() with base 10

We will see how to handle this kind of error later.

### 5.12 Debugging

The traceback Python displays when an error occurs contains a lot of information, but it
can be overwhelming, especially when there are many frames on the stack. The most useful
parts are usually:

- What kind of error it was, and
- Where it occurred.

Syntax errors are usually easy to find, but there are a few gotchas. Whitespace errors can
be tricky because spaces and tabs are invisible and we are used to ignoring them.

>>> x = 5
>>> y = 6
File "<stdin>", line 1
y = 6
^
IndentationError: unexpected indent

In this example, the problem is that the second line is indented by one space. But the error
message points toy, which is misleading. In general, error messages indicate where the
problem was discovered, but the actual error might be earlier in the code, sometimes on a
previous line.


**48 Chapter 5. Conditionals and recursion**

The same is true of runtime errors.

Suppose you are trying to compute a signal-to-noise ratio in decibels. The formula is
SN Rdb=10 log 10 (Psignal/Pnoise). In Python, you might write something like this:

import math
signal_power = 9
noise_power = 10
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print decibels

But when you run it in Python 2, you get an error message.

Traceback (most recent call last):
File "snr.py", line 5, in?
decibels = 10 * math.log10(ratio)
ValueError: math domain error

The error message indicates line 5, but there is nothing wrong with that line. To find the
real error, it might be useful to print the value ofratio, which turns out to be 0. The
problem is in line 4, because dividing two integers does floor division. The solution is to
represent signal power and noise power with floating-point values.

In general, error messages tell you where the problem was discovered, but that is often not
where it was caused.

In Python 3, this example does not cause an error; the division operator performs floating-
point division even with integer operands.

### 5.13 Glossary

**modulus operator:** An operator, denoted with a percent sign (%), that works on integers
and yields the remainder when one number is divided by another.

**boolean expression:** An expression whose value is eitherTrueorFalse.

**relational operator:** One of the operators that compares its operands:==,!=,>,<,>=, and
<=.

**logical operator:** One of the operators that combines boolean expressions: and,or, and
not.

**conditional statement:** A statement that controls the flow of execution depending on some
condition.

**condition:** The boolean expression in a conditional statement that determines which
branch is executed.

**compound statement:** A statement that consists of a header and a body. The header ends
with a colon (:). The body is indented relative to the header.

**branch:** One of the alternative sequences of statements in a conditional statement.

**chained conditional:** A conditional statement with a series of alternative branches.


**5.14. Exercises 49**

**nested conditional:** A conditional statement that appears in one of the branches of another
conditional statement.

**recursion:** The process of calling the function that is currently executing.

**base case:** A conditional branch in a recursive function that does not make a recursive call.

**infinite recursion:** A recursion that doesn’t have a base case, or never reaches it. Eventu-
ally, an infinite recursion causes a runtime error.

### 5.14 Exercises

**Exercise 5.3.** Fermat’s Last Theorem says that there are no positive integers a, b, and c such that

```
an+bn=cn
```
for any values of n greater than 2.

1. Write a function namedcheck_fermatthat takes four parameters—a,b,candn—and that
    checks to see if Fermat’s theorem holds. If n is greater than 2 and it turns out to be true that

```
an+bn=cn
```
```
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”
```
2. Write a function that prompts the user to input values fora,b,candn, converts them to
    integers, and usescheck_fermatto check whether they violate Fermat’s theorem.

**Exercise 5.4.** If you are given three sticks, you may or may not be able to arrange them in a triangle.
For example, if one of the sticks is 12 inches long and the other two are one inch long, it is clear that
you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a
simple test to see if it is possible to form a triangle:

```
If any of the three lengths is greater than the sum of the other two, then you cannot
form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
form what is called a “degenerate” triangle.)
```
1. Write a function namedis_trianglethat takes three integers as arguments, and that prints
    either “Yes” or “No,” depending on whether you can or cannot form a triangle from sticks
    with the given lengths.
2. Write a function that prompts the user to input three stick lengths, converts them to integers,
    and usesis_triangleto check whether sticks with the given lengths can form a triangle.

The following exercises use TurtleWorld from Chapter 4:
**Exercise 5.5.** Read the following function and see if you can figure out what it does. Then run it
(see the examples in Chapter 4).


**50 Chapter 5. Conditionals and recursion**

```
Figure 5.2: A Koch curve.
```
def draw(t, length, n):
if n == 0:
return
angle = 50
fd(t, length*n)
lt(t, angle)
draw(t, length, n-1)
rt(t, 2*angle)
draw(t, length, n-1)
lt(t, angle)
bk(t, length*n)
**Exercise 5.6.** The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch
curve with length x, all you have to do is

1. Draw a Koch curve with length x/3.
2. Turn left 60 degrees.
3. Draw a Koch curve with length x/3.
4. Turn right 120 degrees.
5. Draw a Koch curve with length x/3.
6. Turn left 60 degrees.
7. Draw a Koch curve with length x/3.

The exception is if x is less than 3: in that case, you can just draw a straight line with length x.

1. Write a function calledkochthat takes a turtle and a length as parameters, and that uses the
    turtle to draw a Koch curve with the given length.
2. Write a function calledsnowflakethat draws three Koch curves to make the outline of a
    snowflake.
    Solution:http: // thinkpython. com/ code/ koch. py.
3. The Koch curve can be generalized in several ways. Seehttp: // en. wikipedia. org/
    wiki/ Koch_ snowflakefor examples and implement your favorite.


## Chapter 6

# Fruitful functions

### 6.1 Return values

Some of the built-in functions we have used, such as the math functions, produce results.
Calling the function generates a value, which we usually assign to a variable or use as part
of an expression.

e = math.exp(1.0)
height = radius * math.sin(radians)

All of the functions we have written so far are void; they print something or move turtles
around, but their return value isNone.

In this chapter, we are (finally) going to write fruitful functions. The first example isarea,
which returns the area of a circle with the given radius:

def area(radius):
temp = math.pi * radius**2
return temp

We have seen thereturnstatement before, but in a fruitful function thereturnstatement
includes an expression. This statement means: “Return immediately from this function
and use the following expression as a return value.” The expression can be arbitrarily
complicated, so we could have written this function more concisely:

def area(radius):
return math.pi * radius**2

On the other hand, **temporary variables** liketempoften make debugging easier.

Sometimes it is useful to have multiple return statements, one in each branch of a condi-
tional:

def absolute_value(x):
if x < 0:
return -x
else:
return x


**52 Chapter 6. Fruitful functions**

Since thesereturnstatements are in an alternative conditional, only one will be executed.

As soon as a return statement executes, the function terminates without executing any
subsequent statements. Code that appears after areturnstatement, or any other place the
flow of execution can never reach, is called **dead code**.

In a fruitful function, it is a good idea to ensure that every possible path through the pro-
gram hits areturnstatement. For example:

def absolute_value(x):
if x < 0:
return -x
if x > 0:
return x

This function is incorrect because ifxhappens to be 0, neither condition is true, and the
function ends without hitting areturnstatement. If the flow of execution gets to the end
of a function, the return value isNone, which is not the absolute value of 0.

>>> print absolute_value(0)
None

By the way, Python provides a built-in function calledabsthat computes absolute values.
**Exercise 6.1.** Write acomparefunction that returns 1 ifx > y, 0 ifx == y, and-1ifx < y.

### 6.2 Incremental development

As you write larger functions, you might find yourself spending more time debugging.

To deal with increasingly complex programs, you might want to try a process called **in-
cremental development**. The goal of incremental development is to avoid long debugging
sessions by adding and testing only a small amount of code at a time.

As an example, suppose you want to find the distance between two points, given by the
coordinates(x 1 ,y 1 )and(x 2 ,y 2 ). By the Pythagorean theorem, the distance is:

```
distance=
```
#### √

```
(x 2 −x 1 )^2 + (y 2 −y 1 )^2
```
The first step is to consider what adistancefunction should look like in Python. In other
words, what are the inputs (parameters) and what is the output (return value)?

In this case, the inputs are two points, which you can represent using four numbers. The
return value is the distance, which is a floating-point value.

Already you can write an outline of the function:

def distance(x1, y1, x2, y2):
return 0.0

Obviously, this version doesn’t compute distances; it always returns zero. But it is syn-
tactically correct, and it runs, which means that you can test it before you make it more
complicated.

To test the new function, call it with sample arguments:


**6.2. Incremental development 53**

>>> distance(1, 2, 4, 6)
0.0

I chose these values so that the horizontal distance is 3 and the vertical distance is 4; that
way, the result is 5 (the hypotenuse of a 3-4-5 triangle). When testing a function, it is useful
to know the right answer.

At this point we have confirmed that the function is syntactically correct, and we can start
adding code to the body. A reasonable next step is to find the differencesx 2 −x 1 and
y 2 −y 1. The next version stores those values in temporary variables and prints them.

def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
print'dx is', dx
print'dy is', dy
return 0.0

If the function is working, it should display'dx is 3'and'dy is 4'. If so, we know that
the function is getting the right arguments and performing the first computation correctly.
If not, there are only a few lines to check.

Next we compute the sum of squares ofdxanddy:

def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
dsquared = dx**2 + dy**2
print'dsquared is:', dsquared
return 0.0

Again, you would run the program at this stage and check the output (which should be
25). Finally, you can usemath.sqrtto compute and return the result:

def distance(x1, y1, x2, y2):
dx = x2 - x1
dy = y2 - y1
dsquared = dx**2 + dy**2
result = math.sqrt(dsquared)
return result

If that works correctly, you are done. Otherwise, you might want to print the value of
resultbefore the return statement.

The final version of the function doesn’t display anything when it runs; it only returns
a value. Theprintstatements we wrote are useful for debugging, but once you get the
function working, you should remove them. Code like that is called **scaffolding** because it
is helpful for building the program but is not part of the final product.

When you start out, you should add only a line or two of code at a time. As you gain more
experience, you might find yourself writing and debugging bigger chunks. Either way,
incremental development can save you a lot of debugging time.

The key aspects of the process are:

1. Start with a working program and make small incremental changes. At any point, if
    there is an error, you should have a good idea where it is.


**54 Chapter 6. Fruitful functions**

2. Use temporary variables to hold intermediate values so you can display and check
    them.
3. Once the program is working, you might want to remove some of the scaffolding or
    consolidate multiple statements into compound expressions, but only if it does not
    make the program difficult to read.

**Exercise 6.2.** Use incremental development to write a function calledhypotenusethat returns the
length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record
each stage of the development process as you go.

### 6.3 Composition

As you should expect by now, you can call one function from within another. This ability
is called **composition**.

As an example, we’ll write a function that takes two points, the center of the circle and a
point on the perimeter, and computes the area of the circle.

Assume that the center point is stored in the variablesxcandyc, and the perimeter point is
inxpandyp. The first step is to find the radius of the circle, which is the distance between
the two points. We just wrote a function,distance, that does that:

radius = distance(xc, yc, xp, yp)

The next step is to find the area of a circle with that radius; we just wrote that, too:

result = area(radius)

Encapsulating these steps in a function, we get:

def circle_area(xc, yc, xp, yp):
radius = distance(xc, yc, xp, yp)
result = area(radius)
return result

The temporary variablesradiusandresultare useful for development and debugging,
but once the program is working, we can make it more concise by composing the function
calls:

def circle_area(xc, yc, xp, yp):
return area(distance(xc, yc, xp, yp))

### 6.4 Boolean functions

Functions can return booleans, which is often convenient for hiding complicated tests in-
side functions. For example:

def is_divisible(x, y):
if x % y == 0:
return True
else:
return False


**6.5. More recursion 55**

It is common to give boolean functions names that sound like yes/no questions;
is_divisiblereturns eitherTrueorFalseto indicate whetherxis divisible byy.

Here is an example:

>>> is_divisible(6, 4)
False
>>> is_divisible(6, 3)
True

The result of the==operator is a boolean, so we can write the function more concisely by
returning it directly:

def is_divisible(x, y):
return x % y == 0

Boolean functions are often used in conditional statements:

if is_divisible(x, y):
print'x is divisible by y'

It might be tempting to write something like:

if is_divisible(x, y) == True:
print'x is divisible by y'

But the extra comparison is unnecessary.
**Exercise 6.3.** Write a functionis_between(x, y, z)that returnsTrueif x≤y≤z orFalse
otherwise.

### 6.5 More recursion

We have only covered a small subset of Python, but you might be interested to know that
this subset is acompleteprogramming language, which means that anything that can be
computed can be expressed in this language. Any program ever written could be rewritten
using only the language features you have learned so far (actually, you would need a few
commands to control devices like the keyboard, mouse, disks, etc., but that’s all).

Proving that claim is a nontrivial exercise first accomplished by Alan Turing, one of the
first computer scientists (some would argue that he was a mathematician, but a lot of early
computer scientists started as mathematicians). Accordingly, it is known as the Turing
Thesis. For a more complete (and accurate) discussion of the Turing Thesis, I recommend
Michael Sipser’s bookIntroduction to the Theory of Computation.

To give you an idea of what you can do with the tools you have learned so far, we’ll eval-
uate a few recursively defined mathematical functions. A recursive definition is similar to
a circular definition, in the sense that the definition contains a reference to the thing being
defined. A truly circular definition is not very useful:

**vorpal:** An adjective used to describe something that is vorpal.

If you saw that definition in the dictionary, you might be annoyed. On the other hand,
if you looked up the definition of the factorial function, denoted with the symbol !, you
might get something like this:

```
0!= 1
n!=n(n− 1 )!
```

**56 Chapter 6. Fruitful functions**

This definition says that the factorial of 0 is 1, and the factorial of any other value,n, isn
multiplied by the factorial ofn−1.

So 3! is 3 times 2!, which is 2 times 1!, which is 1 times 0!. Putting it all together, 3! equals 3
times 2 times 1 times 1, which is 6.

If you can write a recursive definition of something, you can usually write a Python pro-
gram to evaluate it. The first step is to decide what the parameters should be. In this case
it should be clear thatfactorialtakes an integer:

def factorial(n):

If the argument happens to be 0, all we have to do is return 1:

def factorial(n):
if n == 0:
return 1

Otherwise, and this is the interesting part, we have to make a recursive call to find the
factorial ofn−1 and then multiply it byn:

def factorial(n):
if n == 0:
return 1
else:
recurse = factorial(n-1)
result = n * recurse
return result

The flow of execution for this program is similar to the flow ofcountdownin Section 5.8. If
we callfactorialwith the value 3:

Since 3 is not 0, we take the second branch and calculate the factorial ofn-1...

```
Since 2 is not 0, we take the second branch and calculate the factorial ofn-1...
```
```
Since 1 is not 0, we take the second branch and calculate the factorial
ofn-1...
Since 0is0, we take the first branch and return 1 without
making any more recursive calls.
```
```
The return value (1) is multiplied byn, which is 1, and the result is
returned.
The return value (1) is multiplied byn, which is 2, and the result is returned.
```
The return value (2) is multiplied byn, which is 3, and the result, 6, becomes the return
value of the function call that started the whole process.

Figure 6.1 shows what the stack diagram looks like for this sequence of function calls.

The return values are shown being passed back up the stack. In each frame, the return
value is the value ofresult, which is the product ofnandrecurse.

In the last frame, the local variablesrecurseandresultdo not exist, because the branch
that creates them does not execute.


**6.6. Leap of faith 57**

```
n 3 recurse 2
```
```
recurse 1
```
```
recurse 1
```
```
<module>
```
```
factorial
```
```
n 2
```
```
n 1
```
```
n 0
```
```
factorial
```
```
factorial
```
```
factorial
```
```
1
```
```
1
```
```
2
```
```
6
```
```
result 1
```
```
2
```
```
result 6
```
```
result
```
```
Figure 6.1: Stack diagram.
```
### 6.6 Leap of faith

Following the flow of execution is one way to read programs, but it can quickly become
labyrinthine. An alternative is what I call the “leap of faith.” When you come to a function
call, instead of following the flow of execution, youassumethat the function works correctly
and returns the right result.

In fact, you are already practicing this leap of faith when you use built-in functions. When
you callmath.cosormath.exp, you don’t examine the bodies of those functions. You just
assume that they work because the people who wrote the built-in functions were good
programmers.

The same is true when you call one of your own functions. For example, in Section 6.4, we
wrote a function calledis_divisiblethat determines whether one number is divisible by
another. Once we have convinced ourselves that this function is correct—by examining the
code and testing—we can use the function without looking at the body again.

The same is true of recursive programs. When you get to the recursive call, instead of
following the flow of execution, you should assume that the recursive call works (yields
the correct result) and then ask yourself, “Assuming that I can find the factorial ofn−1,
can I compute the factorial ofn?” In this case, it is clear that you can, by multiplying byn.

Of course, it’s a bit strange to assume that the function works correctly when you haven’t
finished writing it, but that’s why it’s called a leap of faith!

### 6.7 One more example

Afterfactorial, the most common example of a recursively defined mathematical func-
tion isfibonacci, which has the following definition (seehttp://en.wikipedia.org/
wiki/Fibonacci_number):

```
fibonacci( 0 ) = 0
fibonacci( 1 ) = 1
fibonacci(n) =fibonacci(n− 1 ) +fibonacci(n− 2 )
```
Translated into Python, it looks like this:


**58 Chapter 6. Fruitful functions**

def fibonacci (n):
if n == 0:
return 0
elif n == 1:
return 1
else:
return fibonacci(n-1) + fibonacci(n-2)

If you try to follow the flow of execution here, even for fairly small values ofn, your head
explodes. But according to the leap of faith, if you assume that the two recursive calls work
correctly, then it is clear that you get the right result by adding them together.

### 6.8 Checking types

What happens if we callfactorialand give it 1.5 as an argument?

>>> factorial(1.5)
RuntimeError: Maximum recursion depth exceeded

It looks like an infinite recursion. But how can that be? There is a base case—whenn == 0.
But ifnis not an integer, we canmissthe base case and recurse forever.

In the first recursive call, the value ofnis 0.5. In the next, it is -0.5. From there, it gets
smaller (more negative), but it will never be 0.

We have two choices. We can try to generalize thefactorialfunction to work with
floating-point numbers, or we can makefactorialcheck the type of its argument. The
first option is called the gamma function and it’s a little beyond the scope of this book. So
we’ll go for the second.

We can use the built-in functionisinstanceto verify the type of the argument. While
we’re at it, we can also make sure the argument is positive:

def factorial (n):
if not isinstance(n, int):
print 'Factorial is only defined for integers.'
return None
elif n < 0:
print 'Factorial is not defined for negative integers.'
return None
elif n == 0:
return 1
else:
return n * factorial(n-1)

The first base case handles nonintegers; the second catches negative integers. In both cases,
the program prints an error message and returnsNoneto indicate that something went
wrong:

>>> factorial('fred')
Factorial is only defined for integers.
None
>>> factorial(-2)
Factorial is not defined for negative integers.
None


**6.9. Debugging 59**

If we get past both checks, then we know thatnis positive or zero, so we can prove that
the recursion terminates.

This program demonstrates a pattern sometimes called a **guardian**. The first two condi-
tionals act as guardians, protecting the code that follows from values that might cause an
error. The guardians make it possible to prove the correctness of the code.

In Section 11.3 we will see a more flexible alternative to printing an error message: raising
an exception.

### 6.9 Debugging

Breaking a large program into smaller functions creates natural checkpoints for debugging.
If a function is not working, there are three possibilities to consider:

- There is something wrong with the arguments the function is getting; a precondition
    is violated.
- There is something wrong with the function; a postcondition is violated.
- There is something wrong with the return value or the way it is being used.

To rule out the first possibility, you can add aprintstatement at the beginning of the
function and display the values of the parameters (and maybe their types). Or you can
write code that checks the preconditions explicitly.

If the parameters look good, add aprintstatement before eachreturnstatement that dis-
plays the return value. If possible, check the result by hand. Consider calling the function
with values that make it easy to check the result (as in Section 6.2).

If the function seems to be working, look at the function call to make sure the return value
is being used correctly (or used at all!).

Adding print statements at the beginning and end of a function can help make the flow of
execution more visible. For example, here is a version offactorialwith print statements:

def factorial(n):
space =''* (4 * n)
print space,'factorial', n
if n == 0:
print space,'returning 1'
return 1
else:
recurse = factorial(n-1)
result = n * recurse
print space,'returning', result
return result

spaceis a string of space characters that controls the indentation of the output. Here is the
result offactorial(5):


**60 Chapter 6. Fruitful functions**

```
factorial 5
factorial 4
factorial 3
factorial 2
factorial 1
factorial 0
returning 1
returning 1
returning 2
returning 6
returning 24
returning 120
```
If you are confused about the flow of execution, this kind of output can be helpful. It takes
some time to develop effective scaffolding, but a little bit of scaffolding can save a lot of
debugging.

### 6.10 Glossary

**temporary variable:** A variable used to store an intermediate value in a complex calcula-
tion.

**dead code:** Part of a program that can never be executed, often because it appears after a
returnstatement.

None **:** A special value returned by functions that have no return statement or a return state-
ment without an argument.

**incremental development:** A program development plan intended to avoid debugging by
adding and testing only a small amount of code at a time.

**scaffolding:** Code that is used during program development but is not part of the final
version.

**guardian:** A programming pattern that uses a conditional statement to check for and han-
dle circumstances that might cause an error.

### 6.11 Exercises

**Exercise 6.4.** Draw a stack diagram for the following program. What does the program print?
Solution:http: // thinkpython. com/ code/ stack_ diagram. py.

def b(z):
prod = a(z, z)
print z, prod
return prod

def a(x, y):
x = x + 1
return x * y


**6.11. Exercises 61**

def c(x, y, z):
total = x + y + z
square = b(total)**2
return square

x = 1
y = x + 1
print c(x, y+3, x+y)
**Exercise 6.5.** The Ackermann function, A(m,n), is defined:

```
A(m,n) =
```
#### 

#### 

#### 

```
n+ 1 if m= 0
A(m−1, 1) if m> 0 and n= 0
A(m−1,A(m,n− 1 )) if m> 0 and n>0.
```
Seehttp: // en. wikipedia. org/ wiki/ Ackermann_ function. Write a function namedack
that evaluates Ackermann’s function. Use your function to evaluateack(3, 4), which should be

125. What happens for larger values ofmandn? Solution:http: // thinkpython. com/ code/
ackermann. py.
**Exercise 6.6.** A palindrome is a word that is spelled the same backward and forward, like “noon”
and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the
middle is a palindrome.

The following are functions that take a string argument and return the first, last, and middle letters:

def first(word):
return word[0]

def last(word):
return word[-1]

def middle(word):
return word[1:-1]

We’ll see how they work in Chapter 8.

1. Type these functions into a file namedpalindrome.pyand test them out. What happens if
    you callmiddlewith a string with two letters? One letter? What about the empty string,
    which is written''and contains no letters?
2. Write a function calledis_palindromethat takes a string argument and returnsTrueif it
    is a palindrome andFalseotherwise. Remember that you can use the built-in functionlen
    to check the length of a string.

Solution:http: // thinkpython. com/ code/ palindrome_ soln. py.
**Exercise 6.7.** A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function calledis_powerthat takes parametersaandband returnsTrueifais a power ofb. Note:
you will have to think about the base case.
**Exercise 6.8.** The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder.

One way to find the GCD of two numbers is based on the observation that if r is the remainder when
a is divided by b, then gcd(a,b) =gcd(b,r). As a base case, we can use gcd(a, 0) =a.


**62 Chapter 6. Fruitful functions**

Write a function calledgcdthat takes parametersaandband returns their greatest common divisor.

Credit: This exercise is based on an example from Abelson and Sussman’sStructure and Interpre-
tation of Computer Programs.


## Chapter 7

# Iteration

### 7.1 Multiple assignment

As you may have discovered, it is legal to make more than one assignment to the same
variable. A new assignment makes an existing variable refer to a new value (and stop
referring to the old value).

bruce = 5
print bruce,
bruce = 7
print bruce

The output of this program is5 7, because the first timebruceis printed, its value is 5,
and the second time, its value is 7. The comma at the end of the firstprintstatement
suppresses the newline, which is why both outputs appear on the same line.

Figure 7.1 shows what **multiple assignment** looks like in a state diagram.

With multiple assignment it is especially important to distinguish between an assignment
operation and a statement of equality. Because Python uses the equal sign (=) for assign-
ment, it is tempting to interpret a statement likea = bas a statement of equality. It is not!

First, equality is a symmetric relation and assignment is not. For example, in mathematics,
ifa=7 then 7=a. But in Python, the statementa = 7is legal and7 = ais not.

Furthermore, in mathematics, a statement of equality is either true or false, for all time. If
a=bnow, thenawill always equalb. In Python, an assignment statement can make two
variables equal, but they don’t have to stay that way:

a = 5
b = a # a and b are now equal
a = 3 # a and b are no longer equal

The third line changes the value ofabut does not change the value ofb, so they are no
longer equal.

Although multiple assignment is frequently helpful, you should use it with caution. If the
values of variables change frequently, it can make the code difficult to read and debug.


**64 Chapter 7. Iteration**

```
7
```
```
bruce^5
```
```
Figure 7.1: State diagram.
```
### 7.2 Updating variables

One of the most common forms of multiple assignment is an **update** , where the new value
of the variable depends on the old.

x = x+1

This means “get the current value ofx, add one, and then updatexwith the new value.”

If you try to update a variable that doesn’t exist, you get an error, because Python evaluates
the right side before it assigns a value tox:

>>> x = x+1
NameError: name 'x'is not defined

Before you can update a variable, you have to **initialize** it, usually with a simple assign-
ment:

>>> x = 0
>>> x = x+1

Updating a variable by adding 1 is called an **increment** ; subtracting 1 is called a **decrement**.

### 7.3 Thewhilestatement

Computers are often used to automate repetitive tasks. Repeating identical or similar tasks
without making errors is something that computers do well and people do poorly.

We have seen two programs,countdownandprint_n, that use recursion to perform rep-
etition, which is also called **iteration**. Because iteration is so common, Python provides
several language features to make it easier. One is theforstatement we saw in Section 4.2.
We’ll get back to that later.

Another is thewhilestatement. Here is a version ofcountdownthat uses awhilestatement:

def countdown(n):
while n > 0:
print n
n = n-1
print 'Blastoff!'

You can almost read thewhilestatement as if it were English. It means, “Whilenis greater
than 0, display the value ofnand then reduce the value ofnby 1. When you get to 0,
display the wordBlastoff!”

More formally, here is the flow of execution for awhilestatement:

1. Evaluate the condition, yieldingTrueorFalse.


**7.4.** break **65**

2. If the condition is false, exit thewhilestatement and continue execution at the next
    statement.
3. If the condition is true, execute the body and then go back to step 1.

This type of flow is called a **loop** because the third step loops back around to the top.

The body of the loop should change the value of one or more variables so that eventu-
ally the condition becomes false and the loop terminates. Otherwise the loop will repeat
forever, which is called an **infinite loop**. An endless source of amusement for computer
scientists is the observation that the directions on shampoo, “Lather, rinse, repeat,” are an
infinite loop.

In the case ofcountdown, we can prove that the loop terminates because we know that the
value ofnis finite, and we can see that the value ofngets smaller each time through the
loop, so eventually we have to get to 0. In other cases, it is not so easy to tell:

def sequence(n):
while n != 1:
print n,
if n%2 == 0: # n is even
n = n/2
else: # n is odd
n = n*3+1

The condition for this loop isn != 1, so the loop will continue untilnis 1 , which makes
the condition false.

Each time through the loop, the program outputs the value ofnand then checks whether
it is even or odd. If it is even,nis divided by 2. If it is odd, the value ofnis replaced with
n*3+1. For example, if the argument passed tosequenceis 3, the resulting sequence is 3,
10, 5, 16, 8, 4, 2, 1.

Sincensometimes increases and sometimes decreases, there is no obvious proof thatnwill
ever reach 1, or that the program terminates. For some particular values ofn, we can prove
termination. For example, if the starting value is a power of two, then the value ofnwill be
even each time through the loop until it reaches 1. The previous example ends with such a
sequence, starting with 16.

The hard question is whether we can prove that this program terminates forall posi-
tive valuesofn. So far, no one has been able to prove itordisprove it! (Seehttp:
//en.wikipedia.org/wiki/Collatz_conjecture.)
**Exercise 7.1.** Rewrite the functionprint_nfrom Section 5.8 using iteration instead of recursion.

### 7.4 break

Sometimes you don’t know it’s time to end a loop until you get half way through the body.
In that case you can use thebreakstatement to jump out of the loop.

For example, suppose you want to take input from the user until they typedone. You could
write:


**66 Chapter 7. Iteration**

while True:
line = raw_input('> ')
if line == 'done':
break
print line

print 'Done!'

The loop condition isTrue, which is always true, so the loop runs until it hits the break
statement.

Each time through, it prompts the user with an angle bracket. If the user typesdone, the
breakstatement exits the loop. Otherwise the program echoes whatever the user types and
goes back to the top of the loop. Here’s a sample run:

> not done
not done
> done
Done!

This way of writingwhileloops is common because you can check the condition anywhere
in the loop (not just at the top) and you can express the stop condition affirmatively (“stop
when this happens”) rather than negatively (“keep going until that happens.”).

### 7.5 Square roots

Loops are often used in programs that compute numerical results by starting with an ap-
proximate answer and iteratively improving it.

For example, one way of computing square roots is Newton’s method. Suppose that you
want to know the square root ofa. If you start with almost any estimate,x, you can com-
pute a better estimate with the following formula:

```
y=
```
```
x+a/x
2
```
For example, ifais 4 andxis 3:

>>> a = 4.0
>>> x = 3.0
>>> y = (x + a/x) / 2
>>> print y
2.16666666667

Which is closer to the correct answer (

#### √

4 =2). If we repeat the process with the new
estimate, it gets even closer:

>>> x = y
>>> y = (x + a/x) / 2
>>> print y
2.00641025641

After a few more updates, the estimate is almost exact:


**7.6. Algorithms 67**

>>> x = y
>>> y = (x + a/x) / 2
>>> print y
2.00001024003
>>> x = y
>>> y = (x + a/x) / 2
>>> print y
2.00000000003

In general we don’t know ahead of time how many steps it takes to get to the right answer,
but we know when we get there because the estimate stops changing:

>>> x = y
>>> y = (x + a/x) / 2
>>> print y
2.0
>>> x = y
>>> y = (x + a/x) / 2
>>> print y
2.0

Wheny == x, we can stop. Here is a loop that starts with an initial estimate,x, and im-
proves it until it stops changing:

while True:
print x
y = (x + a/x) / 2
if y == x:
break
x = y

For most values ofathis works fine, but in general it is dangerous to testfloatequality.
Floating-point values are only approximately right: most rational numbers, like 1/3, and

irrational numbers, like

#### √

```
2, can’t be represented exactly with afloat.
```
Rather than checking whetherxandyare exactly equal, it is safer to use the built-in func-
tionabsto compute the absolute value, or magnitude, of the difference between them:

```
if abs(y-x) < epsilon:
break
```
Whereepsilonhas a value like0.0000001that determines how close is close enough.
**Exercise 7.2.** Encapsulate this loop in a function calledsquare_rootthat takesaas a parameter,
chooses a reasonable value ofx, and returns an estimate of the square root ofa.

### 7.6 Algorithms

Newton’s method is an example of an **algorithm** : it is a mechanical process for solving a
category of problems (in this case, computing square roots).

It is not easy to define an algorithm. It might help to start with something that is not an
algorithm. When you learned to multiply single-digit numbers, you probably memorized
the multiplication table. In effect, you memorized 100 specific solutions. That kind of
knowledge is not algorithmic.


**68 Chapter 7. Iteration**

But if you were “lazy,” you probably cheated by learning a few tricks. For example, to
find the product ofnand 9, you can writen−1 as the first digit and 10−nas the second
digit. This trick is a general solution for multiplying any single-digit number by 9. That’s
an algorithm!

Similarly, the techniques you learned for addition with carrying, subtraction with borrow-
ing, and long division are all algorithms. One of the characteristics of algorithms is that
they do not require any intelligence to carry out. They are mechanical processes in which
each step follows from the last according to a simple set of rules.

In my opinion, it is embarrassing that humans spend so much time in school learning to
execute algorithms that, quite literally, require no intelligence.

On the other hand, the process of designing algorithms is interesting, intellectually chal-
lenging, and a central part of what we call programming.

Some of the things that people do naturally, without difficulty or conscious thought, are
the hardest to express algorithmically. Understanding natural language is a good example.
We all do it, but so far no one has been able to explainhowwe do it, at least not in the form
of an algorithm.

### 7.7 Debugging

As you start writing bigger programs, you might find yourself spending more time debug-
ging. More code means more chances to make an error and more place for bugs to hide.

One way to cut your debugging time is “debugging by bisection.” For example, if there
are 100 lines in your program and you check them one at a time, it would take 100 steps.

Instead, try to break the problem in half. Look at the middle of the program, or near it, for
an intermediate value you can check. Add aprintstatement (or something else that has a
verifiable effect) and run the program.

If the mid-point check is incorrect, there must be a problem in the first half of the program.
If it is correct, the problem is in the second half.

Every time you perform a check like this, you halve the number of lines you have to search.
After six steps (which is fewer than 100), you would be down to one or two lines of code,
at least in theory.

In practice it is not always clear what the “middle of the program” is and not always pos-
sible to check it. It doesn’t make sense to count lines and find the exact midpoint. Instead,
think about places in the program where there might be errors and places where it is easy
to put a check. Then choose a spot where you think the chances are about the same that
the bug is before or after the check.

### 7.8 Glossary

**multiple assignment:** Making more than one assignment to the same variable during the
execution of a program.


**7.9. Exercises 69**

**update:** An assignment where the new value of the variable depends on the old.

**initialization:** An assignment that gives an initial value to a variable that will be updated.

**increment:** An update that increases the value of a variable (often by one).

**decrement:** An update that decreases the value of a variable.

**iteration:** Repeated execution of a set of statements using either a recursive function call
or a loop.

**infinite loop:** A loop in which the terminating condition is never satisfied.

### 7.9 Exercises

**Exercise 7.3.** To test the square root algorithm in this chapter, you could compare it with
math.sqrt. Write a function namedtest_square_rootthat prints a table like this:

1.0 1.0 1.0 0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0 2.0 0.0
5.0 2.2360679775 2.2360679775 0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0 3.0 0.0

The first column is a number, a; the second column is the square root of a computed with the function
from Section 7.5; the third column is the square root computed bymath.sqrt; the fourth column is
the absolute value of the difference between the two estimates.
**Exercise 7.4.** The built-in functionevaltakes a string and evaluates it using the Python inter-
preter. For example:

>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<type'float'>

Write a function calledeval_loopthat iteratively prompts the user, takes the resulting input and
evaluates it usingeval, and prints the result.

It should continue until the user enters'done', and then return the value of the last expression it
evaluated.
**Exercise 7.5.** The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of1/ _π_ :

#### 1

```
π
```
#### =

#### 2

#### √

#### 2

#### 9801

```
∞
```
### ∑

```
k= 0
```
```
( 4 k)!( 1103 + 26390 k)
(k!)^43964 k
```

**70 Chapter 7. Iteration**

Write a function calledestimate_pithat uses this formula to compute and return an estimate of
_π_. It should use awhileloop to compute terms of the summation until the last term is smaller than
1e-15(which is Python notation for 10 −^15 ). You can check the result by comparing it tomath.pi.

Solution:http: // thinkpython. com/ code/ pi. py.


## Chapter 8

# Strings

### 8.1 A string is a sequence

A string is a **sequence** of characters. You can access the characters one at a time with the
bracket operator:

>>> fruit ='banana'
>>> letter = fruit[1]

The second statement selects character number 1 fromfruitand assigns it toletter.

The expression in brackets is called an **index**. The index indicates which character in the
sequence you want (hence the name).

But you might not get what you expect:

>>> print letter
a

For most people, the first letter of'banana'isb, nota. But for computer scientists, the
index is an offset from the beginning of the string, and the offset of the first letter is zero.

>>> letter = fruit[0]
>>> print letter
b

Sobis the 0th letter (“zero-eth”) of'banana',ais the 1th letter (“one-eth”), andnis the 2th
(“two-eth”) letter.

You can use any expression, including variables and operators, as an index, but the value
of the index has to be an integer. Otherwise you get:

>>> letter = fruit[1.5]
TypeError: string indices must be integers, not float

### 8.2 len

lenis a built-in function that returns the number of characters in a string:


**72 Chapter 8. Strings**

>>> fruit ='banana'
>>> len(fruit)
6

To get the last letter of a string, you might be tempted to try something like this:

>>> length = len(fruit)
>>> last = fruit[length]
IndexError: string index out of range

The reason for theIndexErroris that there is no letter in'banana'with the index 6. Since
we started counting at zero, the six letters are numbered 0 to 5. To get the last character,
you have to subtract 1 fromlength:

>>> last = fruit[length-1]
>>> print last
a

Alternatively, you can use negative indices, which count backward from the end of the
string. The expressionfruit[-1]yields the last letter,fruit[-2]yields the second to last,
and so on.

### 8.3 Traversal with aforloop

A lot of computations involve processing a string one character at a time. Often they start
at the beginning, select each character in turn, do something to it, and continue until the
end. This pattern of processing is called a **traversal**. One way to write a traversal is with a
whileloop:

index = 0
while index < len(fruit):
letter = fruit[index]
print letter
index = index + 1

This loop traverses the string and displays each letter on a line by itself. The loop condition
isindex < len(fruit), so whenindexis equal to the length of the string, the condition is
false, and the body of the loop is not executed. The last character accessed is the one with
the indexlen(fruit)-1, which is the last character in the string.
**Exercise 8.1.** Write a function that takes a string as an argument and displays the letters backward,
one per line.

Another way to write a traversal is with aforloop:

for char in fruit:
print char

Each time through the loop, the next character in the string is assigned to the variablechar.
The loop continues until no characters are left.

The following example shows how to use concatenation (string addition) and aforloop
to generate an abecedarian series (that is, in alphabetical order). In Robert McCloskey’s
bookMake Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack,
Ouack, Pack, and Quack. This loop outputs these names in order:


**8.4. String slices 73**

### fruit b a n na a ’

```
index 0 1 2 3 4 5 6
```
### ’

```
Figure 8.1: Slice indices.
```
prefixes ='JKLMNOPQ'
suffix ='ack'

for letter in prefixes:
print letter + suffix

The output is:

Jack
Kack
Lack
Mack
Nack
Oack
Pack
Qack

Of course, that’s not quite right because “Ouack” and “Quack” are misspelled.
**Exercise 8.2.** Modify the program to fix this error.

### 8.4 String slices

A segment of a string is called a **slice**. Selecting a slice is similar to selecting a character:

>>> s ='Monty Python'
>>> print s[0:5]
Monty
>>> print s[6:12]
Python

The operator[n:m]returns the part of the string from the “n-eth” character to the “m-eth”
character, including the first but excluding the last. This behavior is counterintuitive, but
it might help to imagine the indices pointingbetweenthe characters, as in Figure 8.1.

If you omit the first index (before the colon), the slice starts at the beginning of the string.
If you omit the second index, the slice goes to the end of the string:

>>> fruit ='banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'

If the first index is greater than or equal to the second the result is an **empty string** , repre-
sented by two quotation marks:

>>> fruit ='banana'
>>> fruit[3:3]
''


**74 Chapter 8. Strings**

An empty string contains no characters and has length 0, but other than that, it is the same
as any other string.
**Exercise 8.3.** Given thatfruitis a string, what doesfruit[:]mean?

### 8.5 Strings are immutable

It is tempting to use the[]operator on the left side of an assignment, with the intention of
changing a character in a string. For example:

>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
TypeError: 'str'object does not support item assignment

The “object” in this case is the string and the “item” is the character you tried to assign. For
now, an **object** is the same thing as a value, but we will refine that definition later. An **item**
is one of the values in a sequence.

The reason for the error is that strings are **immutable** , which means you can’t change an
existing string. The best you can do is create a new string that is a variation on the original:

>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print new_greeting
Jello, world!

This example concatenates a new first letter onto a slice ofgreeting. It has no effect on the
original string.

### 8.6 Searching

What does the following function do?

def find(word, letter):
index = 0
while index < len(word):
if word[index] == letter:
return index
index = index + 1
return -1

In a sense,findis the opposite of the[]operator. Instead of taking an index and extracting
the corresponding character, it takes a character and finds the index where that character
appears. If the character is not found, the function returns-1.

This is the first example we have seen of areturnstatement inside a loop. Ifword[index]
== letter, the function breaks out of the loop and returns immediately.

If the character doesn’t appear in the string, the program exits the loop normally and re-
turns-1.

This pattern of computation—traversing a sequence and returning when we find what we
are looking for—is called a **search**.
**Exercise 8.4.** Modifyfindso that it has a third parameter, the index inwordwhere it should start
looking.


**8.7. Looping and counting 75**

### 8.7 Looping and counting

The following program counts the number of times the letteraappears in a string:

word ='banana'
count = 0
for letter in word:
if letter =='a':
count = count + 1
print count

This program demonstrates another pattern of computation called a **counter**. The variable
countis initialized to 0 and then incremented each time anais found. When the loop exits,
countcontains the result—the total number ofa’s.
**Exercise 8.5.** Encapsulate this code in a function namedcount, and generalize it so that it accepts
the string and the letter as arguments.
**Exercise 8.6.** Rewrite this function so that instead of traversing the string, it uses the three-
parameter version offindfrom the previous section.

### 8.8 String methods

A **method** is similar to a function—it takes arguments and returns a value—but the syntax
is different. For example, the methoduppertakes a string and returns a new string with all
uppercase letters:

Instead of the function syntaxupper(word), it uses the method syntaxword.upper().

>>> word ='banana'
>>> new_word = word.upper()
>>> print new_word
BANANA

This form of dot notation specifies the name of the method,upper, and the name of the
string to apply the method to,word. The empty parentheses indicate that this method
takes no argument.

A method call is called an **invocation** ; in this case, we would say that we are invoking
upperon theword.

As it turns out, there is a string method namedfindthat is remarkably similar to the
function we wrote:

>>> word ='banana'
>>> index = word.find('a')
>>> print index
1

In this example, we invokefindonwordand pass the letter we are looking for as a param-
eter.

Actually, thefindmethod is more general than our function; it can find substrings, not just
characters:

>>> word.find('na')
2


**76 Chapter 8. Strings**

It can take as a second argument the index where it should start:

>>> word.find('na', 3)
4

And as a third argument the index where it should stop:

>>> name = 'bob'
>>> name.find('b', 1, 2)
-1

This search fails becausebdoes not appear in the index range from 1 to 2 (not including 2 ).
**Exercise 8.7.** There is a string method calledcountthat is similar to the function in the previous
exercise. Read the documentation of this method and write an invocation that counts the number of
as in'banana'.
**Exercise 8.8.** Read the documentation of the string methods athttp: // docs. python. org/ 2/
library/ stdtypes. html# string- methods. You might want to experiment with some of them
to make sure you understand how they work.stripandreplaceare particularly useful.

The documentation uses a syntax that might be confusing. For example, in
find(sub[, start[, end]]), the brackets indicate optional arguments. Sosubis required, but
startis optional, and if you includestart, thenendis optional.

### 8.9 Theinoperator

The wordinis a boolean operator that takes two strings and returnsTrueif the first ap-
pears as a substring in the second:

>>>'a'in 'banana'
True
>>>'seed' in 'banana'
False

For example, the following function prints all the letters fromword1that also appear in
word2:

def in_both(word1, word2):
for letter in word1:
if letter in word2:
print letter

With well-chosen variable names, Python sometimes reads like English. You could read
this loop, “for (each) letter in (the first) word, if (the) letter (appears) in (the second) word,
print (the) letter.”

Here’s what you get if you compare apples and oranges:

>>> in_both('apples','oranges')
a
e
s

### 8.10 String comparison

The relational operators work on strings. To see if two strings are equal:


**8.11. Debugging 77**

if word =='banana':
print'All right, bananas.'

Other relational operations are useful for putting words in alphabetical order:

if word <'banana':
print'Your word,' + word +', comes before banana.'
elif word >'banana':
print'Your word,' + word +', comes after banana.'
else:
print'All right, bananas.'

Python does not handle uppercase and lowercase letters the same way that people do. All
the uppercase letters come before all the lowercase letters, so:

Your word, Pineapple, comes before banana.

A common way to address this problem is to convert strings to a standard format, such as
all lowercase, before performing the comparison. Keep that in mind in case you have to
defend yourself against a man armed with a Pineapple.

### 8.11 Debugging

When you use indices to traverse the values in a sequence, it is tricky to get the beginning
and end of the traversal right. Here is a function that is supposed to compare two words
and returnTrueif one of the words is the reverse of the other, but it contains two errors:

def is_reverse(word1, word2):
if len(word1) != len(word2):
return False

```
i = 0
j = len(word2)
```
```
while j > 0:
if word1[i] != word2[j]:
return False
i = i+1
j = j-1
```
```
return True
```
The firstifstatement checks whether the words are the same length. If not, we can return
Falseimmediately and then, for the rest of the function, we can assume that the words are
the same length. This is an example of the guardian pattern in Section 6.8.

iandjare indices:itraversesword1forward whilejtraversesword2backward. If we
find two letters that don’t match, we can returnFalseimmediately. If we get through the
whole loop and all the letters match, we returnTrue.

If we test this function with the words “pots” and “stop”, we expect the return valueTrue,
but we get an IndexError:

>>> is_reverse('pots', 'stop')
...


**78 Chapter 8. Strings**

```
i 0 j 3
```
```
word1 ’pots’ word2 ’stop’
```
```
Figure 8.2: State diagram.
```
File "reverse.py", line 15, in is_reverse
if word1[i] != word2[j]:
IndexError: string index out of range

For debugging this kind of error, my first move is to print the values of the indices imme-
diately before the line where the error appears.

```
while j > 0:
print i, j # print here
```
```
if word1[i] != word2[j]:
return False
i = i+1
j = j-1
```
Now when I run the program again, I get more information:

>>> is_reverse('pots', 'stop')
0 4

IndexError: string index out of range

The first time through the loop, the value of jis 4, which is out of range for the
string'pots'. The index of the last character is 3, so the initial value forjshould be
len(word2)-1.

If I fix that error and run the program again, I get:

>>> is_reverse('pots', 'stop')
0 3
1 2
2 1
True

This time we get the right answer, but it looks like the loop only ran three times, which is
suspicious. To get a better idea of what is happening, it is useful to draw a state diagram.
During the first iteration, the frame foris_reverseis shows in Figure 8.2.

I took a little license by arranging the variables in the frame and adding dotted lines to
show that the values ofiandjindicate characters inword1andword2.
**Exercise 8.9.** Starting with this diagram, execute the program on paper, changing the values ofi
andjduring each iteration. Find and fix the second error in this function.

### 8.12 Glossary

**object:** Something a variable can refer to. For now, you can use “object” and “value”
interchangeably.


**8.13. Exercises 79**

**sequence:** An ordered set; that is, a set of values where each value is identified by an
integer index.

**item:** One of the values in a sequence.

**index:** An integer value used to select an item in a sequence, such as a character in a string.

**slice:** A part of a string specified by a range of indices.

**empty string:** A string with no characters and length 0, represented by two quotation
marks.

**immutable:** The property of a sequence whose items cannot be assigned.

**traverse:** To iterate through the items in a sequence, performing a similar operation on
each.

**search:** A pattern of traversal that stops when it finds what it is looking for.

**counter:** A variable used to count something, usually initialized to zero and then incre-
mented.

**method:** A function that is associated with an object and called using dot notation.

**invocation:** A statement that calls a method.

### 8.13 Exercises

**Exercise 8.10.** A string slice can take a third index that specifies the “step size;” that is, the number
of spaces between successive characters. A step size of 2 means every other character; 3 means every
third, etc.

>>> fruit ='banana'
>>> fruit[0:5:2]
'bnn'

A step size of -1 goes through the word backwards, so the slice[::-1]generates a reversed string.

Use this idiom to write a one-line version ofis_palindromefrom Exercise 6.6.
**Exercise 8.11.** The following functions are allintendedto check whether a string contains any
lowercase letters, but at least some of them are wrong. For each function, describe what the function
actually does (assuming that the parameter is a string).

def any_lowercase1(s):
for c in s:
if c.islower():
return True
else:
return False

def any_lowercase2(s):
for c in s:
if 'c'.islower():
return 'True'


**80 Chapter 8. Strings**

```
else:
return 'False'
```
def any_lowercase3(s):
for c in s:
flag = c.islower()
return flag

def any_lowercase4(s):
flag = False
for c in s:
flag = flag or c.islower()
return flag

def any_lowercase5(s):
for c in s:
if not c.islower():
return False
return True
**Exercise 8.12.** ROT13 is a weak form of encryption that involves “rotating” each letter in a word
by 13 places. To rotate a letter means to shift it through the alphabet, wrapping around to the
beginning if necessary, so ’A’ shifted by 3 is ’D’ and ’Z’ shifted by 1 is ’A’.

Write a function calledrotate_wordthat takes a string and an integer as parameters, and that
returns a new string that contains the letters from the original string “rotated” by the given amount.

For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.

You might want to use the built-in functionsord, which converts a character to a numeric code,
andchr, which converts numeric codes to characters.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13. If you are not easily
offended, find and decode some of them. Solution:http: // thinkpython. com/ code/ rotate.
py.


## Chapter 9

# Case study: word play

### 9.1 Reading word lists

For the exercises in this chapter we need a list of English words. There are lots of word
lists available on the Web, but the one most suitable for our purpose is one of the word lists
collected and contributed to the public domain by Grady Ward as part of the Moby lexi-
con project (seehttp://wikipedia.org/wiki/Moby_Project). It is a list of 113,809 official
crosswords; that is, words that are considered valid in crossword puzzles and other word
games. In the Moby collection, the filename is113809of.fic; you can download a copy,
with the simpler namewords.txt, fromhttp://thinkpython.com/code/words.txt.

This file is in plain text, so you can open it with a text editor, but you can also read it from
Python. The built-in functionopentakes the name of the file as a parameter and returns a
**file object** you can use to read the file.

>>> fin = open('words.txt')
>>> print fin
<open file'words.txt', mode'r'at 0xb7f4b380>

finis a common name for a file object used for input. Mode'r'indicates that this file is
open for reading (as opposed to'w'for writing).

The file object provides several methods for reading, includingreadline, which reads
characters from the file until it gets to a newline and returns the result as a string:

>>> fin.readline()
'aa\r\n'

The first word in this particular list is “aa,” which is a kind of lava. The sequence\r\n
represents two whitespace characters, a carriage return and a newline, that separate this
word from the next.

The file object keeps track of where it is in the file, so if you callreadlineagain, you get
the next word:

>>> fin.readline()
'aah\r\n'

The next word is “aah,” which is a perfectly legitimate word, so stop looking at me like
that. Or, if it’s the whitespace that’s bothering you, we can get rid of it with the string
methodstrip:


**82 Chapter 9. Case study: word play**

>>> line = fin.readline()
>>> word = line.strip()
>>> print word
aahed

You can also use a file object as part of aforloop. This program readswords.txtand
prints each word, one per line:

fin = open('words.txt')
for line in fin:
word = line.strip()
print word
**Exercise 9.1.** Write a program that readswords.txtand prints only the words with more than 20
characters (not counting whitespace).

### 9.2 Exercises

There are solutions to these exercises in the next section. You should at least attempt each
one before you read the solutions.
**Exercise 9.2.** In 1939 Ernest Vincent Wright published a 50,000 word novel calledGadsbythat
does not contain the letter “e.” Since “e” is the most common letter in English, that’s not easy to
do.

In fact, it is difficult to construct a solitary thought without using that most common symbol. It is
slow going at first, but with caution and hours of training you can gradually gain facility.

All right, I’ll stop now.

Write a function calledhas_no_ethat returnsTrueif the given word doesn’t have the letter “e” in
it.

Modify your program from the previous section to print only the words that have no “e” and com-
pute the percentage of the words in the list have no “e.”
**Exercise 9.3.** Write a function namedavoidsthat takes a word and a string of forbidden letters,
and that returnsTrueif the word doesn’t use any of the forbidden letters.

Modify your program to prompt the user to enter a string of forbidden letters and then print the
number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
that excludes the smallest number of words?
**Exercise 9.4.** Write a function nameduses_onlythat takes a word and a string of letters, and
that returnsTrueif the word contains only letters in the list. Can you make a sentence using only
the lettersacefhlo? Other than “Hoe alfalfa?”
**Exercise 9.5.** Write a function nameduses_allthat takes a word and a string of required letters,
and that returnsTrueif the word uses all the required letters at least once. How many words are
there that use all the vowelsaeiou? How aboutaeiouy?
**Exercise 9.6.** Write a function calledis_abecedarianthat returnsTrueif the letters in a word
appear in alphabetical order (double letters are ok). How many abecedarian words are there?

### 9.3 Search

All of the exercises in the previous section have something in common; they can be solved
with the search pattern we saw in Section 8.6. The simplest example is:


**9.4. Looping with indices 83**

def has_no_e(word):
for letter in word:
if letter =='e':
return False
return True

Theforloop traverses the characters inword. If we find the letter “e”, we can immediately
returnFalse; otherwise we have to go to the next letter. If we exit the loop normally, that
means we didn’t find an “e”, so we returnTrue.

avoidsis a more general version ofhas_no_ebut it has the same structure:

def avoids(word, forbidden):
for letter in word:
if letter in forbidden:
return False
return True

We can returnFalseas soon as we find a forbidden letter; if we get to the end of the loop,
we returnTrue.

uses_onlyis similar except that the sense of the condition is reversed:

def uses_only(word, available):
for letter in word:
if letter not in available:
return False
return True

Instead of a list of forbidden letters, we have a list of available letters. If we find a letter in
wordthat is not inavailable, we can returnFalse.

uses_allis similar except that we reverse the role of the word and the string of letters:

def uses_all(word, required):
for letter in required:
if letter not in word:
return False
return True

Instead of traversing the letters inword, the loop traverses the required letters. If any of the
required letters do not appear in the word, we can returnFalse.

If you were really thinking like a computer scientist, you would have recognized that
uses_allwas an instance of a previously-solved problem, and you would have written:

def uses_all(word, required):
return uses_only(required, word)

This is an example of a program development method called **problem recognition** , which
means that you recognize the problem you are working on as an instance of a previously-
solved problem, and apply a previously-developed solution.

### 9.4 Looping with indices

I wrote the functions in the previous section withforloops because I only needed the
characters in the strings; I didn’t have to do anything with the indices.


**84 Chapter 9. Case study: word play**

Foris_abecedarianwe have to compare adjacent letters, which is a little tricky with afor
loop:

def is_abecedarian(word):
previous = word[0]
for c in word:
if c < previous:
return False
previous = c
return True

An alternative is to use recursion:

def is_abecedarian(word):
if len(word) <= 1:
return True
if word[0] > word[1]:
return False
return is_abecedarian(word[1:])

Another option is to use awhileloop:

def is_abecedarian(word):
i = 0
while i < len(word)-1:
if word[i+1] < word[i]:
return False
i = i+1
return True

The loop starts ati=0and ends wheni=len(word)-1. Each time through the loop, it com-
pares theith character (which you can think of as the current character) to thei+1th
character (which you can think of as the next).

If the next character is less than (alphabetically before) the current one, then we have dis-
covered a break in the abecedarian trend, and we returnFalse.

If we get to the end of the loop without finding a fault, then the word passes the test. To
convince yourself that the loop ends correctly, consider an example like'flossy'. The
length of the word is 6, so the last time the loop runs is wheniis 4, which is the index of
the second-to-last character. On the last iteration, it compares the second-to-last character
to the last, which is what we want.

Here is a version ofis_palindrome(see Exercise 6.6) that uses two indices; one starts at
the beginning and goes up; the other starts at the end and goes down.

def is_palindrome(word):
i = 0
j = len(word)-1

```
while i<j:
if word[i] != word[j]:
return False
i = i+1
j = j-1
```
```
return True
```

**9.5. Debugging 85**

Or, if you noticed that this is an instance of a previously-solved problem, you might have
written:

def is_palindrome(word):
return is_reverse(word, word)

Assuming you did Exercise 8.9.

### 9.5 Debugging

Testing programs is hard. The functions in this chapter are relatively easy to test because
you can check the results by hand. Even so, it is somewhere between difficult and impos-
sible to choose a set of words that test for all possible errors.

Takinghas_no_eas an example, there are two obvious cases to check: words that have an
’e’ should returnFalse; words that don’t should returnTrue. You should have no trouble
coming up with one of each.

Within each case, there are some less obvious subcases. Among the words that have an
“e,” you should test words with an “e” at the beginning, the end, and somewhere in the
middle. You should test long words, short words, and very short words, like the empty
string. The empty string is an example of a **special case** , which is one of the non-obvious
cases where errors often lurk.

In addition to the test cases you generate, you can also test your program with a word list
likewords.txt. By scanning the output, you might be able to catch errors, but be careful:
you might catch one kind of error (words that should not be included, but are) and not
another (words that should be included, but aren’t).

In general, testing can help you find bugs, but it is not easy to generate a good set of test
cases, and even if you do, you can’t be sure your program is correct.

According to a legendary computer scientist:

```
Program testing can be used to show the presence of bugs, but never to show
their absence!
— Edsger W. Dijkstra
```
### 9.6 Glossary

**file object:** A value that represents an open file.

**problem recognition:** A way of solving a problem by expressing it as an instance of a
previously-solved problem.

**special case:** A test case that is atypical or non-obvious (and less likely to be handled cor-
rectly).


**86 Chapter 9. Case study: word play**

### 9.7 Exercises

**Exercise 9.7.** This question is based on a Puzzler that was broadcast on the radio programCar
Talk(http: // [http://www.](http://www.) cartalk. com/ content/ puzzlers):

```
Give me a word with three consecutive double letters. I’ll give you a couple of words
that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-
p-p-i. If you could take out those i’s it would work. But there is a word that has three
consecutive pairs of letters and to the best of my knowledge this may be the only word.
Of course there are probably 500 more but I can only think of one. What is the word?
```
Write a program to find it. Solution:http: // thinkpython. com/ code/ cartalk1. py.
**Exercise 9.8.** Here’s another Car Talk Puzzler (http: // [http://www.](http://www.) cartalk. com/ content/
puzzlers):

```
“I was driving on the highway the other day and I happened to notice my odometer.
Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
miles, for example, I’d see 3-0-0-0-0-0.
“Now, what I saw that day was very interesting. I noticed that the last 4 digits were
palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
palindrome, so my odometer could have read 3-1-5-4-4-5.
“One mile later, the last 5 numbers were palindromic. For example, it could have read
3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
you ready for this? One mile later, all 6 were palindromic!
“The question is, what was on the odometer when I first looked?”
```
Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy
these requirements. Solution:http: // thinkpython. com/ code/ cartalk2. py.
**Exercise 9.9.** Here’s anotherCar TalkPuzzler you can solve with a search (http: // [http://www.](http://www.)
cartalk. com/ content/ puzzlers):

```
“Recently I had a visit with my mom and we realized that the two digits that make
up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
wondered how often this has happened over the years but we got sidetracked with other
topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible six times
so far. I also figured out that if we’re lucky it would happen again in a few years, and
if we’re really lucky it would happen one more time after that. In other words, it would
have happened 8 times over all. So the question is, how old am I now?”
```
Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string
methodzfilluseful.

Solution:http: // thinkpython. com/ code/ cartalk3. py.


## Chapter 10

# Lists

### 10.1 A list is a sequence

Like a string, a **list** is a sequence of values. In a string, the values are characters; in a list,
they can be any type. The values in a list are called **elements** or sometimes **items**.

There are several ways to create a new list; the simplest is to enclose the elements in square
brackets ([and]):

[10, 20, 30, 40]
['crunchy frog','ram bladder', 'lark vomit']

The first example is a list of four integers. The second is a list of three strings. The elements
of a list don’t have to be the same type. The following list contains a string, a float, an
integer, and (lo!) another list:

['spam', 2.0, 5, [10, 20]]

A list within another list is **nested**.

A list that contains no elements is called an empty list; you can create one with empty
brackets,[].

As you might expect, you can assign list values to variables:

>>> cheeses = ['Cheddar', 'Edam','Gouda']
>>> numbers = [17, 123]
>>> empty = []
>>> print cheeses, numbers, empty
['Cheddar','Edam','Gouda'] [17, 123] []

### 10.2 Lists are mutable

The syntax for accessing the elements of a list is the same as for accessing the characters
of a string—the bracket operator. The expression inside the brackets specifies the index.
Remember that the indices start at 0:

>>> print cheeses[0]
Cheddar


**88 Chapter 10. Lists**

```
0
1
```
```
list
numbers 17
123
5
```
```
list
empty
```
```
0
1
2
```
```
’Cheddar’
’Edam’
’Gouda’
```
```
list
cheeses
```
```
Figure 10.1: State diagram.
```
Unlike strings, lists are mutable. When the bracket operator appears on the left side of an
assignment, it identifies the element of the list that will be assigned.

>>> numbers = [17, 123]
>>> numbers[1] = 5
>>> print numbers
[17, 5]

The one-eth element ofnumbers, which used to be 123, is now 5.

You can think of a list as a relationship between indices and elements. This relationship is
called a **mapping** ; each index “maps to” one of the elements. Figure 10.1 shows the state
diagram forcheeses,numbersandempty:

Lists are represented by boxes with the word “list” outside and the elements of the list
inside. cheesesrefers to a list with three elements indexed 0, 1 and 2.numberscontains
two elements; the diagram shows that the value of the second element has been reassigned
from 123 to 5.emptyrefers to a list with no elements.

List indices work the same way as string indices:

- Any integer expression can be used as an index.
- If you try to read or write an element that does not exist, you get anIndexError.
- If an index has a negative value, it counts backward from the end of the list.

Theinoperator also works on lists.

>>> cheeses = ['Cheddar','Edam','Gouda']
>>>'Edam' in cheeses
True
>>>'Brie' in cheeses
False


**10.3. Traversing a list 89**

### 10.3 Traversing a list

The most common way to traverse the elements of a list is with aforloop. The syntax is
the same as for strings:

for cheese in cheeses:
print cheese

This works well if you only need to read the elements of the list. But if you want to write
or update the elements, you need the indices. A common way to do that is to combine the
functionsrangeandlen:

for i in range(len(numbers)):
numbers[i] = numbers[i] * 2

This loop traverses the list and updates each element.lenreturns the number of elements
in the list.rangereturns a list of indices from 0 ton−1, wherenis the length of the list.
Each time through the loopigets the index of the next element. The assignment statement
in the body usesito read the old value of the element and to assign the new value.

Aforloop over an empty list never executes the body:

for x in []:
print'This never happens.'

Although a list can contain another list, the nested list still counts as a single element. The
length of this list is four:

['spam', 1, ['Brie','Roquefort','Pol le Veq'], [1, 2, 3]]

### 10.4 List operations

The+operator concatenates lists:

>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print c
[1, 2, 3, 4, 5, 6]

Similarly, the*operator repeats a list a given number of times:

>>> [0] * 4
[0, 0, 0, 0]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

The first example repeats[0]four times. The second example repeats the list[1, 2, 3]
three times.

### 10.5 List slices

The slice operator also works on lists:


**90 Chapter 10. Lists**

>>> t = ['a', 'b', 'c', 'd','e','f']
>>> t[1:3]
['b', 'c']
>>> t[:4]
['a', 'b', 'c','d']
>>> t[3:]
['d', 'e', 'f']

If you omit the first index, the slice starts at the beginning. If you omit the second, the slice
goes to the end. So if you omit both, the slice is a copy of the whole list.

>>> t[:]
['a', 'b', 'c','d','e','f']

Since lists are mutable, it is often useful to make a copy before performing operations that
fold, spindle or mutilate lists.

A slice operator on the left side of an assignment can update multiple elements:

>>> t = ['a', 'b', 'c', 'd','e','f']
>>> t[1:3] = ['x', 'y']
>>> print t
['a', 'x', 'y','d','e','f']

### 10.6 List methods

Python provides methods that operate on lists. For example,appendadds a new element
to the end of a list:

>>> t = ['a', 'b', 'c']
>>> t.append('d')
>>> print t
['a', 'b', 'c','d']

extendtakes a list as an argument and appends all of the elements:

>>> t1 = ['a', 'b','c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> print t1
['a', 'b', 'c','d','e']

This example leavest2unmodified.

sortarranges the elements of the list from low to high:

>>> t = ['d', 'c', 'e', 'b','a']
>>> t.sort()
>>> print t
['a', 'b', 'c','d','e']

List methods are all void; they modify the list and returnNone. If you accidentally writet
= t.sort(), you will be disappointed with the result.


**10.7. Map, filter and reduce 91**

### 10.7 Map, filter and reduce

To add up all the numbers in a list, you can use a loop like this:

def add_all(t):
total = 0
for x in t:
total += x
return total

totalis initialized to 0. Each time through the loop,xgets one element from the list.
The+=operator provides a short way to update a variable. This **augmented assignment
statement** :

```
total += x
```
is equivalent to:

```
total = total + x
```
As the loop executes,totalaccumulates the sum of the elements; a variable used this way
is sometimes called an **accumulator**.

Adding up the elements of a list is such a common operation that Python provides it as a
built-in function,sum:

>>> t = [1, 2, 3]
>>> sum(t)
6

An operation like this that combines a sequence of elements into a single value is some-
times called **reduce**.
**Exercise 10.1.** Write a function callednested_sumthat takes a nested list of integers and add up
the elements from all of the nested lists.

Sometimes you want to traverse one list while building another. For example, the following
function takes a list of strings and returns a new list that contains capitalized strings:

def capitalize_all(t):
res = []
for s in t:
res.append(s.capitalize())
return res

resis initialized with an empty list; each time through the loop, we append the next ele-
ment. Soresis another kind of accumulator.

An operation likecapitalize_allis sometimes called a **map** because it “maps” a function
(in this case the methodcapitalize) onto each of the elements in a sequence.
**Exercise 10.2.** Usecapitalize_allto write a function namedcapitalize_nestedthat takes
a nested list of strings and returns a new nested list with all strings capitalized.

Another common operation is to select some of the elements from a list and return a sublist.
For example, the following function takes a list of strings and returns a list that contains
only the uppercase strings:

def only_upper(t):
res = []
for s in t:


**92 Chapter 10. Lists**

```
if s.isupper():
res.append(s)
return res
```
isupperis a string method that returnsTrueif the string contains only upper case letters.

An operation likeonly_upperis called a **filter** because it selects some of the elements and
filters out the others.

Most common list operations can be expressed as a combination of map, filter and reduce.
Because these operations are so common, Python provides language features to support
them, including the built-in functionmapand an operator called a “list comprehension.”
**Exercise 10.3.** Write a function that takes a list of numbers and returns the cumulative sum; that
is, a new list where the ith element is the sum of the first i+ 1 elements from the original list. For
example, the cumulative sum of[1, 2, 3]is[1, 3, 6].

### 10.8 Deleting elements

There are several ways to delete elements from a list. If you know the index of the element
you want, you can usepop:

>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> print t
['a', 'c']
>>> print x
b

popmodifies the list and returns the element that was removed. If you don’t provide an
index, it deletes and returns the last element.

If you don’t need the removed value, you can use thedeloperator:

>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> print t
['a', 'c']

If you know the element you want to remove (but not the index), you can useremove:

>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> print t
['a', 'c']

The return value fromremoveisNone.

To remove more than one element, you can usedelwith a slice index:

>>> t = ['a', 'b', 'c', 'd','e','f']
>>> del t[1:5]
>>> print t
['a', 'f']

As usual, the slice selects all the elements up to, but not including, the second index.
**Exercise 10.4.** Write a function calledmiddlethat takes a list and returns a new list that contains
all but the first and last elements. Somiddle([1,2,3,4])should return[2,3].
**Exercise 10.5.** Write a function calledchopthat takes a list, modifies it by removing the first and
last elements, and returnsNone.


**10.9. Lists and strings 93**

### 10.9 Lists and strings

A string is a sequence of characters and a list is a sequence of values, but a list of characters
is not the same as a string. To convert from a string to a list of characters, you can uselist:

>>> s ='spam'
>>> t = list(s)
>>> print t
['s','p','a','m']

Becauselistis the name of a built-in function, you should avoid using it as a variable
name. I also avoidlbecause it looks too much like 1. So that’s why I uset.

Thelistfunction breaks a string into individual letters. If you want to break a string into
words, you can use thesplitmethod:

>>> s ='pining for the fjords'
>>> t = s.split()
>>> print t
['pining','for', 'the','fjords']

An optional argument called a **delimiter** specifies which characters to use as word bound-
aries. The following example uses a hyphen as a delimiter:

>>> s ='spam-spam-spam'
>>> delimiter ='-'
>>> s.split(delimiter)
['spam', 'spam','spam']

joinis the inverse ofsplit. It takes a list of strings and concatenates the elements.joinis
a string method, so you have to invoke it on the delimiter and pass the list as a parameter:

>>> t = ['pining', 'for', 'the','fjords']
>>> delimiter =''
>>> delimiter.join(t)
'pining for the fjords'

In this case the delimiter is a space character, sojoinputs a space between words. To
concatenate strings without spaces, you can use the empty string,'', as a delimiter.

### 10.10 Objects and values

If we execute these assignment statements:

a ='banana'
b ='banana'

We know thataandbboth refer to a string, but we don’t know whether they refer to the
samestring. There are two possible states, shown in Figure 10.2.

In one case,aandbrefer to two different objects that have the same value. In the second
case, they refer to the same object.

To check whether two variables refer to the same object, you can use theisoperator.


**94 Chapter 10. Lists**

```
a
b
```
```
’banana’
```
```
a
b
```
```
’banana’
’banana’
```
```
Figure 10.2: State diagram.
```
```
a
b
```
```
[ 1, 2, 3 ]
[ 1, 2, 3 ]
```
```
Figure 10.3: State diagram.
```
>>> a ='banana'
>>> b ='banana'
>>> a is b
True

In this example, Python only created one string object, and bothaandbrefer to it.

But when you create two lists, you get two objects:

>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a is b
False

So the state diagram looks like Figure 10.3.

In this case we would say that the two lists are **equivalent** , because they have the same el-
ements, but not **identical** , because they are not the same object. If two objects are identical,
they are also equivalent, but if they are equivalent, they are not necessarily identical.

Until now, we have been using “object” and “value” interchangeably, but it is more precise
to say that an object has a value. If you execute[1,2,3], you get a list object whose value is
a sequence of integers. If another list has the same elements, we say it has the same value,
but it is not the same object.

### 10.11 Aliasing

Ifarefers to an object and you assignb = a, then both variables refer to the same object:

>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True

The state diagram looks like Figure 10.4.

The association of a variable with an object is called a **reference**. In this example, there are
two references to the same object.

An object with more than one reference has more than one name, so we say that the object
is **aliased**.

If the aliased object is mutable, changes made with one alias affect the other:


**10.12. List arguments 95**

```
a
b
```
```
[ 1, 2, 3 ]
```
```
Figure 10.4: State diagram.
```
```
0
1
2
```
```
’a’
’b’
’c’
```
```
list
```
```
t
```
```
letters
```
```
delete_head
```
```
<module>
```
```
Figure 10.5: Stack diagram.
```
>>> b[0] = 17
>>> print a
[17, 2, 3]

Although this behavior can be useful, it is error-prone. In general, it is safer to avoid
aliasing when you are working with mutable objects.

For immutable objects like strings, aliasing is not as much of a problem. In this example:

a ='banana'
b ='banana'

It almost never makes a difference whetheraandbrefer to the same string or not.

### 10.12 List arguments

When you pass a list to a function, the function gets a reference to the list. If the function
modifies a list parameter, the caller sees the change. For example,delete_headremoves
the first element from a list:

def delete_head(t):
del t[0]

Here’s how it is used:

>>> letters = ['a','b','c']
>>> delete_head(letters)
>>> print letters
['b','c']

The parametertand the variablelettersare aliases for the same object. The stack diagram
looks like Figure 10.5.

Since the list is shared by two frames, I drew it between them.

It is important to distinguish between operations that modify lists and operations that cre-
ate new lists. For example, theappendmethod modifies a list, but the+operator creates a
new list:

>>> t1 = [1, 2]
>>> t2 = t1.append(3)


**96 Chapter 10. Lists**

>>> print t1
[1, 2, 3]
>>> print t2
None

>>> t3 = t1 + [4]
>>> print t3
[1, 2, 3, 4]

This difference is important when you write functions that are supposed to modify lists.
For example, this functiondoes notdelete the head of a list:

def bad_delete_head(t):
t = t[1:] # WRONG!

The slice operator creates a new list and the assignment makestrefer to it, but none of that
has any effect on the list that was passed as an argument.

An alternative is to write a function that creates and returns a new list. For example,tail
returns all but the first element of a list:

def tail(t):
return t[1:]

This function leaves the original list unmodified. Here’s how it is used:

>>> letters = ['a','b','c']
>>> rest = tail(letters)
>>> print rest
['b', 'c']

### 10.13 Debugging

Careless use of lists (and other mutable objects) can lead to long hours of debugging. Here
are some common pitfalls and ways to avoid them:

1. Don’t forget that most list methods modify the argument and returnNone. This is
    the opposite of the string methods, which return a new string and leave the original
    alone.
    If you are used to writing string code like this:

```
word = word.strip()
```
```
It is tempting to write list code like this:
```
```
t = t.sort() # WRONG!
```
```
BecausesortreturnsNone, the next operation you perform withtis likely to fail.
Before using list methods and operators, you should read the documentation care-
fully and then test them in interactive mode. The methods and operators that lists
share with other sequences (like strings) are documented athttp://docs.python.
org/2/library/stdtypes.html#typesseq. The methods and operators that only ap-
ply to mutable sequences are documented athttp://docs.python.org/2/library/
stdtypes.html#typesseq- mutable.
```

**10.14. Glossary 97**

2. Pick an idiom and stick with it.
    Part of the problem with lists is that there are too many ways to do things. For exam-
    ple, to remove an element from a list, you can usepop,remove,del, or even a slice
    assignment.
    To add an element, you can use theappendmethod or the+operator. Assuming that
    tis a list andxis a list element, these are right:

```
t.append(x)
t = t + [x]
```
```
And these are wrong:
```
```
t.append([x]) # WRONG!
t = t.append(x) # WRONG!
t + [x] # WRONG!
t = t + x # WRONG!
```
```
Try out each of these examples in interactive mode to make sure you understand
what they do. Notice that only the last one causes a runtime error; the other three are
legal, but they do the wrong thing.
```
3. Make copies to avoid aliasing.
    If you want to use a method likesortthat modifies the argument, but you need to
    keep the original list as well, you can make a copy.

```
orig = t[:]
t.sort()
```
```
In this example you could also use the built-in functionsorted, which returns a new,
sorted list and leaves the original alone. But in that case you should avoid using
sortedas a variable name!
```
### 10.14 Glossary

**list:** A sequence of values.

**element:** One of the values in a list (or other sequence), also called items.

**index:** An integer value that indicates an element in a list.

**nested list:** A list that is an element of another list.

**list traversal:** The sequential accessing of each element in a list.

**mapping:** A relationship in which each element of one set corresponds to an element of
another set. For example, a list is a mapping from indices to elements.

**accumulator:** A variable used in a loop to add up or accumulate a result.

**augmented assignment:** A statement that updates the value of a variable using an opera-
tor like+=.

**reduce:** A processing pattern that traverses a sequence and accumulates the elements into
a single result.


**98 Chapter 10. Lists**

**map:** A processing pattern that traverses a sequence and performs an operation on each
element.

**filter:** A processing pattern that traverses a list and selects the elements that satisfy some
criterion.

**object:** Something a variable can refer to. An object has a type and a value.

**equivalent:** Having the same value.

**identical:** Being the same object (which implies equivalence).

**reference:** The association between a variable and its value.

**aliasing:** A circumstance where two or more variables refer to the same object.

**delimiter:** A character or string used to indicate where a string should be split.

### 10.15 Exercises

**Exercise 10.6.** Write a function calledis_sortedthat takes a list as a parameter and returnsTrue
if the list is sorted in ascending order andFalseotherwise. You can assume (as a precondition) that
the elements of the list can be compared with the relational operators<,>, etc.

For example,is_sorted([1,2,2])should returnTrueandis_sorted(['b','a'])should re-
turnFalse.
**Exercise 10.7.** Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function calledis_anagramthat takes two strings and returnsTrueif they are anagrams.
**Exercise 10.8.** The (so-called) Birthday Paradox:

1. Write a function calledhas_duplicatesthat takes a list and returnsTrueif there is any
    element that appears more than once. It should not modify the original list.
2. If there are 23 students in your class, what are the chances that two of you have the same
    birthday? You can estimate this probability by generating random samples of 23 birthdays and
    checking for matches. Hint: you can generate random birthdays with therandintfunction
    in therandommodule.

You can read about this problem athttp: // en. wikipedia. org/ wiki/ Birthday_ paradox,
and you can download my solution fromhttp: // thinkpython. com/ code/ birthday. py.
**Exercise 10.9.** Write a function calledremove_duplicatesthat takes a list and returns a new
list with only the unique elements from the original. Hint: they don’t have to be in the same order.
**Exercise 10.10.** Write a function that reads the filewords.txtand builds a list with one element
per word. Write two versions of this function, one using theappendmethod and the other using
the idiomt = t + [x]. Which one takes longer to run? Why?

Hint: use thetimemodule to measure elapsed time. Solution:http: // thinkpython. com/
code/ wordlist. py.
**Exercise 10.11.** To check whether a word is in the word list, you could use theinoperator, but it
would be slow because it searches through the words in order.

Because the words are in alphabetical order, we can speed things up with a bisection search (also
known as binary search), which is similar to what you do when you look a word up in the dictionary.


**10.15. Exercises 99**

You start in the middle and check to see whether the word you are looking for comes before the word
in the middle of the list. If so, then you search the first half of the list the same way. Otherwise you
search the second half.

Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will
take about 17 steps to find the word or conclude that it’s not there.

Write a function calledbisectthat takes a sorted list and a target value and returns the index of
the value in the list, if it’s there, orNoneif it’s not.

Or you could read the documentation of thebisectmodule and use that! Solution:http: //
thinkpython. com/ code/ inlist. py.
**Exercise 10.12.** Two words are a “reverse pair” if each is the reverse of the other. Write a program
that finds all the reverse pairs in the word list. Solution:http: // thinkpython. com/ code/
reverse_ pair. py.
**Exercise 10.13.** Two words “interlock” if taking alternating letters from each forms a new
word. For example, “shoe” and “cold” interlock to form “schooled.” Solution: [http:](http:) //
thinkpython. com/ code/ interlock. py. Credit: This exercise is inspired by an example at
[http:](http:) // puzzlers. org.

1. Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
2. Can you find any words that are three-way interlocked; that is, every third letter forms a
    word, starting from the first, second or third?


**100 Chapter 10. Lists**


## Chapter 11

# Dictionaries

A **dictionary** is like a list, but more general. In a list, the indices have to be integers; in a
dictionary they can be (almost) any type.

You can think of a dictionary as a mapping between a set of indices (which are called **keys** )
and a set of values. Each key maps to a value. The association of a key and a value is called
a **key-value pair** or sometimes an **item**.

As an example, we’ll build a dictionary that maps from English to Spanish words, so the
keys and the values are all strings.

The functiondictcreates a new dictionary with no items. Becausedictis the name of a
built-in function, you should avoid using it as a variable name.

>>> eng2sp = dict()
>>> print eng2sp
{}

The squiggly-brackets,{}, represent an empty dictionary. To add items to the dictionary,
you can use square brackets:

>>> eng2sp['one'] ='uno'

This line creates an item that maps from the key'one'to the value'uno'. If we print the
dictionary again, we see a key-value pair with a colon between the key and value:

>>> print eng2sp
{'one':'uno'}

This output format is also an input format. For example, you can create a new dictionary
with three items:

>>> eng2sp = {'one':'uno','two': 'dos','three':'tres'}

But if you printeng2sp, you might be surprised:

>>> print eng2sp
{'one':'uno','three':'tres', 'two': 'dos'}

The order of the key-value pairs is not the same. In fact, if you type the same example
on your computer, you might get a different result. In general, the order of items in a
dictionary is unpredictable.

But that’s not a problem because the elements of a dictionary are never indexed with inte-
ger indices. Instead, you use the keys to look up the corresponding values:


**102 Chapter 11. Dictionaries**

>>> print eng2sp['two']
'dos'

The key'two'always maps to the value'dos'so the order of the items doesn’t matter.

If the key isn’t in the dictionary, you get an exception:

>>> print eng2sp['four']
KeyError: 'four'

Thelenfunction works on dictionaries; it returns the number of key-value pairs:

>>> len(eng2sp)
3

Theinoperator works on dictionaries; it tells you whether something appears as akeyin
the dictionary (appearing as a value is not good enough).

>>>'one' in eng2sp
True
>>>'uno' in eng2sp
False

To see whether something appears as a value in a dictionary, you can use the method
values, which returns the values as a list, and then use theinoperator:

>>> vals = eng2sp.values()
>>>'uno' in vals
True

Theinoperator uses different algorithms for lists and dictionaries. For lists, it uses a search
algorithm, as in Section 8.6. As the list gets longer, the search time gets longer in direct
proportion. For dictionaries, Python uses an algorithm called a **hashtable** that has a re-
markable property: theinoperator takes about the same amount of time no matter how
many items there are in a dictionary. I won’t explain how that’s possible, but you can read
more about it athttp://en.wikipedia.org/wiki/Hash_table.
**Exercise 11.1.** Write a function that reads the words inwords.txtand stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use theinoperator as a fast way to
check whether a string is in the dictionary.

If you did Exercise 10.11, you can compare the speed of this implementation with the listinoperator
and the bisection search.

### 11.1 Dictionary as a set of counters

Suppose you are given a string and you want to count how many times each letter appears.
There are several ways you could do it:

1. You could create 26 variables, one for each letter of the alphabet. Then you could tra-
    verse the string and, for each character, increment the corresponding counter, proba-
    bly using a chained conditional.
2. You could create a list with 26 elements. Then you could convert each character to
    a number (using the built-in functionord), use the number as an index into the list,
    and increment the appropriate counter.


**11.2. Looping and dictionaries 103**

3. You could create a dictionary with characters as keys and counters as the correspond-
    ing values. The first time you see a character, you would add an item to the dictionary.
    After that you would increment the value of an existing item.

Each of these options performs the same computation, but each of them implements that
computation in a different way.

An **implementation** is a way of performing a computation; some implementations are
better than others. For example, an advantage of the dictionary implementation is that we
don’t have to know ahead of time which letters appear in the string and we only have to
make room for the letters that do appear.

Here is what the code might look like:

def histogram(s):
d = dict()
for c in s:
if c not in d:
d[c] = 1
else:
d[c] += 1
return d

The name of the function is **histogram** , which is a statistical term for a set of counters (or
frequencies).

The first line of the function creates an empty dictionary. Theforloop traverses the string.
Each time through the loop, if the charactercis not in the dictionary, we create a new item
with keycand the initial value 1 (since we have seen this letter once). Ifcis already in the
dictionary we incrementd[c].

Here’s how it works:

>>> h = histogram('brontosaurus')
>>> print h
{'a': 1,'b': 1,'o': 2,'n': 1,'s': 2,'r': 2,'u': 2,'t': 1}

The histogram indicates that the letters'a'and'b'appear once;'o'appears twice, and
so on.
**Exercise 11.2.** Dictionaries have a method calledgetthat takes a key and a default value. If the
key appears in the dictionary,getreturns the corresponding value; otherwise it returns the default
value. For example:

>>> h = histogram('a')
>>> print h
{'a': 1}
>>> h.get('a', 0)
1
>>> h.get('b', 0)
0

Usegetto writehistogrammore concisely. You should be able to eliminate theifstatement.

### 11.2 Looping and dictionaries

If you use a dictionary in aforstatement, it traverses the keys of the dictionary. For exam-
ple,print_histprints each key and the corresponding value:


**104 Chapter 11. Dictionaries**

def print_hist(h):
for c in h:
print c, h[c]

Here’s what the output looks like:

>>> h = histogram('parrot')
>>> print_hist(h)
a 1
p 1
r 2
t 1
o 1

Again, the keys are in no particular order.
**Exercise 11.3.** Dictionaries have a method calledkeysthat returns the keys of the dictionary, in
no particular order, as a list.

Modifyprint_histto print the keys and their values in alphabetical order.

### 11.3 Reverse lookup

Given a dictionarydand a keyk, it is easy to find the corresponding valuev = d[k]. This
operation is called a **lookup**.

But what if you havevand you want to findk? You have two problems: first, there might
be more than one key that maps to the valuev. Depending on the application, you might
be able to pick one, or you might have to make a list that contains all of them. Second,
there is no simple syntax to do a **reverse lookup** ; you have to search.

Here is a function that takes a value and returns the first key that maps to that value:

def reverse_lookup(d, v):
for k in d:
if d[k] == v:
return k
raise ValueError

This function is yet another example of the search pattern, but it uses a feature we haven’t
seen before,raise. Theraisestatement causes an exception; in this case it causes a
ValueError, which generally indicates that there is something wrong with the value of
a parameter.

If we get to the end of the loop, that meansvdoesn’t appear in the dictionary as a value, so
we raise an exception.

Here is an example of a successful reverse lookup:

>>> h = histogram('parrot')
>>> k = reverse_lookup(h, 2)
>>> print k
r

And an unsuccessful one:


**11.4. Dictionaries and lists 105**

>>> k = reverse_lookup(h, 3)
Traceback (most recent call last):
File "<stdin>", line 1, in?
File "<stdin>", line 5, in reverse_lookup
ValueError

The result when you raise an exception is the same as when Python raises one: it prints a
traceback and an error message.

Theraisestatement takes a detailed error message as an optional argument. For example:

>>> raise ValueError('value does not appear in the dictionary')
Traceback (most recent call last):
File "<stdin>", line 1, in?
ValueError: value does not appear in the dictionary

A reverse lookup is much slower than a forward lookup; if you have to do it often, or if the
dictionary gets big, the performance of your program will suffer.
**Exercise 11.4.** Modifyreverse_lookupso that it builds and returns a list ofallkeys that map to
v, or an empty list if there are none.

### 11.4 Dictionaries and lists

Lists can appear as values in a dictionary. For example, if you were given a dictionary that
maps from letters to frequencies, you might want to invert it; that is, create a dictionary
that maps from frequencies to letters. Since there might be several letters with the same
frequency, each value in the inverted dictionary should be a list of letters.

Here is a function that inverts a dictionary:

def invert_dict(d):
inverse = dict()
for key in d:
val = d[key]
if val not in inverse:
inverse[val] = [key]
else:
inverse[val].append(key)
return inverse

Each time through the loop,keygets a key fromdandvalgets the corresponding value.
Ifvalis not ininverse, that means we haven’t seen it before, so we create a new item and
initialize it with a **singleton** (a list that contains a single element). Otherwise we have seen
this value before, so we append the corresponding key to the list.

Here is an example:

>>> hist = histogram('parrot')
>>> print hist
{'a': 1,'p': 1,'r': 2,'t': 1,'o': 1}
>>> inverse = invert_dict(hist)
>>> print inverse
{1: ['a', 'p','t','o'], 2: ['r']}


**106 Chapter 11. Dictionaries**

```
’a’ 1
1
```
```
dict
hist
’p’
```
```
1
’o’ 1
```
```
’r’ 2
’t’
```
```
0
1
```
```
’a’
’p’
```
```
list
```
```
2 ’t’
3 ’o’
```
```
1
```
```
dict
inv
```
```
2 0
```
```
list
’r’
```
```
Figure 11.1: State diagram.
```
Figure 11.1 is a state diagram showinghistandinverse. A dictionary is represented as a
box with the typedictabove it and the key-value pairs inside. If the values are integers,
floats or strings, I usually draw them inside the box, but I usually draw lists outside the
box, just to keep the diagram simple.

Lists can be values in a dictionary, as this example shows, but they cannot be keys. Here’s
what happens if you try:

>>> t = [1, 2, 3]
>>> d = dict()
>>> d[t] = 'oops'
Traceback (most recent call last):
File "<stdin>", line 1, in?
TypeError: list objects are unhashable

I mentioned earlier that a dictionary is implemented using a hashtable and that means that
the keys have to be **hashable**.

A **hash** is a function that takes a value (of any kind) and returns an integer. Dictionaries
use these integers, called hash values, to store and look up key-value pairs.

This system works fine if the keys are immutable. But if the keys are mutable, like lists,
bad things happen. For example, when you create a key-value pair, Python hashes the key
and stores it in the corresponding location. If you modify the key and then hash it again, it
would go to a different location. In that case you might have two entries for the same key,
or you might not be able to find a key. Either way, the dictionary wouldn’t work correctly.

That’s why the keys have to be hashable, and why mutable types like lists aren’t. The
simplest way to get around this limitation is to use tuples, which we will see in the next
chapter.

Since lists and dictionaries are mutable, they can’t be used as keys, but theycanbe used as
values.
**Exercise 11.5.** Read the documentation of the dictionary methodsetdefaultand use it to write a
more concise version ofinvert_dict. Solution:http: // thinkpython. com/ code/ invert_
dict. py.

### 11.5 Memos

If you played with thefibonaccifunction from Section 6.7, you might have noticed that
the bigger the argument you provide, the longer the function takes to run. Furthermore,


**11.5. Memos 107**

```
fibonacci
n 4
```
```
fibonacci
n 3
```
```
fibonacci
n 2
```
```
fibonacci
n 0
```
```
fibonacci
n 1
```
```
fibonacci
n 1
```
```
fibonacci
n 2
```
```
fibonacci
n 0
```
```
fibonacci
n 1
```
```
Figure 11.2: Call graph.
```
the run time increases very quickly.

To understand why, consider Figure 11.2, which shows the **call graph** forfibonacciwith
n=4:

A call graph shows a set of function frames, with lines connecting each frame to the frames
of the functions it calls. At the top of the graph,fibonacciwithn=4callsfibonacciwith
n=3andn=2. In turn,fibonacciwithn=3callsfibonacciwithn=2andn=1. And so on.

Count how many timesfibonacci(0)andfibonacci(1)are called. This is an inefficient
solution to the problem, and it gets worse as the argument gets bigger.

One solution is to keep track of values that have already been computed by storing them
in a dictionary. A previously computed value that is stored for later use is called a **memo**.
Here is a “memoized” version offibonacci:

known = {0:0, 1:1}

def fibonacci(n):
if n in known:
return known[n]

```
res = fibonacci(n-1) + fibonacci(n-2)
known[n] = res
return res
```
knownis a dictionary that keeps track of the Fibonacci numbers we already know. It starts
with two items: 0 maps to 0 and 1 maps to 1.

Wheneverfibonacciis called, it checksknown. If the result is already there, it can return
immediately. Otherwise it has to compute the new value, add it to the dictionary, and
return it.
**Exercise 11.6.** Run this version offibonacciand the original with a range of parameters and
compare their run times.
**Exercise 11.7.** Memoize the Ackermann function from Exercise 6.5 and see if memoization
makes it possible to evaluate the function with bigger arguments. Hint: no. Solution: [http:](http:)
// thinkpython. com/ code/ ackermann_ memo. py.


**108 Chapter 11. Dictionaries**

### 11.6 Global variables

In the previous example,knownis created outside the function, so it belongs to the special
frame called__main__. Variables in__main__are sometimes called **global** because they
can be accessed from any function. Unlike local variables, which disappear when their
function ends, global variables persist from one function call to the next.

It is common to use global variables for **flags** ; that is, boolean variables that indicate (“flag”)
whether a condition is true. For example, some programs use a flag namedverboseto
control the level of detail in the output:

verbose = True

def example1():
if verbose:
print 'Running example1'

If you try to reassign a global variable, you might be surprised. The following example is
supposed to keep track of whether the function has been called:

been_called = False

def example2():
been_called = True # WRONG

But if you run it you will see that the value ofbeen_calleddoesn’t change. The problem
is thatexample2creates a new local variable namedbeen_called. The local variable goes
away when the function ends, and has no effect on the global variable.

To reassign a global variable inside a function you have to **declare** the global variable before
you use it:

been_called = False

def example2():
global been_called
been_called = True

Theglobalstatement tells the interpreter something like, “In this function, when I say
been_called, I mean the global variable; don’t create a local one.”

Here’s an example that tries to update a global variable:

count = 0

def example3():
count = count + 1 # WRONG

If you run it you get:

UnboundLocalError: local variable'count'referenced before assignment

Python assumes thatcountis local, which means that you are reading it before writing it.
The solution, again, is to declarecountglobal.

def example3():
global count
count += 1

If the global value is mutable, you can modify it without declaring it:


**11.7. Long integers 109**

known = {0:0, 1:1}

def example4():
known[2] = 1

So you can add, remove and replace elements of a global list or dictionary, but if you want
to reassign the variable, you have to declare it:

def example5():
global known
known = dict()

### 11.7 Long integers

If you computefibonacci(50), you get:

>>> fibonacci(50)
12586269025L

TheLat the end indicates that the result is a long integer, or typelong. In Python 3,long
is gone; all integers, even really big ones, are typeint.

Values with typeinthave a limited range; long integers can be arbitrarily big, but as they
get bigger they consume more space and time.

The mathematical operators work on long integers, and the functions in themathmodule,
too, so in general any code that works withintwill also work withlong.

Any time the result of a computation is too big to be represented with an integer, Python
converts the result as a long integer:

>>> 1000 * 1000
1000000
>>> 100000 * 100000
10000000000L

In the first case the result has typeint; in the second case it islong.
**Exercise 11.8.** Exponentiation of large integers is the basis of common algorithms for public-key en-
cryption. Read the Wikipedia page on the RSA algorithm (http: // en. wikipedia. org/ wiki/
RSA_ ( algorithm)) and write functions to encode and decode messages.

### 11.8 Debugging

As you work with bigger datasets it can become unwieldy to debug by printing and check-
ing data by hand. Here are some suggestions for debugging large datasets:

**Scale down the input:** If possible, reduce the size of the dataset. For example if the pro-
gram reads a text file, start with just the first 10 lines, or with the smallest example
you can find. You can either edit the files themselves, or (better) modify the program
so it reads only the firstnlines.
If there is an error, you can reducento the smallest value that manifests the error, and
then increase it gradually as you find and correct errors.


**110 Chapter 11. Dictionaries**

**Check summaries and types:** Instead of printing and checking the entire dataset, consider
printing summaries of the data: for example, the number of items in a dictionary or
the total of a list of numbers.
A common cause of runtime errors is a value that is not the right type. For debugging
this kind of error, it is often enough to print the type of a value.

**Write self-checks:** Sometimes you can write code to check for errors automatically. For
example, if you are computing the average of a list of numbers, you could check that
the result is not greater than the largest element in the list or less than the smallest.
This is called a “sanity check” because it detects results that are “insane.”
Another kind of check compares the results of two different computations to see if
they are consistent. This is called a “consistency check.”

**Pretty print the output:** Formatting debugging output can make it easier to spot an error.
We saw an example in Section 6.9. Thepprintmodule provides apprintfunction
that displays built-in types in a more human-readable format.

Again, time you spend building scaffolding can reduce the time you spend debugging.

### 11.9 Glossary

**dictionary:** A mapping from a set of keys to their corresponding values.

**key-value pair:** The representation of the mapping from a key to a value.

**item:** Another name for a key-value pair.

**key:** An object that appears in a dictionary as the first part of a key-value pair.

**value:** An object that appears in a dictionary as the second part of a key-value pair. This is
more specific than our previous use of the word “value.”

**implementation:** A way of performing a computation.

**hashtable:** The algorithm used to implement Python dictionaries.

**hash function:** A function used by a hashtable to compute the location for a key.

**hashable:** A type that has a hash function. Immutable types like integers, floats and strings
are hashable; mutable types like lists and dictionaries are not.

**lookup:** A dictionary operation that takes a key and finds the corresponding value.

**reverse lookup:** A dictionary operation that takes a value and finds one or more keys that
map to it.

**singleton:** A list (or other sequence) with a single element.

**call graph:** A diagram that shows every frame created during the execution of a program,
with an arrow from each caller to each callee.

**histogram:** A set of counters.

**memo:** A computed value stored to avoid unnecessary future computation.


**11.10. Exercises 111**

**global variable:** A variable defined outside a function. Global variables can be accessed
from any function.

**flag:** A boolean variable used to indicate whether a condition is true.

**declaration:** A statement likeglobalthat tells the interpreter something about a variable.

### 11.10 Exercises

**Exercise 11.9.** If you did Exercise 10.8, you already have a function namedhas_duplicatesthat
takes a list as a parameter and returnsTrueif there is any object that appears more than once in the
list.

Use a dictionary to write a faster, simpler version ofhas_duplicates. Solution: [http:](http:) //
thinkpython. com/ code/ has_ duplicates. py.
**Exercise 11.10.** Two words are “rotate pairs” if you can rotate one of them and get the other (see
rotate_wordin Exercise 8.12).

Write a program that reads a wordlist and finds all the rotate pairs. Solution: [http:](http:) //
thinkpython. com/ code/ rotate_ pairs. py.
**Exercise 11.11.** Here’s another Puzzler fromCar Talk(http: // [http://www.](http://www.) cartalk. com/ content/
puzzlers):

```
This was sent in by a fellow named Dan O’Leary. He came upon a common one-syllable,
five-letter word recently that has the following unique property. When you remove the
first letter, the remaining letters form a homophone of the original word, that is a word
that sounds exactly the same. Replace the first letter, that is, put it back and remove
the second letter and the result is yet another homophone of the original word. And the
question is, what’s the word?
Now I’m going to give you an example that doesn’t work. Let’s look at the five-letter
word, ‘wrack.’ W-R-A-C-K, you know like to ‘wrack with pain.’ If I remove the first
letter, I am left with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the
rack on that buck! It must have been a nine-pointer!’ It’s a perfect homophone. If you
put the ‘w’ back, and remove the ‘r,’ instead, you’re left with the word, ‘wack,’ which is
a real word, it’s just not a homophone of the other two words.
But there is, however, at least one word that Dan and we know of, which will yield two
homophones if you remove either of the first two letters to make two, new four-letter
words. The question is, what’s the word?
```
You can use the dictionary from Exercise 11.1 to check whether a string is in the word list.

To check whether two words are homophones, you can use the CMU Pronouncing Dictionary.
You can download it fromhttp: // [http://www.](http://www.) speech. cs. cmu. edu/ cgi- bin/ cmudict or from
[http:](http:) // thinkpython. com/ code/ c06dand you can also downloadhttp: // thinkpython.
com/ code/ pronounce. py, which provides a function namedread_dictionarythat reads the
pronouncing dictionary and returns a Python dictionary that maps from each word to a string that
describes its primary pronunciation.

Write a program that lists all the words that solve the Puzzler. Solution:http: // thinkpython.
com/ code/ homophone. py.


**112 Chapter 11. Dictionaries**


## Chapter 12

# Tuples

### 12.1 Tuples are immutable

A tuple is a sequence of values. The values can be any type, and they are indexed by
integers, so in that respect tuples are a lot like lists. The important difference is that tuples
are immutable.

Syntactically, a tuple is a comma-separated list of values:

>>> t ='a', 'b', 'c', 'd','e'

Although it is not necessary, it is common to enclose tuples in parentheses:

>>> t = ('a', 'b', 'c','d','e')

To create a tuple with a single element, you have to include a final comma:

>>> t1 ='a',
>>> type(t1)
<type'tuple'>

A value in parentheses is not a tuple:

>>> t2 = ('a')
>>> type(t2)
<type'str'>

Another way to create a tuple is the built-in functiontuple. With no argument, it creates
an empty tuple:

>>> t = tuple()
>>> print t
()

If the argument is a sequence (string, list or tuple), the result is a tuple with the elements of
the sequence:

>>> t = tuple('lupins')
>>> print t
('l','u','p','i','n', 's')

Becausetupleis the name of a built-in function, you should avoid using it as a variable
name.

Most list operators also work on tuples. The bracket operator indexes an element:


**114 Chapter 12. Tuples**

>>> t = ('a', 'b', 'c', 'd','e')
>>> print t[0]
'a'

And the slice operator selects a range of elements.

>>> print t[1:3]
('b', 'c')

But if you try to modify one of the elements of the tuple, you get an error:

>>> t[0] = 'A'
TypeError: object doesn't support item assignment

You can’t modify the elements of a tuple, but you can replace one tuple with another:

>>> t = ('A',) + t[1:]
>>> print t
('A', 'b', 'c','d','e')

### 12.2 Tuple assignment

It is often useful to swap the values of two variables. With conventional assignments, you
have to use a temporary variable. For example, to swapaandb:

>>> temp = a
>>> a = b
>>> b = temp

This solution is cumbersome; **tuple assignment** is more elegant:

>>> a, b = b, a

The left side is a tuple of variables; the right side is a tuple of expressions. Each value
is assigned to its respective variable. All the expressions on the right side are evaluated
before any of the assignments.

The number of variables on the left and the number of values on the right have to be the
same:

>>> a, b = 1, 2, 3
ValueError: too many values to unpack

More generally, the right side can be any kind of sequence (string, list or tuple). For exam-
ple, to split an email address into a user name and a domain, you could write:

>>> addr = 'monty@python.org'
>>> uname, domain = addr.split('@')

The return value fromsplitis a list with two elements; the first element is assigned to
uname, the second todomain.

>>> print uname
monty
>>> print domain
python.org


**12.3. Tuples as return values 115**

### 12.3 Tuples as return values

Strictly speaking, a function can only return one value, but if the value is a tuple, the effect
is the same as returning multiple values. For example, if you want to divide two integers
and compute the quotient and remainder, it is inefficient to computex/yand thenx%y. It
is better to compute them both at the same time.

The built-in functiondivmodtakes two arguments and returns a tuple of two values, the
quotient and remainder. You can store the result as a tuple:

>>> t = divmod(7, 3)
>>> print t
(2, 1)

Or use tuple assignment to store the elements separately:

>>> quot, rem = divmod(7, 3)
>>> print quot
2
>>> print rem
1

Here is an example of a function that returns a tuple:

def min_max(t):
return min(t), max(t)

maxandminare built-in functions that find the largest and smallest elements of a sequence.
min_maxcomputes both and returns a tuple of two values.

### 12.4 Variable-length argument tuples

Functions can take a variable number of arguments. A parameter name that begins with
* **gathers** arguments into a tuple. For example,printalltakes any number of arguments
and prints them:

def printall(*args):
print args

The gather parameter can have any name you like, butargsis conventional. Here’s how
the function works:

>>> printall(1, 2.0,' 3 ')
(1, 2.0,' 3 ')

The complement of gather is **scatter**. If you have a sequence of values and you want to pass
it to a function as multiple arguments, you can use the*operator. For example,divmod
takes exactly two arguments; it doesn’t work with a tuple:

>>> t = (7, 3)
>>> divmod(t)
TypeError: divmod expected 2 arguments, got 1

But if you scatter the tuple, it works:

>>> divmod(*t)
(2, 1)
**Exercise 12.1.** Many of the built-in functions use variable-length argument tuples. For example,
maxandmincan take any number of arguments:


**116 Chapter 12. Tuples**

>>> max(1,2,3)
3

Butsumdoes not.

>>> sum(1,2,3)
TypeError: sum expected at most 2 arguments, got 3

Write a function calledsumallthat takes any number of arguments and returns their sum.

### 12.5 Lists and tuples

zipis a built-in function that takes two or more sequences and “zips” them into a list of
tuples where each tuple contains one element from each sequence. In Python 3,zipreturns
an iterator of tuples, but for most purposes, an iterator behaves like a list.

This example zips a string and a list:

>>> s ='abc'
>>> t = [0, 1, 2]
>>> zip(s, t)
[('a', 0), ('b', 1), ('c', 2)]

The result is a list of tuples where each tuple contains a character from the string and the
corresponding element from the list.

If the sequences are not the same length, the result has the length of the shorter one.

>>> zip('Anne','Elk')
[('A','E'), ('n', 'l'), ('n', 'k')]

You can use tuple assignment in aforloop to traverse a list of tuples:

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
print number, letter

Each time through the loop, Python selects the next tuple in the list and assigns the ele-
ments toletterandnumber. The output of this loop is:

0 a
1 b
2 c

If you combinezip,forand tuple assignment, you get a useful idiom for traversing two
(or more) sequences at the same time. For example,has_matchtakes two sequences,t1
andt2, and returnsTrueif there is an indexisuch thatt1[i] == t2[i]:

def has_match(t1, t2):
for x, y in zip(t1, t2):
if x == y:
return True
return False

If you need to traverse the elements of a sequence and their indices, you can use the built-in
functionenumerate:

for index, element in enumerate('abc'):
print index, element


**12.6. Dictionaries and tuples 117**

The output of this loop is:

0 a
1 b
2 c

Again.

### 12.6 Dictionaries and tuples

Dictionaries have a method calleditemsthat returns a list of tuples, where each tuple is a
key-value pair.

>>> d = {'a':0,'b':1,'c':2}
>>> t = d.items()
>>> print t
[('a', 0), ('c', 2), ('b', 1)]

As you should expect from a dictionary, the items are in no particular order. In Python 3,
itemsreturns an iterator, but for many purposes, iterators behave like lists.

Going in the other direction, you can use a list of tuples to initialize a new dictionary:

>>> t = [('a', 0), ('c', 2), ('b', 1)]
>>> d = dict(t)
>>> print d
{'a': 0,'c': 2,'b': 1}

Combiningdictwithzipyields a concise way to create a dictionary:

>>> d = dict(zip('abc', range(3)))
>>> print d
{'a': 0,'c': 2,'b': 1}

The dictionary methodupdatealso takes a list of tuples and adds them, as key-value pairs,
to an existing dictionary.

Combiningitems, tuple assignment andfor, you get the idiom for traversing the keys and
values of a dictionary:

for key, val in d.items():
print val, key

The output of this loop is:

0 a
2 c
1 b

Again.

It is common to use tuples as keys in dictionaries (primarily because you can’t use lists). For
example, a telephone directory might map from last-name, first-name pairs to telephone
numbers. Assuming that we have definedlast,firstandnumber, we could write:

directory[last,first] = number

The expression in brackets is a tuple. We could use tuple assignment to traverse this dic-
tionary.


**118 Chapter 12. Tuples**

```
0
1
```
```
’Cleese’
’John’
```
```
tuple
```
```
Figure 12.1: State diagram.
```
```
(’Cleese’, ’John’) ’08700 100 222’
’08700 100 222’
’08700 100 222’
’08700 100 222’
’08700 100 222’
```
```
(’Chapman’, ’Graham’)
(’Idle’, ’Eric’)
```
```
(’Jones’, ’Terry’)
```
```
(’Gilliam’, ’Terry’)
```
```
(’Palin’, ’Michael’) ’08700 100 222’
```
```
dict
```
```
Figure 12.2: State diagram.
```
for last, first in directory:
print first, last, directory[last,first]

This loop traverses the keys indirectory, which are tuples. It assigns the elements of each
tuple tolastandfirst, then prints the name and corresponding telephone number.

There are two ways to represent tuples in a state diagram. The more detailed version
shows the indices and elements just as they appear in a list. For example, the tuple
('Cleese', 'John')would appear as in Figure 12.1.

But in a larger diagram you might want to leave out the details. For example, a diagram of
the telephone directory might appear as in Figure 12.2.

Here the tuples are shown using Python syntax as a graphical shorthand.

The telephone number in the diagram is the complaints line for the BBC, so please don’t
call it.

### 12.7 Comparing tuples

The relational operators work with tuples and other sequences; Python starts by comparing
the first element from each sequence. If they are equal, it goes on to the next elements, and
so on, until it finds elements that differ. Subsequent elements are not considered (even if
they are really big).

>>> (0, 1, 2) < (0, 3, 4)
True
>>> (0, 1, 2000000) < (0, 3, 4)
True

Thesortfunction works the same way. It sorts primarily by first element, but in the case
of a tie, it sorts by second element, and so on.

This feature lends itself to a pattern called **DSU** for


**12.8. Sequences of sequences 119**

**Decorate** a sequence by building a list of tuples with one or more sort keys preceding the
elements from the sequence,

**Sort** the list of tuples, and

**Undecorate** by extracting the sorted elements of the sequence.

For example, suppose you have a list of words and you want to sort them from longest to
shortest:

def sort_by_length(words):
t = []
for word in words:
t.append((len(word), word))

```
t.sort(reverse=True)
```
```
res = []
for length, word in t:
res.append(word)
return res
```
The first loop builds a list of tuples, where each tuple is a word preceded by its length.

sortcompares the first element, length, first, and only considers the second element to
break ties. The keyword argumentreverse=Truetellssortto go in decreasing order.

The second loop traverses the list of tuples and builds a list of words in descending order
of length.
**Exercise 12.2.** In this example, ties are broken by comparing words, so words with the same length
appear in reverse alphabetical order. For other applications you might want to break ties at ran-
dom. Modify this example so that words with the same length appear in random order. Hint:
see therandomfunction in therandommodule. Solution:http: // thinkpython. com/ code/
unstable_ sort. py.

### 12.8 Sequences of sequences

I have focused on lists of tuples, but almost all of the examples in this chapter also work
with lists of lists, tuples of tuples, and tuples of lists. To avoid enumerating the possible
combinations, it is sometimes easier to talk about sequences of sequences.

In many contexts, the different kinds of sequences (strings, lists and tuples) can be used
interchangeably. So how and why do you choose one over the others?

To start with the obvious, strings are more limited than other sequences because the ele-
ments have to be characters. They are also immutable. If you need the ability to change the
characters in a string (as opposed to creating a new string), you might want to use a list of
characters instead.

Lists are more common than tuples, mostly because they are mutable. But there are a few
cases where you might prefer tuples:

1. In some contexts, like areturnstatement, it is syntactically simpler to create a tuple
    than a list. In other contexts, you might prefer a list.


**120 Chapter 12. Tuples**

2. If you want to use a sequence as a dictionary key, you have to use an immutable type
    like a tuple or string.
3. If you are passing a sequence as an argument to a function, using tuples reduces the
    potential for unexpected behavior due to aliasing.

Because tuples are immutable, they don’t provide methods likesortandreverse, which
modify existing lists. But Python provides the built-in functionssortedandreversed,
which take any sequence as a parameter and return a new list with the same elements in a
different order.

### 12.9 Debugging

Lists, dictionaries and tuples are known generically as **data structures** ; in this chapter we
are starting to see compound data structures, like lists of tuples, and dictionaries that con-
tain tuples as keys and lists as values. Compound data structures are useful, but they are
prone to what I call **shape errors** ; that is, errors caused when a data structure has the wrong
type, size or composition. For example, if you are expecting a list with one integer and I
give you a plain old integer (not in a list), it won’t work.

To help debug these kinds of errors, I have written a module calledstructshapethat
provides a function, also calledstructshape, that takes any kind of data structure as
an argument and returns a string that summarizes its shape. You can download it from
[http://thinkpython.com/code/structshape.py](http://thinkpython.com/code/structshape.py)

Here’s the result for a simple list:

>>> from structshape import structshape
>>> t = [1,2,3]
>>> print structshape(t)
list of 3 int

A fancier program might write “list of 3 ints,” but it was easier not to deal with plurals.
Here’s a list of lists:

>>> t2 = [[1,2], [3,4], [5,6]]
>>> print structshape(t2)
list of 3 list of 2 int

If the elements of the list are not the same type,structshapegroups them, in order, by
type:

>>> t3 = [1, 2, 3, 4.0, ' 5 ',' 6 ', [7], [8], 9]
>>> print structshape(t3)
list of (3 int, float, 2 str, 2 list of int, int)

Here’s a list of tuples:

>>> s ='abc'
>>> lt = zip(t, s)
>>> print structshape(lt)
list of 3 tuple of (int, str)

And here’s a dictionary with 3 items that map integers to strings.

>>> d = dict(lt)
>>> print structshape(d)
dict of 3 int->str

If you are having trouble keeping track of your data structures,structshapecan help.


**12.10. Glossary 121**

### 12.10 Glossary

**tuple:** An immutable sequence of elements.

**tuple assignment:** An assignment with a sequence on the right side and a tuple of vari-
ables on the left. The right side is evaluated and then its elements are assigned to the
variables on the left.

**gather:** The operation of assembling a variable-length argument tuple.

**scatter:** The operation of treating a sequence as a list of arguments.

**DSU:** Abbreviation of “decorate-sort-undecorate,” a pattern that involves building a list
of tuples, sorting, and extracting part of the result.

**data structure:** A collection of related values, often organized in lists, dictionaries, tuples,
etc.

**shape (of a data structure):** A summary of the type, size and composition of a data struc-
ture.


### 12.11 Exercises

**Exercise 12.3.** Write a function calledmost_frequentthat takes a string and prints the let-
ters in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages. Compare your results with the tables athttp: //
en. wikipedia. org/ wiki/ Letter_ frequencies. Solution:http: // thinkpython. com/
code/ most_ frequent. py.
**Exercise 12.4.** More anagrams!

1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
    words that are anagrams.
    Here is an example of what the output might look like:

```
['deltas','desalt','lasted', 'salted', 'slated','staled']
['retainers', 'ternaries']
['generating', 'greatening']
['resmelts','smelters','termless']
```
```
Hint: you might want to build a dictionary that maps from a set of letters to a list of words
that can be spelled with those letters. The question is, how can you represent the set of letters
in a way that can be used as a key?
```
2. Modify the previous program so that it prints the largest set of anagrams first, followed by the
    second larg
