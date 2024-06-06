#4 Sum 2
"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

1)0 <= i, j, k, l < n
2)nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
"""

from collections import defaultdict 
def Sum(nums1,nums2,nums3,nums4):
    hashmap = defaultdict(int)
    count = 0

    for i in nums1:
        for j in nums2:
            hashmap[i+j] += 1
    
    for k in nums3:
        for l in nums4:
            count += hashmap[-(k+l)]

    return count

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

print(Sum(nums1,nums2,nums3,nums4))