#Given an integer array nums, find the SUbArray with the largest sum, and return its sum

def SubArray(arr):
    hashmap = {}
    n = len(arr)

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]

            if sum in hashmap:
                hashmap[sum] += 1
            else:
                hashmap[sum] = 1

    return max(hashmap)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(SubArray(nums))