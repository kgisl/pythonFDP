# Unit 5
## FILES, MODULES, PACKAGES

A file is a container in a computer system for storing information. Files used in computers are similar in features to that of paper documents used in library and office files. In a computer operating system, files can be stored on optical drives, hard drives or other types of storage devices.

### Types of Files

* Text files
* Data files
* Directory files
* Binary files
* Graphic files

### Basic File Operations

1. Creation of a new file
2. Modification of data or file attributes
3. Reading of data from the file
4. Opening the file in order to make the contents available to other programs
5. Writing data to the file
6. Closing or terminating a file operation

## How to read a file in python
*Code example*
```python
datafile = open("data.txt","r");
data = datafile.read();
print(data)
```
*File contents*
```file
Apple Orange Mango
```
*Output*
```console
Datafile Contents: Apple Orange Mango
```