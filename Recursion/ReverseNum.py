def Reverse(arr,left,right):
    if left>=right:
        return arr
    arr[left],arr[right]=arr[right],arr[left]
    return Reverse(arr,left+1,right-1)
arr=[5,7,3,2,6,1,5,9]
print(Reverse(arr,2,5))