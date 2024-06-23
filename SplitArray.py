#Split Array Largest Sum
"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum 
of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.
"""

def SplitArray(nums,k):
    low , high = 1 , sum(nums)

    def CanSplit(nums,maxSum,m):
        Splits , CurrentSum = 1 , 0
        for i in range(len(nums)):
            if CurrentSum + nums[i] > maxSum:
                Splits += 1
                CurrentSum = nums[i]
                if Splits > m:
                    return False
            else:
                CurrentSum += nums[i]
        return True

    while low <= high:
        mid = low + (high - low)//2

        if CanSplit(nums,mid,k):
            high = mid - 1
        else:
            low = mid + 1
    return low

nums = [7,2,5,10,8]
k = 2
print(SplitArray(nums,k))

#Time Completity O(Nlog(Sum(nums)))