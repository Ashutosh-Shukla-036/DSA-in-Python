#Replace Element in Array.
"""
You are given a 0-indexed array nums that consists of n distinct positive integers. Apply m operations to this
 array, where in the ith operation you replace the number operations[i][0] with operations[i][1].

It is guaranteed that in the ith operation:
1)operations[i][0] exists in nums.
2)operations[i][1] does not exist in nums.

Return the array obtained after applying all the operations.

Example 1:
Input: nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]
Output: [3,2,7,1]
Explanation: We perform the following operations on nums:
- Replace the number 1 with 3. nums becomes [3,2,4,6].
- Replace the number 4 with 7. nums becomes [3,2,7,6].
- Replace the number 6 with 1. nums becomes [3,2,7,1].
We return the final array [3,2,7,1].
"""

def ReplaceElement(nums,operation):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i in range(len(operation)):
        old , new = operation[i][0] , operation[i][1]
    
        index = hashmap.pop(old)
        nums[index] = new
        hashmap[new] = index

    return nums

nums = [1,2,4,6]
operations = [[1,3],[4,7],[6,1]]

print(ReplaceElement(nums,operations))