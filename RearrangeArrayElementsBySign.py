""""You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the the array follows the given conditions:

1)Every consecutive pair of integers have opposite signs.
2)For all integers with the same sign, the order in which they were present in nums is preserved.
3)The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions."""

def Array(nums):
    pos = []
    neg = []

    for i in range(len(nums)):
        if(nums[i] > 0):
            pos.append(nums[i])
        else:
            neg.append(nums[i])

    for i in range(len(pos)):
        nums[2*i] = pos[i]
    for i in range(len(neg)):
        nums[2*i+1] = neg[i]

    return nums

nums = [1,4,5,-2,3,-2,-9,5,-1,-8]
print(Array(nums))