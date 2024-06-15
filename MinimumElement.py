#find the Minimum in rotated sorted array. must solve in O(logn) time complexity.

def Minimum(nums):
    low , high = 0 , len(nums) - 1
    ans = float("inf")
    while(low <= high):
        mid = low + (high-low)//2

        if (nums[low] <= nums[mid]):
            if ans > nums[low]:
                ans = nums[low]
            low = mid + 1
        else:
            if ans > nums[mid]:
                ans = nums[mid]
            high = mid - 1
    return ans

nums = [4,5,6,7,0,1,2,3]
print(Minimum(nums))