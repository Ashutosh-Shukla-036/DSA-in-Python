from typing import List
def combinationSum2(nums: List[int], target: int) -> List[int]:
    result = set()
    nums.sort()

    def BackTrack(index: int, combination: List[int], Sum: int):
        if Sum == target:
            result.add(tuple(combination))
            return
        
        if Sum > target:
            return
        
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            combination.append(nums[i])
            BackTrack(i + 1,combination,Sum + nums[i])
            combination.pop()

    BackTrack(0,[],0)

    return [list(temp) for temp in result]

nums = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(nums,target))