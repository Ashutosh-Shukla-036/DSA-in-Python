"""
Climbing Stairs Problem:
In the Climbing Stairs problem, you're given n stairs, and you can reach each stair by either taking:

A single step (from stair n-1), or
A double step (from stair n-2).
So, the number of ways to reach the nth stair is the sum of:

The number of ways to reach stair n-1 (since you take 1 step from there).
The number of ways to reach stair n-2 (since you take 2 steps from there).
This gives the recurrence relation for the Climbing Stairs problem:
   ways(n)=ways(n-1)+ways(n-2)
"""

def Climbing_Stairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n+1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

print(Climbing_Stairs(4))


def Climbing_Stairs_Space_Optimized(n):
    if n <= 2:
        return n
    
    prev2 = 1
    prev1 = 2

    for i in range(3,n+1):
        current = prev2 + prev1
        prev2 = prev1
        prev1 = current

    return current

print(Climbing_Stairs_Space_Optimized(4))