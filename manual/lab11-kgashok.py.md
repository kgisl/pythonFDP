

# Lab 11: Programs that take command line arguments

Write a Python program that does counting of words and sentences in a file. The program should accept multiple file names when it is invoked and duely process them. 

## Examples 

`wordcount("python"`) -> `1 # 1 word and no sentences `
`wordcount("python is great language")` ->  `4 # 4 words and no sentences`
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
	- The total lines in all the files to be calculated and displayed 
	- If the filename with the specified command line argument is not available, print **"Final not available**." 
    - If there are other exceptions, catch them as well and print **"Unknown error!"**

## Bonus
Make your program to behave as close as possible to the Unix command [`wc`](https://en.wikipedia.org/wiki/Wc_(Unix)). See the most important examples at https://www.tecmint.com/wc-command-examples/

	- For example, `wc -l file.txt` ->  `112` (if there are 112 lines) 


## CD Links

