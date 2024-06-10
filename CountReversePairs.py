#Reverse Pairs

"""
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:
1)0 <= i < j < nums.length and
2)nums[i] > 2 * nums[j].
"""

def Merge(arr,low,mid,high):
    left = low
    right = mid+1
    temp =[]

    while(left <= mid and right <= high):
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while(left <= mid):
        temp.append(arr[left])
        left += 1
    while(right <= high):
        temp.append(arr[right])
        right += 1
    for i in range(low , high+1):
        arr[i] = temp[i-low]

def countMerge(arr,low,mid,high):
    count = 0
    right = mid + 1

    for i in range(low,mid+1):
        while(right <= high and arr[i] > 2 * arr[right]):
            right += 1
        count += (right - (mid+1))
    return count

def MergeSort(arr,low,high):
    count = 0
    if low >= high:
        return count
    mid = (low+high)//2
    count += MergeSort(arr,low,mid)
    count += MergeSort(arr,mid+1,high)
    count += countMerge(arr,low,mid,high)
    Merge(arr,low,mid,high)
    return count

nums = [40,20,2,6,10,25]
print(MergeSort(nums,0,len(nums)-1))
print(nums)