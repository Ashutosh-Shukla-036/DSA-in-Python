# Longest Substring with out repeating characters
"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example :
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
# Time complexity is O(2n)
def SubString(s):
    n = len(s)

    if n == 0:
        return 0
    
    maxLen , seen = 0 , set()
    i , j = 0 , 0

    while j < n:
        while j < n and s[j] not in seen:
            seen.add(s[j])
            j += 1
            maxLen = max(maxLen,j-i)
        while j < n and s[j] in seen:
            seen.remove(s[i])
            i += 1

    return maxLen

s = "abcabcbb"
print(SubString(s))

#Optimal solution using hashmap and sliding window
def String(s):
    hashmap , maxLen = {} , 0
    i , j = 0 , 0

    for j in range(len(s)):
        
        if s[j] in hashmap and i <= hashmap[s[j]]:
            i = hashmap[s[j]] + 1
        hashmap[s[j]] = j
        maxLen = max(maxLen,j-i+1)
    return maxLen

s = "abcabcbb"
print(String(s))