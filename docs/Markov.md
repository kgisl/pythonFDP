# Markov

Encapsulates the statistical summary of a text.

## Methods

### **init**

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |

### process_file

Reads a file and performs Markov analysis.  
filename: string order: integer number of words in the prefix  
Returns: map from prefix to list of possible suffixes.

#### Parameters

| name     | description | default |
| -------- | ----------- | ------- |
| self     |             |
| filename |             |
| order    |             | 2       |

### process_word

Processes each word.  
word: string order: integer  
During the first few iterations, all we do is store up the words; after that we start adding entries to the dictionary.

#### Parameters

| name  | description | default |
| ----- | ----------- | ------- |
| self  |             |
| word  |             |
| order |             | 2       |

### random_text

Generates random wordsfrom the analyzed text.  
Starts with a random prefix from the dictionary.  
n: number of words to generate

#### Parameters

| name | description | default |
| ---- | ----------- | ------- |
| self |             |
| n    |             | 100     |
