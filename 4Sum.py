#$ Sum
"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
such that:

1)0 <= a, b, c, d < n
2)a, b, c, and d are distinct.
3)nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
"""

#Brute force
def FourSum(arr,target):
    n = len(arr)
    result = set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if arr[i]+arr[j]+arr[k]+arr[l] == target:
                        List = sorted([arr[i],arr[j],arr[k],arr[l]])
                        result.add(tuple(List))
    return [list(tuplets) for tuplets in result]
nums = [1,0,-1,0,-2,2] 
target = 0
print(FourSum(nums,target))#Time Complexity is O(n*n*n*n)

#Better Solution using hashmap
def Four_Sum(nums,target):
    n = len(nums)
    result = set()

    for i in range(n):
        for j in range(i+1,n):
            hashmap = {}
            for k in range(j+1,n):
                l = target - (nums[i] + nums[j] + nums[k])

                if l in hashmap:
                    List = sorted([nums[i],nums[j],nums[k],l])
                    result.add(tuple(List))
                else:
                    hashmap[nums[k]] = 1
    return [list(tuplets) for tuplets in result]
nums = [1,0,-1,0,-2,2] 
target = 0
print(Four_Sum(nums,target))#Time complexity is O(n*n*n) 

#Optimal solution using pointers
def Sum(nums,target):
    n = len(nums)
    nums.sort()
    result = []

    for i in range(n):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n):
            if j!=i+1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            l = n - 1

            while(k < l):
                sum = nums[i] + nums[j] + nums[k] + nums[l]

                if sum == target:
                    result.append([nums[i],nums[j],nums[k],nums[l]])
                    k = k + 1
                    l = l - 1
                    while(k<l and nums[k] == nums[k-1]):
                        k = k + 1
                    while(k<l and nums[l] == nums[l+1]):
                        l = l - 1
                elif sum > target:
                    l = l - 1
                else:
                    k = k + 1
    return result
nums = [1,0,-1,0,-2,2] 
target = 0
print(Sum(nums,target))