#Search the element in rotated Sorted array. All elements unique. Return index if found else -1.
#Time complexity must be O(logn)


def Serach(nums,target):
    low , high = 0 , len(nums)-1

    while(low <= high):
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1 

nums = [6,7,8,9,0,1,2,3,4,5]
print(Serach(nums,6))