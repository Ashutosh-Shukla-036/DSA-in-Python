#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

#first method brute force

def Rotate(arr,k):
    n = len(arr)
    k = k % n
    temp = []

    for i in range(n-k,n):
        temp.append(arr[i])

    for i in range(n-k-1,-1,-1):
        arr[i+k] = arr[i]

    for i in range(k):
        arr[i] = temp[i]

nums = [1, 2, 3, 4, 5, 6, 7]
Rotate(nums, 3)
print(nums)  # Output should be [5, 6, 7, 1, 2, 3, 4]

#optimal solution

def RotateArray(arr,k):
    n = len(arr)
    k = k % n

    def reverse(arr,start,end):
        while(start < end):
            arr[start] , arr[end] = arr[end] , arr[start]
            start += 1
            end -= 1

    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)

nums = [1, 2, 3, 4, 5, 6, 7]
RotateArray(nums, 3)
print(nums)