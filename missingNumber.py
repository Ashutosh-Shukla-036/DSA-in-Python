def misssingNumber(arr):

    n = len(arr)+1

    hash = [0] * (n+1)

    for i in range(len(arr)):
        hash[arr[i]] = 1

    for i in range(1,n+1):
        if(hash[i] == 0):
            return i
        
    return -1

nums = [1,2,4,3,5,9,0,8,6]

print(misssingNumber(nums))