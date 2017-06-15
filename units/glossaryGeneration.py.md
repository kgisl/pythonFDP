

### Artoo for Client Side Web Scraping 
http://medialab.github.io/artoo/quick_start/ 

```javascript 

var termlist = artoo.scrape('div#glossary.section dt')
var deflist  = artoo.scrape('div#glossary.section dd')

desired = ['argument', 'attribute', 'binary file', 'BDFL', 'coroutine', 'dictionary', 'dictionary view', 'docstring', 'expression', 'file object', 'function', 'immutable', 'iterable', 'list', 'list comprehension', 'mapping', 'method', 'module', 'mutable', 'package', 'parameter', 'positional argument', 'keyword argument', 'sequence', 'slice', 'special method', 'statement', 'text file', 'triple-quoted string', 'Zen of Python']

var glist = [];

for (var i = 0; i < 133; i++) { 
   if (desired.indexOf(termlist[i]) >=0)
     glist.push({"term": termlist[i], "definition":deflist[i]}); 
}

artoo.savePrettyJson(glist);  // got saved to data.json 
```

### A Python Script for the Markdown

```python 

import json
from pprint import pprint

with open('data.json') as data_file:    
    data = json.load(data_file)

# pprint(data)
for elem in data: 
	print ("##", elem['term'])
	print (elem['definition'])
	print ("\n")
```
