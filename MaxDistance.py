# Minimise Maximum Distance between Gas Stations

def MaxDistance(nums,k):
    HowMany = [0] * (len(nums)-1)
    for gas in range(k):
        maxValue , maxIndex = -1 , -1
        for i in range(len(nums)-1):
            diff = nums[i+1] - nums[i]
            SectionLength = diff / (HowMany[i] + 1)
            if maxValue < SectionLength:
                maxValue = SectionLength
                maxIndex = i
        HowMany[maxIndex] += 1
    
    maxAns = -1
    for i in range(len(nums)-1):
        SectionLength = (nums[i+1] - nums[i])/(HowMany[i] + 1)
        maxAns = max(maxAns,SectionLength)
    return maxAns

nums = [1,13,17,23]
k = 5
print(MaxDistance(nums,k))