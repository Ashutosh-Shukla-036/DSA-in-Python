#Find Nth root of M
"""
You are given 2 numbers (n , m); the task is to find n√m (nth root of m).
"""

def NthRoot(n,m):
    if m == 0:
        return 0
    if n == 1:
        return m
    
    low , high = 0 , m
    while low <= high:
        mid = (low+high)//2
        power = mid ** n

        if power == m:
            return mid
        elif power < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(NthRoot(3,64))