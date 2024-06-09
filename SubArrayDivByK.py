#SubArray Sum Divisible by K
"""
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""

def SubArray(nums,k):
    n = len(nums)
    count = 0
    prefixSum = 0
    hashmap = {0:1}

    for i in range(n):
        prefixSum += nums[i]
        rem = prefixSum % k

        if rem < 0:
            rem += k

        if rem in hashmap:
            count += hashmap[rem]
            hashmap[rem] += 1
        else:
            hashmap[rem] = 1
    return count

nums = [4,5,0,-2,-3,1]
k = 5
print(SubArray(nums,k)) 