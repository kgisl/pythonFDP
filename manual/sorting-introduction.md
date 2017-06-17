# Sorting



## A Visualization is worth a 1000 tables 

http://j.mp/mergeVsQuick

## A Table is Worth a 1000 pictures





**"A picture is worth a 1000 words."** The pictures help convey the contrasting dynamics that occur between the four sorts that need to covered in the lab.

\[TOC\]

## Modified Bubble Sort Approach

* Typically `O(n**2)` and therefore good only for small data sets. 
* Most likely they are **stable** sorts - meaning they maintain the order in which equal elements appear in the list 
* [http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html)
* [http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html)

### Selection Sort

![selection](https://cdn.rawgit.com/kgisl/pythonFDP/67362bd2/img/selectionsortnew.png)

### Insertion Sort

![insertion](https://cdn.rawgit.com/kgisl/pythonFDP/67362bd2/img/insertionsort.png)

## Divide and Conquer Approach

* Typically `O(n*logn)` and therefore suitably for bigger data sets. 
* As in the case of Merge Sort, it requires additional space \(so for real large sets, this can be a disadvantage\). For Quick Sort, additional `nlog(n)` space is required. 
* Typically,  as in the case of Quick Sort, they are also not **stable** sorts - the order of equal elements may not be maintained after the sort is complete 
* [http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html)
* [http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html)

### Merge Sort

![Merge](https://cdn.rawgit.com/kgisl/pythonFDP/b3dcfbb1/img/merge-sort.png)

![mergeA](https://cdn.rawgit.com/kgisl/pythonFDP/67362bd2/img/mergesortA.png)  
![mergeB](https://cdn.rawgit.com/kgisl/pythonFDP/67362bd2/img/mergesortB.png)

### Quick Sort

![split](https://cdn.rawgit.com/kgisl/pythonFDP/67362bd2/img/firstsplit.png)

![partition1](https://cdn.rawgit.com/kgisl/pythonFDP/67362bd2/img/partitionA.png)

![partition2](https://cdn.rawgit.com/kgisl/pythonFDP/67362bd2/img/partitionB.png)

## Clarifying Questions

1. Which of the following sort algorithms are guaranteed to be O\(n log n\) even in the worst case?

2. \(A\) Selection Sort

3. \(B\) Quick Sort  
4. \(C\) Merge Sort  
5. \(D\) Insertion Sort

6. Which takes the least amount of extra space for sorting to happen? Which takes the most amount of extra space?

7. A.  Selection Sort, Merge Sort

8. B. Insertion Sort, Quick Sort  
9. C. Insertion Sort, Merge Sort  
10. D. None of the above combinations  

1. What is the correct order in terms of _**increased**_ efficiency of sorting?

2. A. Selection, Insertion, Quick and Merge

3. B. Insertion, Selection, Merge and Quick  
4. C. Selection, Insertion, Merge and Quick  
5. D. None of the above  



