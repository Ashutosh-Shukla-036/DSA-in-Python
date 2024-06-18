#Minimum days to make M bouquets

"""
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly 
one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is 
impossible to make m bouquets return -1.
"""

def minDays(nums,m,k):
    low , high , ans = min(nums) , max(nums) , -1

    if m * k > len(nums): #impossible case
        return -1
    
    def Count(nums,days,m,k):
        count , Bouquets = 0 , 0
        for i in range(len(nums)):
            if nums[i] <= days:
                count += 1
                if count == k:
                    Bouquets += 1
                    count = 0
            else:
                count = 0
        return Bouquets >= m  #returns True/False

    while low <= high:
        mid = (low + high)//2
        result = Count(nums,mid,m,k)

        if result:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(minDays(bloomDay,m,k))