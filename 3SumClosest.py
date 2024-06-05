##sum Closest

"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum 
is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
"""

def Sum(arr,target):
    n = len(arr)
    arr.sort()
    closestSum = float('inf')

    for i in range(n-2):
        j = i + 1
        k = n - 1
        while(j < k):
            sum = arr[i] + arr[j] + arr[k]
            if abs(sum - target) < abs(closestSum - target):
                closestSum = sum
            if sum > target:
                k -= 1
            elif sum < target:
                j += 1
            else:
                return sum
    return closestSum

nums = [-1,2,1,-4]
target = 1

print(Sum(nums,target))