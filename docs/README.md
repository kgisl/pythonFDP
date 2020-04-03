# Python Documentation

## Classes

**[PokerHand](PokerHand.md)**: Represents a poker hand. 

**[Time](Time.md)**: Represents the time of day.   
attributes: hour, minute, second 

**[Kangaroo](Kangaroo.md)**: A Kangaroo is a marsupial. 

**[Time](Time.md)**: Represents the time of day.   
attributes: hour, minute, second 

**[Kangaroo](Kangaroo.md)**: A Kangaroo is a marsupial. 

**[Point](Point.md)**: Represents a point in 2-D space.   
attributes: x, y 

**[Rectangle](Rectangle.md)**: Represents a rectangle.   
attributes: width, height, corner. 

**[Time](Time.md)**: Represents the time of day.   
attributes: hour, minute, second 

**[Card](Card.md)**: Represents a standard playing card.   
Attributes: suit: integer 0-3 rank: integer 1-13 

**[Deck](Deck.md)**: Represents a deck of cards.   
Attributes: cards: list of Card objects. 

**[Hand](Hand.md)**: Represents a hand of playing cards. 

**[Point](Point.md)**: Represents a point in 2-D space.   
attributes: x, y 

**[Test](Test.md)**: 

**[Circle](Circle.md)**: Represents a circle.   
Attributes: center, radius 

**[Hist](Hist.md)**: A map from each item (x) to its frequency. 

**[PokerHand](PokerHand.md)**: Represents a poker hand. 

**[PokerDeck](PokerDeck.md)**: Represents a deck of cards that can deal poker hands. 

**[LinearMap](LinearMap.md)**: A simple implementation of a map using a list of tuples where each tuple is a key-value pair. 

**[BetterMap](BetterMap.md)**: A faster implementation of a map using a list of LinearMaps and the built-in function hash() to determine which LinearMap to put each key into. 

**[HashMap](HashMap.md)**: An implementation of a hashtable using a BetterMap that grows so that the number of items never exceeds the number of LinearMaps.   
The amortized cost of add should be O(1) provided that the implementation of sum in resize is linear. 

**[Markov](Markov.md)**: Encapsulates the statistical summary of a text. 


## Functions

### fprint


My own function source code inspection function Filters out any print statements and input statements 
#### Parameters
name | description | default
--- | --- | ---
fname |  | 





### divideTwo


function which takes a list and returns two halves 
#### Parameters
name | description | default
--- | --- | ---
al |  | 





### merge


merge generates a new sorted list containing all elements contained in both sorted lists 
#### Parameters
name | description | default
--- | --- | ---
A |  | 
B |  | 





### mergesort


sorts the list using the mergesort algorithm 
#### Parameters
name | description | default
--- | --- | ---
alist |  | 





### fprint


