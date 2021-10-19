# Lab 11: Programs that take command line arguments

Write a Python program that does counting of words and sentences in a file. The program should accept multiple file names when it is invoked and duely process them.

## Examples

`wordcount("python"`) -> `1 # 1 word and no sentences `  
`wordcount("python is great language")` -> `4 # 4 words and no sentences`  
`wordcount("Sentence 1. Sentence 2.")` -> `(4, 2) # 4 words and 2 sentences`

## Solution Key

```python
def wordcount(input, sentence=False):

    delimit = " "
    numwords = len(input.strip().split())

    if sentence:
        delimit = "."
        tokens  = input.strip().split(delimit)
        numsentences = len([t for t in tokens if len(t) != 0])
        return (numwords, numsentences)

    return numwords


if __name__ == '__main__':
    import sys
    total = 0
    for arg in sys.argv[1:]:
        print (arg, end=", ")
        try:
            f = open(arg, 'r')
            text = f.read()
            print(wordcount(text, sentence=True))
            f.close()
        except:
            print("File not available!")

```

## Pre-Lab Questions

## Post-Lab Questions

1. Modify the version (make suitable changes to `wordcount.py file`) available in http://cyberdojo1.kgfsl.com/enter/show/3080E868E6 so that

   - The total sentences in all the files to be calculated and displayed
   - If the filename with the specified command line argument is not available, print **"File not available**." by using the appropriate named exception.
   - If there are other errors, catch them as well and print **"Unknown error!"**

2. Refactor the solution to the Question_1 to use `getopt` and handle the exceptions for handling options flags in an appropriate manner. For example, choose a option flag which can be used to denote which file can be updated with the results of the processing.

3. Provide support for processing adhoc strings through the command line option. For example, when program is invoked with `-s` option,  

   wcount.py -s "This is a sentence. Another one." file1.txt

It must process the string within **quotes** and also the contents within the `file1.txt` file as well.

## Bonus

Make your program to behave as close as possible to the Unix command [`wc`](<https://en.wikipedia.org/wiki/Wc_(Unix)>).

See the most important examples at https://www.tecmint.com/wc-command-examples/

    - For example, `wc -l file.txt` ->  `112` (if there are 112 lines)

## Bonus 2

How to test all the various refactorings that were done as part of the post-lab Questions?

## Related Material

Using [**getopt**](http://www.diveintopython.net/scripts_and_streams/command_line_arguments.html)

Basic command line [**argument handling**](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)

## CD Links
