# def BubbleSort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-1-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr

# print(BubbleSort([10,7,22,15,40,60,5]))



def SelectionSort(arr):
    for i in range(len(arr)-1):
        small=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[small]:
                small=j
        arr[i],arr[small]=arr[small],arr[i]
    return arr

print(SelectionSort([10,7,22,15,40,60,5]))

