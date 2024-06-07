#Merge Intervals

"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an 
array of the non-overlapping intervals that cover all the intervals in the input.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""

#Brute force
def Merge(intervals):
    n = len(intervals)
    result  = []
    intervals.sort()

    for i in range(n):
        start , end = intervals[i][0] , intervals[i][1]

        if result and end <= result[-1][1]:
            continue

        for j in range(i+1,n):
            if intervals[j][0] <= end:
                end = max(end,intervals[j][1])
            else:
                break
        result.append([start,end])
    return result
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Merge(intervals))#Time Complexity is O(n*n)


#optimal solution
def MergeInterval(intervals):
    n = len(intervals)
    result = []
    intervals.sort()

    for i in range(n):
        if not result or intervals[i][0] > result[-1][1]:
            result.append(intervals[i])
        else:
            result[-1][1] = max(result[-1][1],intervals[i][1])
    return result
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(MergeInterval(intervals))#Time complexity is O(n)