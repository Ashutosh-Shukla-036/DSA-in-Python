#finding the peak element in array

"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple
peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly 
greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time
"""

#Brute force time complexity is O(n)
def Peak(nums):
    n = len(nums)
    for i in range(n):
        if((i==0 or nums[i-1]<nums[i]) and (i==n-1 or nums[i] > nums[i+1])):
            return i
nums = [1,2,2,4,5,6,7,8,5,1]
print(Peak(nums))

#optimal solution using binary search time complexity is O(logn)
def PeakElement(nums):
    n = len(nums)
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[n-1] > nums[n-2]:
        return n-1
    
    low , high = 0 , n - 2

    while(low <= high):
        mid = low + (high - low)//2

        if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid-1] < nums[mid] :
            low = mid + 1
        else:
            high = mid - 1
    return -1

nums = [1,2,3,4,5,6,7,8,5,1]
print(PeakElement(nums))