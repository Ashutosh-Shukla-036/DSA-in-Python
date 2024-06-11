#Maximum product SubArray
"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

"""
#optimal solution with time Complexity of O(n)
import sys
def MaxProduct(nums):
    n = len(nums)
    product , prefix , suffix = -sys.maxsize-1 , 1 , 1

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= nums[i]
        suffix *= nums[n-i-1]

        product = max(product,max(prefix,suffix))
    return product
nums = [-2,0,-1]
print(MaxProduct(nums))