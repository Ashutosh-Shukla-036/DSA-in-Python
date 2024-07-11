#Printing the SubArray with maxSum

from typing import List
def SubArray(nums: List[int]):

    if not nums:
        print("Empty SubArray")
        return

    maxSum , currentSum = nums[0] , 0
    start , startIndex , endIndex = 0 , 0 , 0

    for i in range(len(nums)):

        currentSum += nums[i]

        if maxSum < currentSum:
            maxSum = currentSum
            startIndex = start
            endIndex = i

        if currentSum < 0:
            currentSum = 0
            start = i + 1
        
    print("Max Sum is:",maxSum)
    print("SubArray is:")
    for i in range(startIndex,endIndex+1):
        print(nums[i],end=" ")
    print("\n")

test_cases = [
    [],  # Empty array
    [5],  # Single positive element
    [-5],  # Single negative element
    [1, 2, 3, 4, 5],  # All positive numbers
    [-1, -2, -3, -4, -5],  # All negative numbers
    [2, 3, -1, 2, -4, 3],  # Mixed positive and negative numbers
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Mixed positive and negative numbers
]

for nums in test_cases:
    print(f"Testing with input: {nums}")
    SubArray(nums)
    print()