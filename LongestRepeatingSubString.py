#Longest repeating character replacement

"""
You are given a string s and an integer k. You can choose any character of the string and change it to any
other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above
operations.
"""

def characterReplacement(s: str, k: int) -> int:
    maxLen , hashmap = 0 , {}
    count , i , n = 0 , 0 , len(s)

    for j in range(n):
        if s[j] not in hashmap:
            hashmap[s[j]] = 0
        hashmap[s[j]] += 1

        count = max(count,hashmap[s[j]])

        while (j - i + 1) - count > k:
            hashmap[s[i]] -= 1
            i += 1

        maxLen = max(maxLen,j-i+1)
    
    return maxLen

s = "AABABBA"
k = 1
print(characterReplacement(s,k))