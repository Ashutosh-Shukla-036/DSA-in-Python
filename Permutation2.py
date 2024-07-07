#Permutation II

"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in 
any order.

Example:
Input: nums = [1,1,2]
Output:
[[1,1,2],[1,2,1],[2,1,1]]
"""

#Use Set data structure to store unique combination
def Permutation(nums):
    result = set()

    def BackTrack(index,nums):
        if index == len(nums):
            result.add(tuple(nums))
            return
        
        for i in range(index,len(nums)):
            nums[index] , nums[i] = nums[i] , nums[index]
            BackTrack(index+1,nums)
            nums[index] , nums[i] = nums[i] , nums[index]

    BackTrack(0,nums)
    return [list(temp) for temp in result]

nums = [1,1,2]
print(Permutation(nums)) 
#Time complexity O(n! * n) and space O(n)

"""We can avoid recursion and backtracking for duplicate permutation by sorting the array and checking for
duplicate elements which reduces the time significantly"""

def Permute(nums):
    result  = []
    nums.sort()
    def BackTrack(index,nums):
        if len(nums) == index:
            result.append(nums[:])
            return
        
        seen = set()

        for i in range(index,len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            nums[index] , nums[i] = nums[i] , nums[index]
            BackTrack(index+1,nums)
            nums[index] , nums[i] = nums[i] , nums[index]

    BackTrack(0,nums)
    return result

nums = [1,1,2]
print(Permute(nums))