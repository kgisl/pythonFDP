# Unit 5 
## FILES, MODULES, PACKAGES
### Object
*Files and exception: text files, reading and writing files, format operator; command line arguments, errors and exceptions, handling exceptions, modules, packages; Illustrative programs: word count, copy file.*

# Key Terms
-   **File**  : A file is a container in a computer system for storing information. Files used in computers are similar in features to that of paper documents used in library and office files. In a computer operating system, files can be stored on optical drives, hard drives or other types of storage devices.
-   **Binary file**  : Binary file is a collection of bytes or a character stream. The data that is written into and read from binary file remain unchanged, with no separation between lines and no use of end-of-line characters and the interpretation of the file is left to the programmer.
-   **Text file**  : A text file is a stream of characters that can be processed sequentially and logically in the forward direction. The maximum number of characters in each line is limited to 255 characters.
-   **Sequential file access**: In case of sequential file access, data is read from or written to a file in a sequential manner while the  `position indicator`  automatically gets adjusted by the stream I/O functions.
-   **Random file access**: Random access means reading from or writing to any position in a file without reading or writing all the preceding data by controlling the  `position indicator`
-   **Record**: A record consist of a collection of data fields that conforms to a previously defined structure that can be stored on or retrieved from a file.
-   **Stream**: The stream is a common, logical interface to the various devices that comprise the computer and is a logical interface to a file. Although files differ in form and capabilities, all streams are the same.
-   **File management**: It basically means all operations related to creating, renaming, deleting, merging, reading, writing, etc. of any type of files.
-   **Path**: The path specifies the drive and/or directory (or folder) where the file is located. On PCs, the backslash character is used to separate directory names in a path. Some systems like Unix use the forward slash (/) as the directory separator.

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
fileToRead = open("source.txt","r")
data = fileToRead.read()
print("Source contents:",data)
```
*File contents*
```file
Apple Orange Mango
```
*Output*
```console
Source contents: Apple Orange Mango
```

![](https://github.com/rajasekaranap/pythonFDP/blob/master/img/fileintro.JPG)

Demo
[https://repl.it/@kiteit/ReadFromFile](https://repl.it/@kiteit/ReadFromFile)

### Types of File Modes

File Mode | Description |
|:---:|--- |
| `r` | Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode. |
| `rb` | Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode. |
|`r+` | Opens a file for both reading and writing. The file pointer placed at the beginning of the file. |
`rb+`|Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.|
`w`|Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.|
`wb`|Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.|
`w+`|Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.|
`wb+`|Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.|
`a`|Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.|
`ab`|Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.|
`a+`|Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.|
`ab+`|Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.|

### File Methods
|File Methods|Description|Prototype|
|------------|-----------|---------|
|close()	 |Closes the file|``` fileobject.close()```|
|flush()	 |Flushes the internal buffer|``` fileobject.flush()```|
|read()	     |Returns the file content|``` data = fileobject.read()```|
|readable()	 |Returns whether the file stream can be read or not|```boolean = fileobject.flush()```|
|readline()	 |Returns one line from the file|``` data = fileobject.readline()```|
|readlines() |Returns a list of lines from the file|``` filelines = fileobject.read()```|
|seek()	     |Change the file position|``` filelines = fileobject.seek(offset)```|
|seekable()	 |Returns whether the file allows us to change the file position|``` bool = fileobject.seekable()```|
|tell()	     |Returns the current file position|``` position = fileobject.tell()```|
|truncate()	 |Resizes the file to a specified size|``` fileobject.truncate(size)```|
|writeable() |Returns whether the file can be written to or not|```bool = fileobject.writeable()```|
|write()	 |Writes the specified string to the file|``` fileobject.write(data)```|
|writelines()|Writes a list of strings to the file|``` fileobject.writelines(listofstrings[])```|

# File Writing
### code
```python
fileToWrite = open("destination.txt","w")
data = "Hello Python";
fileToWrite.write(data)
fileToWrite.close();
print("done with file writing")
```
### output
```console
done with file writing
```
### destination
|Before Writing|After Writing |
|--|--|
|![](https://github.com/rajasekaranap/pythonFDP/blob/master/img/bfw.JPG)|![](https://github.com/rajasekaranap/pythonFDP/blob/master/img/afw.JPG)|
Demo
[https://repl.it/@kiteit/WritingToFile](https://repl.it/@kiteit/WritingToFile)

**Difference between Append and Write Mode**

Write (w) mode and Append (a) mode, while opening a file are almost the same. Both are used to write in a file. In both the modes, new file is created if it doesn’t exists already.

The only difference they have is, when you open a file in the write mode, the file is reset, resulting in deletion of any data already present in the file. While in append mode this will not happen. Append mode is used to append or add data to the existing data of file (if any). Hence, when you open a file in Append(a) mode, the cursor is positioned at the end of the present data in the file.

## Reading binary files in python
*Code example*
```python
binfile = open("bindata.PNG","rb")
data = binfile.read()
print("source contents:",data)
```
*File contents*
![](https://github.com/rajasekaranap/pythonFDP/blob/master/img/pythonlogo.jpg)
*Output*
```console
Source contents:b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00C\x00\x06\x04\x05\x06\x05\x04\x06\x
06\x05\x06\x07\x07\x06\x08\n\x10\n\n\t\t\n\x14\x0e\x0f\x0c\x10\x17\x14\x18\x18\x17\x14\x16\x16\x1a\x1d%\x1f\x1a\x1b#\x1c\x16\x16 , #&\
')*)\x19\x1f-0-(0%()(\xff\xdb\x00C\x01\x07\x07\x07\n\x08\n\x13\n\n\x13(\x1a\x16\x1a((((((((((((((((((((((((((((((((((((((((((((((((((\
xff\xc2\x00\x11\x08\x03\x00\x03\x00\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1b\x00\x01\x00\x02\x03\x01\x01\x00\x00\x00\x00\x
00\x00\x00\x00\x00\x00\x00\x01\x04\x02\x03\x05\x06\x07\xff\xc4\x00\x1a\x01\x01\x00\x03\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x01\x02\x03\x04\x05\x06\xff\xda\x00\x0c\x03\x01\x00\x02\x10\x03\x10\x00\x00\x01\xfa\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x009>n\xd5\xf7X\xfc\x9f\x89z}
```

![](https://github.com/rajasekaranap/pythonFDP/blob/master/img/fileintro.JPG)

Demo
[https://repl.it/@kiteit/BinaryFile](https://repl.it/@kiteit/BinaryFile)

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAwNjAwODcxMCwtNjI0ODkxMjQyLC00Nz
E1NDgxNzcsNTcwNDQ4NzM1LDEyMDk2NDQ3NDIsLTE3NzMyMDI3
MjIsLTcwNzI5MDEyLC02NjU5NDg0NCwxMTk3MzAwNzcyLC0xOD
M2OTExNjAyLDE2NjMyOTAxMjgsLTc1NTQyOTQ0MywtMTUyODA3
MTE5MCwtNzU1NDI5NDQzLC0yMDcwOTY2NTU0LC00MTg5ODAwOT
JdfQ==
-->