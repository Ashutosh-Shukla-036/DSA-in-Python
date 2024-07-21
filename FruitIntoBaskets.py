#Longest subarray with at most two elements .

#Brute force : Time complexity is O(n*n)
from typing import List
def SubArray(nums: List[int]) -> int:
    n , maxLen = len(nums) , 0
    for i in range(n):
        seen = set()
        for j in range(i,n):
            seen.add(nums[j])
            if len(seen) > 2:
                break
            maxLen = max(maxLen,j-i+1) 
    return maxLen

nums = [3,3,3,1,2,2,1,1,2,1,4,1,2,1,3,4,3,4]
print(SubArray(nums))    

#optimal solution using sliding window and hashmap : time complexity is O(2n)
from typing import List
def SubArrayWithTwoUnique(nums: List[int]) -> int:
    maxLen , hashmap = 0 , {}
    l , r , n = 0 , 0 , len(nums)

    while r < n:
        if nums[r] in hashmap:
            hashmap[nums[r]] += 1
        else:
            hashmap[nums[r]] = 1
        
        while len(hashmap) > 2:
            hashmap[nums[l]] -= 1
            if hashmap[nums[l]] == 0:
                del hashmap[nums[l]]
            l += 1
        
        maxLen = max(maxLen,r-l+1)
        r += 1
    
    return maxLen
nums = [3,3,3,1,2,2,1,1,2,1,4,1,2,1,3,4,3,4]
print(SubArrayWithTwoUnique(nums))  