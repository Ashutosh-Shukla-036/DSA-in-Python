#RichestCustomerWealth

"""You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the
jth bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer
that has the maximum wealth.

Example :
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10
"""
#Brute force
import sys
def MaxWealth(accounts):
    maxi = -sys.maxsize - 1
    def SumMatrix(i):
        sum = 0
        for j in range(len(accounts[0])):
            sum += accounts[i][j]
        return sum
        
    for i in range(len(accounts)):
        sum = SumMatrix(i)
        if(maxi < sum):
            maxi = sum
    return maxi
accounts = [[1,5],[7,3],[3,5]]
print(MaxWealth(accounts))
#Time compexit  O(N) * O(M)

#optimal solution using map function of python
def Max(accounts):
    return max(map(sum,accounts))
accounts = [[1,5],[7,3],[3,5]]
print(MaxWealth(accounts))
#Time compexit  O(N) * O(M)