#Dynamic programming using memoization. Time complexity is O(n) and Space Complexity is O(n) + O(n).
def Fibo(n):
    if (n <= 1):
        return n
    
    if (dp[n] != -1):
        return dp[n]
    
    dp[n] = Fibo(n-1) + Fibo(n-2)
    return dp[n]

#Dynamic programming using tabulation Time complexity is O(n) and Space Complexity is O(n).
def fibo(n):
    Dp = [-1] * (n + 1)
    Dp[0] , Dp[1] = 0 , 1

    for i in range(2,n+1):
        Dp[i] = Dp[i-1] + Dp[i-2]
    
    return Dp[n]

#Space-Optimized DP. Time complexity is O(n) and space complexity is O(1).
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    previous_One = 1
    previous_Two = 0
    
    for i in range(2, n + 1):
        result = previous_One + previous_Two
        previous_Two = previous_One
        previous_One = result
    
    return result

n = int(input("Enter number for fibonacci:"))
dp = [-1] * (n + 1)
print(Fibo(n))
print(fibo(n))
print(fibonacci(n))
  