def SubArray(arr,k):
    sum = 0
    maxLen = 0
    hashmap = {}
    n = len(arr)

    for i in range(n):
        sum += arr[i]

        if sum == k:
            maxLen = max(maxLen,i+1)

        rem = sum - k

        if rem in hashmap:
            length = i - hashmap[rem]
            maxLen = max(maxLen,length)

        if sum not in hashmap:
            hashmap[sum] = i

    return maxLen

nums = [1,2,-3,1,1,1,1,2,3,4]
print(SubArray(nums,3))