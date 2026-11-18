#Quick Sort
#It follow divide and conquer Technique
#1 Pick first element as pivot element
#2 Take two pointers as i & j set i=0, j=len(aize)-1
#3 Inc value of i until it find greater than pivot, dec value of j until it find value smaller than or equal to pivot element.
#4 If i<j , swap value at i and j
#5 if i>j , swap pivot element with value at j
#6 Repeat the step recursively until the list is sorted.

def partition(arr,low,high):
    i=low
    j=high
    pivot=arr[low]
    while True:
        while i<=high and arr[i]<=pivot:
            i+=1
        while arr[j]>pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j



def quickSort(arr,low,high):
    if low<high:
        j=partition(arr,low,high) #j-->Pivot index
        quickSort(arr,low,j-1)
        quickSort(arr,j+1,high)


arr=[1,34,23,20,15,5]
print("Original Array:",arr)
quickSort(arr,0,len(arr)-1)
print("Array After Sorting:",arr)

#Time Complexity
# Best Case,Avg Case-1 O(n logn)
# Worst case- O(n^2)