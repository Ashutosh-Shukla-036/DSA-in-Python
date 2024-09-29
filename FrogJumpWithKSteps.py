"""
There is an array arr of heights of stone and frog is standing at the first stone and can jump to one of the 
following: Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will 
be |hi-hj| is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the 
Frog reaches the last stone
"""
#using recursion.
def minCost(k,arr):
    def BackTrack(index):
        if index == 0:
            return 0
        
        minStep = float("inf")

        for i in range(1,k+1):
            if index - i >= 0:
                jump = BackTrack(index-i) + abs(arr[index] - arr[index-i])
                minStep = min(minStep,jump)
            
        return minStep
    return BackTrack(len(arr)-1)
k = 3
arr = [10, 30, 40, 50, 20]
print(minCost(k,arr))

#using dp with memoization
def min_Cost(k,arr):
    def BackTrack(index):
        if index == 0:
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        minStep = float("inf")

        for i in range(1,k+1):
            if index - i >= 0:
                jump = BackTrack(index-i) + abs(arr[index] - arr[index-i])
                minStep = min(minStep,jump)
            
        dp[index] = minStep
        return dp[index]
    return BackTrack(len(arr)-1)

k = 3
arr = [10, 30, 40, 50, 20]
dp = [-1] * (len(arr))
print(min_Cost(k,arr))

#using tabulation
def MinCost(k,arr):
    n = len(arr)
    dp = [float("inf")] * n
    dp[0] = 0

    for index in range(1,n):
        for i in range(1,k+1):
            if index-i >= 0:
                dp[index] = min(dp[index],dp[index-i]+abs(arr[index]-arr[index-i]))

    return dp[n-1]
k = 3
arr = [10, 30, 40, 50, 20]
print(MinCost(k,arr))
