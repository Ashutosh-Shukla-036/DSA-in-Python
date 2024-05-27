#Given an integer array nums, find the SUbArray with the largest sum, and return its sum

def SubArray(arr):
    hashmap = {}
    n = len(arr)

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]

            if sum in hashmap:
                hashmap[sum] += 1
            else:
                hashmap[sum] = 1

    return max(hashmap)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(SubArray(nums))

import sys
def MaxSubArray(arr):
    maxi = -sys.maxsize - 1
    sum = 0
    start = 0
    ansStart , ansEnd = 0,0

    for i in range(len(arr)):
            
        sum += arr[i]

        if sum > maxi:
            maxi = sum

            ansStart = start
            ansEnd = i

        if sum < 0:
            sum = 0
            start = i+1
    print("maximum sum is:",maxi)
    print("SubArray is [",end=" ")
    for i in range(ansStart,ansEnd+1):
        print(arr[i],end=" ")
    print("]")


nums = [-2,1,-3,4,-1,2,1,-5,4]
MaxSubArray(nums)     