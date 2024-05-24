#finding the longest SubArray with (sum = k) and printing the length of SubArray


#brute force : generate all the subArray and print length of longest SubArray.
def LargestSubArray(arr,k):
    n = len(arr)
    length = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]
            if(sum == k):
                length = max(length,j-i+1)
    return length

nums = [1,2,3,1,1,1,1,4,2,3]
print(LargestSubArray(nums,4))
#Time complexity is almost arround O(N*N).


#Optimal solution using two pointers 
def SubArray(arr,k):
    left , right = 0 , 0
    sum = arr[0]
    maxLen = 0
    n = len(arr)

    while(right < n):
        while(left <= right and sum>k):
            sum -= arr[left]
            left += 1
        if(sum == k):
            maxLen = max(maxLen,right-left+1)
        right += 1
        if(right < n):
            sum += arr[right]
    return maxLen

num = [1,2,3,1,1,1,1,2,3]
print(SubArray(num,5))
#Time compexity is around O(2N). Reason , because the inner while loop is only working when the sum is greater the sum.