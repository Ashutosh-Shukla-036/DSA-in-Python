"""
In mathematics, a subsequence of a given sequence is a sequence that can be derived from the given sequence by
deleting some or no elements without changing the order of the remaining elements
"""

def SubSequence(index,List,nums,n):
    
    if index == n:
        print(List)
        return
    
    #Taken
    List.append(nums[index])
    SubSequence(index+1,List,nums,n)
    List.pop()

    #not Taken
    SubSequence(index+1,List,nums,n)

nums = [3,1,2]
List = []
SubSequence(0,List,nums,3)
#time complexity is O(2**n) and space complexity is O(n)