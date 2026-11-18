#List is divided into two parts, i.e sorted and unsorted.
#It takes the elements from unsorted list one by one and inserted them into sorted list at its proper location.
#It always consist n-1 passes.

arr=[11,45,21,66,7,25]
def InsertionSort(arr):
    for i in range(1,len(arr)):
        sorted=arr[i]
        j=i-1

        while j>=0 and arr[j]>sorted:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=sorted
    return arr
print(InsertionSort(arr))

#Time Complexity
#Best case- O(n)
#Avg, Worst- O(n^2)
