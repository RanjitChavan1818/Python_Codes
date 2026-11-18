#Travel Start from 0 index upto desired element found
#Compare each element with target.
#If Element found written index otherwise not found

# arr=[1,2,23,45,21,34,43]
# target=43
# flag=0
# for i in range(len(arr)):
#     if arr[i]==target:
#         flag=1
#         break
# if  flag:
#     print(i)
# else:
#     print("Not found")

def LinearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

arr=[1,2,23,45,21,34,43]
target=44
print(LinearSearch(arr,target))
#Time Complexity
#Best case- O(1)
#Avg and worst- O(n)