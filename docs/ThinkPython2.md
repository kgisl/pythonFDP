### 12.11 Exercises

**Exercise 12.3.** Write a function calledmost_frequentthat takes a string and prints the let-
ters in decreasing order of frequency. Find text samples from several different languages and see
how letter frequency varies between languages. Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies
Solution: http://thinkpython.com/code/most_frequent.py .

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
   second largest set, and so on.
3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
   the board, to form an eight-letter word. What set of 8 letters forms the most possible bingos?
   Hint: there are seven.
   Solution:http: // thinkpython. com/ code/ anagram\_ sets. py.

**122 Chapter 12. Tuples**

**Exercise 12.5.** Two words form a “metathesis pair” if you can transform one into the other by
swapping two letters; for example, “converse” and “conserve.” Write a program that finds all of
the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible
swaps. Solution:http: // thinkpython. com/ code/ metathesis. py. Credit: This exercise is
inspired by an example athttp: // puzzlers. org.
**Exercise 12.6.** Here’s another Car Talk Puzzler (http: // [http://www.](http://www.) cartalk. com/ content/
puzzlers):

```
What is the longest English word, that remains a valid English word, as you remove its
letters one at a time?
Now, letters can be removed from either end, or the middle, but you can’t rearrange any
of the letters. Every time you drop a letter, you wind up with another English word. If
you do that, you’re eventually going to wind up with one letter and that too is going
to be an English word—one that’s found in the dictionary. I want to know what’s the
longest word and how many letters does it have?
I’m going to give you a little modest example: Sprite. Ok? You start off with sprite,
you take a letter off, one from the interior of the word, take the r away, and we’re left
with the word spite, then we take the e off the end, we’re left with spit, we take the s off,
we’re left with pit, it, and I.
```

Write a program to find all words that can be reduced in this way, and then find the longest one.

This exercise is a little more challenging than most, so here are some suggestions:

1. You might want to write a function that takes a word and computes a list of all the words that
   can be formed by removing one letter. These are the “children” of the word.
2. Recursively, a word is reducible if any of its children are reducible. As a base case, you can
   consider the empty string reducible.
3. The wordlist I provided,words.txt, doesn’t contain single letter words. So you might want
   to add “I”, “a”, and the empty string.
4. To improve the performance of your program, you might want to memoize the words that are
   known to be reducible.

Solution:http: // thinkpython. com/ code/ reducible. py.

## Chapter 13

# Case study: data structure

# selection

### 13.1 Word frequency analysis

As usual, you should at least attempt the following exercises before you read my solutions.
**Exercise 13.1.** Write a program that reads a file, breaks each line into words, strips whitespace and
punctuation from the words, and converts them to lowercase.

Hint: Thestringmodule provides strings namedwhitespace, which contains space, tab, newline,
etc., andpunctuationwhich contains the punctuation characters. Let’s see if we can make Python
swear:

> > > import string
> > > print string.punctuation
> > > !"#$%&'()\*+,-./:;<=>?@[\]^\_`{|}~

