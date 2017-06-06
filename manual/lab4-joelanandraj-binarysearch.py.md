def Bsearch(lst,searchElement):
    lst.sort()
    length=len(lst)
    left=0
    right=length-1  
   
    if length==0:
        return "The list is Empty"  
 
 
    while(left<=right):
        middle=round((left+right)/2)
 
        if searchElement==lst[middle]:
            return "The Element is found in the position "+str(middle)
        elif searchElement<lst[middle]:
            right=middle-1
        elif searchElement>lst[middle]:
            left=middle+1
    
    return "The Element is not present in the list"
 
