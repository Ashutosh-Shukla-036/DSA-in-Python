#Permutations

"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in 
any order.

Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

#Use Backtracking and a data structure to keep track of all elements to make all possible permutations
def Permutation(nums):
    result = []

    def BackTrack(combination,seen):
        if len(combination) == len(nums):
            result.append(combination[:])
            return
        
        for i in range(len(nums)):
            if nums[i] not in seen:
                combination.append(nums[i])
                seen.append(nums[i])
                BackTrack(combination,seen)
                combination.pop()
                seen.pop()

    BackTrack([],[])
    return result

nums = [1,2,3]
print(Permutation(nums))
#Time complexity is O(n! * n) and space complexity is O(n*n)

#Optimal solution uing swap method to reduce extra space complexity , time complexity is same.
def Permute(nums):
    result = []
    
    def BackTrack(index,nums):
        if index == len(nums):
            result.append(nums[:])
            return
        
        for i in range(index,len(nums)):
            nums[index] , nums[i] = nums[i] , nums[index]
            BackTrack(index+1,nums)
            nums[index] , nums[i] = nums[i] , nums[index]

    BackTrack(0,nums)
    return result

nums = [1,2,3]
print(Permute(nums))