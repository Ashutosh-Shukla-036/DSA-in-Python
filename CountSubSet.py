"""
Given an array arr of size n of non-negative integers and an integer sum, the task is to count all subsets of 
the given array with a sum equal to a given sum.

Example:
Input: 
n = 6, arr = [5, 2, 3, 10, 6, 8], sum = 10
Output: 
3
Explanation: 
{5, 2, 3}, {2, 8}, {10} are possible subsets.
"""

from typing import List
def CountSubSet(index: int, nums: List[int], target: int, n: int, Sum: int) -> int:
    if index == n:
        if Sum == target:
            return 1
        else:
            return 0
    #taken
    Sum += nums[index]
    Left = CountSubSet(index+1,nums,target,n,Sum)

    #not taken
    Sum -= nums[index]
    Right = CountSubSet(index+1,nums,target,n,Sum)

    return Left + Right

n = 6
arr = [5, 2, 3, 10, 6, 8]
sum = 10

print(CountSubSet(0,arr,sum,n,0))