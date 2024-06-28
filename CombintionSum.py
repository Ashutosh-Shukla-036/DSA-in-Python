from typing import List
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    def BackTrack(start: int, Combination: List[int], Sum: int) -> int:
        # Base case: if the current sum equals the target, add the combination to the result
        if Sum == target:
            result.append(list(Combination))
            return
        
        # If the current sum exceeds the target, stop further exploration
        if Sum > target:
            return
        
        # Iterate over the candidates starting from the current index
        for i in range(start,len(candidates)):
            # Add the current candidate to the combination
            Combination.append(candidates[i])
            # Recursively call BackTrack with the updated sum and combination
            BackTrack(i,Combination,Sum+candidates[i])
             # Backtrack by removing the last added candidate
            Combination.pop()
    # Start backtracking from index 0 with an empty combination and sum of 0
    BackTrack(0,[],0)
    return result

nums = [3,2,4,1]
target = 6

print(combinationSum(nums,target))