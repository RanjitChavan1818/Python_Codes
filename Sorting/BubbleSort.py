#Bubble Sort
#It make multiple passes throughout the list.
#It compare adjacent elements and exchange them if they are not in order
#In every pass largets element place at its sortred location

arr=[54,26,93,17,77,31]
def BuubbleSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(BuubbleSort(arr))

#Time Complexity
#Best,Avg,Worst- O(n^2)
