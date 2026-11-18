#Binary Search
#Array must be sorted before applying binary search.
#Comparing target element with middle element of array.
#If target>middle element then low=mid+1
#otherwise high=mid-1
#if low>high then element not found
arr=[1,2,5,6,10,20]
low=0
high=len(arr)-1
target=20
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        print(mid)
        break
    elif target>arr[mid]:
        low=mid+1
    else:
        high=mid-1

if low>high:
    print("Not found")