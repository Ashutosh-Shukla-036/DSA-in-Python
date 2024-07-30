#Binary SubArrays with Sum
"""
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.
"""

#Brute force by generate all subarrays. Time complexity is O(n*n) and space complexity is O(1)
from typing import List
def SubArray(nums: List, goal: int) -> int:
    count = 0
    for i in range(len(nums)):
        Sum = 0
        for j in range(i,len(nums)):
            Sum += nums[j]
            if Sum == goal:
                count += 1
            if Sum > goal:
                break
    return count 

nums = [1,0,1,0,1,0,0,1]
goal = 2
print(SubArray(nums,goal))

#Better solution using perfix and hashmap . Time complexity is O(n) and space complexity is O(n)
def SubArrays(nums: List, goal: int) -> int:
    count , Sum = 0 , 0
    hashmap = {0:1}

    for i in range(len(nums)):
        Sum += nums[i]
        rem = Sum - goal

        if rem in hashmap:
            count += hashmap[rem]

        if Sum in hashmap:
            hashmap[Sum] += 1
        else:
            hashmap[Sum] = 1
    
    return count

nums = [1,0,1,0,1,0,0,1]
goal = 2
print(SubArrays(nums,goal))

#Optimal solution using two pointers and sliding window . Time complexity is O(2n) and space complexity is O(1)
def SubArrayWithGoal(nums: List, goal: int) -> int:
    def atMost(goal: int) -> int:
        if goal < 0:
            return 0
        count , Sum = 0 , 0
        i = 0

        for j in range(len(nums)):
            Sum += nums[j]
            while Sum > goal:
                Sum -= nums[i]
                i += 1
            count += (j-i+1)

        return count
    return atMost(goal) - atMost(goal-1)

nums = [1,0,1,0,1,0,0,1]
goal = 2
print(SubArrayWithGoal(nums,goal))
