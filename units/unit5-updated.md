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
datafile = open("data.txt","r");
dataFromFile = datafile.read();
print(dataFromFile)
```
*File contents*
```file
Apple Orange Mango
```
*Output*
```console
Datafile Contents: Apple Orange Mango
```

[https://github.com/rajasekaranap/pythonFDP/blob/master/img/fileintro.JPG](https://github.com/rajasekaranap/pythonFDP/blob/master/img/fileintro.JPG)

### Types of File Modes

| S.No | File Mode | Description |
|--- |:---:|--- |
| 1 | `r` | Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode. |
| 2 | `rb` | Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode. |
| 3 | `r+` | Opens a file for both reading and writing. The file pointer placed at the beginning of the file. |
|4|`rb+`|Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.|
|5|`w`|Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.|
|6|`wb`|Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.|
|7|`w+`|Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.|
|8|`wb+`|Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.|
|9|`a`|Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.|
|10|`ab`|Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.|
|11|`a+`|Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.|
|12|`ab+`|Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.|

### File Methods
|S.No|File Methods|Description|Prototype|
|----|------------|-----------|---------|
|1   |close()	 |Closes the file|``` fileobject.close()```|
|4   |flush()	 |Flushes the internal buffer|``` fileobject.flush()```|
|6   |read()	     |Returns the file content|``` data = fileobject.read()```|
|7   |readable()	 |Returns whether the file stream can be read or not|```boolean = fileobject.flush()```|
|8   |readline()	 |Returns one line from the file|``` data = fileobject.readline()```|
|9   |readlines() |Returns a list of lines from the file|``` filelines = fileobject.read()```|
|10  |seek()	     |Change the file position|
|11  |seekable()	 |Returns whether the file allows us to change the file position|
|12  |tell()	     |Returns the current file position|
|13  |truncate()	 |Resizes the file to a specified size|
|14  |writeable() |Returns whether the file can be written to or not|
|15  |write()	 |Writes the specified string to the file|
|16  |writelines()|Writes a list of strings to the file|

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
```
done with file writing
```
### destination
|Before Writing|After Writing |
|--|--|
|![](https://github.com/rajasekaranap/pythonFDP/blob/master/img/bfw.JPG)|![](https://github.com/rajasekaranap/pythonFDP/blob/master/img/afw.JPG)|


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY2NTk0ODQ0LDExOTczMDA3NzIsLTE4Mz
Y5MTE2MDIsMTY2MzI5MDEyOCwtNzU1NDI5NDQzLC0xNTI4MDcx
MTkwLC03NTU0Mjk0NDMsLTIwNzA5NjY1NTQsLTQxODk4MDA5Ml
19
-->