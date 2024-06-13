#Find the first and last position of element in sorted array.

"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a
given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
#Optimal solution using Binary Serach.
def SearchArray(nums,target):
    def SerachFirst(nums,target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = -1
        while low <= high :
            mid = (low + high) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    ans = mid
                    break
                else:
                    high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def SerachLast(nums,target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                if mid == n - 1 or nums[mid+1] != target:
                    ans = mid
                    break
                else:
                    low = mid + 1
            elif nums[mid] > target:
                high  = mid - 1
            else:
                low = mid + 1
        return ans
    
    start = SerachFirst(nums,target)
    end = SerachLast(nums,target)
    return [start,end]

nums = [5,7,7,8,8,10]
print(SearchArray(nums,6))