Also, you might consider using the string methodsstrip,replaceandtranslate.
**Exercise 13.2.** Go to Project Gutenberg (http: // gutenberg. org) and download your favorite
out-of-copyright book in plain text format.

Modify your program from the previous exercise to read the book you downloaded, skip over the
header information at the beginning of the file, and process the rest of the words as before.

Then modify the program to count the total number of words in the book, and the number of times
each word is used.

Print the number of different words used in the book. Compare different books by different authors,
written in different eras. Which author uses the most extensive vocabulary?
**Exercise 13.3.** Modify the program from the previous exercise to print the 20 most frequently-used
words in the book.
**Exercise 13.4.** Modify the previous program to read a word list (see Section 9.1) and then print all
the words in the book that are not in the word list. How many of them are typos? How many of
them are common words thatshouldbe in the word list, and how many of them are really obscure?

**124 Chapter 13. Case study: data structure selection**

### 13.2 Random numbers

Given the same inputs, most computer programs generate the same outputs every time,
so they are said to be **deterministic**. Determinism is usually a good thing, since we expect
the same calculation to yield the same result. For some applications, though, we want the
computer to be unpredictable. Games are an obvious example, but there are more.

Making a program truly nondeterministic turns out to be not so easy, but there are ways
to make it at least seem nondeterministic. One of them is to use algorithms that generate
**pseudorandom** numbers. Pseudorandom numbers are not truly random because they are
generated by a deterministic computation, but just by looking at the numbers it is all but
impossible to distinguish them from random.

Therandommodule provides functions that generate pseudorandom numbers (which I
will simply call “random” from here on).

The functionrandomreturns a random float between 0.0 and 1.0 (including 0.0 but not 1.0).
Each time you callrandom, you get the next number in a long series. To see a sample, run
this loop:

import random

for i in range(10):
x = random.random()
print x

The functionrandinttakes parameterslowandhighand returns an integer betweenlow
andhigh(including both).

> > > random.randint(5, 10)
> > > 5
> > > random.randint(5, 10)
> > > 9

To choose an element from a sequence at random, you can usechoice:

> > > t = [1, 2, 3]
> > > random.choice(t)
> > > 2
> > > random.choice(t)
> > > 3

Therandommodule also provides functions to generate random values from continuous
distributions including Gaussian, exponential, gamma, and a few more.
**Exercise 13.5.** Write a function namedchoose_from_histthat takes a histogram as defined in
Section 11.1 and returns a random value from the histogram, chosen with probability in proportion
to frequency. For example, for this histogram:

> > > t = ['a', 'a', 'b']
> > > hist = histogram(t)
> > > print hist
> > > {'a': 2,'b': 1}

your function should return'a'with probability2/3and'b'with probability1/3.

**13.3. Word histogram 125**

### 13.3 Word histogram

You should attempt the previous exercises before you go on. You can download my so-
lution fromhttp://thinkpython.com/code/analyze_book.py. You will also needhttp:
//thinkpython.com/code/emma.txt.

Here is a program that reads a file and builds a histogram of the words in the file:

import string

def process_file(filename):
hist = dict()
fp = open(filename)
for line in fp:
process_line(line, hist)
return hist

def process_line(line, hist):
line = line.replace('-','')

```
for word in line.split():
word = word.strip(string.punctuation + string.whitespace)
word = word.lower()
```

```
hist[word] = hist.get(word, 0) + 1
```

hist = process_file('emma.txt')

This program readsemma.txt, which contains the text ofEmmaby Jane Austen.

process_fileloops through the lines of the file, passing them one at a time to
process_line. The histogramhistis being used as an accumulator.

process_lineuses the string methodreplaceto replace hyphens with spaces before using
splitto break the line into a list of strings. It traverses the list of words and usesstrip
andlowerto remove punctuation and convert to lower case. (It is a shorthand to say that
strings are “converted;” remember that string are immutable, so methods likestripand
lowerreturn new strings.)

Finally,process_lineupdates the histogram by creating a new item or incrementing an
existing one.

To count the total number of words in the file, we can add up the frequencies in the his-
togram:

def total_words(hist):
return sum(hist.values())

The number of different words is just the number of items in the dictionary:

def different_words(hist):
return len(hist)

Here is some code to print the results:

print'Total number of words:', total_words(hist)
print'Number of different words:', different_words(hist)

**126 Chapter 13. Case study: data structure selection**

And the results:

Total number of words: 161080
Number of different words: 7214

### 13.4 Most common words

To find the most common words, we can apply the DSU pattern;most_commontakes a
histogram and returns a list of word-frequency tuples, sorted in reverse order by frequency:

def most_common(hist):
t = []
for key, value in hist.items():
t.append((value, key))

```
t.sort(reverse=True)
return t
```

Here is a loop that prints the ten most common words:

t = most_common(hist)
print 'The most common words are:'
for freq, word in t[0:10]:
print word,'\t', freq

And here are the results fromEmma:

The most common words are:
to 5242
the 5205
and 4897
of 4295
i 3191
a 3130
it 2529
her 2483
was 2400
she 2364

### 13.5 Optional parameters

We have seen built-in functions and methods that take a variable number of arguments. It
is possible to write user-defined functions with optional arguments, too. For example, here
is a function that prints the most common words in a histogram

def print_most_common(hist, num=10):
t = most_common(hist)
print 'The most common words are:'
for freq, word in t[:num]:
print word,'\t', freq

The first parameter is required; the second is optional. The **default value** ofnumis 10.

If you only provide one argument:

**13.6. Dictionary subtraction 127**

print_most_common(hist)

numgets the default value. If you provide two arguments:

print_most_common(hist, 20)

numgets the value of the argument instead. In other words, the optional argument **over-
rides** the default value.

If a function has both required and optional parameters, all the required parameters have
to come first, followed by the optional ones.

### 13.6 Dictionary subtraction

Finding the words from the book that are not in the word list fromwords.txtis a problem
you might recognize as set subtraction; that is, we want to find all the words from one set
(the words in the book) that are not in another set (the words in the list).

subtracttakes dictionariesd1andd2and returns a new dictionary that contains all the
keys fromd1that are not ind2. Since we don’t really care about the values, we set them all
to None.

def subtract(d1, d2):
res = dict()
for key in d1:
if key not in d2:
res[key] = None
return res

To find the words in the book that are not inwords.txt, we can useprocess_fileto build
a histogram forwords.txt, and then subtract:

words = process_file('words.txt')
diff = subtract(hist, words)

print "The words in the book that aren't in the word list are:"
for word in diff.keys():
print word,

Here are some of the results fromEmma:

The words in the book that aren't in the word list are:
rencontre jane's blanche woodhouses disingenuousness
friend's venice apartment ...

Some of these words are names and possessives. Others, like “rencontre,” are no longer in
common use. But a few are common words that should really be in the list!
**Exercise 13.6.** Python provides a data structure calledsetthat provides many common set opera-
tions. Read the documentation athttp: // docs. python. org/ 2/ library/ stdtypes. html#
types- setand write a program that uses set subtraction to find words in the book that are not in
the word list. Solution:http: // thinkpython. com/ code/ analyze\_ book2. py.

### 13.7 Random words

To choose a random word from the histogram, the simplest algorithm is to build a list with
multiple copies of each word, according to the observed frequency, and then choose from
the list:

**128 Chapter 13. Case study: data structure selection**

def random_word(h):
t = []
for word, freq in h.items():
t.extend([word] \* freq)

```
return random.choice(t)
```

The expression[word] \* freqcreates a list withfreqcopies of the stringword. The
extendmethod is similar toappendexcept that the argument is a sequence.
**Exercise 13.7.** This algorithm works, but it is not very efficient; each time you choose a random
word, it rebuilds the list, which is as big as the original book. An obvious improvement is to build
the list once and then make multiple selections, but the list is still big.

An alternative is:

1. Usekeysto get a list of the words in the book.
2. Build a list that contains the cumulative sum of the word frequencies (see Exercise 10.3). The
   last item in this list is the total number of words in the book, n.
3. Choose a random number from 1 to n. Use a bisection search (See Exercise 10.11) to find the
   index where the random number would be inserted in the cumulative sum.
4. Use the index to find the corresponding word in the word list.

Write a program that uses this algorithm to choose a random word from the book. Solution:http:
// thinkpython. com/ code/ analyze\_ book3. py.

### 13.8 Markov analysis

If you choose words from the book at random, you can get a sense of the vocabulary, you
probably won’t get a sentence:

this the small regard harriet which knightley's it most things

A series of random words seldom makes sense because there is no relationship between
successive words. For example, in a real sentence you would expect an article like “the” to
be followed by an adjective or a noun, and probably not a verb or adverb.

One way to measure these kinds of relationships is Markov analysis, which characterizes,
for a given sequence of words, the probability of the word that comes next. For example,
the songEric, the Half a Beebegins:

```
Half a bee, philosophically,
Must, ipso facto, half not be.
But half the bee has got to be
Vis a vis, its entity. D’you see?
```

```
But can a bee be said to be
Or not to be an entire bee
When half the bee is not a bee
Due to some ancient injury?
```

**13.9. Data structures 129**

In this text, the phrase “half the” is always followed by the word “bee,” but the phrase “the
bee” might be followed by either “has” or “is”.

The result of Markov analysis is a mapping from each prefix (like “half the” and “the bee”)
to all possible suffixes (like “has” and “is”).

Given this mapping, you can generate a random text by starting with any prefix and choos-
ing at random from the possible suffixes. Next, you can combine the end of the prefix and
the new suffix to form the next prefix, and repeat.

For example, if you start with the prefix “Half a,” then the next word has to be “bee,”
because the prefix only appears once in the text. The next prefix is “a bee,” so the next
suffix might be “philosophically,” “be” or “due.”

In this example the length of the prefix is always two, but you can do Markov analysis with
any prefix length. The length of the prefix is called the “order” of the analysis.
**Exercise 13.8.** Markov analysis:

1. Write a program to read a text from a file and perform Markov analysis. The result should be
   a dictionary that maps from prefixes to a collection of possible suffixes. The collection might
   be a list, tuple, or dictionary; it is up to you to make an appropriate choice. You can test your
   program with prefix length two, but you should write the program in a way that makes it easy
   to try other lengths.
2. Add a function to the previous program to generate random text based on the Markov analysis.
   Here is an example fromEmmawith prefix length 2:
   He was very clever, be it sweetness or be angry, ashamed or only amused, at such
   a stroke. She had never thought of Hannah till you were never meant for me?" "I
   cannot make speeches, Emma:" he soon cut it all himself.
   For this example, I left the punctuation attached to the words. The result is almost syntacti-
   cally correct, but not quite. Semantically, it almost makes sense, but not quite.
   What happens if you increase the prefix length? Does the random text make more sense?
3. Once your program is working, you might want to try a mash-up: if you analyze text from
   two or more books, the random text you generate will blend the vocabulary and phrases from
   the sources in interesting ways.

Credit: This case study is based on an example from Kernighan and Pike,The Practice of Pro-
gramming, Addison-Wesley, 1999.

You should attempt this exercise before you go on; then you can can download my
solution fromhttp://thinkpython.com/code/markov.py. You will also needhttp://
thinkpython.com/code/emma.txt.

### 13.9 Data structures

Using Markov analysis to generate random text is fun, but there is also a point to this
exercise: data structure selection. In your solution to the previous exercises, you had to
choose:

- How to represent the prefixes.

**130 Chapter 13. Case study: data structure selection**

- How to represent the collection of possible suffixes.
- How to represent the mapping from each prefix to the collection of possible suffixes.

Ok, the last one is easy; the only mapping type we have seen is a dictionary, so it is the
natural choice.

For the prefixes, the most obvious options are string, list of strings, or tuple of strings. For
the suffixes, one option is a list; another is a histogram (dictionary).

How should you choose? The first step is to think about the operations you will need to
implement for each data structure. For the prefixes, we need to be able to remove words
from the beginning and add to the end. For example, if the current prefix is “Half a,” and
the next word is “bee,” you need to be able to form the next prefix, “a bee.”

Your first choice might be a list, since it is easy to add and remove elements, but we also
need to be able to use the prefixes as keys in a dictionary, so that rules out lists. With tuples,
you can’t append or remove, but you can use the addition operator to form a new tuple:

def shift(prefix, word):
return prefix[1:] + (word,)

shifttakes a tuple of words,prefix, and a string,word, and forms a new tuple that has
all the words inprefixexcept the first, andwordadded to the end.

For the collection of suffixes, the operations we need to perform include adding a new
suffix (or increasing the frequency of an existing one), and choosing a random suffix.

Adding a new suffix is equally easy for the list implementation or the histogram. Choosing
a random element from a list is easy; choosing from a histogram is harder to do efficiently
(see Exercise 13.7).

So far we have been talking mostly about ease of implementation, but there are other fac-
tors to consider in choosing data structures. One is run time. Sometimes there is a theoreti-
cal reason to expect one data structure to be faster than other; for example, I mentioned that
theinoperator is faster for dictionaries than for lists, at least when the number of elements
is large.

But often you don’t know ahead of time which implementation will be faster. One option is
to implement both of them and see which is better. This approach is called **benchmarking**.
A practical alternative is to choose the data structure that is easiest to implement, and then
see if it is fast enough for the intended application. If so, there is no need to go on. If not,
there are tools, like theprofilemodule, that can identify the places in a program that take
the most time.

The other factor to consider is storage space. For example, using a histogram for the col-
lection of suffixes might take less space because you only have to store each word once, no
matter how many times it appears in the text. In some cases, saving space can also make
your program run faster, and in the extreme, your program might not run at all if you run
out of memory. But for many applications, space is a secondary consideration after run
time.

One final thought: in this discussion, I have implied that we should use one data structure
for both analysis and generation. But since these are separate phases, it would also be pos-
sible to use one structure for analysis and then convert to another structure for generation.
This would be a net win if the time saved during generation exceeded the time spent in
conversion.

**13.10. Debugging 131**

### 13.10 Debugging

When you are debugging a program, and especially if you are working on a hard bug,
there are four things to try:

**reading:** Examine your code, read it back to yourself, and check that it says what you
meant to say.

**running:** Experiment by making changes and running different versions. Often if you dis-
play the right thing at the right place in the program, the problem becomes obvious,
but sometimes you have to spend some time to build scaffolding.

**ruminating:** Take some time to think! What kind of error is it: syntax, runtime, semantic?
What information can you get from the error messages, or from the output of the
program? What kind of error could cause the problem you’re seeing? What did you
change last, before the problem appeared?

**retreating:** At some point, the best thing to do is back off, undoing recent changes, until
you get back to a program that works and that you understand. Then you can start
rebuilding.

Beginning programmers sometimes get stuck on one of these activities and forget the oth-
ers. Each activity comes with its own failure mode.

For example, reading your code might help if the problem is a typographical error, but
not if the problem is a conceptual misunderstanding. If you don’t understand what your
program does, you can read it 100 times and never see the error, because the error is in
your head.

Running experiments can help, especially if you run small, simple tests. But if you run
experiments without thinking or reading your code, you might fall into a pattern I call
“random walk programming,” which is the process of making random changes until the
program does the right thing. Needless to say, random walk programming can take a long
time.

You have to take time to think. Debugging is like an experimental science. You should have
at least one hypothesis about what the problem is. If there are two or more possibilities, try
to think of a test that would eliminate one of them.

Taking a break helps with the thinking. So does talking. If you explain the problem to
someone else (or even yourself), you will sometimes find the answer before you finish
asking the question.

But even the best debugging techniques will fail if there are too many errors, or if the code
you are trying to fix is too big and complicated. Sometimes the best option is to retreat,
simplifying the program until you get to something that works and that you understand.

Beginning programmers are often reluctant to retreat because they can’t stand to delete a
line of code (even if it’s wrong). If it makes you feel better, copy your program into another
file before you start stripping it down. Then you can paste the pieces back in a little bit at a
time.

Finding a hard bug requires reading, running, ruminating, and sometimes retreating. If
you get stuck on one of these activities, try the others.

**132 Chapter 13. Case study: data structure selection**

### 13.11 Glossary

**deterministic:** Pertaining to a program that does the same thing each time it runs, given
the same inputs.

**pseudorandom:** Pertaining to a sequence of numbers that appear to be random, but are
generated by a deterministic program.

**default value:** The value given to an optional parameter if no argument is provided.

**override:** To replace a default value with an argument.

**benchmarking:** The process of choosing between data structures by implementing alter-
natives and testing them on a sample of the possible inputs.

### 13.12 Exercises

**Exercise 13.9.** The “rank” of a word is its position in a list of words sorted by frequency: the most
common word has rank 1, the second most common has rank 2, etc.

Zipf’s law describes a relationship between the ranks and frequencies of words in natural languages
(http: // en. wikipedia. org/ wiki/ Zipf' s\_ law). Specifically, it predicts that the frequency,
f , of the word with rank r is:

```
f=cr−s
```

where s and c are parameters that depend on the language and the text. If you take the logarithm of
both sides of this equation, you get:

```
logf=logc−slogr
```

So if you plot log f versus log r, you should get a straight line with slope−s and intercept log c.

Write a program that reads a text from a file, counts word frequencies, and prints one line for each
word, in descending order of frequency, with log f and log r. Use the graphing program of your
choice to plot the results and check whether they form a straight line. Can you estimate the value of
s?

Solution:http: // thinkpython. com/ code/ zipf. py. To make the plots, you might have to
install matplotlib (seehttp: // matplotlib. sourceforge. net/).

## Chapter 14

# Files

### 14.1 Persistence

Most of the programs we have seen so far are transient in the sense that they run for a short
time and produce some output, but when they end, their data disappears. If you run the
program again, it starts with a clean slate.

Other programs are **persistent** : they run for a long time (or all the time); they keep at least
some of their data in permanent storage (a hard drive, for example); and if they shut down
and restart, they pick up where they left off.

Examples of persistent programs are operating systems, which run pretty much whenever
a computer is on, and web servers, which run all the time, waiting for requests to come in
on the network.

One of the simplest ways for programs to maintain their data is by reading and writing
text files. We have already seen programs that read text files; in this chapter we will see
programs that write them.

An alternative is to store the state of the program in a database. In this chapter I will present
a simple database and a module,pickle, that makes it easy to store program data.

### 14.2 Reading and writing

A text file is a sequence of characters stored on a permanent medium like a hard drive,
flash memory, or CD-ROM. We saw how to open and read a file in Section 9.1.

To write a file, you have to open it with mode'w'as a second parameter:

> > > fout = open('output.txt','w')
> > > print fout
> > > <open file'output.txt', mode'w'at 0xb7eb2410>

If the file already exists, opening it in write mode clears out the old data and starts fresh,
so be careful! If the file doesn’t exist, a new one is created.

Thewritemethod puts data into the file.

**134 Chapter 14. Files**

> > > line1 = "This here's the wattle,\n"
> > > fout.write(line1)

Again, the file object keeps track of where it is, so if you callwriteagain, it adds the new
data to the end.

> > > line2 = "the emblem of our land.\n"
> > > fout.write(line2)

When you are done writing, you have to close the file.

> > > fout.close()

### 14.3 Format operator

The argument ofwritehas to be a string, so if we want to put other values in a file, we
have to convert them to strings. The easiest way to do that is withstr:

> > > x = 52
> > > fout.write(str(x))

An alternative is to use the **format operator** ,%. When applied to integers,%is the modulus
operator. But when the first operand is a string,%is the format operator.

The first operand is the **format string** , which contains one or more **format sequences** ,
which specify how the second operand is formatted. The result is a string.

For example, the format sequence'%d'means that the second operand should be format-
ted as an integer (dstands for “decimal”):

> > > camels = 42
> > > '%d'% camels
> > > ' 42 '

The result is the string' 42 ', which is not to be confused with the integer value 42.

A format sequence can appear anywhere in the string, so you can embed a value in a
sentence:

> > > camels = 42
> > > 'I have spotted %d camels.' % camels
> > > 'I have spotted 42 camels.'

If there is more than one format sequence in the string, the second argument has to be a
tuple. Each format sequence is matched with an element of the tuple, in order.

The following example uses'%d'to format an integer,'%g'to format a floating-point num-
ber (don’t ask why), and'%s'to format a string:

> > > 'In %d years I have spotted %g %s.' % (3, 0.1,'camels')
> > > 'In 3 years I have spotted 0.1 camels.'

The number of elements in the tuple has to match the number of format sequences in the
string. Also, the types of the elements have to match the format sequences:

> > > '%d %d %d' % (1, 2)
> > > TypeError: not enough arguments for format string
> > > '%d'% 'dollars'
> > > TypeError: illegal argument type for built-in operation

**14.4. Filenames and paths 135**

In the first example, there aren’t enough elements; in the second, the element is the wrong
type.

The format operator is powerful, but it can be difficult to use. You can read more about it
athttp://docs.python.org/2/library/stdtypes.html#string- formatting.

### 14.4 Filenames and paths

Files are organized into **directories** (also called “folders”). Every running program has a
“current directory,” which is the default directory for most operations. For example, when
you open a file for reading, Python looks for it in the current directory.

Theosmodule provides functions for working with files and directories (“os” stands for
“operating system”).os.getcwdreturns the name of the current directory:

> > > import os
> > > cwd = os.getcwd()
> > > print cwd
> > > /home/dinsdale

cwdstands for “current working directory.” The result in this example is/home/dinsdale,
which is the home directory of a user nameddinsdale.

A string likecwdthat identifies a file is called a **path**. A **relative path** starts from the current
directory; an **absolute path** starts from the topmost directory in the file system.

The paths we have seen so far are simple filenames, so they are relative to the current
directory. To find the absolute path to a file, you can useos.path.abspath:

> > > os.path.abspath('memo.txt')
> > > '/home/dinsdale/memo.txt'

os.path.existschecks whether a file or directory exists:

> > > os.path.exists('memo.txt')
> > > True

If it exists,os.path.isdirchecks whether it’s a directory:

> > > os.path.isdir('memo.txt')
> > > False
> > > os.path.isdir('music')
> > > True

Similarly,os.path.isfilechecks whether it’s a file.

os.listdirreturns a list of the files (and other directories) in the given directory:

> > > os.listdir(cwd)
> > > ['music', 'photos','memo.txt']

To demonstrate these functions, the following example “walks” through a directory, prints
the names of all the files, and calls itself recursively on all the directories.

def walk(dirname):
for name in os.listdir(dirname):
path = os.path.join(dirname, name)

**136 Chapter 14. Files**

```
if os.path.isfile(path):
print path
else:
walk(path)
```

os.path.jointakes a directory and a file name and joins them into a complete path.
**Exercise 14.1.** Theosmodule provides a function calledwalkthat is similar to this one but more
versatile. Read the documentation and use it to print the names of the files in a given directory and
its subdirectories.

Solution:http: // thinkpython. com/ code/ walk. py.

### 14.5 Catching exceptions

A lot of things can go wrong when you try to read and write files. If you try to open a file
that doesn’t exist, you get anIOError:

> > > fin = open('bad_file')
> > > IOError: [Errno 2] No such file or directory: 'bad_file'

If you don’t have permission to access a file:

> > > fout = open('/etc/passwd', 'w')
> > > IOError: [Errno 13] Permission denied:'/etc/passwd'

And if you try to open a directory for reading, you get

> > > fin = open('/home')
> > > IOError: [Errno 21] Is a directory

To avoid these errors, you could use functions likeos.path.existsandos.path.isfile,
but it would take a lot of time and code to check all the possibilities (if “Errno 21” is any
indication, there are at least 21 things that can go wrong).

It is better to go ahead and try—and deal with problems if they happen—which is exactly
what thetrystatement does. The syntax is similar to anifstatement:

try:
fin = open('bad_file')
for line in fin:
print line
fin.close()
except:
print 'Something went wrong.'

Python starts by executing thetryclause. If all goes well, it skips theexceptclause and
proceeds. If an exception occurs, it jumps out of thetryclause and executes theexcept
clause.

Handling an exception with atrystatement is called **catching** an exception. In this exam-
ple, theexceptclause prints an error message that is not very helpful. In general, catching
an exception gives you a chance to fix the problem, or try again, or at least end the program
gracefully.
**Exercise 14.2.** Write a function calledsedthat takes as arguments a pattern string, a replacement
string, and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.

**14.6. Databases 137**

If an error occurs while opening, reading, writing or closing files, your program should catch the
exception, print an error message, and exit. Solution:http: // thinkpython. com/ code/ sed.
py.

### 14.6 Databases

A **database** is a file that is organized for storing data. Most databases are organized like a
dictionary in the sense that they map from keys to values. The biggest difference is that the
database is on disk (or other permanent storage), so it persists after the program ends.

The moduleanydbmprovides an interface for creating and updating database files. As an
example, I’ll create a database that contains captions for image files.

Opening a database is similar to opening other files:

> > > import anydbm
> > > db = anydbm.open('captions.db', 'c')

The mode'c'means that the database should be created if it doesn’t already exist. The
result is a database object that can be used (for most operations) like a dictionary. If you
create a new item,anydbmupdates the database file.

> > > db['cleese.png'] ='Photo of John Cleese.'

When you access one of the items,anydbmreads the file:

> > > print db['cleese.png']
> > > Photo of John Cleese.

If you make another assignment to an existing key,anydbmreplaces the old value:

> > > db['cleese.png'] ='Photo of John Cleese doing a silly walk.'
> > > print db['cleese.png']
> > > Photo of John Cleese doing a silly walk.

Many dictionary methods, likekeysanditems, also work with database objects. So does
iteration with aforstatement.

for key in db:
print key

As with other files, you should close the database when you are done:

> > > db.close()

### 14.7 Pickling

A limitation ofanydbmis that the keys and values have to be strings. If you try to use any
other type, you get an error.

Thepicklemodule can help. It translates almost any type of object into a string suitable
for storage in a database, and then translates strings back into objects.

pickle.dumpstakes an object as a parameter and returns a string representation (dumpsis
short for “dump string”):

**138 Chapter 14. Files**

> > > import pickle
> > > t = [1, 2, 3]
> > > pickle.dumps(t)
> > > '(lp0\nI1\naI2\naI3\na.'

The format isn’t obvious to human readers; it is meant to be easy forpickleto interpret.
pickle.loads(“load string”) reconstitutes the object:

> > > t1 = [1, 2, 3]
> > > s = pickle.dumps(t1)
> > > t2 = pickle.loads(s)
> > > print t2
> > > [1, 2, 3]

Although the new object has the same value as the old, it is not (in general) the same object:

> > > t1 == t2
> > > True
> > > t1 is t2
> > > False

In other words, pickling and then unpickling has the same effect as copying the object.

You can usepickleto store non-strings in a database. In fact, this combination is so com-
mon that it has been encapsulated in a module calledshelve.
**Exercise 14.3.** If you download my solution to Exercise 12.4 fromhttp: // thinkpython. com/
code/ anagram\_ sets. py, you’ll see that it creates a dictionary that maps from a sorted string of
letters to the list of words that can be spelled with those letters. For example,'opst'maps to the
list['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that importsanagram*setsand provides two new functions:store_anagrams
should store the anagram dictionary in a “shelf;”read_anagramsshould look up a word and return
a list of its anagrams. Solution:http: // thinkpython. com/ code/ anagram* db. py

### 14.8 Pipes

Most operating systems provide a command-line interface, also known as a **shell**. Shells
usually provide commands to navigate the file system and launch applications. For exam-
ple, in Unix you can change directories withcd, display the contents of a directory withls,
and launch a web browser by typing (for example)firefox.

Any program that you can launch from the shell can also be launched from Python using
a **pipe**. A pipe is an object that represents a running program.

For example, the Unix commandls -lnormally displays the contents of the current di-
rectory (in long format). You can launchlswithos.popen^1 :

> > > cmd = 'ls -l'
> > > fp = os.popen(cmd)

The argument is a string that contains a shell command. The return value is an object that
behaves just like an open file. You can read the output from thelsprocess one line at a
time withreadlineor get the whole thing at once withread:

(^1) popenis deprecated now, which means we are supposed to stop using it and start using thesubprocess
module. But for simple cases, I findsubprocessmore complicated than necessary. So I am going to keep using
popenuntil they take it away.

**14.9. Writing modules 139**

> > > res = fp.read()

When you are done, you close the pipe like a file:

> > > stat = fp.close()
> > > print stat
> > > None

The return value is the final status of thelsprocess;Nonemeans that it ended normally
(with no errors).

For example, most Unix systems provide a command calledmd5sumthat reads the contents
of a file and computes a “checksum.” You can read about MD5 at http://en.wikipedia.org/wiki/Md5 . This command provides an efficient way to check whether two files have
the same contents. The probability that different contents yield the same checksum is very
small (that is, unlikely to happen before the universe collapses).

You can use a pipe to runmd5sumfrom Python and get the result:

> > > filename ='book.tex'
> > > cmd ='md5sum '+ filename
> > > fp = os.popen(cmd)
> > > res = fp.read()
> > > stat = fp.close()
> > > print res
> > > 1e0033f0ed0656636de0d75144ba32e0 book.tex
> > > print stat
> > > None
> > > **Exercise 14.4.** In a large collection of MP3 files, there may be more than one copy of the same song,
> > > stored in different directories or with different file names. The goal of this exercise is to search for
> > > duplicates.

1. Write a program that searches a directory and all of its subdirectories, recursively, and returns
   a list of complete paths for all files with a given suffix (like.mp3). Hint:os.pathprovides
   several useful functions for manipulating file and path names.
2. To recognize duplicates, you can usemd5sumto compute a “checksum” for each files. If two
   files have the same checksum, they probably have the same contents.
3. To double-check, you can use the Unix commanddiff.

Solution:http: // thinkpython. com/ code/ find\_ duplicates. py.

### 14.9 Writing modules

Any file that contains Python code can be imported as a module. For example, suppose
you have a file namedwc.pywith the following code:

def linecount(filename):
count = 0
for line in open(filename):
count += 1
return count

print linecount('wc.py')

**140 Chapter 14. Files**

If you run this program, it reads itself and prints the number of lines in the file, which is 7.
You can also import it like this:

> > > import wc
> > > 7

Now you have a module objectwc:

> > > print wc
> > > <module'wc'from 'wc.py'>

That provides a function calledlinecount:

> > > wc.linecount('wc.py')
> > > 7

So that’s how you write modules in Python.

The only problem with this example is that when you import the module it executes the
test code at the bottom. Normally when you import a module, it defines new functions but
it doesn’t execute them.

Programs that will be imported as modules often use the following idiom:

if **name** == '**main**':
print linecount('wc.py')

**name**is a built-in variable that is set when the program starts. If the program is run-
ning as a script,**name**has the value**main**; in that case, the test code is executed.
Otherwise, if the module is being imported, the test code is skipped.
**Exercise 14.5.** Type this example into a file namedwc.pyand run it as a script. Then run the
Python interpreter andimport wc. What is the value of**name**when the module is being
imported?

Warning: If you import a module that has already been imported, Python does nothing. It does not
re-read the file, even if it has changed.

If you want to reload a module, you can use the built-in functionreload, but it can be tricky, so
the safest thing to do is restart the interpreter and then import the module again.

### 14.10 Debugging

When you are reading and writing files, you might run into problems with whitespace.
These errors can be hard to debug because spaces, tabs and newlines are normally invisible:

> > > s ='1 2\t 3\n 4'
> > > print s
> > > 1 2 3
> > > 4

The built-in functionreprcan help. It takes any object as an argument and returns a string
representation of the object. For strings, it represents whitespace characters with backslash
sequences:

> > > print repr(s)
> > > '1 2\t 3\n 4'

**14.11. Glossary 141**

This can be helpful for debugging.

One other problem you might run into is that different systems use different characters to
indicate the end of a line. Some systems use a newline, represented\n. Others use a return
character, represented\r. Some use both. If you move files between different systems,
these inconsistencies might cause problems.

For most systems, there are applications to convert from one format to another. You can
find them (and read more about this issue) at http://en.wikipedia.org/wiki/Newline . Or, of course, you could write one yourself.

### 14.11 Glossary

**persistent:** Pertaining to a program that runs indefinitely and keeps at least some of its
data in permanent storage.

**format operator:** An operator,%, that takes a format string and a tuple and generates a
string that includes the elements of the tuple formatted as specified by the format
string.

**format string:** A string, used with the format operator, that contains format sequences.

**format sequence:** A sequence of characters in a format string, like%d, that specifies how a
value should be formatted.

**text file:** A sequence of characters stored in permanent storage like a hard drive.

**directory:** A named collection of files, also called a folder.

**path:** A string that identifies a file.

**relative path:** A path that starts from the current directory.

**absolute path:** A path that starts from the topmost directory in the file system.

**catch:** To prevent an exception from terminating a program using thetryandexceptstate-
ments.

**database:** A file whose contents are organized like a dictionary with keys that correspond
to values.

### 14.12 Exercises

**Exercise 14.6.** Theurllibmodule provides methods for manipulating URLs and downloading
information from the web. The following example downloads and prints a secret message from http://thinkpython.com :

```
import urllib
conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn:
	print line.strip()
```

Run this code and follow the instructions you see there.
Solution: http://thinkpython.com/code/zip_code.py

**142 Chapter 14. Files**

## Chapter 15

# Classes and objects

Code examples from this chapter are available fromhttp://thinkpython.com/code/
Point1.py; solutions to the exercises are available fromhttp://thinkpython.com/code/
Point1_soln.py.

### 15.1 User-defined types

We have used many of Python’s built-in types; now we are going to define a new type. As
an example, we will create a type calledPointthat represents a point in two-dimensional
space.

In mathematical notation, points are often written in parentheses with a comma separating
the coordinates. For example,(0, 0)represents the origin, and(x,y)represents the pointx
units to the right andyunits up from the origin.

There are several ways we might represent points in Python:

- We could store the coordinates separately in two variables,xandy.
- We could store the coordinates as elements in a list or tuple.
- We could create a new type to represent points as objects.

Creating a new type is (a little) more complicated than the other options, but it has advan-
tages that will be apparent soon.

A user-defined type is also called a **class**. A class definition looks like this:

class Point(object):
"""Represents a point in 2-D space."""

This header indicates that the new class is aPoint, which is a kind ofobject, which is a
built-in type.

The body is a docstring that explains what the class is for. You can define variables and
functions inside a class definition, but we will get back to that later.

Defining a class namedPointcreates a class object.

**144 Chapter 15. Classes and objects**

```
x
y
```

```
3.0
4.0
```

```
blank
```

```
Point
```

```
Figure 15.1: Object diagram.
```

> > > print Point
> > > <class '**main**.Point'>

BecausePointis defined at the top level, its “full name” is**main**.Point.

The class object is like a factory for creating objects. To create a Point, you callPointas if it
were a function.

> > > blank = Point()
> > > print blank
> > > <**main**.Point instance at 0xb7e9d3ac>

The return value is a reference to a Point object, which we assign toblank. Creating a new
object is called **instantiation** , and the object is an **instance** of the class.

When you print an instance, Python tells you what class it belongs to and where it is stored
in memory (the prefix0xmeans that the following number is in hexadecimal).

### 15.2 Attributes

You can assign values to an instance using dot notation:

> > > blank.x = 3.0
> > > blank.y = 4.0

This syntax is similar to the syntax for selecting a variable from a module, such asmath.pi
orstring.whitespace. In this case, though, we are assigning values to named elements of
an object. These elements are called **attributes**.

As a noun, “AT-trib-ute” is pronounced with emphasis on the first syllable, as opposed to
“a-TRIB-ute,” which is a verb.

The following diagram shows the result of these assignments. A state diagram that shows
an object and its attributes is called an **object diagram** ; see Figure 15.1.

The variableblankrefers to a Point object, which contains two attributes. Each attribute
refers to a floating-point number.

You can read the value of an attribute using the same syntax:

> > > print blank.y
> > > 4.0
> > > x = blank.x
> > > print x
> > > 3.0

The expressionblank.xmeans, “Go to the objectblankrefers to and get the value ofx.”
In this case, we assign that value to a variable namedx. There is no conflict between the
variablexand the attributex.

You can use dot notation as part of any expression. For example:

**15.3. Rectangles 145**

> > > print'(%g, %g)'% (blank.x, blank.y)
> > > (3.0, 4.0)
> > > distance = math.sqrt(blank.x**2 + blank.y**2)
> > > print distance
> > > 5.0

You can pass an instance as an argument in the usual way. For example:

def print_point(p):
print'(%g, %g)'% (p.x, p.y)

print_pointtakes a point as an argument and displays it in mathematical notation. To
invoke it, you can passblankas an argument:

> > > print_point(blank)
> > > (3.0, 4.0)

Inside the function,pis an alias forblank, so if the function modifiesp,blankchanges.
**Exercise 15.1.** Write a function calleddistance_between_pointsthat takes two Points as ar-
guments and returns the distance between them.

### 15.3 Rectangles

Sometimes it is obvious what the attributes of an object should be, but other times you have
to make decisions. For example, imagine you are designing a class to represent rectangles.
What attributes would you use to specify the location and size of a rectangle? You can ig-
nore angle; to keep things simple, assume that the rectangle is either vertical or horizontal.

There are at least two possibilities:

- You could specify one corner of the rectangle (or the center), the width, and the
  height.
- You could specify two opposing corners.

At this point it is hard to say whether either is better than the other, so we’ll implement the
first one, just as an example.

Here is the class definition:

class Rectangle(object):
"""Represents a rectangle.

```
attributes: width, height, corner.
"""
```

The docstring lists the attributes:widthandheightare numbers;corneris a Point object
that specifies the lower-left corner.

To represent a rectangle, you have to instantiate a Rectangle object and assign values to the
attributes:

box = Rectangle()
box.width = 100.0
box.height = 200.0

**146 Chapter 15. Classes and objects**

```
y
```

```
x 0.0
0.0
```

```
width 100.0
```

```
corner
```

```
200.0
```

```
Point
```

```
Rectangle
box
height
```

```
Figure 15.2: Object diagram.
```

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

The expressionbox.corner.xmeans, “Go to the objectboxrefers to and select the attribute
namedcorner; then go to that object and select the attribute namedx.”

Figure 15.2 shows the state of this object. An object that is an attribute of another object is
**embedded**.

### 15.4 Instances as return values

Functions can return instances. For example,find_centertakes aRectangleas an argu-
ment and returns aPointthat contains the coordinates of the center of theRectangle:

def find_center(rect):
p = Point()
p.x = rect.corner.x + rect.width/2.0
p.y = rect.corner.y + rect.height/2.0
return p

Here is an example that passesboxas an argument and assigns the resulting Point to
center:

> > > center = find_center(box)
> > > print_point(center)
> > > (50.0, 100.0)

### 15.5 Objects are mutable

You can change the state of an object by making an assignment to one of its attributes. For
example, to change the size of a rectangle without changing its position, you can modify
the values ofwidthandheight:

box.width = box.width + 50
box.height = box.width + 100

You can also write functions that modify objects. For example,grow_rectangletakes a
Rectangle object and two numbers,dwidthanddheight, and adds the numbers to the
width and height of the rectangle:

def grow_rectangle(rect, dwidth, dheight):
rect.width += dwidth
rect.height += dheight

**15.6. Copying 147**

Here is an example that demonstrates the effect:

> > > print box.width
> > > 100.0
> > > print box.height
> > > 200.0
> > > grow_rectangle(box, 50, 100)
> > > print box.width
> > > 150.0
> > > print box.height
> > > 300.0

Inside the function,rectis an alias forbox, so if the function modifiesrect,boxchanges.
**Exercise 15.2.** Write a function namedmove_rectanglethat takes a Rectangle and two numbers
nameddxanddy. It should change the location of the rectangle by addingdxto thexcoordinate of
cornerand addingdyto theycoordinate ofcorner.

### 15.6 Copying

Aliasing can make a program difficult to read because changes in one place might have
unexpected effects in another place. It is hard to keep track of all the variables that might
refer to a given object.

Copying an object is often an alternative to aliasing. Thecopymodule contains a function
calledcopythat can duplicate any object:

> > > p1 = Point()
> > > p1.x = 3.0
> > > p1.y = 4.0

> > > import copy
> > > p2 = copy.copy(p1)

p1andp2contain the same data, but they are not the same Point.

> > > print_point(p1)
> > > (3.0, 4.0)
> > > print_point(p2)
> > > (3.0, 4.0)
> > > p1 is p2
> > > False
> > > p1 == p2
> > > False

Theisoperator indicates thatp1andp2are not the same object, which is what we expected.
But you might have expected==to yieldTruebecause these points contain the same data.
In that case, you will be disappointed to learn that for instances, the default behavior of the
==operator is the same as theisoperator; it checks object identity, not object equivalence.
This behavior can be changed—we’ll see how later.

If you usecopy.copyto duplicate a Rectangle, you will find that it copies the Rectangle
object but not the embedded Point.

**148 Chapter 15. Classes and objects**

```
y
```

```
x 0.0
0.0
```

```
width
height
```

```
100.0
```

```
corner
```

```
200.0
```

```
box 100.0
200.0
```

```
width
height
corner
```

```
box2
```

```
Figure 15.3: Object diagram.
```

> > > box2 = copy.copy(box)
> > > box2 is box
> > > False
> > > box2.corner is box.corner
> > > True

Figure 15.3 shows what the object diagram looks like. This operation is called a **shallow
copy** because it copies the object and any references it contains, but not the embedded
objects.

For most applications, this is not what you want. In this example, invoking
grow_rectangle on one of the Rectangles would not affect the other, but invoking
move_rectangleon either would affect both! This behavior is confusing and error-prone.

Fortunately, thecopymodule contains a method nameddeepcopythat copies not only the
object but also the objects it refers to, and the objectstheyrefer to, and so on. You will not
be surprised to learn that this operation is called a **deep copy**.

> > > box3 = copy.deepcopy(box)
> > > box3 is box
> > > False
> > > box3.corner is box.corner
> > > False

box3andboxare completely separate objects.
**Exercise 15.3.** Write a version ofmove_rectanglethat creates and returns a new Rectangle
instead of modifying the old one.

### 15.7 Debugging

When you start working with objects, you are likely to encounter some new exceptions. If
you try to access an attribute that doesn’t exist, you get anAttributeError:

> > > p = Point()
> > > print p.z
> > > AttributeError: Point instance has no attribute'z'

If you are not sure what type an object is, you can ask:

> > > type(p)
> > > <type '**main**.Point'>

If you are not sure whether an object has a particular attribute, you can use the built-in
functionhasattr:

> > > hasattr(p, 'x')
> > > True
> > > hasattr(p, 'z')
> > > False

**15.8. Glossary 149**

The first argument can be any object; the second argument is astringthat contains the name
of the attribute.

### 15.8 Glossary

**class:** A user-defined type. A class definition creates a new class object.

**class object:** An object that contains information about a user-defined type. The class ob-
ject can be used to create instances of the type.

**instance:** An object that belongs to a class.

**attribute:** One of the named values associated with an object.

**embedded (object):** An object that is stored as an attribute of another object.

**shallow copy:** To copy the contents of an object, including any references to embedded
objects; implemented by thecopyfunction in thecopymodule.

**deep copy:** To copy the contents of an object as well as any embedded objects, and any
objects embedded in them, and so on; implemented by thedeepcopyfunction in the
copymodule.

**object diagram:** A diagram that shows objects, their attributes, and the values of the at-
tributes.

### 15.9 Exercises

**Exercise 15.4.** Swampy (see Chapter 4) provides a module namedWorld, which defines a user-
defined type also calledWorld. You can import it like this:

from swampy.World import World

Or, depending on how you installed Swampy, like this:

from World import World

The following code creates a World object and calls themainloopmethod, which waits for the user.

world = World()
world.mainloop()

A window should appear with a title bar and an empty square. We will use this window to draw
Points, Rectangles and other shapes. Add the following lines before callingmainloopand run the
program again.

canvas = world.ca(width=500, height=500, background='white')
bbox = [[-150,-100], [150, 100]]
canvas.rectangle(bbox, outline='black', width=2, fill='green4')

You should see a green rectangle with a black outline. The first line creates a Canvas, which appears
in the window as a white square. The Canvas object provides methods likerectanglefor drawing
various shapes.

bboxis a list of lists that represents the “bounding box” of the rectangle. The first pair of coordinates
is the lower-left corner of the rectangle; the second pair is the upper-right corner.

You can draw a circle like this:

**150 Chapter 15. Classes and objects**

canvas.circle([-25,0], 70, outline=None, fill='red')

The first parameter is the coordinate pair for the center of the circle; the second parameter is the
radius.

If you add this line to the program, the result should resemble the national flag of Bangladesh (see
[http:](http:) // en. wikipedia. org/ wiki/ Gallery* of* sovereign- state\_ flags).

1. Write a function calleddraw_rectanglethat takes a Canvas and a Rectangle as arguments
   and draws a representation of the Rectangle on the Canvas.
2. Add an attribute namedcolorto your Rectangle objects and modifydraw_rectangleso
   that it uses the color attribute as the fill color.
3. Write a function calleddraw_pointthat takes a Canvas and a Point as arguments and draws
   a representation of the Point on the Canvas.
4. Define a new class called Circle with appropriate attributes and instantiate a few Circle ob-
   jects. Write a function calleddraw_circlethat draws circles on the canvas.
5. Write a program that draws the national flag of the Czech Republic. Hint: you can draw a
   polygon like this:

```
points = [[-150,-100], [150, 100], [150, -100]]
canvas.polygon(points, fill='blue')
```

I have written a small program that lists the available colors; you can download it fromhttp:
// thinkpython. com/ code/ color\_ list. py.

## Chapter 16

# Classes and functions

Code examples from this chapter are available fromhttp://thinkpython.com/code/
Time1.py.

### 16.1 Time

As another example of a user-defined type, we’ll define a class calledTimethat records the
time of day. The class definition looks like this:

class Time(object):
"""Represents the time of day.

```
attributes: hour, minute, second
"""
```

We can create a newTimeobject and assign attributes for hours, minutes, and seconds:

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

The state diagram for theTimeobject looks like Figure 16.1.
**Exercise 16.1.** Write a function calledprint_timethat takes a Time object and prints it in the
formhour:minute:second. Hint: the format sequence'%.2d'prints an integer using at least
two digits, including a leading zero if necessary.
**Exercise 16.2.** Write a boolean function calledis_afterthat takes two Time objects,t1andt2,
and returnsTrueift1followst2chronologically andFalseotherwise. Challenge: don’t use anif
statement.

### 16.2 Pure functions

In the next few sections, we’ll write two functions that add time values. They demonstrate
two kinds of functions: pure functions and modifiers. They also demonstrate a develop-
ment plan I’ll call **prototype and patch** , which is a way of tackling a complex problem by
starting with a simple prototype and incrementally dealing with the complications.

**152 Chapter 16. Classes and functions**

```
59
30
```

```
hour
minute
second
```

```
11
```

```
Time
time
```

```
Figure 16.1: Object diagram.
```

Here is a simple prototype ofadd_time:

def add_time(t1, t2):
sum = Time()
sum.hour = t1.hour + t2.hour
sum.minute = t1.minute + t2.minute
sum.second = t1.second + t2.second
return sum

The function creates a newTimeobject, initializes its attributes, and returns a reference to
the new object. This is called a **pure function** because it does not modify any of the objects
passed to it as arguments and it has no effect, like displaying a value or getting user input,
other than returning a value.

To test this function, I’ll create two Time objects:startcontains the start time of a movie,
likeMonty Python and the Holy Grail, anddurationcontains the run time of the movie,
which is one hour 35 minutes.

add_timefigures out when the movie will be done.

> > > start = Time()
> > > start.hour = 9
> > > start.minute = 45
> > > start.second = 0

> > > duration = Time()
> > > duration.hour = 1
> > > duration.minute = 35
> > > duration.second = 0

> > > done = add_time(start, duration)
> > > print_time(done)
> > > 10:80:00

The result,10:80:00might not be what you were hoping for. The problem is that this
function does not deal with cases where the number of seconds or minutes adds up to
more than sixty. When that happens, we have to “carry” the extra seconds into the minute
column or the extra minutes into the hour column.

Here’s an improved version:

def add_time(t1, t2):
sum = Time()
sum.hour = t1.hour + t2.hour
sum.minute = t1.minute + t2.minute
sum.second = t1.second + t2.second

**16.3. Modifiers 153**

```
if sum.second >= 60:
sum.second -= 60
sum.minute += 1
```

```
if sum.minute >= 60:
sum.minute -= 60
sum.hour += 1
```

```
return sum
```

Although this function is correct, it is starting to get big. We will see a shorter alternative
later.

### 16.3 Modifiers

Sometimes it is useful for a function to modify the objects it gets as parameters. In that case,
the changes are visible to the caller. Functions that work this way are called **modifiers**.

increment, which adds a given number of seconds to aTimeobject, can be written naturally
as a modifier. Here is a rough draft:

def increment(time, seconds):
time.second += seconds

```
if time.second >= 60:
time.second -= 60
time.minute += 1
```

```
if time.minute >= 60:
time.minute -= 60
time.hour += 1
```

The first line performs the basic operation; the remainder deals with the special cases we
saw before.

Is this function correct? What happens if the parametersecondsis much greater than sixty?

In that case, it is not enough to carry once; we have to keep doing it untiltime.secondis
less than sixty. One solution is to replace theifstatements withwhilestatements. That
would make the function correct, but not very efficient.
**Exercise 16.3.** Write a correct version ofincrementthat doesn’t contain any loops.

Anything that can be done with modifiers can also be done with pure functions. In fact,
some programming languages only allow pure functions. There is some evidence that
programs that use pure functions are faster to develop and less error-prone than programs
that use modifiers. But modifiers are convenient at times, and functional programs tend to
be less efficient.

In general, I recommend that you write pure functions whenever it is reasonable and resort
to modifiers only if there is a compelling advantage. This approach might be called a
**functional programming style**.
**Exercise 16.4.** Write a “pure” version ofincrementthat creates and returns a new Time object
rather than modifying the parameter.

**154 Chapter 16. Classes and functions**

### 16.4 Prototyping versus planning

The development plan I am demonstrating is called “prototype and patch.” For each func-
tion, I wrote a prototype that performed the basic calculation and then tested it, patching
errors along the way.

This approach can be effective, especially if you don’t yet have a deep understanding
of the problem. But incremental corrections can generate code that is unnecessarily
complicated—since it deals with many special cases—and unreliable—since it is hard to
know if you have found all the errors.

An alternative is **planned development** , in which high-level insight into the problem can
make the programming much easier. In this case, the insight is that a Time object is really
a three-digit number in base 60 (see http://en.wikipedia.org/wiki/Sexagesimal )! The second attribute is the “ones column,” the minute attribute is the “sixties column,” and the hour attribute is the “thirty-six hundreds column.”

When we wroteadd_timeandincrement, we were effectively doing addition in base 60, which is why we had to carry from one column to the next.

This observation suggests another approach to the whole problem—we can convert Time objects to integers and take advantage of the fact that the computer knows how to do integer arithmetic.

Here is a function that converts Times to integers:

def time*to_int(time):
minutes = time.hour * 60 + time.minute
seconds = minutes \_ 60 + time.second
return seconds

And here is the function that converts integers to Times (recall thatdivmoddivides the first
argument by the second and returns the quotient and remainder as a tuple).

def int_to_time(seconds):
time = Time()
minutes, time.second = divmod(seconds, 60)
time.hour, time.minute = divmod(minutes, 60)
return time

You might have to think a bit, and run some tests, to convince yourself that these functions
are correct. One way to test them is to check thattime_to_int(int_to_time(x)) == xfor
many values ofx. This is an example of a consistency check.

Once you are convinced they are correct, you can use them to rewriteadd_time:

def add_time(t1, t2):
seconds = time_to_int(t1) + time_to_int(t2)
return int_to_time(seconds)

This version is shorter than the original, and easier to verify.
**Exercise 16.5.** Rewriteincrementusingtime_to_intandint_to_time.

In some ways, converting from base 60 to base 10 and back is harder than just dealing with
times. Base conversion is more abstract; our intuition for dealing with time values is better.

But if we have the insight to treat times as base 60 numbers and make the investment of
writing the conversion functions (time_to_intandint_to_time), we get a program that
is shorter, easier to read and debug, and more reliable.

**16.5. Debugging 155**

It is also easier to add features later. For example, imagine subtracting two Times to find
the duration between them. The naive approach would be to implement subtraction with
borrowing. Using the conversion functions would be easier and more likely to be correct.

Ironically, sometimes making a problem harder (or more general) makes it easier (because
there are fewer special cases and fewer opportunities for error).

### 16.5 Debugging

A Time object is well-formed if the values ofminuteandsecondare between 0 and 60
(including 0 but not 60) and ifhouris positive.hourandminuteshould be integral values,
but we might allowsecondto have a fraction part.

Requirements like these are called **invariants** because they should always be true. To put
it a different way, if they are not true, then something has gone wrong.

Writing code to check your invariants can help you detect errors and find their causes. For
example, you might have a function likevalid_timethat takes a Time object and returns
Falseif it violates an invariant:

def valid_time(time):
if time.hour < 0 or time.minute < 0 or time.second < 0:
return False
if time.minute >= 60 or time.second >= 60:
return False
return True

Then at the beginning of each function you could check the arguments to make sure they
are valid:

def add_time(t1, t2):
if not valid_time(t1) or not valid_time(t2):
raise ValueError('invalid Time object in add_time')
seconds = time_to_int(t1) + time_to_int(t2)
return int_to_time(seconds)

Or you could use anassertstatement, which checks a given invariant and raises an ex-
ception if it fails:

def add_time(t1, t2):
assert valid_time(t1) and valid_time(t2)
seconds = time_to_int(t1) + time_to_int(t2)
return int_to_time(seconds)

assertstatements are useful because they distinguish code that deals with normal condi-
tions from code that checks for errors.

### 16.6 Glossary

**prototype and patch:** A development plan that involves writing a rough draft of a pro-
gram, testing, and correcting errors as they are found.

**planned development:** A development plan that involves high-level insight into the prob-
lem and more planning than incremental development or prototype development.

**156 Chapter 16. Classes and functions**

**pure function:** A function that does not modify any of the objects it receives as arguments.
Most pure functions are fruitful.

**modifier:** A function that changes one or more of the objects it receives as arguments. Most
modifiers are fruitless.

**functional programming style:** A style of program design in which the majority of func-
tions are pure.

**invariant:** A condition that should always be true during the execution of a program.

### 16.7 Exercises

Code examples from this chapter are available fromhttp://thinkpython.com/code/
Time1.py; solutions to these exercises are available fromhttp://thinkpython.com/code/
Time1_soln.py.
**Exercise 16.6.** Write a function calledmul_timethat takes a Time object and a number and returns
a new Time object that contains the product of the original Time and the number.

Then usemul_timeto write a function that takes a Time object that represents the finishing time
in a race, and a number that represents the distance, and returns a Time object that represents the
average pace (time per mile).
**Exercise 16.7.** Thedatetimemodule providesdateandtimeobjects that are similar to the Date
and Time objects in this chapter, but they provide a rich set of methods and operators. Read the
documentation athttp: // docs. python. org/ 2/ library/ datetime. html.

1. Use thedatetimemodule to write a program that gets the current date and prints the day of
   the week.
2. Write a program that takes a birthday as input and prints the user’s age and the number of
   days, hours, minutes and seconds until their next birthday.
3. For two people born on different days, there is a day when one is twice as old as the other.
   That’s their Double Day. Write a program that takes two birthdays and computes their Double
   Day.
4. For a little more challenge, write the more general version that computes the day when one
   person is n times older than the other.

## Chapter 17

# Classes and methods

Code examples from this chapter are available fromhttp://thinkpython.com/code/
Time2.py.

### 17.1 Object-oriented features

Python is an **object-oriented programming language** , which means that it provides fea-
tures that support object-oriented programming.

It is not easy to define object-oriented programming, but we have already seen some of its
characteristics:

- Programs are made up of object definitions and function definitions, and most of the
  computation is expressed in terms of operations on objects.
- Each object definition corresponds to some object or concept in the real world, and
  the functions that operate on that object correspond to the ways real-world objects
  interact.

For example, theTimeclass defined in Chapter 16 corresponds to the way people record
the time of day, and the functions we defined correspond to the kinds of things people do
with times. Similarly, thePointandRectangleclasses correspond to the mathematical
concepts of a point and a rectangle.

So far, we have not taken advantage of the features Python provides to support object-
oriented programming. These features are not strictly necessary; most of them provide
alternative syntax for things we have already done. But in many cases, the alternative is
more concise and more accurately conveys the structure of the program.

For example, in theTimeprogram, there is no obvious connection between the class defi-
nition and the function definitions that follow. With some examination, it is apparent that
every function takes at least oneTimeobject as an argument.

This observation is the motivation for **methods** ; a method is a function that is associated
with a particular class. We have seen methods for strings, lists, dictionaries and tuples. In
this chapter, we will define methods for user-defined types.

Methods are semantically the same as functions, but there are two syntactic differences:

**158 Chapter 17. Classes and methods**

- Methods are defined inside a class definition in order to make the relationship be-
  tween the class and the method explicit.
- The syntax for invoking a method is different from the syntax for calling a function.

In the next few sections, we will take the functions from the previous two chapters and
transform them into methods. This transformation is purely mechanical; you can do it
simply by following a sequence of steps. If you are comfortable converting from one form
to another, you will be able to choose the best form for whatever you are doing.

### 17.2 Printing objects

In Chapter 16, we defined a class namedTimeand in Exercise 16.1, you wrote a function
namedprint_time:

class Time(object):
"""Represents the time of day."""

def print_time(time):
print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)

To call this function, you have to pass aTimeobject as an argument:

> > > start = Time()
> > > start.hour = 9
> > > start.minute = 45
> > > start.second = 00
> > > print_time(start)
> > > 09:45:00

To makeprint_timea method, all we have to do is move the function definition inside the
class definition. Notice the change in indentation.

class Time(object):
def print_time(time):
print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)

Now there are two ways to callprint_time. The first (and less common) way is to use
function syntax:

> > > Time.print_time(start)
> > > 09:45:00

In this use of dot notation,Timeis the name of the class, andprint_timeis the name of the
method.startis passed as a parameter.

The second (and more concise) way is to use method syntax:

> > > start.print_time()
> > > 09:45:00

In this use of dot notation,print_timeis the name of the method (again), andstartis
the object the method is invoked on, which is called the **subject**. Just as the subject of
a sentence is what the sentence is about, the subject of a method invocation is what the
method is about.

Inside the method, the subject is assigned to the first parameter, so in this casestartis
assigned totime.

**17.3. Another example 159**

By convention, the first parameter of a method is calledself, so it would be more common
to writeprint_timelike this:

class Time(object):
def print_time(self):
print '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

The reason for this convention is an implicit metaphor:

- The syntax for a function call,print_time(start), suggests that the function is the
  active agent. It says something like, “Heyprint_time! Here’s an object for you to
  print.”
- In object-oriented programming, the objects are the active agents. A method invoca-
  tion likestart.print_time()says “Heystart! Please print yourself.”

This change in perspective might be more polite, but it is not obvious that it is useful. In the
examples we have seen so far, it may not be. But sometimes shifting responsibility from the
functions onto the objects makes it possible to write more versatile functions, and makes it
easier to maintain and reuse code.
**Exercise 17.1.** Rewritetime_to_int(from Section 16.4) as a method. It is probably not appro-
priate to rewriteint_to_timeas a method; what object you would invoke it on?

### 17.3 Another example

Here’s a version ofincrement(from Section 16.3) rewritten as a method:

# inside class Time:

```
def increment(self, seconds):
seconds += self.time_to_int()
return int_to_time(seconds)
```

This version assumes thattime_to_intis written as a method, as in Exercise 17.1. Also,
note that it is a pure function, not a modifier.

Here’s how you would invokeincrement:

> > > start.print_time()
> > > 09:45:00
> > > end = start.increment(1337)
> > > end.print_time()
> > > 10:07:17

The subject,start, gets assigned to the first parameter,self. The argument, 1337 , gets
assigned to the second parameter,seconds.

This mechanism can be confusing, especially if you make an error. For example, if you
invokeincrementwith two arguments, you get:

> > > end = start.increment(1337, 460)
> > > TypeError: increment() takes exactly 2 arguments (3 given)

The error message is initially confusing, because there are only two arguments in paren-
theses. But the subject is also considered an argument, so all together that’s three.

**160 Chapter 17. Classes and methods**

### 17.4 A more complicated example

is_after(from Exercise 16.2) is slightly more complicated because it takes two Time ob-
jects as parameters. In this case it is conventional to name the first parameterselfand the
second parameterother:

# inside class Time:

```
def is_after(self, other):
return self.time_to_int() > other.time_to_int()
```

To use this method, you have to invoke it on one object and pass the other as an argument:

> > > end.is_after(start)
> > > True

One nice thing about this syntax is that it almost reads like English: “end is after start?”

### 17.5 The init method

The init method (short for “initialization”) is a special method that gets invoked when an
object is instantiated. Its full name is**init**(two underscore characters, followed by
init, and then two more underscores). An init method for theTimeclass might look like
this:

# inside class Time:

```
def __init__(self, hour=0, minute=0, second=0):
self.hour = hour
self.minute = minute
self.second = second
```

It is common for the parameters of**init**to have the same names as the attributes. The
statement

```
self.hour = hour
```

stores the value of the parameterhouras an attribute ofself.

The parameters are optional, so if you callTimewith no arguments, you get the default
values.

> > > time = Time()
> > > time.print_time()
> > > 00:00:00

If you provide one argument, it overrideshour:

> > > time = Time (9)
> > > time.print_time()
> > > 09:00:00

If you provide two arguments, they overridehourandminute.

> > > time = Time(9, 45)
> > > time.print_time()
> > > 09:45:00

And if you provide three arguments, they override all three default values.
**Exercise 17.2.** Write an init method for thePointclass that takesxandyas optional parameters
and assigns them to the corresponding attributes.

**17.6. The** **str** **method 161**

### 17.6 The**str**method

**str**is a special method, like**init**, that is supposed to return a string representa-
tion of an object.

For example, here is astrmethod for Time objects:

# inside class Time:

```
def __str__(self):
return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
```

When youprintan object, Python invokes thestrmethod:

> > > time = Time(9, 45)
> > > print time
> > > 09:45:00

When I write a new class, I almost always start by writing**init**, which makes it easier
to instantiate objects, and**str**, which is useful for debugging.
**Exercise 17.3.** Write astrmethod for thePointclass. Create a Point object and print it.

### 17.7 Operator overloading

By defining other special methods, you can specify the behavior of operators on user-
defined types. For example, if you define a method named**add**for theTimeclass,
you can use the+operator on Time objects.

Here is what the definition might look like:

# inside class Time:

```
def __add__(self, other):
seconds = self.time_to_int() + other.time_to_int()
return int_to_time(seconds)
```

And here is how you could use it:

> > > start = Time(9, 45)
> > > duration = Time(1, 35)
> > > print start + duration
> > > 11:20:00

When you apply the+operator to Time objects, Python invokes**add**. When you print
the result, Python invokes**str**. So there is quite a lot happening behind the scenes!

Changing the behavior of an operator so that it works with user-defined types is called **op-
erator overloading**. For every operator in Python there is a corresponding special method,
like**add**. For more details, seehttp://docs.python.org/2/reference/datamodel.
html#specialnames.
**Exercise 17.4.** Write anaddmethod for the Point class.

**162 Chapter 17. Classes and methods**

### 17.8 Type-based dispatch

In the previous section we added two Time objects, but you also might want to add an
integer to a Time object. The following is a version of**add**that checks the type of
otherand invokes eitheradd_timeorincrement:

# inside class Time:

```
def __add__(self, other):
if isinstance(other, Time):
return self.add_time(other)
else:
return self.increment(other)
```

```
def add_time(self, other):
seconds = self.time_to_int() + other.time_to_int()
return int_to_time(seconds)
```

```
def increment(self, seconds):
seconds += self.time_to_int()
return int_to_time(seconds)
```

The built-in functionisinstancetakes a value and a class object, and returnsTrueif the
value is an instance of the class.

Ifotheris a Time object,**add**invokesadd_time. Otherwise it assumes that the param-
eter is a number and invokesincrement. This operation is called a **type-based dispatch**
because it dispatches the computation to different methods based on the type of the argu-
ments.

Here are examples that use the+operator with different types:

> > > start = Time(9, 45)
> > > duration = Time(1, 35)
> > > print start + duration
> > > 11:20:00
> > > print start + 1337
> > > 10:07:17

Unfortunately, this implementation of addition is not commutative. If the integer is the
first operand, you get

> > > print 1337 + start
> > > TypeError: unsupported operand type(s) for +: 'int'and'instance'

The problem is, instead of asking the Time object to add an integer, Python is asking an
integer to add a Time object, and it doesn’t know how to do that. But there is a clever
solution for this problem: the special method**radd**, which stands for “right-side add.”
This method is invoked when a Time object appears on the right side of the+operator.
Here’s the definition:

# inside class Time:

```
def __radd__(self, other):
return self.__add__(other)
```

And here’s how it’s used:

**17.9. Polymorphism 163**

> > > print 1337 + start
> > > 10:07:17
> > > **Exercise 17.5.** Write anaddmethod for Points that works with either a Point object or a tuple:

- If the second operand is a Point, the method should return a new Point whose x coordinate is
  the sum of the x coordinates of the operands, and likewise for the y coordinates.
- If the second operand is a tuple, the method should add the first element of the tuple to the x
  coordinate and the second element to the y coordinate, and return a new Point with the result.

### 17.9 Polymorphism

Type-based dispatch is useful when it is necessary, but (fortunately) it is not always neces-
sary. Often you can avoid it by writing functions that work correctly for arguments with
different types.

Many of the functions we wrote for strings will actually work for any kind of sequence.
For example, in Section 11.1 we usedhistogramto count the number of times each letter
appears in a word.

def histogram(s):
d = dict()
for c in s:
if c not in d:
d[c] = 1
else:
d[c] = d[c]+1
return d

This function also works for lists, tuples, and even dictionaries, as long as the elements of
sare hashable, so they can be used as keys ind.

> > > t = ['spam','egg','spam', 'spam', 'bacon', 'spam']
> > > histogram(t)
> > > {'bacon': 1, 'egg': 1,'spam': 4}

Functions that can work with several types are called **polymorphic**. Polymorphism can
facilitate code reuse. For example, the built-in functionsum, which adds the elements of a
sequence, works as long as the elements of the sequence support addition.

Since Time objects provide anaddmethod, they work withsum:

> > > t1 = Time(7, 43)
> > > t2 = Time(7, 41)
> > > t3 = Time(7, 37)
> > > total = sum([t1, t2, t3])
> > > print total
> > > 23:01:00

In general, if all of the operations inside a function work with a given type, then the func-
tion works with that type.

The best kind of polymorphism is the unintentional kind, where you discover that a func-
tion you already wrote can be applied to a type you never planned for.

**164 Chapter 17. Classes and methods**

### 17.10 Debugging

It is legal to add attributes to objects at any point in the execution of a program, but if you
are a stickler for type theory, it is a dubious practice to have objects of the same type with
different attribute sets. It is usually a good idea to initialize all of an object’s attributes in
the init method.

If you are not sure whether an object has a particular attribute, you can use the built-in
functionhasattr(see Section 15.7).

Another way to access the attributes of an object is through the special attribute**dict**,
which is a dictionary that maps attribute names (as strings) and values:

> > > p = Point(3, 4)
> > > print p.**dict**
> > > {'y': 4,'x': 3}

For purposes of debugging, you might find it useful to keep this function handy:

def print_attributes(obj):
for attr in obj.**dict**:
print attr, getattr(obj, attr)

print_attributestraverses the items in the object’s dictionary and prints each attribute
name and its corresponding value.

The built-in functiongetattrtakes an object and an attribute name (as a string) and returns
the attribute’s value.

### 17.11 Interface and implementation

One of the goals of object-oriented design is to make software more maintainable, which
means that you can keep the program working when other parts of the system change, and
modify the program to meet new requirements.

A design principle that helps achieve that goal is to keep interfaces separate from imple-
mentations. For objects, that means that the methods a class provides should not depend
on how the attributes are represented.

For example, in this chapter we developed a class that represents a time of day. Methods
provided by this class includetime_to_int,is_after, andadd_time.

We could implement those methods in several ways. The details of the implementation
depend on how we represent time. In this chapter, the attributes of aTimeobject arehour,
minute, andsecond.

As an alternative, we could replace these attributes with a single integer representing the
number of seconds since midnight. This implementation would make some methods, like
is_after, easier to write, but it makes some methods harder.

After you deploy a new class, you might discover a better implementation. If other parts
of the program are using your class, it might be time-consuming and error-prone to change
the interface.

But if you designed the interface carefully, you can change the implementation without
changing the interface, which means that other parts of the program don’t have to change.

**17.12. Glossary 165**

Keeping the interface separate from the implementation means that you have to hide the
attributes. Code in other parts of the program (outside the class definition) should use
methods to read and modify the state of the object. They should not access the attributes di-
rectly. This principle is called **information hiding** ; see http://en.wikipedia.org/wiki/Information_hiding.

**Exercise 17.6.** Download the code from this chapter ( http://thinkpython.com/code/Time2. py ). Change the attributes ofTimeto be a single integer representing seconds since mid-
night. Then modify the methods (and the functionint_to_time) to work with the new implemen-
tation. You should not have to modify the test code inmain. When you are done, the output should
be the same as before. Solution: http://thinkpython.com/code/Time2_soln.py

### 17.12 Glossary

**object-oriented language:** A language that provides features, such as user-defined classes
and method syntax, that facilitate object-oriented programming.

**object-oriented programming:** A style of programming in which data and the operations
that manipulate it are organized into classes and methods.

**method:** A function that is defined inside a class definition and is invoked on instances of
that class.

**subject:** The object a method is invoked on.

**operator overloading:** Changing the behavior of an operator like+so it works with a user-
defined type.

**type-based dispatch:** A programming pattern that checks the type of an operand and in-
vokes different functions for different types.

**polymorphic:** Pertaining to a function that can work with more than one type.

**information hiding:** The principle that the interface provided by an object should not de-
pend on its implementation, in particular the representation of its attributes.

### 17.13 Exercises

**Exercise 17.7.** This exercise is a cautionary tale about one of the most common, and difficult to
find, errors in Python. Write a definition for a class namedKangaroowith the following methods:

1. An**init**method that initializes an attribute namedpouch_contentsto an empty list.
2. A method named put_in_pouch that takes an object of any type and adds it to
   pouch_contents.
3. A**str**method that returns a string representation of the Kangaroo object and the con-
   tents of the pouch.

Test your code by creating twoKangarooobjects, assigning them to variables namedkangaand
roo, and then addingrooto the contents ofkanga’s pouch.

**166 Chapter 17. Classes and methods**

Downloadhttp: // thinkpython. com/ code/ BadKangaroo. py. It contains a solution to the
previous problem with one big, nasty bug. Find and fix the bug.

If you get stuck, you can downloadhttp: // thinkpython. com/ code/ GoodKangaroo. py,
which explains the problem and demonstrates a solution.
**Exercise 17.8.** Visual is a Python module that provides 3-D graphics. It is not always included
in a Python installation, so you might have to install it from your software repository or, if it’s not
there, fromhttp: // vpython. org.

The following example creates a 3-D space that is 256 units wide, long and high, and sets the
“center” to be the point(128, 128, 128). Then it draws a blue sphere.

from visual import \*

scene.range = (256, 256, 256)
scene.center = (128, 128, 128)

color = (0.1, 0.1, 0.9) # mostly blue
sphere(pos=scene.center, radius=128, color=color)

coloris an RGB tuple; that is, the elements are Red-Green-Blue levels between 0.0 and 1.0 (see
[http:](http:) // en. wikipedia. org/ wiki/ RGB* color* model).

If you run this code, you should see a window with a black background and a blue sphere. If you
drag the middle button up and down, you can zoom in and out. You can also rotate the scene by
dragging the right button, but with only one sphere in the world, it is hard to tell the difference.

The following loop creates a cube of spheres:

t = range(0, 256, 51)
for x in t:
for y in t:
for z in t:
pos = x, y, z
sphere(pos=pos, radius=10, color=color)

1. Put this code in a script and make sure it works for you.
2. Modify the program so that each sphere in the cube has the color that corresponds to its
   position in RGB space. Notice that the coordinates are in the range 0–255, but the RGB
   tuples are in the range 0.0–1.0.
3. Downloadhttp: // thinkpython. com/ code/ color\_ list. py and use the function
   read_colorsto generate a list of the available colors on your system, their names and RGB
   values. For each named color draw a sphere in the position that corresponds to its RGB values.

You can see my solution athttp: // thinkpython. com/ code/ color\_ space. py.

## Chapter 18

# Inheritance

In this chapter I present classes to represent playing cards, decks of cards, and poker hands.
If you don’t play poker, you can read about it at http://en.wikipedia.org/wiki/Poker,
but you don’t have to; I’ll tell you what you need to know for the exercises. Code examples
from this chapter are available fromhttp://thinkpython.com/code/Card.py.

If you are not familiar with Anglo-American playing cards, you can read about them at [http://en.wikipedia.org/wiki/Playing_cards](http://en.wikipedia.org/wiki/Playing_cards.).

### 18.1 Card objects

There are fifty-two cards in a deck, each of which belongs to one of four suits and one of
thirteen ranks. The suits are Spades, Hearts, Diamonds, and Clubs (in descending order in
bridge). The ranks are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. Depending on
the game that you are playing, an Ace may be higher than King or lower than 2.

If we want to define a new object to represent a playing card, it is obvious what the at-
tributes should be:rankandsuit. It is not as obvious what type the attributes should be.
One possibility is to use strings containing words like'Spade'for suits and'Queen'for
ranks. One problem with this implementation is that it would not be easy to compare cards
to see which had a higher rank or suit.

An alternative is to use integers to **encode** the ranks and suits. In this context, “encode”
means that we are going to define a mapping between numbers and suits, or between
numbers and ranks. This kind of encoding is not meant to be a secret (that would be
“encryption”).

For example, this table shows the suits and the corresponding integer codes:

```
Spades 7→ 3
Hearts 7→ 2
Diamonds 7→ 1
Clubs 7→ 0
```

This code makes it easy to compare cards; because higher suits map to higher numbers, we
can compare suits by comparing their codes.

**168 Chapter 18. Inheritance**

The mapping for ranks is fairly obvious; each of the numerical ranks maps to the corre-
sponding integer, and for face cards:

```
Jack 7→ 11
Queen 7→ 12
King 7→ 13
```

I am using the7→symbol to make it clear that these mappings are not part of the Python
program. They are part of the program design, but they don’t appear explicitly in the code.

The class definition forCardlooks like this:

class Card(object):
"""Represents a standard playing card."""

```
def __init__(self, suit=0, rank=2):
self.suit = suit
self.rank = rank
```

As usual, the init method takes an optional parameter for each attribute. The default card
is the 2 of Clubs.

To create a Card, you callCardwith the suit and rank of the card you want.

queen_of_diamonds = Card(1, 12)

### 18.2 Class attributes

In order to print Card objects in a way that people can easily read, we need a mapping
from the integer codes to the corresponding ranks and suits. A natural way to do that is
with lists of strings. We assign these lists to **class attributes** :

# inside class Card:

```
suit_names = ['Clubs', 'Diamonds','Hearts', 'Spades']
rank_names = [None, 'Ace', ' 2 ', ' 3 ', ' 4 ', ' 5 ',' 6 ',' 7 ',
' 8 ', ' 9 ', ' 10 ','Jack','Queen','King']
```

```
def __str__(self):
return '%s of %s'% (Card.rank_names[self.rank],
Card.suit_names[self.suit])
```

Variables likesuit_namesandrank_names, which are defined inside a class but outside
of any method, are called class attributes because they are associated with the class object
Card.

This term distinguishes them from variables likesuitandrank, which are called **instance
attributes** because they are associated with a particular instance.

Both kinds of attribute are accessed using dot notation. For example, in**str**,self
is a Card object, and self.rank is its rank. Similarly, Cardis a class object, and
Card.rank_namesis a list of strings associated with the class.

Every card has its ownsuitandrank, but there is only one copy ofsuit_namesand
rank_names.

**18.3. Comparing cards 169**

```
list
suit_names
```

```
list
rank_names
```

```
Card
```

```
type
```

```
1
11
```

```
suit
rank
```

```
card1
```

```
Card
```

```
Figure 18.1: Object diagram.
```

Putting it all together, the expressionCard.rank_names[self.rank]means “use the at-
tributerankfrom the objectselfas an index into the listrank_namesfrom the classCard,
and select the appropriate string.”

The first element ofrank_namesisNonebecause there is no card with rank zero. By includ-
ingNoneas a place-keeper, we get a mapping with the nice property that the index 2 maps
to the string' 2 ', and so on. To avoid this tweak, we could have used a dictionary instead
of a list.

With the methods we have so far, we can create and print cards:

> > > card1 = Card(2, 11)
> > > print card1
> > > Jack of Hearts

Figure 18.1 is a diagram of theCardclass object and one Card instance. Cardis a class
object, so it has typetype.card1has typeCard. (To save space, I didn’t draw the contents
ofsuit_namesandrank_names).

### 18.3 Comparing cards

For built-in types, there are relational operators (<,>,==, etc.) that compare values and de-
termine when one is greater than, less than, or equal to another. For user-defined types, we
can override the behavior of the built-in operators by providing a method named**cmp**.

**cmp**takes two parameters,selfandother, and returns a positive number if the first
object is greater, a negative number if the second object is greater, and 0 if they are equal to
each other.

The correct ordering for cards is not obvious. For example, which is better, the 3 of Clubs
or the 2 of Diamonds? One has a higher rank, but the other has a higher suit. In order to
compare cards, you have to decide whether rank or suit is more important.

The answer might depend on what game you are playing, but to keep things simple, we’ll
make the arbitrary choice that suit is more important, so all of the Spades outrank all of the
Diamonds, and so on.

With that decided, we can write**cmp**:

**170 Chapter 18. Inheritance**

# inside class Card:

```
def __cmp__(self, other):
# check the suits
if self.suit > other.suit: return 1
if self.suit < other.suit: return -1
```

```
# suits are the same... check ranks
if self.rank > other.rank: return 1
if self.rank < other.rank: return -1
```

```
# ranks are the same... it's a tie
return 0
```

You can write this more concisely using tuple comparison:

# inside class Card:

```
def __cmp__(self, other):
t1 = self.suit, self.rank
t2 = other.suit, other.rank
return cmp(t1, t2)
```

The built-in functioncmphas the same interface as the method**cmp**: it takes two values
and returns a positive number if the first is larger, a negative number if the second is larger,
and 0 if they are equal.

In Python 3,cmpno longer exists, and the**cmp**method is not supported. Instead you
should provide**lt**, which returnsTrueifselfis less thanother. You can implement
**lt**using tuples and the<operator.
**Exercise 18.1.** Write a**cmp**method for Time objects. Hint: you can use tuple comparison, but
you also might consider using integer subtraction.

### 18.4 Decks

Now that we have Cards, the next step is to define Decks. Since a deck is made up of cards,
it is natural for each Deck to contain a list of cards as an attribute.

The following is a class definition forDeck. The init method creates the attributecardsand
generates the standard set of fifty-two cards:

class Deck(object):

```
def __init__(self):
self.cards = []
for suit in range(4):
for rank in range(1, 14):
card = Card(suit, rank)
self.cards.append(card)
```

The easiest way to populate the deck is with a nested loop. The outer loop enumerates the
suits from 0 to 3. The inner loop enumerates the ranks from 1 to 13. Each iteration creates
a new Card with the current suit and rank, and appends it toself.cards.

**18.5. Printing the deck 171**

### 18.5 Printing the deck

Here is a**str**method forDeck:

#inside class Deck:

```
def __str__(self):
res = []
for card in self.cards:
res.append(str(card))
return '\n'.join(res)
```

This method demonstrates an efficient way to accumulate a large string: building a list of
strings and then usingjoin. The built-in functionstrinvokes the**str**method on each
card and returns the string representation.

Since we invokejoinon a newline character, the cards are separated by newlines. Here’s
what the result looks like:

> > > deck = Deck()
> > > print deck
> > > Ace of Clubs
> > > 2 of Clubs
> > > 3 of Clubs

10 of Spades
Jack of Spades
Queen of Spades
King of Spades

Even though the result appears on 52 lines, it is one long string that contains newlines.

### 18.6 Add, remove, shuffle and sort

To deal cards, we would like a method that removes a card from the deck and returns it.
The list methodpopprovides a convenient way to do that:

#inside class Deck:

```
def pop_card(self):
return self.cards.pop()
```

Sincepopremoves thelastcard in the list, we are dealing from the bottom of the deck. In
real life “bottom dealing” is frowned upon, but in this context it’s ok.

To add a card, we can use the list methodappend:

#inside class Deck:

```
def add_card(self, card):
self.cards.append(card)
```

A method like this that uses another function without doing much real work is sometimes
called a **veneer**. The metaphor comes from woodworking, where it is common to glue a
thin layer of good quality wood to the surface of a cheaper piece of wood.

**172 Chapter 18. Inheritance**

In this case we are defining a “thin” method that expresses a list operation in terms that are
appropriate for decks.

As another example, we can write a Deck method namedshuffleusing the function
shufflefrom therandommodule:

# inside class Deck:

```
def shuffle(self):
random.shuffle(self.cards)
```

Don’t forget to importrandom.
**Exercise 18.2.** Write a Deck method namedsortthat uses the list methodsortto sort the cards
in aDeck.sortuses the**cmp**method we defined to determine sort order.

### 18.7 Inheritance

The language feature most often associated with object-oriented programming is **inher-
itance**. Inheritance is the ability to define a new class that is a modified version of an
existing class.

It is called “inheritance” because the new class inherits the methods of the existing class.
Extending this metaphor, the existing class is called the **parent** and the new class is called
the **child**.

As an example, let’s say we want a class to represent a “hand,” that is, the set of cards held
by one player. A hand is similar to a deck: both are made up of a set of cards, and both
require operations like adding and removing cards.

A hand is also different from a deck; there are operations we want for hands that don’t
make sense for a deck. For example, in poker we might compare two hands to see which
one wins. In bridge, we might compute a score for a hand in order to make a bid.

This relationship between classes—similar, but different—lends itself to inheritance.

The definition of a child class is like other class definitions, but the name of the parent class
appears in parentheses:

class Hand(Deck):
"""Represents a hand of playing cards."""

This definition indicates thatHandinherits fromDeck; that means we can use methods like
pop_cardandadd_cardfor Hands as well as Decks.

Handalso inherits**init**fromDeck, but it doesn’t really do what we want: instead of
populating the hand with 52 new cards, the init method for Hands should initializecards
with an empty list.

If we provide an init method in theHandclass, it overrides the one in theDeckclass:

# inside class Hand:

```
def __init__(self, label=''):
self.cards = []
self.label = label
```

**18.8. Class diagrams 173**

So when you create a Hand, Python invokes this init method:

> > > hand = Hand('new hand')
> > > print hand.cards
> > > []
> > > print hand.label
> > > new hand

But the other methods are inherited fromDeck, so we can usepop_cardandadd_cardto
deal a card:

> > > deck = Deck()
> > > card = deck.pop_card()
> > > hand.add_card(card)
> > > print hand
> > > King of Spades

A natural next step is to encapsulate this code in a method calledmove_cards:

#inside class Deck:

```
def move_cards(self, hand, num):
for i in range(num):
hand.add_card(self.pop_card())
```

move_cardstakes two arguments, a Hand object and the number of cards to deal. It modi-
fies bothselfandhand, and returnsNone.

In some games, cards are moved from one hand to another, or from a hand back to the
deck. You can usemove_cardsfor any of these operations:selfcan be either a Deck or a
Hand, andhand, despite the name, can also be aDeck.
**Exercise 18.3.** Write a Deck method calleddeal_handsthat takes two parameters, the number of
hands and the number of cards per hand, and that creates new Hand objects, deals the appropriate
number of cards per hand, and returns a list of Hand objects.

Inheritance is a useful feature. Some programs that would be repetitive without inheritance
can be written more elegantly with it. Inheritance can facilitate code reuse, since you can
customize the behavior of parent classes without having to modify them. In some cases,
the inheritance structure reflects the natural structure of the problem, which makes the
program easier to understand.

On the other hand, inheritance can make programs difficult to read. When a method is
invoked, it is sometimes not clear where to find its definition. The relevant code may
be scattered among several modules. Also, many of the things that can be done using
inheritance can be done as well or better without it.

### 18.8 Class diagrams

So far we have seen stack diagrams, which show the state of a program, and object dia-
grams, which show the attributes of an object and their values. These diagrams represent
a snapshot in the execution of a program, so they change as the program runs.

They are also highly detailed; for some purposes, too detailed. A class diagram is a more
abstract representation of the structure of a program. Instead of showing individual ob-
jects, it shows classes and the relationships between them.

**174 Chapter 18. Inheritance**

```
Hand
```

```
Deck * Card
```

```
Figure 18.2: Class diagram.
```

There are several kinds of relationship between classes:

- Objects in one class might contain references to objects in another class. For example,
  each Rectangle contains a reference to a Point, and each Deck contains references to
  many Cards. This kind of relationship is called **HAS-A** , as in, “a Rectangle has a
  Point.”
- One class might inherit from another. This relationship is called **IS-A** , as in, “a Hand
  is a kind of a Deck.”
- One class might depend on another in the sense that changes in one class would
  require changes in the other.

A **class diagram** is a graphical representation of these relationships. For example, Fig-
ure 18.2 shows the relationships betweenCard,DeckandHand.

The arrow with a hollow triangle head represents an IS-A relationship; in this case it indi-
cates that Hand inherits from Deck.

The standard arrow head represents a HAS-A relationship; in this case a Deck has refer-
ences to Card objects.

The star (\*) near the arrow head is a **multiplicity** ; it indicates how many Cards a Deck has.
A multiplicity can be a simple number, like 52 , a range, like5..7or a star, which indicates
that a Deck can have any number of Cards.

A more detailed diagram might show that a Deck actually contains alistof Cards, but
built-in types like list and dict are usually not included in class diagrams.
**Exercise 18.4.** ReadTurtleWorld.py,World.pyandGui.pyand draw a class diagram that
shows the relationships among the classes defined there.

### 18.9 Debugging

Inheritance can make debugging a challenge because when you invoke a method on an
object, you might not know which method will be invoked.

Suppose you are writing a function that works with Hand objects. You would like it to
work with all kinds of Hands, like PokerHands, BridgeHands, etc. If you invoke a method
likeshuffle, you might get the one defined inDeck, but if any of the subclasses override
this method, you’ll get that version instead.

Any time you are unsure about the flow of execution through your program, the sim-
plest solution is to add print statements at the beginning of the relevant methods. If

**18.10. Data encapsulation 175**

Deck.shuffleprints a message that says something likeRunning Deck.shuffle, then as
the program runs it traces the flow of execution.

As an alternative, you could use this function, which takes an object and a method name
(as a string) and returns the class that provides the definition of the method:

def find_defining_class(obj, meth_name):
for ty in type(obj).mro():
if meth_name in ty.**dict**:
return ty

Here’s an example:

> > > hand = Hand()
> > > print find_defining_class(hand,'shuffle')
> > > <class'Card.Deck'>

So theshufflemethod for this Hand is the one inDeck.

find_defining_classuses themromethod to get the list of class objects (types) that will
be searched for methods. “MRO” stands for “method resolution order.”

Here’s a program design suggestion: whenever you override a method, the interface of the
new method should be the same as the old. It should take the same parameters, return the
same type, and obey the same preconditions and postconditions. If you obey this rule, you
will find that any function designed to work with an instance of a superclass, like a Deck,
will also work with instances of subclasses like a Hand or PokerHand.

If you violate this rule, your code will collapse like (sorry) a house of cards.

### 18.10 Data encapsulation

Chapter 16 demonstrates a development plan we might call “object-oriented design.” We
identified objects we needed—Time,PointandRectangle—and defined classes to repre-
sent them. In each case there is an obvious correspondence between the object and some
entity in the real world (or at least a mathematical world).

But sometimes it is less obvious what objects you need and how they should interact. In
that case you need a different development plan. In the same way that we discovered
function interfaces by encapsulation and generalization, we can discover class interfaces
by **data encapsulation**.

Markov analysis, from Section 13.8, provides a good example. If you download my
code fromhttp://thinkpython.com/code/markov.py, you’ll see that it uses two global
variables—suffix_mapandprefix—that are read and written from several functions.

suffix_map = {}
prefix = ()

Because these variables are global we can only run one analysis at a time. If we read two
texts, their prefixes and suffixes would be added to the same data structures (which makes
for some interesting generated text).

To run multiple analyses, and keep them separate, we can encapsulate the state of each
analysis in an object. Here’s what that looks like:

**176 Chapter 18. Inheritance**

class Markov(object):

```
def __init__(self):
self.suffix_map = {}
self.prefix = ()
```

Next, we transform the functions into methods. For example, here’sprocess_word:

```
def process_word(self, word, order=2):
if len(self.prefix) < order:
self.prefix += (word,)
return
```

```
try:
self.suffix_map[self.prefix].append(word)
except KeyError:
# if there is no entry for this prefix, make one
self.suffix_map[self.prefix] = [word]
```

```
self.prefix = shift(self.prefix, word)
```

Transforming a program like this—changing the design without changing the function—is
another example of refactoring (see Section 4.7).

This example suggests a development plan for designing objects and methods:

1. Start by writing functions that read and write global variables (when necessary).
2. Once you get the program working, look for associations between global variables
   and the functions that use them.
3. Encapsulate related variables as attributes of an object.
4. Transform the associated functions into methods of the new class.

**Exercise 18.5.** Download my code from Section 13.8 (http: // thinkpython. com/ code/
markov. py), and follow the steps described above to encapsulate the global variables as attributes
of a new class calledMarkov. Solution:http: // thinkpython. com/ code/ Markov. py(note
the capital M).

### 18.11 Glossary

**encode:** To represent one set of values using another set of values by constructing a map-
ping between them.

**class attribute:** An attribute associated with a class object. Class attributes are defined
inside a class definition but outside any method.

**instance attribute:** An attribute associated with an instance of a class.

**veneer:** A method or function that provides a different interface to another function with-
out doing much computation.

**inheritance:** The ability to define a new class that is a modified version of a previously
defined class.

**18.12. Exercises 177**

**parent class:** The class from which a child class inherits.

**child class:** A new class created by inheriting from an existing class; also called a “sub-
class.”

**IS-A relationship:** The relationship between a child class and its parent class.

**HAS-A relationship:** The relationship between two classes where instances of one class
contain references to instances of the other.

**class diagram:** A diagram that shows the classes in a program and the relationships be-
tween them.

**multiplicity:** A notation in a class diagram that shows, for a HAS-A relationship, how
many references there are to instances of another class.

### 18.12 Exercises

**Exercise 18.6.** The following are the possible hands in poker, in increasing order of value (and
decreasing order of probability):

**pair:** two cards with the same rank

**two pair:** two pairs of cards with the same rank

**three of a kind:** three cards with the same rank

**straight:** five cards with ranks in sequence (aces can be high or low, soAce-2-3-4-5is a straight
and so is10-Jack-Queen-King-Ace, butQueen-King-Ace-2-3is not.)

**flush:** five cards with the same suit

**full house:** three cards with one rank, two cards with another

**four of a kind:** four cards with the same rank

**straight flush:** five cards in sequence (as defined above) and with the same suit

The goal of these exercises is to estimate the probability of drawing these various hands.

1. Download the following files fromhttp: // thinkpython. com/ code:
   Card.py: A complete version of theCard,DeckandHandclasses in this chapter.
   PokerHand.py: An incomplete implementation of a class that represents a poker hand, and
   some code that tests it.
2. If you runPokerHand.py, it deals seven 7-card poker hands and checks to see if any of them
   contains a flush. Read this code carefully before you go on.
3. Add methods toPokerHand.pynamedhas_pair,has_twopair, etc. that return True or
   False according to whether or not the hand meets the relevant criteria. Your code should
   work correctly for “hands” that contain any number of cards (although 5 and 7 are the most
   common sizes).
4. Write a method namedclassifythat figures out the highest-value classification for a hand
   and sets thelabelattribute accordingly. For example, a 7-card hand might contain a flush
   and a pair; it should be labeled “flush”.

**178 Chapter 18. Inheritance**

5. When you are convinced that your classification methods are working, the next step is to esti-
   mate the probabilities of the various hands. Write a function inPokerHand.pythat shuffles
   a deck of cards, divides it into hands, classifies the hands, and counts the number of times
   various classifications appear.
6. Print a table of the classifications and their probabilities. Run your program with larger and
   larger numbers of hands until the output values converge to a reasonable degree of accu-
   racy. Compare your results to the values athttp: // en. wikipedia. org/ wiki/ Hand\_
   rankings.

Solution:http: // thinkpython. com/ code/ PokerHandSoln. py.
**Exercise 18.7.** This exercise uses TurtleWorld from Chapter 4. You will write code that makes
Turtles play tag. If you are not familiar with the rules of tag, seehttp: // en. wikipedia. org/
wiki/ Tag\_ ( game).

1. Downloadhttp: // thinkpython. com/ code/ Wobbler. pyand run it. You should see a
   TurtleWorld with three Turtles. If you press theRunbutton, the Turtles wander at random.
2. Read the code and make sure you understand how it works. TheWobblerclass inherits from
   Turtle, which means that theTurtlemethodslt,rt,fdandbkwork on Wobblers.
   Thestepmethod gets invoked by TurtleWorld. It invokessteer, which turns the Turtle
   in the desired direction,wobble, which makes a random turn in proportion to the Turtle’s
   clumsiness, andmove, which moves forward a few pixels, depending on the Turtle’s speed.
3. Create a file namedTagger.py. Import everything fromWobbler, then define a class named
   Taggerthat inherits fromWobbler. Callmake_worldpassing theTaggerclass object as an
   argument.
4. Add asteermethod toTaggerto override the one inWobbler. As a starting place, write a
   version that always points the Turtle toward the origin. Hint: use the math functionatan2
   and the Turtle attributesx,yandheading.
5. Modifysteerso that the Turtles stay in bounds. For debugging, you might want to use the
   Stepbutton, which invokessteponce on each Turtle.
6. Modifysteerso that each Turtle points toward its nearest neighbor. Hint: Turtles have an
   attribute,world, that is a reference to the TurtleWorld they live in, and the TurtleWorld has
   an attribute,animals, that is a list of all Turtles in the world.
7. Modifysteerso the Turtles play tag. You can add methods toTaggerand you can override
   steerand**init**, but you may not modify or overridestep,wobbleormove. Also,
   steeris allowed to change the heading of the Turtle but not the position.
   Adjust the rules and yoursteermethod for good quality play; for example, it should be
   possible for the slow Turtle to tag the faster Turtles eventually.

Solution:http: // thinkpython. com/ code/ Tagger. py.

## Chapter 19

# Case study: Tkinter

## 19.1 GUI

Most of the programs we have seen so far are text-based, but many programs use **graphical
user interfaces** , also known as **GUIs**.

Python provides several choices for writing GUI-based programs, including wxPython,
Tkinter, and Qt. Each has pros and cons, which is why Python has not converged on a
standard.

The one I will present in this chapter is Tkinter because I think it is the easiest to get started
with. Most of the concepts in this chapter apply to the other GUI modules, too.

There are several books and web pages about Tkinter. One of the best online resources is
An Introduction to Tkinterby Fredrik Lundh.

I have written a module calledGui.pythat comes with Swampy. It provides a simplified
interface to the functions and classes in Tkinter. The examples in this chapter are based on
this module.

Here is a simple example that creates and displays a Gui:

To create a GUI, you have to importGuifrom Swampy:

from swampy.Gui import \*

Or, depending on how you installed Swampy, like this:

from Gui import \*

Then instantiate a Gui object:

g = Gui()
g.title('Gui')
g.mainloop()

When you run this code, a window should appear with an empty gray square and the
titleGui. mainloopruns the **event loop** , which waits for the user to do something and

**180 Chapter 19. Case study: Tkinter**

responds accordingly. It is an infinite loop; it runs until the user closes the window, or
presses Control-C, or does something that causes the program to quit.

This Gui doesn’t do much because it doesn’t have any **widgets**. Widgets are the elements
that make up a GUI; they include:

**Button:** A widget, containing text or an image, that performs an action when pressed.

**Canvas:** A region that can display lines, rectangles, circles and other shapes.

**Entry:** A region where users can type text.

**Scrollbar:** A widget that controls the visible part of another widget.

**Frame:** A container, often invisible, that contains other widgets.

The empty gray square you see when you create a Gui is a Frame. When you create a new
widget, it is added to this Frame.

### 19.2 Buttons and callbacks

The methodbucreates a Button widget:

button = g.bu(text='Press me.')

The return value frombuis a Button object. The button that appears in the Frame is a
graphical representation of this object; you can control the button by invoking methods on
it.

butakes up to 32 parameters that control the appearance and function of the button. These
parameters are called **options**. Instead of providing values for all 32 options, you can use
keyword arguments, liketext='Press me.', to specify only the options you need and use
the default values for the rest.

When you add a widget to the Frame, it gets “shrink-wrapped;” that is, the Frame shrinks
to the size of the Button. If you add more widgets, the Frame grows to accommodate them.

The methodlacreates a Label widget:

label = g.la(text='Press the button.')

By default, Tkinter stacks the widgets top-to-bottom and centers them. We’ll see how to
override that behavior soon.

If you press the button, you will see that it doesn’t do much. That’s because you haven’t
“wired it up;” that is, you haven’t told it what to do!

The option that controls the behavior of a button iscommand. The value ofcommandis a
function that gets executed when the button is pressed. For example, here is a function
that creates a new Label:

def make_label():
g.la(text='Thank you.')

Now we can create a button with this function as its command:

**19.3. Canvas widgets 181**

button2 = g.bu(text='No, press me!', command=make_label)

When you press this button, it should executemake_labeland a new label should appear.

The value of thecommandoption is a function object, which is known as a **callback** because
after you callbuto create the button, the flow of execution “calls back” when the user
presses the button.

This kind of flow is characteristic of **event-driven programming**. User actions, like but-
ton presses and key strokes, are called **events**. In event-driven programming, the flow of
execution is determined by user actions rather than by the programmer.

The challenge of event-driven programming is to construct a set of widgets and callbacks
that work correctly (or at least generate appropriate error messages) for any sequence of
user actions.
**Exercise 19.1.** Write a program that creates a GUI with a single button. When the button is
pressed it should create a second button. Whenthatbutton is pressed, it should create a label that
says, “Nice job!”.

What happens if you press the buttons more than once? Solution:http: // thinkpython. com/
code/ button\_ demo. py

### 19.3 Canvas widgets

One of the most versatile widgets is the Canvas, which creates a region for drawing lines,
circles and other shapes. If you did Exercise 15.4 you are already familiar with canvases.

The methodcacreates a new Canvas:

canvas = g.ca(width=500, height=500)

widthandheightare the dimensions of the canvas in pixels.

After you create a widget, you can still change the values of the options with theconfig
method. For example, thebgoption changes the background color:

canvas.config(bg='white')

The value ofbgis a string that names a color. The set of legal color names is different for
different implementations of Python, but all implementations provide at least:

white black
red green blue
cyan yellow magenta

Shapes on a Canvas are called **items**. For example, the Canvas methodcircledraws (you
guessed it) a circle:

item = canvas.circle([0,0], 100, fill='red')

The first argument is a coordinate pair that specifies the center of the circle; the second is
the radius.

Gui.pyprovides a standard Cartesian coordinate system with the origin at the center of
the Canvas and the positiveyaxis pointing up. This is different from some other graphics
systems where the origin is in the upper left corner, with theyaxis pointing down.

Thefilloption specifies that the circle should be filled in with red.

The return value fromcircleis an Item object that provides methods for modifying the
item on the canvas. For example, you can useconfigto change any of the circle’s options:

**182 Chapter 19. Case study: Tkinter**

item.config(fill='yellow', outline='orange', width=10)

widthis the thickness of the outline in pixels;outlineis the color.
**Exercise 19.2.** Write a program that creates a Canvas and a Button. When the user presses the
Button, it should draw a circle on the canvas.

### 19.4 Coordinate sequences

Therectanglemethod takes a sequence of coordinates that specify opposite corners of the
rectangle. This example draws a blue rectangle with the lower left corner at the origin and
the upper right corner at(200, 100):

canvas.rectangle([[0, 0], [200, 100]],
fill='blue', outline='orange', width=10)

This way of specifying corners is called a **bounding box** because the two points bound the
rectangle.

ovaltakes a bounding box and draws an oval within the specified rectangle:

canvas.oval([[0, 0], [200, 100]], outline='orange', width=10)

linetakes a sequence of coordinates and draws a line that connects the points. This exam-
ple draws two legs of a triangle:

canvas.line([[0, 100], [100, 200], [200, 100]], width=10)

polygontakes the same arguments, but it draws the last leg of the polygon (if necessary)
and fills it in:

canvas.polygon([[0, 100], [100, 200], [200, 100]],
fill='red', outline='orange', width=10)

### 19.5 More widgets

Tkinter provides two widgets that let users type text: an Entry, which is a single line, and
a Text widget, which has multiple lines.

encreates a new Entry:

entry = g.en(text='Default text.')

Thetextoption allows you to put text into the entry when it is created. Thegetmethod
returns the contents of the Entry (which may have been changed by the user):

> > > entry.get()
> > > 'Default text.'

tecreates a Text widget:

text = g.te(width=100, height=5)

widthandheightare the dimensions of the widget in characters and lines.

insertputs text into the Text widget:

text.insert(END,'A line of text.')

**19.6. Packing widgets 183**

ENDis a special index that indicates the last character in the Text widget.

You can also specify a character using a dotted index, like1.1, which has the line num-
ber before the dot and the column number after. The following example adds the letters
'nother'after the first character of the first line.

> > > text.insert(1.1,'nother')

Thegetmethod reads the text in the widget; it takes a start and end index as arguments.
The following example returns all the text in the widget, including the newline character:

> > > text.get(0.0, END)
> > > 'Another line of text.\n'

Thedeletemethod removes text from the widget; the following example deletes all but
the first two characters:

> > > text.delete(1.2, END)
> > > text.get(0.0, END)
> > > 'An\n'
> > > **Exercise 19.3.** Modify your solution to Exercise 19.2 by adding an Entry widget and a second
> > > button. When the user presses the second button, it should read a color name from the Entry and
> > > use it to change the fill color of the circle. Useconfigto modify the existing circle; don’t create a
> > > new one.

Your program should handle the case where the user tries to change the color of a circle that hasn’t
been created, and the case where the color name is invalid.

You can see my solution athttp: // thinkpython. com/ code/ circle\_ demo. py.

### 19.6 Packing widgets

So far we have been stacking widgets in a single column, but in most GUIs the layout is
more complicated. For example, Figure 19.1 shows a simplified version of TurtleWorld (see
Chapter 4).

This section presents the code that creates this GUI, broken into a series of
steps. You can download the complete example fromhttp://thinkpython.com/code/
SimpleTurtleWorld.py.

At the top level, this GUI contains two widgets—a Canvas and a Frame—arranged in a
row. So the first step is to create the row.

class SimpleTurtleWorld(TurtleWorld):
"""This class is identical to TurtleWorld, but the code that
lays out the GUI is simplified for explanatory purposes."""

```
def setup(self):
self.row()
...
```

setupis the function that creates and arranges the widgets. Arranging widgets in a GUI is
called **packing**.

rowcreates a row Frame and makes it the “current Frame.” Until this Frame is closed or
another Frame is created, all subsequent widgets are packed in a row.

Here is the code that creates the Canvas and the column Frame that hold the other widgets:

**184 Chapter 19. Case study: Tkinter**

```
Figure 19.1: TurtleWorld after running the snowflake code.
```

```
self.canvas = self.ca(width=400, height=400, bg='white')
self.col()
```

The first widget in the column is a grid Frame, which contains four buttons arranged two-
by-two:

```
self.gr(cols=2)
self.bu(text='Print canvas', command=self.canvas.dump)
self.bu(text='Quit', command=self.quit)
self.bu(text='Make Turtle', command=self.make_turtle)
self.bu(text='Clear', command=self.clear)
self.endgr()
```

grcreates the grid; the argument is the number of columns. Widgets in the grid are laid
out left-to-right, top-to-bottom.

The first button usesself.canvas.dumpas a callback; the second usesself.quit. These
are **bound methods** , which means they are associated with a particular object. When they
are invoked, they are invoked on the object.

The next widget in the column is a row Frame that contains a Button and an Entry:

```
self.row([0,1], pady=30)
self.bu(text='Run file', command=self.run_file)
self.en_file = self.en(text='snowflake.py', width=5)
self.endrow()
```

The first argument torowis a list of weights that determines how extra space is allocated
between widgets. The list[0,1]means that all extra space is allocated to the second wid-
get, which is the Entry. If you run this code and resize the window, you will see that the
Entry grows and the Button doesn’t.

The optionpady“pads” this row in theydirection, adding 30 pixels of space above and
below.

**19.7. Menus and Callables 185**

endrowends this row of widgets, so subsequent widgets are packed in the column Frame.
Gui.pykeeps a stack of Frames:

- When you userow,colorgrto create a Frame, it goes on top of the stack and becomes
  the current Frame.
- When you useendrow,endcolorendgrto close a Frame, it gets popped off the stack
  and the previous Frame on the stack becomes the current Frame.

The methodrun_filereads the contents of the Entry, uses it as a filename, reads the con-
tents and passes it torun_code.self.interis an Interpreter object that knows how to take
a string and execute it as Python code.

```
def run_file(self):
filename = self.en_file.get()
fp = open(filename)
source = fp.read()
self.inter.run_code(source, filename)
```

The last two widgets are a Text widget and a Button:

```
self.te_code = self.te(width=25, height=10)
self.te_code.insert(END, 'world.clear()\n')
self.te_code.insert(END, 'bob = Turtle(world)\n')
```

```
self.bu(text='Run code', command=self.run_text)
```

run_textis similar torun_fileexcept that it takes the code from the Text widget instead
of from a file:

```
def run_text(self):
source = self.te_code.get(1.0, END)
self.inter.run_code(source, '<user-provided code>')
```

Unfortunately, the details of widget layout are different in other languages, and in different
Python modules. Tkinter alone provides three different mechanisms for arranging widgets.
These mechanisms are called **geometry managers**. The one I demonstrated in this section
is the “grid” geometry manager; the others are called “pack” and “place”.

Fortunately, most of the concepts in this section apply to other GUI modules and other
languages.

### 19.7 Menus and Callables

A Menubutton is a widget that looks like a button, but when pressed it pops up a menu.
After the user selects an item, the menu disappears.

Here is code that creates a color selection Menubutton (you can download it fromhttp:
//thinkpython.com/code/menubutton_demo.py):

g = Gui()
g.la('Select a color:')
colors = ['red','green', 'blue']
mb = g.mb(text=colors[0])

**186 Chapter 19. Case study: Tkinter**

mbcreates the Menubutton. Initially, the text on the button is the name of the default color.
The following loop creates one menu item for each color:

for color in colors:
g.mi(mb, text=color, command=Callable(set_color, color))

The first argument ofmiis the Menubutton these items are associated with.

Thecommandoption is a Callable object, which is something new. So far we have seen
functions and bound methods used as callbacks, which works fine if you don’t have to
pass any arguments to the function. Otherwise you have to construct a Callable object that
contains a function, likeset_color, and its arguments, likecolor.

The Callable object stores a reference to the function and the arguments as attributes. Later,
when the user clicks on a menu item, the callback calls the function and passes the stored
arguments.

Here is whatset_colormight look like:

def set_color(color):
mb.config(text=color)
print color

When the user selects a menu item andset_coloris called, it configures the Menubutton
to display the newly-selected color. It also print the color; if you try this example, you can
confirm thatset_coloris called when you select an item (andnotcalled when you create
the Callable object).

### 19.8 Binding

A **binding** is an association between a widget, an event and a callback: when an event (like
a button press) happens on a widget, the callback is invoked.

Many widgets have default bindings. For example, when you press a button, the default
binding changes the relief of the button to make it look depressed. When you release the
button, the binding restores the appearance of the button and invokes the callback specified
with thecommandoption.

You can use thebindmethod to override these default bindings or to add new ones. For
example, this code creates a binding for a canvas (you can download the code in this section
fromhttp://thinkpython.com/code/draggable_demo.py):

ca.bind('<ButtonPress-1>', make_circle)

The first argument is an event string; this event is triggered when the user presses
the left mouse button. Other mouse events includeButtonMotion,ButtonReleaseand
Double-Button.

The second argument is an event handler. An event handler is a function or bound method,
like a callback, but an important difference is that an event handler takes an Event object
as a parameter. Here is an example:

def make_circle(event):
pos = ca.canvas_coords([event.x, event.y])
item = ca.circle(pos, 5, fill='red')

**19.8. Binding 187**

The Event object contains information about the type of event and details like the coordi-
nates of the mouse pointer. In this example the information we need is the location of the
mouse click. These values are in “pixel coordinates,” which are defined by the underlying
graphical system. The methodcanvas_coordstranslates them to “Canvas coordinates,”
which are compatible with Canvas methods likecircle.

For Entry widgets, it is common to bind the<Return>event, which is triggered when the
user presses theReturnorEnterkey. For example, the following code creates a Button and
an Entry.

bu = g.bu('Make text item:', make_text)
en = g.en()
en.bind('<Return>', make_text)

make_textis called when the Button is pressed or when the user hitsReturnwhile typing
in the Entry. To make this work, we need a function that can be called as a command (with
no arguments) or as an event handler (with an Event as an argument):

def make_text(event=None):
text = en.get()
item = ca.text([0,0], text)

make_textgets the contents of the Entry and displays it as a Text item in the Canvas.

It is also possible to create bindings for Canvas items. The following is a class definition
forDraggable, which is a child class ofItemthat provides bindings that implement drag-
and-drop capability.

class Draggable(Item):

```
def __init__(self, item):
self.canvas = item.canvas
self.tag = item.tag
self.bind('<Button-3>', self.select)
self.bind('<B3-Motion>', self.drag)
self.bind('<Release-3>', self.drop)
```

The init method takes an Item as a parameter. It copies the attributes of the Item and then
creates bindings for three events: a button press, button motion, and button release.

The event handlerselectstores the coordinates of the current event and the original color
of the item, then changes the color to yellow:

```
def select(self, event):
self.dragx = event.x
self.dragy = event.y
```

```
self.fill = self.cget('fill')
self.config(fill='yellow')
```

cgetstands for “get configuration;” it takes the name of an option as a string and returns
the current value of that option.

dragcomputes how far the object has moved relative to the starting place, updates the
stored coordinates, and then moves the item.

```
def drag(self, event):
dx = event.x - self.dragx
```

**188 Chapter 19. Case study: Tkinter**

```
dy = event.y - self.dragy
```

```
self.dragx = event.x
self.dragy = event.y
```

```
self.move(dx, dy)
```

This computation is done in pixel coordinates; there is no need to convert to Canvas coor-
dinates.

Finally,droprestores the original color of the item:

```
def drop(self, event):
self.config(fill=self.fill)
```

You can use theDraggableclass to add drag-and-drop capability to an existing item. For
example, here is a modified version ofmake_circlethat usescircleto create an Item and
Draggableto make it draggable:

def make_circle(event):
pos = ca.canvas_coords([event.x, event.y])
item = ca.circle(pos, 5, fill='red')
item = Draggable(item)

This example demonstrates one of the benefits of inheritance: you can modify the capa-
bilities of a parent class without modifying its definition. This is particularly useful if you
want to change behavior defined in a module you did not write.

### 19.9 Debugging

One of the challenges of GUI programming is keeping track of which things happen while
the GUI is being built and which things happen later in response to user events.

For example, when you are setting up a callback, it is a common error to call the function
rather than passing a reference to it:

def the_callback():
print 'Called.'

g.bu(text='This is wrong!', command=the_callback())

If you run this code, you will see that it callsthe_callbackimmediately, andthencreates
the button. When you press the button, it does nothing because the return value from
the_callbackisNone. Usually you do not want to invoke a callback while you are setting
up the GUI; it should only be invoked later in response to a user event.

Another challenge of GUI programming is that you don’t have control of the flow of exe-
cution. Which parts of the program execute and their order are determined by user actions.
That means that you have to design your program to work correctly for any possible se-
quence of events.

For example, the GUI in Exercise 19.3 has two widgets: one creates a Circle item and the
other changes the color of the Circle. If the user creates the circle and then changes its color,
there’s no problem. But what if the user changes the color of a circle that doesn’t exist yet?
Or creates more than one circle?

**19.10. Glossary 189**

As the number of widgets grows, it is increasingly difficult to imagine all possible se-
quences of events. One way to manage this complexity is to encapsulate the state of the
system in an object and then consider:

- What are the possible states? In the Circle example, we might consider two states:
  before and after the user creates the first circle.
- In each state, what events can occur? In the example, the user can press either of the
  buttons, or quit.
- For each state-event pair, what is the desired outcome? Since there are two states and
  two buttons, there are four state-event pairs to consider.
- What can cause a transition from one state to another? In this case, there is a transition
  when the user creates the first circle.

You might also find it useful to define, and check, invariants that should hold regardless of
the sequence of events.

This approach to GUI programming can help you write correct code without taking the
time to test every possible sequence of user events!

### 19.10 Glossary

**GUI:** A graphical user interface.

**widget:** One of the elements that makes up a GUI, including buttons, menus, text entry
fields, etc.

**option:** A value that controls the appearance or function of a widget.

**keyword argument:** An argument that indicates the parameter name as part of the func-
tion call.

**callback:** A function associated with a widget that is called when the user performs an
action.

**bound method:** A method associated with a particular instance.

**event-driven programming:** A style of programming in which the flow of execution is
determined by user actions.

**event:** A user action, like a mouse click or key press, that causes a GUI to respond.

**event loop:** An infinite loop that waits for user actions and responds.

**item:** A graphical element on a Canvas widget.

**bounding box:** A rectangle that encloses a set of items, usually specified by two opposing
corners.

**pack:** To arrange and display the elements of a GUI.

**geometry manager:** A system for packing widgets.

**binding:** An association between a widget, an event, and an event handler. The event
handler is called when the event occurs in the widget.

**190 Chapter 19. Case study: Tkinter**

### 19.11 Exercises

**Exercise 19.4.** For this exercise, you will write an image viewer. Here is a simple example:

g = Gui()
canvas = g.ca(width=300)
photo = PhotoImage(file='danger.gif')
canvas.image([0,0], image=photo)
g.mainloop()

PhotoImagereads a file and returns aPhotoImageobject that Tkinter can display.Canvas.image
puts the image on the canvas, centered on the given coordinates. You can also put images on labels,
buttons, and some other widgets:

g.la(image=photo)
g.bu(image=photo)

PhotoImage can only handle a few image formats, like GIF and PPM, but we can use the Python
Imaging Library (PIL) to read other files.

The name of the PIL module isImage, but Tkinter defines an object with the same name. To avoid
the conflict, you can useimport...aslike this:

import Image as PIL
import ImageTk

The first line importsImageand gives it the local namePIL. The second line importsImageTk,
which can translate a PIL image into a Tkinter PhotoImage. Here’s an example:

image = PIL.open('allen.png')
photo2 = ImageTk.PhotoImage(image)
g.la(image=photo2)

1. Downloadimage_demo.py,danger.gifandallen.pngfromhttp: // thinkpython.
   com/ code. Runimage_demo.py. You might have to installPILandImageTk. They
   are probably in your software repository, but if not you can get them fromhttp: //
   pythonware. com/ products/ pil.
2. Inimage_demo.pychange the name of the second PhotoImage fromphoto2tophotoand
   run the program again. You should see the second PhotoImage but not the first.
   The problem is that when you reassignphotoit overwrites the reference to the first PhotoIm-
   age, which then disappears. The same thing happens if you assign a PhotoImage to a local
   variable; it disappears when the function ends.
   To avoid this problem, you have to store a reference to each PhotoImage you want to keep. You
   can use a global variable, or store PhotoImages in a data structure or as an attribute of an
   object.
   This behavior can be frustrating, which is why I am warning you (and why the example image
   says “Danger!”).
3. Starting with this example, write a program that takes the name of a directory and loops
   through all the files, displaying any files that PIL recognizes as images. You can use atry
   statement to catch the files PIL doesn’t recognize.
   When the user clicks on the image, the program should display the next one.

**19.11. Exercises 191**

4. PIL provides a variety of methods for manipulating images. You can read about them at
   [http:](http:) // pythonware. com/ library/ pil/ handbook. As a challenge, choose a few of
   these methods and provide a GUI for applying them to images.

Solution:http: // thinkpython. com/ code/ ImageBrowser. py.
**Exercise 19.5.** A vector graphics editor is a program that allows users to draw and edit shapes on
the screen and generate output files in vector graphics formats like Postscript and SVG.

Write a simple vector graphics editor using Tkinter. At a minimum, it should allow users to draw
lines, circles and rectangles, and it should useCanvas.dumpto generate a Postscript description of
the contents of the Canvas.

As a challenge, you could allow users to select and resize items on the Canvas.
**Exercise 19.6.** Use Tkinter to write a basic web browser. It should have a Text widget where the
user can enter a URL and a Canvas to display the contents of the page.

You can use theurllibmodule to download files (see Exercise 14.6) and theHTMLParsermodule
to parse the HTML tags (seehttp: // docs. python. org/ 2/ library/ htmlparser. html).

At a minimum your browser should handle plain text and hyperlinks. As a challenge you could
handle background colors, text formatting tags and images.

**192 Chapter 19. Case study: Tkinter**

## Appendix A

# Debugging

Different kinds of errors can occur in a program, and it is useful to distinguish among them
in order to track them down more quickly:

- Syntax errors are produced by Python when it is translating the source code into
  byte code. They usually indicate that there is something wrong with the syntax of
  the program. Example: Omitting the colon at the end of adefstatement yields the
  somewhat redundant messageSyntaxError: invalid syntax.
- Runtime errors are produced by the interpreter if something goes wrong while the
  program is running. Most runtime error messages include information about where
  the error occurred and what functions were executing. Example: An infinite recur-
  sion eventually causes the runtime error “maximum recursion depth exceeded.”
- Semantic errors are problems with a program that runs without producing error mes-
  sages but doesn’t do the right thing. Example: An expression may not be evaluated
  in the order you expect, yielding an incorrect result.

The first step in debugging is to figure out which kind of error you are dealing with. Al-
though the following sections are organized by error type, some techniques are applicable
in more than one situation.

## A.1 Syntax errors

Syntax errors are usually easy to fix once you figure out what they are. Unfortunately,
the error messages are often not helpful. The most common messages areSyntaxError:
invalid syntaxandSyntaxError: invalid token, neither of which is very informa-
tive.

On the other hand, the message does tell you where in the program the problem occurred.
Actually, it tells you where Python noticed a problem, which is not necessarily where the
error is. Sometimes the error is prior to the location of the error message, often on the
preceding line.

**194 Appendix A. Debugging**

If you are building the program incrementally, you should have a good idea about where
the error is. It will be in the last line you added.

If you are copying code from a book, start by comparing your code to the book’s code
very carefully. Check every character. At the same time, remember that the book might be
wrong, so if you see something that looks like a syntax error, it might be.

Here are some ways to avoid the most common syntax errors:

1. Make sure you are not using a Python keyword for a variable name.
2. Check that you have a colon at the end of the header of every compound statement,
   includingfor,while,if, anddefstatements.
3. Make sure that any strings in the code have matching quotation marks.
4. If you have multiline strings with triple quotes (single or double), make sure you
   have terminated the string properly. An unterminated string may cause aninvalid
   tokenerror at the end of your program, or it may treat the following part of the
   program as a string until it comes to the next string. In the second case, it might not
   produce an error message at all!
5. An unclosed opening operator—(,{, or[—makes Python continue with the next line
   as part of the current statement. Generally, an error occurs almost immediately in the
   next line.
6. Check for the classic=instead of==inside a conditional.
7. Check the indentation to make sure it lines up the way it is supposed to. Python
   can handle space and tabs, but if you mix them it can cause problems. The best way
   to avoid this problem is to use a text editor that knows about Python and generates
   consistent indentation.

If nothing works, move on to the next section...

**A.1.1 I keep making changes and it makes no difference.**

If the interpreter says there is an error and you don’t see it, that might be because you and
the interpreter are not looking at the same code. Check your programming environment to
make sure that the program you are editing is the one Python is trying to run.

If you are not sure, try putting an obvious and deliberate syntax error at the beginning of
the program. Now run it again. If the interpreter doesn’t find the new error, you are not
running the new code.

There are a few likely culprits:

- You edited the file and forgot to save the changes before running it again. Some
  programming environments do this for you, but some don’t.
- You changed the name of the file, but you are still running the old name.
- Something in your development environment is configured incorrectly.

**A.2. Runtime errors 195**

- If you are writing a module and usingimport, make sure you don’t give your module
  the same name as one of the standard Python modules.
- If you are usingimportto read a module, remember that you have to restart the
  interpreter or usereloadto read a modified file. If you import the module again, it
  doesn’t do anything.

If you get stuck and you can’t figure out what is going on, one approach is to start again
with a new program like “Hello, World!,” and make sure you can get a known program to
run. Then gradually add the pieces of the original program to the new one.

### A.2 Runtime errors

Once your program is syntactically correct, Python can compile it and at least start running
it. What could possibly go wrong?

**A.2.1 My program does absolutely nothing.**

This problem is most common when your file consists of functions and classes but does
not actually invoke anything to start execution. This may be intentional if you only plan to
import this module to supply classes and functions.

If it is not intentional, make sure that you are invoking a function to start execution, or
execute one from the interactive prompt. Also see the “Flow of Execution” section below.

**A.2.2 My program hangs.**

If a program stops and seems to be doing nothing, it is “hanging.” Often that means that it
is caught in an infinite loop or infinite recursion.

- If there is a particular loop that you suspect is the problem, add aprintstatement
  immediately before the loop that says “entering the loop” and another immediately
  after that says “exiting the loop.”
  Run the program. If you get the first message and not the second, you’ve got an
  infinite loop. Go to the “Infinite Loop” section below.
- Most of the time, an infinite recursion will cause the program to run for a while and
  then produce a “RuntimeError: Maximum recursion depth exceeded” error. If that
  happens, go to the “Infinite Recursion” section below.
  If you are not getting this error but you suspect there is a problem with a recursive
  method or function, you can still use the techniques in the “Infinite Recursion” sec-
  tion.
- If neither of those steps works, start testing other loops and other recursive functions
  and methods.
- If that doesn’t work, then it is possible that you don’t understand the flow of execu-
  tion in your program. Go to the “Flow of Execution” section below.

**196 Appendix A. Debugging**

**Infinite Loop**

If you think you have an infinite loop and you think you know what loop is causing the
problem, add aprintstatement at the end of the loop that prints the values of the variables
in the condition and the value of the condition.

For example:

while x > 0 and y < 0 :

# do something to x

# do something to y

```
print "x: ", x
print "y: ", y
print "condition: ", (x > 0 and y < 0)
```

Now when you run the program, you will see three lines of output for each time through
the loop. The last time through the loop, the condition should befalse. If the loop keeps
going, you will be able to see the values ofxandy, and you might figure out why they are
not being updated correctly.

**Infinite Recursion**

Most of the time, an infinite recursion will cause the program to run for a while and then
produce aMaximum recursion depth exceedederror.

If you suspect that a function or method is causing an infinite recursion, start by checking
to make sure that there is a base case. In other words, there should be some condition that
will cause the function or method to return without making a recursive invocation. If not,
then you need to rethink the algorithm and identify a base case.

If there is a base case but the program doesn’t seem to be reaching it, add aprintstatement
at the beginning of the function or method that prints the parameters. Now when you
run the program, you will see a few lines of output every time the function or method is
invoked, and you will see the parameters. If the parameters are not moving toward the
base case, you will get some ideas about why not.

**Flow of Execution**

If you are not sure how the flow of execution is moving through your program, addprint
statements to the beginning of each function with a message like “entering functionfoo,”
wherefoois the name of the function.

Now when you run the program, it will print a trace of each function as it is invoked.

**A.2.3 When I run the program I get an exception.**

If something goes wrong during runtime, Python prints a message that includes the name
of the exception, the line of the program where the problem occurred, and a traceback.

The traceback identifies the function that is currently running, and then the function that
invoked it, and then the function that invokedthat, and so on. In other words, it traces the

**A.2. Runtime errors 197**

sequence of function invocations that got you to where you are. It also includes the line
number in your file where each of these calls occurs.

The first step is to examine the place in the program where the error occurred and see if
you can figure out what happened. These are some of the most common runtime errors:

**NameError:** You are trying to use a variable that doesn’t exist in the current environment.
Remember that local variables are local. You cannot refer to them from outside the
function where they are defined.

**TypeError:** There are several possible causes:

- You are trying to use a value improperly. Example: indexing a string, list, or
  tuple with something other than an integer.
- There is a mismatch between the items in a format string and the items passed
  for conversion. This can happen if either the number of items does not match or
  an invalid conversion is called for.
- You are passing the wrong number of arguments to a function or method. For
  methods, look at the method definition and check that the first parameter is
  self. Then look at the method invocation; make sure you are invoking the
  method on an object with the right type and providing the other arguments
  correctly.

**KeyError:** You are trying to access an element of a dictionary using a key that the dictio-
nary does not contain.

**AttributeError:** You are trying to access an attribute or method that does not exist. Check
the spelling! You can usedirto list the attributes that do exist.
If an AttributeError indicates that an object hasNoneType, that means that it isNone.
One common cause is forgetting to return a value from a function; if you get to the
end of a function without hitting areturnstatement, it returnsNone. Another com-
mon cause is using the result from a list method, likesort, that returnsNone.

**IndexError:** The index you are using to access a list, string, or tuple is greater than its
length minus one. Immediately before the site of the error, add aprintstatement to
display the value of the index and the length of the array. Is the array the right size?
Is the index the right value?

The Python debugger (pdb) is useful for tracking down Exceptions because it allows you
to examine the state of the program immediately before the error. You can read aboutpdb
athttp://docs.python.org/2/library/pdb.html.

**A.2.4 I added so many** print **statements I get inundated with output.**

One of the problems with usingprintstatements for debugging is that you can end up
buried in output. There are two ways to proceed: simplify the output or simplify the
program.

To simplify the output, you can remove or comment outprintstatements that aren’t help-
ing, or combine them, or format the output so it is easier to understand.

**198 Appendix A. Debugging**

To simplify the program, there are several things you can do. First, scale down the problem
the program is working on. For example, if you are searching a list, search asmalllist. If
the program takes input from the user, give it the simplest input that causes the problem.

Second, clean up the program. Remove dead code and reorganize the program to make
it as easy to read as possible. For example, if you suspect that the problem is in a deeply
nested part of the program, try rewriting that part with simpler structure. If you suspect a
large function, try splitting it into smaller functions and testing them separately.

Often the process of finding the minimal test case leads you to the bug. If you find that
a program works in one situation but not in another, that gives you a clue about what is
going on.

Similarly, rewriting a piece of code can help you find subtle bugs. If you make a change
that you think shouldn’t affect the program, and it does, that can tip you off.

### A.3 Semantic errors

In some ways, semantic errors are the hardest to debug, because the interpreter provides
no information about what is wrong. Only you know what the program is supposed to do.

The first step is to make a connection between the program text and the behavior you are
seeing. You need a hypothesis about what the program is actually doing. One of the things
that makes that hard is that computers run so fast.

You will often wish that you could slow the program down to human speed, and with
some debuggers you can. But the time it takes to insert a few well-placedprintstatements
is often short compared to setting up the debugger, inserting and removing breakpoints,
and “stepping” the program to where the error is occurring.

**A.3.1 My program doesn’t work.**

You should ask yourself these questions:

- Is there something the program was supposed to do but which doesn’t seem to be
  happening? Find the section of the code that performs that function and make sure
  it is executing when you think it should.
- Is something happening that shouldn’t? Find code in your program that performs
  that function and see if it is executing when it shouldn’t.
- Is a section of code producing an effect that is not what you expected? Make sure that
  you understand the code in question, especially if it involves invocations to functions
  or methods in other Python modules. Read the documentation for the functions you
  invoke. Try them out by writing simple test cases and checking the results.

In order to program, you need to have a mental model of how programs work. If you write
a program that doesn’t do what you expect, very often the problem is not in the program;
it’s in your mental model.

**A.3. Semantic errors 199**

The best way to correct your mental model is to break the program into its components
(usually the functions and methods) and test each component independently. Once you
find the discrepancy between your model and reality, you can solve the problem.

Of course, you should be building and testing components as you develop the program.
If you encounter a problem, there should be only a small amount of new code that is not
known to be correct.

**A.3.2 I’ve got a big hairy expression and it doesn’t do what I expect.**

Writing complex expressions is fine as long as they are readable, but they can be hard to
debug. It is often a good idea to break a complex expression into a series of assignments to
temporary variables.

For example:

self.hands[i].addCard(self.hands[self.findNeighbor(i)].popCard())

This can be rewritten as:

neighbor = self.findNeighbor(i)
pickedCard = self.hands[neighbor].popCard()
self.hands[i].addCard(pickedCard)

The explicit version is easier to read because the variable names provide additional docu-
mentation, and it is easier to debug because you can check the types of the intermediate
variables and display their values.

Another problem that can occur with big expressions is that the order of evaluation may
not be what you expect. For example, if you are translating the expression 2 x _π_ into Python,
you might write:

y = x / 2 \* math.pi

That is not correct because multiplication and division have the same precedence and are
evaluated from left to right. So this expression computesx _π_ /2.

A good way to debug expressions is to add parentheses to make the order of evaluation
explicit:

```
y = x / (2 * math.pi)
```

Whenever you are not sure of the order of evaluation, use parentheses. Not only will the
program be correct (in the sense of doing what you intended), it will also be more readable
for other people who haven’t memorized the rules of precedence.

**A.3.3 I’ve got a function or method that doesn’t return what I expect.**

If you have areturnstatement with a complex expression, you don’t have a chance to print
thereturnvalue before returning. Again, you can use a temporary variable. For example,
instead of:

return self.hands[i].removeMatches()

you could write:

count = self.hands[i].removeMatches()
return count

Now you have the opportunity to display the value ofcountbefore returning.

**200 Appendix A. Debugging**

**A.3.4 I’m really, really stuck and I need help.**

First, try getting away from the computer for a few minutes. Computers emit waves that
affect the brain, causing these symptoms:

- Frustration and rage.
- Superstitious beliefs (“the computer hates me”) and magical thinking (“the program
  only works when I wear my hat backward”).
- Random walk programming (the attempt to program by writing every possible pro-
  gram and choosing the one that does the right thing).

If you find yourself suffering from any of these symptoms, get up and go for a walk. When
you are calm, think about the program. What is it doing? What are some possible causes
of that behavior? When was the last time you had a working program, and what did you
do next?

Sometimes it just takes time to find a bug. I often find bugs when I am away from the
computer and let my mind wander. Some of the best places to find bugs are trains, showers,
and in bed, just before you fall asleep.

**A.3.5 No, I really need help.**

It happens. Even the best programmers occasionally get stuck. Sometimes you work on a
program so long that you can’t see the error. A fresh pair of eyes is just the thing.

Before you bring someone else in, make sure you are prepared. Your program should be as
simple as possible, and you should be working on the smallest input that causes the error.
You should haveprintstatements in the appropriate places (and the output they produce
should be comprehensible). You should understand the problem well enough to describe
it concisely.

When you bring someone in to help, be sure to give them the information they need:

- If there is an error message, what is it and what part of the program does it indicate?
- What was the last thing you did before this error occurred? What were the last lines
  of code that you wrote, or what is the new test case that fails?
- What have you tried so far, and what have you learned?

When you find the bug, take a second to think about what you could have done to find it
faster. Next time you see something similar, you will be able to find the bug more quickly.

Remember, the goal is not just to make the program work. The goal is to learn how to make
the program work.

## Appendix B

# Analysis of Algorithms

```
This appendix is an edited excerpt fromThink Complexity, by Allen B. Downey,
also published by O’Reilly Media (2011). When you are done with this book,
you might want to move on to that one.
```

**Analysis of algorithms** is a branch of computer science that studies the performance of
algorithms, especially their run time and space requirements. See http://en.wikipedia.org/wiki/Analysis_of_algorithms .

The practical goal of algorithm analysis is to predict the performance of different algorithms in order to guide design decisions.

During the 2008 United States Presidential Campaign, candidate Barack Obama was asked
to perform an impromptu analysis when he visited Google. Chief executive Eric Schmidt
jokingly asked him for “the most efficient way to sort a million 32-bit integers.” Obama
had apparently been tipped off, because he quickly replied, “I think the bubble sort would
be the wrong way to go.” Seehttp://www.youtube.com/watch?v=k4RRi_ntQc8.

This is true: bubble sort is conceptually simple but slow for large datasets. The an-
swer Schmidt was probably looking for is “radix sort” (http://en.wikipedia.org/wiki/Radix_sort) .

The goal of algorithm analysis is to make meaningful comparisons between algorithms, but there are some problems:

- The relative performance of the algorithms might depend on characteristics of the
  hardware, so one algorithm might be faster on Machine A, another on Machine B.
  The general solution to this problem is to specify a **machine model** and analyze the
  number of steps, or operations, an algorithm requires under a given model.
- Relative performance might depend on the details of the dataset. For example, some
  sorting algorithms run faster if the data are already partially sorted; other algorithms

(^1) But if you get a question like this in an interview, I think a better answer is, “The fastest way to sort a million
integers is to use whatever sort function is provided by the language I’m using. Its performance is good enough
for the vast majority of applications, but if it turned out that my application was too slow, I would use a profiler
to see where the time was being spent. If it looked like a faster sort algorithm would have a significant effect on
performance, then I would look around for a good implementation of radix sort.”

**202 Appendix B. Analysis of Algorithms**

```
run slower in this case. A common way to avoid this problem is to analyze the worst
case scenario. It is sometimes useful to analyze average case performance, but that’s
usually harder, and it might not be obvious what set of cases to average over.
```

- Relative performance also depends on the size of the problem. A sorting algorithm
  that is fast for small lists might be slow for long lists. The usual solution to this
  problem is to express run time (or number of operations) as a function of problem
  size, and to compare the functions **asymptotically** as the problem size increases.

The good thing about this kind of comparison that it lends itself to simple classification of
algorithms. For example, if I know that the run time of Algorithm A tends to be propor-
tional to the size of the input,n, and Algorithm B tends to be proportional ton^2 , then I
expect A to be faster than B for large values ofn.

This kind of analysis comes with some caveats, but we’ll get to that later.

### B.1 Order of growth

Suppose you have analyzed two algorithms and expressed their run times in terms of the
size of the input: Algorithm A takes 100n+1 steps to solve a problem with sizen; Algo-
rithm B takesn^2 +n+1 steps.

The following table shows the run time of these algorithms for different problem sizes:

```
Input Run time of Run time of
size Algorithm A Algorithm B
10 1 001 111
100 10 001 10 101
1 000 100 001 1 001 001
10 000 1 000 001 > 1010
```

Atn=10, Algorithm A looks pretty bad; it takes almost 10 times longer than Algorithm
B. But forn=100 they are about the same, and for larger values A is much better.

The fundamental reason is that for large values ofn, any function that contains ann^2 term
will grow faster than a function whose leading term isn. The **leading term** is the term with
the highest exponent.

For Algorithm A, the leading term has a large coefficient, 100, which is why B does better
than A for smalln. But regardless of the coefficients, there will always be some value ofn
wherean^2 >bn.

The same argument applies to the non-leading terms. Even if the run time of Algorithm A
weren+1000000, it would still be better than Algorithm B for sufficiently largen.

In general, we expect an algorithm with a smaller leading term to be a better algorithm for
large problems, but for smaller problems, there may be a **crossover point** where another
algorithm is better. The location of the crossover point depends on the details of the algo-
rithms, the inputs, and the hardware, so it is usually ignored for purposes of algorithmic
analysis. But that doesn’t mean you can forget about it.

If two algorithms have the same leading order term, it is hard to say which is better; again,
the answer depends on the details. So for algorithmic analysis, functions with the same
leading term are considered equivalent, even if they have different coefficients.

**B.1. Order of growth 203**

An **order of growth** is a set of functions whose asymptotic growth behavior is considered
equivalent. For example, 2n, 100nandn+1 belong to the same order of growth, which is
writtenO(n)in **Big-Oh notation** and often called **linear** because every function in the set
grows linearly withn.

All functions with the leading termn^2 belong toO(n^2 ); they are **quadratic** , which is a fancy
word for functions with the leading termn^2.

The following table shows some of the orders of growth that appear most commonly in
algorithmic analysis, in increasing order of badness.

```
Order of Name
growth
O( 1 ) constant
O(logbn) logarithmic (for anyb)
O(n) linear
O(nlogbn) “en log en”
O(n^2 ) quadratic
O(n^3 ) cubic
O(cn) exponential (for anyc)
```

For the logarithmic terms, the base of the logarithm doesn’t matter; changing bases is the
equivalent of multiplying by a constant, which doesn’t change the order of growth. Sim-
ilarly, all exponential functions belong to the same order of growth regardless of the base
of the exponent. Exponential functions grow very quickly, so exponential algorithms are
only useful for small problems.
**Exercise B.1.** Read the Wikipedia page on Big-Oh notation athttp: // en. wikipedia. org/
wiki/ Big* O* notationand answer the following questions:

1. What is the order of growth of n^3 +n^2? What about 1000000 n^3 +n^2? What about n^3 +
   1000000 n^2?
2. What is the order of growth of(n^2 +n)·(n+ 1 )? Before you start multiplying, remember
   that you only need the leading term.
3. If f is in O(g), for some unspecified function g, what can we say about a f+b?
4. If f 1 and f 2 are in O(g), what can we say about f 1 +f 2?
5. If f 1 is in O(g)and f 2 is in O(h), what can we say about f 1 +f 2?
6. If f 1 is in O(g)and f 2 is O(h), what can we say about f 1 ·f 2?

Programmers who care about performance often find this kind of analysis hard to swal-
low. They have a point: sometimes the coefficients and the non-leading terms make a
real difference. Sometimes the details of the hardware, the programming language, and
the characteristics of the input make a big difference. And for small problems asymptotic
behavior is irrelevant.

But if you keep those caveats in mind, algorithmic analysis is a useful tool. At least for
large problems, the “better” algorithms is usually better, and sometimes it ismuchbetter.
The difference between two algorithms with the same order of growth is usually a constant
factor, but the difference between a good algorithm and a bad algorithm is unbounded!

**204 Appendix B. Analysis of Algorithms**

### B.2 Analysis of basic Python operations

Most arithmetic operations are constant time; multiplication usually takes longer than ad-
dition and subtraction, and division takes even longer, but these run times don’t depend
on the magnitude of the operands. Very large integers are an exception; in that case the run
time increases with the number of digits.

Indexing operations—reading or writing elements in a sequence or dictionary—are also
constant time, regardless of the size of the data structure.

Aforloop that traverses a sequence or dictionary is usually linear, as long as all of the
operations in the body of the loop are constant time. For example, adding up the elements
of a list is linear:

```
total = 0
for x in t:
total += x
```

The built-in functionsumis also linear because it does the same thing, but it tends to be
faster because it is a more efficient implementation; in the language of algorithmic analysis,
it has a smaller leading coefficient.

If you use the same loop to “add” a list of strings, the run time is quadratic because string
concatenation is linear.

The string methodjoinis usually faster because it is linear in the total length of the strings.

As a rule of thumb, if the body of a loop is inO(na)then the whole loop is inO(na+^1 ). The
exception is if you can show that the loop exits after a constant number of iterations. If a
loop runsktimes regardless ofn, then the loop is inO(na), even for largek.

Multiplying bykdoesn’t change the order of growth, but neither does dividing. So if the
body of a loop is inO(na)and it runsn/ktimes, the loop is inO(na+^1 ), even for largek.

Most string and tuple operations are linear, except indexing andlen, which are constant
time. The built-in functionsminandmaxare linear. The run-time of a slice operation is
proportional to the length of the output, but independent of the size of the input.

All string methods are linear, but if the lengths of the strings are bounded by a constant—
for example, operations on single characters—they are considered constant time.

Most list methods are linear, but there are some exceptions:

- Adding an element to the end of a list is constant time on average; when it runs
  out of room it occasionally gets copied to a bigger location, but the total time forn
  operations isO(n), so we say that the “amortized” time for one operation isO( 1 ).
- Removing an element from the end of a list is constant time.
- Sorting isO(nlogn).

Most dictionary operations and methods are constant time, but there are some exceptions:

- The run time ofcopyis proportional to the number of elements, but not the size of
  the elements (it copies references, not the elements themselves).

```
B.3. Analysis of search algorithms 205
```

- The run time ofupdateis proportional to the size of the dictionary passed as a pa-
  rameter, not the dictionary being updated.
- keys, values and items are linear because they return new lists; iterkeys,
  itervaluesanditeritemsare constant time because they return iterators. But if
  you loop through the iterators, the loop will be linear. Using the “iter” functions
  saves some overhead, but it doesn’t change the order of growth unless the number of
  items you access is bounded.

```
The performance of dictionaries is one of the minor miracles of computer science. We will
see how they work in Section B.4.
Exercise B.2. Read the Wikipedia page on sorting algorithms athttp: // en. wikipedia. org/
wiki/ Sorting_ algorithmand answer the following questions:
```

1. What is a “comparison sort?” What is the best worst-case order of growth for a comparison
   sort? What is the best worst-case order of growth for any sort algorithm?
2. What is the order of growth of bubble sort, and why does Barack Obama think it is “the wrong
   way to go?”
3. What is the order of growth of radix sort? What preconditions do we need to use it?
4. What is a stable sort and why might it matter in practice?
5. What is the worst sorting algorithm (that has a name)?
6. What sort algorithm does the C library use? What sort algorithm does Python use? Are these
   algorithms stable? You might have to Google around to find these answers.
7. Many of the non-comparison sorts are linear, so why does does Python use an O(nlogn)
   comparison sort?

### B.3 Analysis of search algorithms

```
A search is an algorithm that takes a collection and a target item and determines whether
the target is in the collection, often returning the index of the target.
```

```
The simplest search algorithm is a “linear search,” which traverses the items of the collec-
tion in order, stopping if it finds the target. In the worst case it has to traverse the entire
collection, so the run time is linear.
```

```
Theinoperator for sequences uses a linear search; so do string methods likefindand
count.
```

If the elements of the sequence are in order, you can use a **bisection search** , which is
O(logn). Bisection search is similar to the algorithm you probably use to look a word
up in a dictionary (a real dictionary, not the data structure). Instead of starting at the be-
ginning and checking each item in order, you start with the item in the middle and check
whether the word you are looking for comes before or after. If it comes before, then you
search the first half of the sequence. Otherwise you search the second half. Either way, you
cut the number of remaining items in half.

```
If the sequence has 1,000,000 items, it will take about 20 steps to find the word or conclude
that it’s not there. So that’s about 50,000 times faster than a linear search.
```

**206 Appendix B. Analysis of Algorithms**

**Exercise B.3.** Write a function calledbisectionthat takes a sorted list and a target value and
returns the index of the value in the list, if it’s there, orNoneif it’s not.

Or you could read the documentation of thebisectmodule and use that!

Bisection search can be much faster than linear search, but it requires the sequence to be in
order, which might require extra work.

There is another data structure, called a **hashtable** that is even faster—it can do a search
in constant time—and it doesn’t require the items to be sorted. Python dictionaries are
implemented using hashtables, which is why most dictionary operations, including thein
operator, are constant time.

### B.4 Hashtables

To explain how hashtables work and why their performance is so good, I start with a simple
implementation of a map and gradually improve it until it’s a hashtable.

I use Python to demonstrate these implementations, but in real life you wouldn’t write
code like this in Python; you would just use a dictionary! So for the rest of this chapter, you
have to imagine that dictionaries don’t exist and you want to implement a data structure
that maps from keys to values. The operations you have to implement are:

add(k, v) **:** Add a new item that maps from keykto valuev. With a Python dictionary,d,
this operation is writtend[k] = v.

get(target) **:** Look up and return the value that corresponds to keytarget. With a Python
dictionary,d, this operation is writtend[target]ord.get(target).

For now, I assume that each key only appears once. The simplest implementation of this
interface uses a list of tuples, where each tuple is a key-value pair.

class LinearMap(object):

```
def __init__(self):
self.items = []
```

```
def add(self, k, v):
self.items.append((k, v))
```

```
def get(self, k):
for key, val in self.items:
if key == k:
return val
raise KeyError
```

addappends a key-value tuple to the list of items, which takes constant time.

getuses aforloop to search the list: if it finds the target key it returns the corresponding
value; otherwise it raises aKeyError. Sogetis linear.

An alternative is to keep the list sorted by key. Thengetcould use a bisection search,
which isO(logn). But inserting a new item in the middle of a list is linear, so this might

**B.4. Hashtables 207**

not be the best option. There are other data structures (see http://en.wikipedia.org/wiki/Red- black_tree) that can implement add and getin log time, but that’s still not as good as constant time, so let’s move on.

One way to improveLinearMapis to break the list of key-value pairs into smaller lists.
Here’s an implementation calledBetterMap, which is a list of 100 LinearMaps. As we’ll
see in a second, the order of growth forgetis still linear, butBetterMapis a step on the
path toward hashtables:

class BetterMap(object):

```
def __init__(self, n=100):
self.maps = []
for i in range(n):
self.maps.append(LinearMap())
```

```
def find_map(self, k):
index = hash(k) % len(self.maps)
return self.maps[index]
```

```
def add(self, k, v):
m = self.find_map(k)
m.add(k, v)
```

```
def get(self, k):
m = self.find_map(k)
return m.get(k)
```

**init**makes a list ofn LinearMaps.

find_mapis used byaddandgetto figure out which map to put the new item in, or which
map to search.

find_mapuses the built-in functionhash, which takes almost any Python object and returns
an integer. A limitation of this implementation is that it only works with hashable keys.
Mutable types like lists and dictionaries are unhashable.

Hashable objects that are considered equal return the same hash value, but the converse is
not necessarily true: two different objects can return the same hash value.

find_mapuses the modulus operator to wrap the hash values into the range from 0 to
len(self.maps), so the result is a legal index into the list. Of course, this means that many
different hash values will wrap onto the same index. But if the hash function spreads things
out pretty evenly (which is what hash functions are designed to do), then we expectn/100
items per LinearMap.

Since the run time ofLinearMap.getis proportional to the number of items, we expect
BetterMap to be about 100 times faster than LinearMap. The order of growth is still linear,
but the leading coefficient is smaller. That’s nice, but still not as good as a hashtable.

Here (finally) is the crucial idea that makes hashtables fast: if you can keep the maximum
length of the LinearMaps bounded,LinearMap.getis constant time. All you have to do is
keep track of the number of items and when the number of items per LinearMap exceeds
a threshold, resize the hashtable by adding more LinearMaps.

Here is an implementation of a hashtable:

**208 Appendix B. Analysis of Algorithms**

class HashMap(object):

```
def __init__(self):
self.maps = BetterMap(2)
self.num = 0
```

```
def get(self, k):
return self.maps.get(k)
```

```
def add(self, k, v):
if self.num == len(self.maps.maps):
self.resize()
```

```
self.maps.add(k, v)
self.num += 1
```

```
def resize(self):
new_maps = BetterMap(self.num * 2)
```

```
for m in self.maps.maps:
for k, v in m.items:
new_maps.add(k, v)
```

```
self.maps = new_maps
```

EachHashMapcontains aBetterMap;**init**starts with just 2 LinearMaps and initializes
num, which keeps track of the number of items.

getjust dispatches toBetterMap. The real work happens inadd, which checks the number
of items and the size of theBetterMap: if they are equal, the average number of items per
LinearMap is 1, so it callsresize.

resizemake a newBetterMap, twice as big as the previous one, and then “rehashes” the
items from the old map to the new.

Rehashing is necessary because changing the number of LinearMaps changes the denom-
inator of the modulus operator infind_map. That means that some objects that used to
wrap into the same LinearMap will get split up (which is what we wanted, right?).

Rehashing is linear, soresizeis linear, which might seem bad, since I promised thatadd
would be constant time. But remember that we don’t have to resize every time, soaddis
usually constant time and only occasionally linear. The total amount of work to runaddn
times is proportional ton, so the average time of eachaddis constant time!

To see how this works, think about starting with an empty HashTable and adding a se-
quence of items. We start with 2 LinearMaps, so the first 2 adds are fast (no resizing re-
quired). Let’s say that they take one unit of work each. The next add requires a resize, so
we have to rehash the first two items (let’s call that 2 more units of work) and then add the
third item (one more unit). Adding the next item costs 1 unit, so the total so far is 6 units
of work for 4 items.

The nextaddcosts 5 units, but the next three are only one unit each, so the total is 14 units
for the first 8 adds.

**B.4. Hashtables 209**

```
Figure B.1: The cost of a hashtable add.
```

The nextaddcosts 9 units, but then we can add 7 more before the next resize, so the total is
30 units for the first 16 adds.

After 32 adds, the total cost is 62 units, and I hope you are starting to see a pattern. Aftern
adds, wherenis a power of two, the total cost is 2n−2 units, so the average work per add
is a little less than 2 units. Whennis a power of two, that’s the best case; for other values of
nthe average work is a little higher, but that’s not important. The important thing is that it
isO( 1 ).

Figure B.1 shows how this works graphically. Each block represents a unit of work. The
columns show the total work for each add in order from left to right: the first twoaddscost
1 units, the third costs 3 units, etc.

The extra work of rehashing appears as a sequence of increasingly tall towers with increas-
ing space between them. Now if you knock over the towers, amortizing the cost of resizing
over all adds, you can see graphically that the total cost afternadds is 2n−2.

An important feature of this algorithm is that when we resize the HashTable it grows
geometrically; that is, we multiply the size by a constant. If you increase the size
arithmetically—adding a fixed number each time—the average time peraddis linear.

You can download my implementation of HashMap from http://thinkpython/code/Map.py, but remember that there is no reason to use it; if you want a map, just use a Python dictionary.

**210 Appendix B. Analysis of Algorithms**

## Appendix C

# Lumpy

Throughout the book, I have used diagrams to represent the state of running programs.

In Section 2.2, we used a state diagram to show the names and values of variables. In
Section 3.10 I introduced a stack diagram, which shows one frame for each function call.
Each frame shows the parameters and local variables for the function or method. Stack
diagrams for recursive functions appear in Section 5.9 and Section 6.5.

Section 10.2 shows what a list looks like in a state diagram, Section 11.4 shows what a
dictionary looks like, and Section 12.6 shows two ways to represent tuples.

Section 15.2 introduces object diagrams, which show the state of an object’s attributes, and
their attributes, and so on. Section 15.3 has object diagrams for Rectangles and their em-
bedded Points. Section 16.1 shows the state of a Time object. Section 18.2 has a diagram
that includes a class object and an instance, each with their own attributes.

Finally, Section 18.8 introduces class diagrams, which show the classes that make up a
program and the relationships between them.

These diagrams are based on the Unified Modeling Language (UML), which is a stan-
dardized graphical language used by software engineers to communicate about program
design, especially for object-oriented programs.

UML is a rich language with many kinds of diagrams that represent many kinds of rela-
tionship between objects and classes. What I presented in this book is a small subset of the
language, but it is the subset most commonly used in practice.

The purpose of this appendix is to review the diagrams presented in the previous chapters,
and to introduce Lumpy. Lumpy, which stands for “UML in Python,” with some of the
letters rearranged, is part of Swampy, which you already installed if you worked on the
case study in Chapter 4 or Chapter 19, or if you did Exercise 15.4,

Lumpy uses Python’sinspectmodule to examine the state of a running program and
generate object diagrams (including stack diagrams) and class diagrams.

## C.1 State diagram

Here’s an example that uses Lumpy to generate a state diagram.

**212 Appendix C. Lumpy**

```
n 17
```

```
message 'And now for something complete'
```

```
pi 3.14159265359
```

```
<module>
```

```
Figure C.1: State diagram generated by Lumpy.
```

```
<module> countdownn 2 countdownn 1 countdownn 0
```

```
Figure C.2: Stack diagram.
```

from swampy.Lumpy import Lumpy

lumpy = Lumpy()
lumpy.make_reference()

message = 'And now for something completely different'
n = 17
pi = 3.1415926535897932

lumpy.object_diagram()

The first line imports the Lumpy class fromswampy.Lumpy. If you don’t have Swampy
installed as a package, make sure the Swampy files are in Python’s search path and use
thisimportstatement instead:

from Lumpy import Lumpy

The next lines create aLumpyobject and make a “reference” point, which means that Lumpy
records the objects that have been defined so far.

Next we define new variables and invokeobject_diagram, which draws the objects that
have been defined since the reference point, in this casemessage,nandpi.

Figure C.1 shows the result. The graphical style is different from what I showed earlier; for
example, each reference is represented by a circle next to the variable name and a line to
the value. And long strings are truncated. But the information conveyed by the diagram is
the same.

The variable names are in a frame labeled<module>, which indicates that these are module-
level variables, also known as global.

You can download this example fromhttp://thinkpython.com/code/lumpy_demo1.py.
Try adding some additional assignments and see what the diagram looks like.

### C.2 Stack diagram

Here’s an example that uses **Lumpy** to generate a stack diagram. You can download it from [http://thinkpython.com/code/lumpy_demo2.py](http://thinkpython.com/code/lumpy_demo2.py)

**C.3. Object diagrams 213**

```
cheeses 0 'Cheddar'
```

```
1 'Edam'
```

```
2 'Gouda'
```

```
list
```

```
numbers 0 17
```

```
1 123
```

```
list
```

```
empty list
```

```
<module>
```

```
Figure C.3: Object diagram.
```

```python
from swampy.Lumpy import Lumpy

def countdown(n):
if n <= 0:
print 'Blastoff!'
lumpy.object_diagram()
else:
print n
countdown(n-1)

lumpy = Lumpy()
lumpy.make_reference()
countdown(3)
```

Figure C.2 shows the result. Each frame is represented with a box that has the function’s name outside and variables inside. Since this function is recursive, there is one frame for each level of recursion.

Remember that a stack diagram shows the state of the program at a particular point in its execution. To get the diagram you want, sometimes you have to think about where to invoke object_diagram.

In this case I invokeobject_diagramafter executing the base case of the recursion; that way the stack diagram shows each level of the recursion. You can call `object_diagram` more than once to get a series of snapshots of the program’s execution.

### C.3 Object diagrams

This example generates an object diagram showing the lists from Section 10.1. You can download it from http://thinkpython.com/code/lumpy_demo3.py.

```python
from swampy.Lumpy import Lumpy

lumpy = Lumpy()
lumpy.make_reference()

cheeses = ['Cheddar', 'Edam','Gouda']
```

**214 Appendix C. Lumpy**

```
inverse 1 0 'a'
```

```
1 'p'
```

```
2 't'
```

```
3 'o'
```

```
list
```

```
2 0 'r'
```

```
list
```

```
dict
```

```
hist 'a' 1
```

```
'p' 1
```

```
'r' 2
```

```
't' 1
```

```
'o' 1
```

```
dict
```

```
<module>
```

```
Figure C.4: Object diagram.
```

numbers = [17, 123]
empty = []

lumpy.object_diagram()

Figure C.3 shows the result. Lists are represented by a box that shows the indices mapping
to the elements. This representation is slightly misleading, since indices are not actually
part of the list, but I think they make the diagram easier to read. The empty list is repre-
sented by an empty box.

And here’s an example showing the dictionaries from Section 11.4. You can download it
fromhttp://thinkpython.com/code/lumpy_demo4.py.

from swampy.Lumpy import Lumpy

lumpy = Lumpy()
lumpy.make_reference()

hist = histogram('parrot')
inverse = invert_dict(hist)

lumpy.object_diagram()

Figure C.4 shows the result.histis a dictionary that maps from characters (single-letter
strings) to integers;inversemaps from integers to lists of strings.

This example generates an object diagram for Point and Rectangle objects, as in Sec-
tion 15.6. You can download it fromhttp://thinkpython.com/code/lumpy_demo5.py.

import copy
from swampy.Lumpy import Lumpy

**C.4. Function and class objects 215**

```
box width 100.0
```

```
corner y 0.0
```

```
x 0.0
```

```
Point
```

```
height 200.0
```

```
Rectangle
```

```
box2
```

```
width 100.0
```

```
height 200.0
```

```
corner
```

```
Rectangle
```

```
<module>
```

```
Figure C.5: Object diagram.
```

```
Point __name__ 'Point'
```

```
type
```

```
instantiate __name__ 'instantiate'
```

```
function
```

```
Rectangle __name__ 'Rectangle'
```

```
type
```

```
<module>
obj
Point
```

```
constructor
```

```
instantiate
```

```
Figure C.6: Object diagram.
```

lumpy = Lumpy()
lumpy.make_reference()

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

box2 = copy.copy(box)

lumpy.object_diagram()

Figure C.5 shows the result.copy.copymake a shallow copy, soboxandbox2have their
ownwidthandheight, but they share the same embedded Point object. This kind of
sharing is usually fine with immutable objects, but with mutable types, it is highly error-
prone.

### C.4 Function and class objects

When I use Lumpy to make object diagrams, I usually define the functions and classes
before I make the reference point. That way, function and class objects don’t appear in the
diagram.

**216 Appendix C. Lumpy**

```
object Rectangle
corner
height
width
```

```
Point
x
y
```

```
Figure C.7: Class diagram.
```

But if you are passing functions and classes as parameters, you might want them to appear.
This example shows what that looks like; you can download it fromhttp://thinkpython.
com/code/lumpy_demo6.py.

import copy
from swampy.Lumpy import Lumpy

lumpy = Lumpy()
lumpy.make_reference()

class Point(object):
"""Represents a point in 2-D space."""

class Rectangle(object):
"""Represents a rectangle."""

def instantiate(constructor):
"""Instantiates a new object."""
obj = constructor()
lumpy.object_diagram()
return obj

point = instantiate(Point)

Figure C.6 shows the result. Since we invokeobject_diagraminside a function, we get
a stack diagram with a frame for the module-level variables and for the invocation of
instantiate.

At the module level,PointandRectanglerefer to class objects (which have typetype);
instantiaterefers to a function object.

This diagram might clarify two points of common confusion: (1) the difference between the
class object,Point, and the instance of Point,obj, and (2) the difference between the func-
tion object created wheninstantiateis defined, and the frame created with it is called.

### C.5 Class Diagrams

Although I distinguish between state diagrams, stack diagrams and object diagrams, they
are mostly the same thing: they show the state of a running program at a point in time.

**C.5. Class Diagrams 217**

```
object Deck
__init__
__str__
add_card
move_cards
pop_card
remove_card
shuffle
sort
cards
```

```
Hand
__init__
```

```
PokerHand
has_flush
suit_hist
cards
label
```

```
Card
__cmp__
__init__
__str__
rank_names
suit_names
rank
suit
```

```
Figure C.8: Class diagram.
```

Class diagrams are different. They show the classes that make up a program and the re-
lationships between them. They are timeless in the sense that they describe the program
as a whole, not any particular point in time. For example, if an instance of Class A gener-
ally contains a reference to an instance of Class B, we say there is a “HAS-A relationship”
between those classes.

Here’s an example that shows a HAS-A relationship. You can download it fromhttp:
//thinkpython.com/code/lumpy_demo7.py.

from swampy.Lumpy import Lumpy

lumpy = Lumpy()
lumpy.make_reference()

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

lumpy.class_diagram()

Figure C.7 shows the result. Each class is represented with a box that contains the name of
the class, any methods the class provides, any class variables, and any instance variables.
In this example,RectangleandPointhave instance variables, but no methods or class
variables.

The arrow fromRectangletoPointshows that Rectangles contain an embedded Point.
In addition,RectangleandPointboth inherit fromobject, which is represented in the
diagram with a triangle-headed arrow.

**218 Appendix C. Lumpy**

Here’s a more complex example using my solution to Exercise 18.6. You can download
the code fromhttp://thinkpython.com/code/lumpy_demo8.py; you will also needhttp:
//thinkpython.com/code/PokerHand.py.

from swampy.Lumpy import Lumpy

from PokerHand import \*

lumpy = Lumpy()
lumpy.make_reference()

deck = Deck()
hand = PokerHand()
deck.move_cards(hand, 7)

lumpy.class_diagram()

Figure C.8 shows the result.PokerHandinherits fromHand, which inherits fromDeck. Both
DeckandPokerHandhave Cards.

This diagram does not show thatHandalso has cards, because in the program there are no
instances of Hand. This example demonstrates a limitation of Lumpy; it only knows about
the attributes and HAS-A relationships of objects that are instantiated.
