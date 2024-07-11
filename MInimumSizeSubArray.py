#Minimum Size Subarray Sum
"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""

#Optimal Solution using sliding window
def SubArray(nums,target):
    minLen , Sum = float("inf") , 0
    i , j = 0 , 0

    while j < len(nums):
        Sum += nums[j]
        while Sum >= target:
            CurrentLen = j - i + 1
            if CurrentLen < minLen:
                minLen = CurrentLen 
            Sum -= nums[i]
            i += 1
        j += 1
    
    if minLen == float("inf"):
        return 0
    return minLen

nums = [2,3,1,2,4,3]
target = 7
print(SubArray(nums,target))