In IPython, you have the very convenient "func"?? which will inspect the source code (http://j.mp/inspectThis)   
My own function source code inspection function Filters out any print statements and input statements 
#### Parameters
name | description | default
--- | --- | ---
fname |  | 





### selection_sort


Pure implementation of the selection sort algorithm in Python :param collection: some mutable ordered collection with heterogeneous comparable items inside :return: the same collection ordered by ascending Examples: >>> selection_sort([0, 5, 3, 2, 2]) [0, 2, 2, 3, 5] >>> selection_sort([]) [] >>> selection_sort([-2, -5, -45]) [-45, -5, -2] 
#### Parameters
name | description | default
--- | --- | ---
collection |  | 





### swap


swap two elements in a list 
#### Parameters
name | description | default
--- | --- | ---
alist |  | 
ai |  | 
bi |  | 





### min_index



#### Parameters
name | description | default
--- | --- | ---
alist |  | 
i |  | 





### print_history



#### Parameters
name | description | default
--- | --- | ---
hlist |  | 





### selectsort



#### Parameters
name | description | default
--- | --- | ---
alist |  | 





### selectsortf



#### Parameters
name | description | default
--- | --- | ---
alist |  | 





### selectsortc



#### Parameters
name | description | default
--- | --- | ---
alist |  | 





### selectsortd



#### Parameters
name | description | default
--- | --- | ---
alist |  | 





### min_index_c


function returns the index of the minimum value in the sublist alist[i:] 
#### Parameters
name | description | default
--- | --- | ---
alist |  | 
i |  | 





### make_word_list


Reads lines from a file and builds a list using append.   
returns: list of strings 




### in_bisect


Checks whether a word is in a list using bisection search.   
Precondition: the words in the list are sorted   
word_list: list of strings word: string 
#### Parameters
name | description | default
--- | --- | ---
word_list |  | 
word |  | 





### in_bisect_cheat


Checks whether a word is in a list using bisection search.   
Precondition: the words in the list are sorted   
word_list: list of strings word: string 
#### Parameters
name | description | default
--- | --- | ---
word_list |  | 
word |  | 





### int_to_time


Makes a new Time object.   
seconds: int seconds since midnight. 
#### Parameters
name | description | default
--- | --- | ---
seconds |  | 





### main







### make_word_list1


Reads lines from a file and builds a list using append. 




### make_word_list2


Reads lines from a file and builds a list using list +. 




### int_to_time


Makes a new Time object.   
seconds: int seconds since midnight. 
#### Parameters
name | description | default
--- | --- | ---
seconds |  | 





### main







### ackermann


Computes the Ackermann function A(m, n)   
See http://en.wikipedia.org/wiki/Ackermann_function   
n, m: non-negative integers 
#### Parameters
name | description | default
--- | --- | ---
m |  | 
n |  | 





### make_word_dict


Read the words in words.txt and return a dictionary that contains the words as keys 




### rotate_pairs


Prints all words that can be generated by rotating word.   
word: string word_dict: dictionary with words as keys 
#### Parameters
name | description | default
--- | --- | ---
word |  | 
word_dict |  | 





### most_frequent


Sorts the letters in s in reverse order of frequency.   
s: string   
Returns: list of letters 
#### Parameters
name | description | default
--- | --- | ---
s |  | 





### make_histogram


Make a map from letters to number of times they appear in s.   
s: string   
Returns: map from letter to frequency 
#### Parameters
name | description | default
--- | --- | ---
s |  | 





### read_file


Returns the contents of a file as a string. 
#### Parameters
name | description | default
--- | --- | ---
filename |  | 





### process_file


Reads a file and performs Markov analysis.   
filename: string order: integer number of words in the prefix   
returns: map from prefix to list of possible suffixes. 
#### Parameters
name | description | default
--- | --- | ---
filename |  | 
order |  | 2





### skip_gutenberg_header


Reads from fp until it finds the line that ends the header.   
fp: open file object 
#### Parameters
name | description | default
--- | --- | ---
fp |  | 





### process_word


Processes each word.   
word: string order: integer   
During the first few iterations, all we do is store up the words; after that we start adding entries to the dictionary. 
#### Parameters
name | description | default
--- | --- | ---
word |  | 
order |  | 2





### random_text


Generates random wordsfrom the analyzed text.   
Starts with a random prefix from the dictionary.   
n: number of words to generate 
#### Parameters
name | description | default
--- | --- | ---
n |  | 100





### shift


Forms a new tuple by removing the head and adding word to the tail.   
t: tuple of strings word: string   
Returns: tuple of strings 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
word |  | 





### main



#### Parameters
name | description | default
--- | --- | ---
script |  | 
filename |  | "emma.txt"
n |  | 100
order |  | 2





### is_triple_double


Tests if a word contains three consecutive double letters.   
word: string   
returns: bool 
#### Parameters
name | description | default
--- | --- | ---
word |  | 





### find_triple_double


Reads a word list and prints words with triple double letters. 




### is_after


Returns True if t1 is after t2; false otherwise. 
#### Parameters
name | description | default
--- | --- | ---
t1 |  | 
t2 |  | 





### increment


Adds seconds to a Time object. 
#### Parameters
name | description | default
--- | --- | ---
t1 |  | 
seconds |  | 





### mul_time


Multiplies a Time object by a factor. 
#### Parameters
name | description | default
--- | --- | ---
t1 |  | 
factor |  | 





### days_until_birthday


How long until my next birthday? 
#### Parameters
name | description | default
--- | --- | ---
birthday |  | 





### double_day


Compute the day when one person is twice as old as the other.   
b1: datetime birthday of the younger person b2: datetime birthday of the older person 
#### Parameters
name | description | default
--- | --- | ---
b1 |  | 
b2 |  | 





### datetime_exercises


Exercise solutions. 




### main







### do_twice


Runs a function twice.   
func: function object arg: argument passed to the function 
#### Parameters
name | description | default
--- | --- | ---
func |  | 
arg |  | 





### print_twice


Prints the argument twice.   
arg: anything printable 
#### Parameters
name | description | default
--- | --- | ---
arg |  | 





### do_four


Runs a function four times.   
func: function object arg: argument passed to the function 
#### Parameters
name | description | default
--- | --- | ---
func |  | 
arg |  | 





### koch


Draws a koch curve with length n. 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### snowflake


Draws a snowflake (a triangle with a Koch curve for each side). 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### fd



#### Parameters
name | description | default
--- | --- | ---
t |  | 
length |  | 





### bk



#### Parameters
name | description | default
--- | --- | ---
t |  | 
length |  | 





### lt



#### Parameters
name | description | default
--- | --- | ---
t |  | 
angle |  | 90





### rt



#### Parameters
name | description | default
--- | --- | ---
t |  | 
angle |  | 90





### pd



#### Parameters
name | description | default
--- | --- | ---
t |  | 





### pu



#### Parameters
name | description | default
--- | --- | ---
t |  | 





### fdlt


forward and left 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
angle |  | 90





### fdbk


forward and back, ending at the original position 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### skip


lift the pen and move 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### stump


Makes a vertical line and leave the turtle at the top, facing right 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
angle |  | 90





### hollow


move the turtle vertically and leave it at the top, facing right 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### post


Makes a vertical line and return to the original position 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### beam


Makes a horizontal line at the given height and return. 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
height |  | 





### hangman


Makes a vertical line to the given height and a horizontal line at the given height and then return. This is efficient to implement, and turns out to be useful, but it's not so semantically clean. 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
height |  | 





### diagonal


Makes a diagonal line to the given x, y offsets and return 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
x |  | 
y |  | 





### vshape



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
height |  | 





### bump


Makes a bump with radius n at height*n  
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
height |  | 





### draw_a



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_b



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_c



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_d



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_ef



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_e



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_f



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_g



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_h



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_i



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_j



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_k



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_l



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_n



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_m



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_o



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_p



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_q



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_r



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_s



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_t



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_u



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_v



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_w



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_x



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_v



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_y



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_z



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### draw_



#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 





### str_fill


Returns i as a string with at least n digits.   
i: int n: int length   
returns: string 
#### Parameters
name | description | default
--- | --- | ---
i |  | 
n |  | 





### are_reversed


Checks if i and j are the reverse of each other.   
i: int j: int   
returns:bool 
#### Parameters
name | description | default
--- | --- | ---
i |  | 
j |  | 





### num_instances


Counts the number of palindromic ages.   
Returns the number of times the mother and daughter have palindromic ages in their lives, given the difference in age.   
diff: int difference in ages flag: bool, if True, prints the details 
#### Parameters
name | description | default
--- | --- | ---
diff |  | 
flag |  | False





### check_diffs


Finds age differences that satisfy the problem.   
Enumerates the possible differences in age between mother and daughter, and for each difference, counts the number of times over their lives they will have ages that are the reverse of each other. 




### draw_circle


Draws a circle.   
t: Turtle circle: Circle 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
circle |  | 





### draw_rect


Draws a rectangle.   
t: Turtle rect: Rectangle 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
rect |  | 





### print_point


Print a Point object in human-readable format. 
#### Parameters
name | description | default
--- | --- | ---
p |  | 





### find_center


Returns a Point at the center of a Rectangle.   
rect: Rectangle   
returns: new Point 
#### Parameters
name | description | default
--- | --- | ---
rect |  | 





### grow_rectangle


Modifies the Rectangle by adding to its width and height.   
rect: Rectangle object. dwidth: change in width (can be negative). dheight: change in height (can be negative). 
#### Parameters
name | description | default
--- | --- | ---
rect |  | 
dwidth |  | 
dheight |  | 





### main







### structshape


Returns a string that describes the shape of a data structure.   
ds: any Python object   
Returns: string 
#### Parameters
name | description | default
--- | --- | ---
ds |  | 





### listrep


Returns a string representation of a list of type strings.   
t: list of strings   
Returns: string 
#### Parameters
name | description | default
--- | --- | ---
t |  | 





### setrep


Returns a string representation of a set of type strings.   
s: set of strings   
Returns: string 
#### Parameters
name | description | default
--- | --- | ---
s |  | 





### append


Adds a new element to a list of type strings.   
Modifies res.   
res: list of type strings typestr: the new type string count: how many of the new type there are   
Returns: None 
#### Parameters
name | description | default
--- | --- | ---
res |  | 
typestr |  | 
count |  | 





### subtract


Returns a set of all keys that appear in d1 but not d2.   
d1, d2: dictionaries 
#### Parameters
name | description | default
--- | --- | ---
d1 |  | 
d2 |  | 





### main







### print_time


Prints a string representation of the time.   
t: Time object 
#### Parameters
name | description | default
--- | --- | ---
t |  | 





### int_to_time


Makes a new Time object.   
seconds: int seconds since midnight. 
#### Parameters
name | description | default
--- | --- | ---
seconds |  | 





### time_to_int


Computes the number of seconds since midnight.   
time: Time object. 
#### Parameters
name | description | default
--- | --- | ---
time |  | 





### add_times


Adds two time objects.   
t1, t2: Time   
returns: Time 
#### Parameters
name | description | default
--- | --- | ---
t1 |  | 
t2 |  | 





### valid_time


Checks whether a Time object satisfies the invariants.   
time: Time   
returns: boolean 
#### Parameters
name | description | default
--- | --- | ---
time |  | 





### main







### nested_sum


Computes the total of all numbers in a list of lists.   
t: list of list of numbers   
returns: number 
#### Parameters
name | description | default
--- | --- | ---
t |  | 





### cumsum


Computes the cumulative sum of the numbers in t.   
t: list of numbers   
returns: list of numbers 
#### Parameters
name | description | default
--- | --- | ---
t |  | 





### middle


Returns all but the first and last elements of t.   
t: list   
returns: new list 
#### Parameters
name | description | default
--- | --- | ---
t |  | 





### chop


Removes the first and last elements of t.   
t: list   
returns: None 
#### Parameters
name | description | default
--- | --- | ---
t |  | 





### is_sorted


Checks whether a list is sorted.   
t: list   
returns: boolean 
#### Parameters
name | description | default
--- | --- | ---
t |  | 





### is_anagram


Checks whether two words are anagrams   
word1: string or list word2: string or list   
returns: boolean 
#### Parameters
name | description | default
--- | --- | ---
word1 |  | 
word2 |  | 





### has_duplicates


Returns True if any element appears more than once in a sequence.   
s: string or list   
returns: bool 
#### Parameters
name | description | default
--- | --- | ---
s |  | 





### main







### read_dictionary


Reads from a file and builds a dictionary that maps from each word to a string that describes its primary pronunciation.   
Secondary pronunciations are added to the dictionary with a number, in parentheses, at the end of the key, so the key for the second pronunciation of "abdominal" is "abdominal(2)".   
filename: string returns: map from string to pronunciation 
#### Parameters
name | description | default
--- | --- | ---
filename |  | "c06d"





### has_duplicates


Returns True if any element appears more than once in a sequence.   
t: list   
returns: bool 
#### Parameters
name | description | default
--- | --- | ---
t |  | 





### random_bdays


Returns a list of integers between 1 and 365, with length n.   
n: int   
returns: list of int 
#### Parameters
name | description | default
--- | --- | ---
n |  | 





### count_matches


Generates a sample of birthdays and counts duplicates.   
num_students: how many students in the group num_samples: how many groups to simulate   
returns: int 
#### Parameters
name | description | default
--- | --- | ---
num_students |  | 
num_simulations |  | 





### main


Runs the birthday simulation and prints the number of matches. 




### rotate_letter


Rotates a letter by n places.  Does not change other chars.   
letter: single-letter string n: int   
Returns: single-letter string 
#### Parameters
name | description | default
--- | --- | ---
letter |  | 
n |  | 





### rotate_word


Rotates a word by n places.   
word: string n: integer   
Returns: string 
#### Parameters
name | description | default
--- | --- | ---
word |  | 
n |  | 





### reverse_pair


Checks whether a reversed word appears in word_list.   
word_list: list of strings word: string 
#### Parameters
name | description | default
--- | --- | ---
word_list |  | 
word |  | 





### find_defining_class


Finds and returns the class object that will provide the definition of method_name (as a string) if it is invoked on obj.   
obj: any python object method_name: string method name 
#### Parameters
name | description | default
--- | --- | ---
obj |  | 
method_name |  | 





### interlock


Checks whether a word contains two interleaved words.   
word_list: list of strings word: string 
#### Parameters
name | description | default
--- | --- | ---
word_list |  | 
word |  | 





### interlock_general


Checks whether a word contains n interleaved words.   
word_list: list of strings word: string n: number of interleaved words 
#### Parameters
name | description | default
--- | --- | ---
word_list |  | 
word |  | 
n |  | 3





### draw_spiral


Draws an Archimedian spiral starting at the origin.   
Args: n: how many line segments to draw length: how long each segment is a: how loose the initial spiral starts out (larger is looser) b: how loosly coiled the spiral is (larger is looser)   
http://en.wikipedia.org/wiki/Spiral 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
length |  | 3
a |  | 0.1
b |  | 0.0002





### ackermann


Computes the Ackermann function A(m, n)   
See http://en.wikipedia.org/wiki/Ackermann_function   
n, m: non-negative integers 
#### Parameters
name | description | default
--- | --- | ---
m |  | 
n |  | 





### factorial


Computes factorial of n recursively. 
#### Parameters
name | description | default
--- | --- | ---
n |  | 





### estimate_pi


Computes an estimate of pi.   
Algorithm due to Srinivasa Ramanujan, from http://en.wikipedia.org/wiki/Pi 




### make_word_dict


Read. the words in words.txt and return a dictionary that contains the words as keys. 




### homophones


Checks if words two can be pronounced the same way.   
If either word is not in the pronouncing dictionary, return False   
a, b: strings phonetic: map from words to pronunciation codes 
#### Parameters
name | description | default
--- | --- | ---
a |  | 
b |  | 
phonetic |  | 





### check_word


Checks to see if the word has the following property: removing the first letter yields a word with the same pronunciation, and removing the second letter yields a word with the same pronunciation.   
word: string word_dict: dictionary with words as keys phonetic: map from words to pronunciation codes 
#### Parameters
name | description | default
--- | --- | ---
word |  | 
word_dict |  | 
phonetic |  | 





### do_twice



#### Parameters
name | description | default
--- | --- | ---
f |  | 





### do_four



#### Parameters
name | description | default
--- | --- | ---
f |  | 





### print_beam







### print_post







### print_beams







### print_posts







### print_row







### print_grid







### one_four_one



#### Parameters
name | description | default
--- | --- | ---
f |  | 
g |  | 
h |  | 





### print_plus







### print_dash







### print_bar







### print_space







### print_end







### nothing


do nothing 




### print1beam







### print1post







### print4beams







### print4posts







### print_row







### print_grid







### metathesis_pairs


Print all pairs of words that differ by swapping two letters.   
d: map from word to list of anagrams 
#### Parameters
name | description | default
--- | --- | ---
d |  | 





### word_distance


Computes the number of differences between two words.   
word1, word2: strings   
Returns: integer 
#### Parameters
name | description | default
--- | --- | ---
word1 |  | 
word2 |  | 





### sort_by_length


Sort a list of words in reverse order by length.   
This is the version in the book; it is stable in the sense that words with the same length appear in the same order   
words: list of strings   
Returns: list of strings 
#### Parameters
name | description | default
--- | --- | ---
words |  | 





### sort_by_length_random


Sort a list of words in reverse order by length.   
This is the solution to the exercise.  It is unstable in the sense that if two words have the same length, their order in the output list is random.   
It works by extending the list of tuples with a column of random numbers; when there is a tie in the first column, the random column determines the output order.   
words: list of strings   
Returns: list of strings 
#### Parameters
name | description | default
--- | --- | ---
words |  | 





### main







### make_word_dict


Reads a word list and returns a dictionary. 




### is_reducible


If word is reducible, returns a list of its reducible children.   
Also adds an entry to the memo dictionary.   
A string is reducible if it has at least one child that is reducible.  The empty string is also reducible.   
word: string word_dict: dictionary with words as keys 
#### Parameters
name | description | default
--- | --- | ---
word |  | 
word_dict |  | 





### children


Returns a list of all words that can be formed by removing one letter.   
word: string   
Returns: list of strings 
#### Parameters
name | description | default
--- | --- | ---
word |  | 
word_dict |  | 





### all_reducible


Checks all words in the word_dict; returns a list reducible ones.   
word_dict: dictionary with words as keys 
#### Parameters
name | description | default
--- | --- | ---
word_dict |  | 





### print_trail


Prints the sequence of words that reduces this word to the empty string.   
If there is more than one choice, it chooses the first.   
word: string 
#### Parameters
name | description | default
--- | --- | ---
word |  | 





### print_longest_words


Finds the longest reducible words and prints them.   
word_dict: dictionary of valid words 
#### Parameters
name | description | default
--- | --- | ---
word_dict |  | 





### random_word


Chooses a random word from a histogram.   
The probability of each word is proportional to its frequency.   
hist: map from word to frequency 
#### Parameters
name | description | default
--- | --- | ---
hist |  | 





### main







### petal


Draws a petal using two arcs.   
t: Turtle r: radius of the arcs angle: angle (degrees) that subtends the arcs 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
r |  | 
angle |  | 





### flower


Draws a flower with n petals.   
t: Turtle n: number of petals r: radius of the arcs angle: angle (degrees) that subtends the arcs 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
r |  | 
angle |  | 





### move


Move Turtle (t) forward (length) units without leaving a trail. Leaves the pen down. 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
length |  | 





### has_duplicates


Checks whether any element appears more than once in a sequence.   
Simple version using a for loop.   
t: sequence 
#### Parameters
name | description | default
--- | --- | ---
t |  | 





### has_duplicates2


Checks whether any element appears more than once in a sequence.   
Faster version using a set.   
t: sequence 
#### Parameters
name | description | default
--- | --- | ---
t |  | 





### first


Returns the first character of a string. 
#### Parameters
name | description | default
--- | --- | ---
word |  | 





### last


Returns the last of a string. 
#### Parameters
name | description | default
--- | --- | ---
word |  | 





### middle


Returns all but the first and last characters of a string. 
#### Parameters
name | description | default
--- | --- | ---
word |  | 





### is_palindrome


Returns True if word is a palindrome. 
#### Parameters
name | description | default
--- | --- | ---
word |  | 





### draw_pie


Draws a pie, then moves into position to the right.   
t: Turtle n: number of segments r: length of the radial spokes 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
r |  | 





### polypie


Draws a pie divided into radial segments.   
t: Turtle n: number of segments r: length of the radial spokes 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
r |  | 





### isosceles


Draws an icosceles triangle.   
The turtle starts and ends at the peak, facing the middle of the base.   
t: Turtle r: length of the equal legs angle: peak angle in degrees 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
r |  | 
angle |  | 





### walk


Finds the names of all files in dirname and its subdirectories.   
dirname: string name of directory 
#### Parameters
name | description | default
--- | --- | ---
dirname |  | 





### compute_checksum


Computes the MD5 checksum of the contents of a file.   
filename: string 
#### Parameters
name | description | default
--- | --- | ---
filename |  | 





### check_diff


Computes the difference between the contents of two files.   
name1, name2: string filenames 
#### Parameters
name | description | default
--- | --- | ---
name1 |  | 
name2 |  | 





### pipe


Runs a command in a subprocess.   
cmd: string Unix command   
Returns (res, stat), the output of the subprocess and the exit status. 
#### Parameters
name | description | default
--- | --- | ---
cmd |  | 





### compute_checksums


Computes checksums for all files with the given suffix.   
dirname: string name of directory to search suffix: string suffix to match   
Returns: map from checksum to list of files with that checksum 
#### Parameters
name | description | default
--- | --- | ---
dirname |  | 
suffix |  | 





### check_pairs


Checks whether any in a list of files differs from the others.   
names: list of string filenames 
#### Parameters
name | description | default
--- | --- | ---
names |  | 





### print_duplicates


Checks for duplicate files.   
Reports any files with the same checksum and checks whether they are, in fact, identical.   
d: map from checksum to list of files with that checksum 
#### Parameters
name | description | default
--- | --- | ---
d |  | 





### point_in_circle


Checks whether a point lies inside a circle (or on the boundary).   
point: Point object circle: Circle object 
#### Parameters
name | description | default
--- | --- | ---
point |  | 
circle |  | 





### rect_in_circle


Checks whether the corners of a rect fall in/on a circle.   
rect: Rectangle object circle: Circle object 
#### Parameters
name | description | default
--- | --- | ---
rect |  | 
circle |  | 





### rect_circle_overlap


Checks whether any corners of a rect fall in/on a circle.   
rect: Rectangle object circle: Circle object 
#### Parameters
name | description | default
--- | --- | ---
rect |  | 
circle |  | 





### main







### has_palindrome


Checks if the string representation of i has a palindrome.   
i: integer start: where in the string to start length: length of the palindrome to check for 
#### Parameters
name | description | default
--- | --- | ---
i |  | 
start |  | 
length |  | 





### check


Checks if the integer (i) has the desired properties.   
i: int 
#### Parameters
name | description | default
--- | --- | ---
i |  | 





### check_all


Enumerate the six-digit numbers and print any winners.  




### signature


Returns the signature of this string.   
Signature is a string that contains all of the letters in order.   
s: string 
#### Parameters
name | description | default
--- | --- | ---
s |  | 





### all_anagrams


Finds all anagrams in a list of words.   
filename: string filename of the word list   
Returns: a map from each word to a list of its anagrams. 
#### Parameters
name | description | default
--- | --- | ---
filename |  | 





### print_anagram_sets


Prints the anagram sets in d.   
d: map from words to list of their anagrams 
#### Parameters
name | description | default
--- | --- | ---
d |  | 





### print_anagram_sets_in_order


Prints the anagram sets in d in decreasing order of size.   
d: map from words to list of their anagrams 
#### Parameters
name | description | default
--- | --- | ---
d |  | 





### filter_length


Select only the words in d that have n letters.   
d: map from word to list of anagrams n: integer number of letters   
returns: new map from word to list of anagrams 
#### Parameters
name | description | default
--- | --- | ---
d |  | 
n |  | 





### main







### main







### main







### walk


Prints the names of all files in dirname and its subdirectories.   
This is the version in the book.   
dirname: string name of directory 
#### Parameters
name | description | default
--- | --- | ---
dirname |  | 





### walk2


Prints the names of all files in dirname and its subdirectories.   
This is the exercise solution, which uses os.walk.   
dirname: string name of directory 
#### Parameters
name | description | default
--- | --- | ---
dirname |  | 





### store_anagrams


Stores the anagrams from a dictionary in a shelf.   
filename: string file name of shelf anagram_map: dictionary that maps strings to list of anagrams 
#### Parameters
name | description | default
--- | --- | ---
filename |  | 
anagram_map |  | 





### read_anagrams


Looks up a word in a shelf and returns a list of its anagrams.   
filename: string file name of shelf word: word to look up 
#### Parameters
name | description | default
--- | --- | ---
filename |  | 
word |  | 





### main



#### Parameters
name | description | default
--- | --- | ---
script |  | 
command |  | "make_db"





### distance_between_points


Computes the distance between two Point objects.   
p1: Point p2: Point   
returns: float 
#### Parameters
name | description | default
--- | --- | ---
p1 |  | 
p2 |  | 





### move_rectangle


Move the Rectangle by modifying its corner object.   
rect: Rectangle object. dx: change in x coordinate (can be negative). dy: change in y coordinate (can be negative). 
#### Parameters
name | description | default
--- | --- | ---
rect |  | 
dx |  | 
dy |  | 





### move_rectangle_copy


Move the Rectangle and return a new Rectangle object.   
rect: Rectangle object. dx: change in x coordinate (can be negative). dy: change in y coordinate (can be negative).   
returns: new Rectangle 
#### Parameters
name | description | default
--- | --- | ---
rect |  | 
dx |  | 
dy |  | 





### main







### main



#### Parameters
name | description | default
--- | --- | ---
script |  | 
filename |  | "emma.txt"
n |  | 100
order |  | 2





### rank_freq


Returns a list of (rank, freq) tuples.   
hist: map from word to frequency   
returns: list of (rank, freq) tuples 
#### Parameters
name | description | default
--- | --- | ---
hist |  | 





### print_ranks


Prints the rank vs. frequency data.   
hist: map from word to frequency 
#### Parameters
name | description | default
--- | --- | ---
hist |  | 





### plot_ranks


Plots frequency vs. rank.   
hist: map from word to frequency scale: string 'linear' or 'log' 
#### Parameters
name | description | default
--- | --- | ---
hist |  | 
scale |  | "log"





### main



#### Parameters
name | description | default
--- | --- | ---
script |  | 
filename |  | "emma.txt"
flag |  | "plot"





### walk


Finds the names of all files in dirname and its subdirectories.   
dirname: string name of directory 
#### Parameters
name | description | default
--- | --- | ---
dirname |  | 





### compute_checksum


Computes the MD5 checksum of the contents of a file.   
filename: string 
#### Parameters
name | description | default
--- | --- | ---
filename |  | 





### check_diff


Computes the difference between the contents of two files.   
name1, name2: string filenames 
#### Parameters
name | description | default
--- | --- | ---
name1 |  | 
name2 |  | 





### pipe


Runs a command in a subprocess.   
cmd: string Unix command   
Returns (res, stat), the output of the subprocess and the exit status. 
#### Parameters
name | description | default
--- | --- | ---
cmd |  | 





### compute_checksums


Computes checksums for all files with the given suffix.   
dirname: string name of directory to search suffix: string suffix to match   
Returns: map from checksum to list of files with that checksum 
#### Parameters
name | description | default
--- | --- | ---
dirname |  | 
suffix |  | 





### check_pairs


Checks whether any in a list of files differs from the others.   
names: list of string filenames 
#### Parameters
name | description | default
--- | --- | ---
names |  | 





### print_duplicates


Checks for duplicate files.   
Reports any files with the same checksum and checks whether they are, in fact, identical.   
d: map from checksum to list of files with that checksum 
#### Parameters
name | description | default
--- | --- | ---
d |  | 





### teleport


Moves the turtle without drawing a line.   
Postcondition: pen is down   
t: Turtle x: coordinate y: coordinate 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
x |  | 
y |  | 





### keypress


Handles the event when a user presses a key.   
Checks if there is a function with the right name; otherwise it prints an error message.   
char: string, letter to draw 
#### Parameters
name | description | default
--- | --- | ---
char |  | 





### carriage_return


Moves to the beginning of the next line.  




### presser


Returns a function object that executes keypress.   
char: character to draw when the function is executed   
returns: function with no arguments 
#### Parameters
name | description | default
--- | --- | ---
char |  | 





### sed


Reads a source file and writes the destination file.   
In each line, replaces pattern with replace.   
pattern: string replace: string source: string filename dest: string filename 
#### Parameters
name | description | default
--- | --- | ---
pattern |  | 
replace |  | 
source |  | 
dest |  | 





### main







### square


Draws a square with sides of the given length.   
Returns the Turtle to the starting position and location. 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
length |  | 





### polyline


Draws n line segments.   
t: Turtle object n: number of line segments length: length of each segment angle: degrees between segments 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
length |  | 
angle |  | 





### polygon


Draws a polygon with n sides.   
t: Turtle n: number of sides length: length of each side. 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
n |  | 
length |  | 





### arc


Draws an arc with the given radius and angle.   
t: Turtle r: radius angle: angle subtended by the arc, in degrees 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
r |  | 
angle |  | 





### circle


Draws a circle with the given radius.   
t: Turtle r: radius 
#### Parameters
name | description | default
--- | --- | ---
t |  | 
r |  | 





### pipe


Runs a command in a subprocess.   
cmd: string Unix command   
Returns (res, stat), the output of the subprocess and the exit status. 
#### Parameters
name | description | default
--- | --- | ---
cmd |  | 





### invert_dict


Inverts a dictionary, returning a map from val to a list of keys.   
If the mapping key->val appears in d, then in the new dictionary val maps to a list that includes key.   
d: dict   
Returns: dict 
#### Parameters
name | description | default
--- | --- | ---
d |  | 





### process_file


Makes a histogram that contains the words from a file.   
filename: string skip_header: boolean, whether to skip the Gutenberg header   
returns: map from each word to the number of times it appears. 
#### Parameters
name | description | default
--- | --- | ---
filename |  | 
skip_header |  | 





### skip_gutenberg_header


Reads from fp until it finds the line that ends the header.   
fp: open file object 
#### Parameters
name | description | default
--- | --- | ---
fp |  | 





### process_line


Adds the words in the line to the histogram.   
Modifies hist.   
line: string hist: histogram (map from word to frequency) 
#### Parameters
name | description | default
--- | --- | ---
line |  | 
hist |  | 





### most_common


Makes a list of word-freq pairs in descending order of frequency.   
hist: map from word to frequency   
returns: list of (frequency, word) pairs 
#### Parameters
name | description | default
--- | --- | ---
hist |  | 





### print_most_common


Prints the most commons words in a histgram and their frequencies.   
hist: histogram (map from word to frequency) num: number of words to print 
#### Parameters
name | description | default
--- | --- | ---
hist |  | 
num |  | 10





### subtract


Returns a dictionary with all keys that appear in d1 but not d2.   
d1, d2: dictionaries 
#### Parameters
name | description | default
--- | --- | ---
d1 |  | 
d2 |  | 





### total_words


Returns the total of the frequencies in a histogram. 
#### Parameters
name | description | default
--- | --- | ---
hist |  | 





### different_words


Returns the number of different words in a histogram. 
#### Parameters
name | description | default
--- | --- | ---
hist |  | 





### random_word


Chooses a random word from a histogram.   
The probability of each word is proportional to its frequency. 
#### Parameters
name | description | default
--- | --- | ---
hist |  | 





### main







### getOutBoundURLs



#### Parameters
name | description | default
--- | --- | ---
a_tags |  | 





### generateBanner



#### Parameters
name | description | default
--- | --- | ---
url |  | 
anchorCount |  | 
linkCount |  | 





### printURLs



#### Parameters
name | description | default
--- | --- | ---
url |  | 
anchors |  | 
f |  | None





### getOutBoundURLs2



#### Parameters
name | description | default
--- | --- | ---
anchors |  | 





### getOutBoundHttpURLs



#### Parameters
name | description | default
--- | --- | ---
alist |  | 





### qsort



#### Parameters
name | description | default
--- | --- | ---
array |  | 





### qsort



#### Parameters
name | description | default
--- | --- | ---
L |  | 





### getOutBoundURLs


http://www.w3.org/TR/html5/text-level-semantics.html#the-a-element   
anchors contains all <a> tag elements from the HTML content. Iterate through the list of anchors and build list containing the href addresses whenever it is available 
#### Parameters
name | description | default
--- | --- | ---
anchors |  | 





### getOutBoundHttpURLs



#### Parameters
name | description | default
--- | --- | ---
alist |  | 





### generateBanner



#### Parameters
name | description | default
--- | --- | ---
url |  | 
anchorCount |  | 
outBoundCount |  | 
linkCount |  | 





### printURLs


Print only those addresses that start with 'https' from valid anchors if 'f'ilename is valid, write extracted URLs to file as well 
#### Parameters
name | description | default
--- | --- | ---
url |  | 
anchors |  | 
f |  | None





### get_addresses



#### Parameters
name | description | default
--- | --- | ---
anchors |  | 





### printURLs



#### Parameters
name | description | default
--- | --- | ---
url |  | 
anchors |  | 
f |  | None





### googleSearch



#### Parameters
name | description | default
--- | --- | ---
query |  | 





### googlesearch



#### Parameters
name | description | default
--- | --- | ---
searchfor |  | 





### test_random_lists


Generates 20 lists of random sizes within the range -5, 10, inclusive. Modify these as per your choice 




### test_random_lists


Generates 20 lists of random sizes within the range - 5, 10, inclusive.Modify these as per your choice 




### missing_plane



#### Parameters
name | description | default
--- | --- | ---
alist |  | 





### mergesort



#### Parameters
name | description | default
--- | --- | ---
alist |  | 
verbose |  | False





### mergesort2



#### Parameters
name | description | default
--- | --- | ---
w |  | 





### test_life_the_universe_and_everything


a simple example to start you off 




### calculateGrade



#### Parameters
name | description | default
--- | --- | ---
score |  | 
gradeChart |  | 





### classAverage



#### Parameters
name | description | default
--- | --- | ---
scores |  | 
gc |  | 





### mergesort



#### Parameters
name | description | default
--- | --- | ---
series |  | 





### calculateGrade



#### Parameters
name | description | default
--- | --- | ---
score |  | 
gradeChart |  | 





### classAverage



#### Parameters
name | description | default
--- | --- | ---
scores |  | 
gc |  | 





### printlist



#### Parameters
name | description | default
--- | --- | ---
alist |  | 




