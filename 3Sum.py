##Sum
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
 and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
#brute force
def ThreeSum(arr):
    n = len(arr)
    result = set()

    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i] + arr[j] + arr[k] == 0:
                    List = [arr[i],arr[j],arr[k]]
                    List.sort()
                    result.add(tuple(List))

    return [list(triplet) for triplet in result]

nums = [-1,0,1,2,-1,-4]
print(ThreeSum(nums)) #Time complexity is O(n*n*n) 

#Better solution using Hashing
def Three_Sum(arr):
    n = len(arr)
    result = set()

    for i in range(n):
        hashmap = {}
        for j in range(i+1,n):
            k = -(arr[i]+arr[j])
            if k in hashmap:
                List = sorted([arr[i],arr[j],k])
                result.add(tuple(List))
            else:
                hashmap[arr[j]] = 1
    
    return [list(triplet) for triplet in result]


nums = [-1,0,1,2,-1,-4]
print(Three_Sum(nums))#Time complexity is O(n*n) but extra space of hashmap and set

#Optimal solution using two pointer
def Sum(arr):
    n = len(arr)
    result = []
    arr.sort()
    for i in range(n):
        if (i>0 and arr[i] == arr[i-1]):
            continue
        j = i+1
        k = n-1

        while(j<k):
            sum = arr[i] + arr[j] + arr[k]

            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                temp = [arr[i],arr[j],arr[k]]
                result.append(temp)
                j += 1
                k -= 1
                while(j<k and arr[j] == arr[j-1]):
                    j += 1
                while(j<k and arr[k] == arr[k+1]):
                    k -= 1
    return result

nums = [1,-1,-1,0]
print(Sum(nums))#Time complexity is O(nlogn) + O(n*n)