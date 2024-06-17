#Koko eat's bananas

"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone
and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k 
bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more
bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
"""

import math

#Using brute force : linear search . Time complexity is O(n*m)
def Count(nums,hours):
    totalHours = 0
    for i in range(0,len(nums)):
        totalHours += math.ceil(nums[i]/hours)
    return totalHours

def MinSpeed(nums,hour):
    n = len(nums)
    for i in range(1,max(nums)+1):
        reqTime = Count(nums,i)
        if reqTime <= hour:
            return i
        
piles = [30,11,23,4,20]
h = 5
print(MinSpeed(piles,h))

#Optimal solution using binary serach . Time complexity is O(nlogm)
def MinCount(nums,h):
    totalHours = 0
    for i in range(len(nums)):
        totalHours += math.ceil(nums[i]/h)
    return totalHours

def MinEatingSpeed(piles,h):
    low , high = 0 , max(piles)
    ans = high

    while low <= high:
        mid = (low+high)//2
        result = MinCount(piles,mid)

        if result <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

piles = [30,11,23,4,20]
h = 5
print(MinEatingSpeed(piles,h))
