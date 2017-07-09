# Quicksort

Among the sorting algorithms, it is the most efficient. It is also not the most easiest to explain especially the recursive in-place version. The best way to understand the code is to single-step through the code through the Python Visualizer \(

http://j.mp/tutorQuickSort\)



## The Code

Find below the code, which is heavily commented so it can be understood better, both by reading and also when stepping through the visualizer.

\`\`\`python

 def swap\(arr,x,y\):

 mem = arr\[x\]

 arr\[x\] = arr\[y\]

 arr\[y\] = mem

 return arr

 def qsort\(ar,start,end\):

 \# base case

 if end-start 

&lt;

= 0:

 return ar

 \# pivot

 pivot = ar\[end\]

 \# init index for the next pivot

 \# which is used in the next rec calls in \#27, \#29

 ind = start

 \# loop less final value \(pivot\)

 for i in range\(start,end\):

 elem = ar\[i\]

 if elem 

&lt;

= pivot:

 \# move lesser elements to the left side

 ar = swap\(ar,i,ind\)

 ind += 1

 else:

 \# leave greater elements as-is

 pass

 swap\(ar,ind,end\) \# swap in the pivot element

 print\(ar\)

 \# left side contains pivot, and lesser elements

 ar = qsort\(ar,start,ind-1\)

 \# right side contain greater elements than pivot

 ar = qsort\(ar,ind+1,end\)

 return ar

 n = int\(input\(\)\)

 ar = \[int\(x\) for x in input\(\).split\(\)\]

 qsort\(ar,0,n-1\)

\`\`\`

  




## The Screenshots



