"""Leader in a array is a element which is greater then all the elements on its right side"""

import sys
def leaderInArray(arr):
    nums = []
    maxi = -sys.maxsize - 1
    for i in range(len(arr)-1,-1,-1):
        if(arr[i] > maxi):
            maxi = arr[i]
            nums.append(arr[i])
    return nums
nums = [10,22,12,3,0,6]
print(leaderInArray(nums))