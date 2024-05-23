#Finding the missing numberin the array.

#using Hashing Concept
def MissingNumber(arr):

    n = len(arr)+1

    hash = [0] * (n+1)

    for i in range(len(arr)):
        hash[arr[i]] = 1

    for i in range(1,n):
        if(hash[i] == 0):
            return i
        
    return -1

num = [1,2,4,5]
print(MissingNumber(num))

#optimal solution

def missingnumberInArray(arr):
    n = len(arr) + 1
    sum = ( n * (n+1) ) // 2
    sum2 = 0
    for i in range(n-1):
        sum2 = sum2 + arr[i]
    return sum - sum2

nums = [1,2,3,5]
print(missingnumberInArray(nums))
