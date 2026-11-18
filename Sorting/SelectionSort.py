#Selection Sort
# It improves bubble sort by making only one exchange in each pass.
#In complition of each pass smallest element placed at its proper location.
#It make n-1 passes

def SelectionSort(arr):
    for i in range(len(arr)-1):
        small=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[small]:
                small=j
        arr[i],arr[small]=arr[small],arr[i]
    return arr
arr=[10,5,6,52,67,7]
print(SelectionSort(arr))

#Time Complexity
#Best,Avg,Worst- O(n^2)
