""""Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of 
the same color are adjacent, with the colors in the order red, white, and blue.We will use the integers 
0, 1, and 2 to represent the color red, white, and blue, respectively.You must solve this problem without
using the library's sort function."""

#Brute force to use merge sort or Quick sort
arr = [0,1,2,0,0,1,0,2,1,1,1,0,2,2,0]
arr.sort()
print(arr)
#Time complexity is O(NlogN) 

#Better solution to use counter variable
def sort(arr):
    count0 = 0
    count1 = 0
    count2 = 0
    n = len(arr)

    for i in range(n):
        if(arr[i] == 0):
            count0 += 1
        elif(arr[i] == 1):
            count1 += 1
        elif(arr[i] == 2):
            count2 +=1

    for i in range(count0):
        arr[i] = 0
    for i in range(count0,count1+count0):
        arr[i] = 1
    for i in range(count0+count1,n):
        arr[i] = 2
    return arr

num = [0,1,2,0,0,1,0,2,1,1,1,0,2,2,0]
print(sort(num))
#Time complexity is O(2N)

#optimal Solution using DNF Algorithm (Dutch National Flag Algorithm)
def SortArray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high :
        if (arr[mid] == 0):
            arr[low] , arr[mid] = arr[mid] , arr[low]
            low += 1
            mid += 1
        elif (arr[mid] == 1):
            mid += 1
        elif(arr[mid] == 2):
            arr[mid] , arr[high] = arr[high] , arr[mid]
            high -= 1
    return arr

nums = [0,1,2,0,0,1,0,2,1,1,1,0,2,2,0]
print(SortArray(nums))
#Time complexity is O(N)