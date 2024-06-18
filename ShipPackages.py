#Capacity to Ship Packages within D Days
"""
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the 
conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the 
ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being 
shipped within days days.
"""

def ShipWithinDays(nums,days):
    low , high , ans = max(nums) , sum(nums) , float("inf")

    def Count(nums,capacity):
        days , load = 1 , 0
        for i in range(len(nums)):
            if load + nums[i] > capacity:
                load = nums[i]
                days += 1
            else:
                load += nums[i]
        return days

    while low<= high:
        mid = (low+high)//2
        result = Count(nums,mid)

        if result <= days:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(ShipWithinDays(weights,days))