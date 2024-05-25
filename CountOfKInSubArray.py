#Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

#optimal solution using Hashmap
def SubArrayCount(arr,k):
    prefixsum = 0
    count = 0
    n = len(arr)
    hashmap = {0:1} # Handles the edge case where prefixsum itself is equal to k

    for i in range(n):
        prefixsum += arr[i]

        rem = prefixsum - k
        if rem in hashmap :
            count += hashmap[rem]

        if prefixsum in hashmap:
            hashmap[prefixsum] += 1
        else:
            hashmap[prefixsum] = 1

    return count

nums = [0,0,0,0,0,0,0]
print(SubArrayCount(nums,0))