"""
Problem Intuition:
You're given a beginWord, a target endWord, and a list of valid intermediate words (the wordList). You can only 
change one letter at a time, and every intermediate word must be in the wordList.

Your task is to find the minimum number of transformations required to turn beginWord into endWord.

-------------------------------------------------------------------------------------------

🌐 Real-Life Analogy (Optional for Notes)
Imagine you're playing a word game:
You can change one letter of a word to make a new word, and you must get from "hit" to "cog" by making only real words from the dictionary.

--------------------------------------------------------------------------------------------

🎯 Goal:
Find the shortest transformation sequence (in terms of steps) from beginWord to endWord.

🔍 Why BFS and Not DFS?
BFS (Breadth-First Search) is perfect for finding the shortest path in unweighted graphs.

It explores all words level by level, ensuring that as soon as we reach the target word, it's in the fewest possible steps.

DFS might go deep into one path, possibly missing the shortest one or reaching it later.

-------------------------------------------------------------------------------------------

🧠 Graph Intuition:
Think of each word as a node in a graph.

Two words are connected by an edge if they differ by exactly one character.

The graph is not explicitly given — we generate connections dynamically by trying all one-letter variations.

--------------------------------------------------------------------------------------------------

📊 Level-wise BFS Expansion (Illustration):
Let's say:

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

Imagine the transformation tree:

Level 1:       hit
                |
Level 2:       hot
              /   \
Level 3:    dot   lot
            |       |
Level 4:   dog     log
              \     /
Level 5:       cog

From "hit", we can go to "hot" (change 'i' → 'o').

From "hot", we go to "dot" or "lot".

Then to "dog" or "log", and finally to "cog".

We find "cog" at Level 5, so the answer is 5.

-----------------------------------------------------------------------------------------------------

✅ Important Logic Points:
You only explore valid words (i.e., those in the wordList).

Once a word is visited, you don't revisit it — this avoids cycles and improves efficiency.

You try all 26 letters at each position of the word to form possible next words.

The process stops as soon as the endWord is found.
"""
from collections import deque

class Pair:
    def __init__(self, word, level):
        self.word = word
        self.level = level

class Solution:
    def ladderLength(self,beginWord, endWord, wordList):
        visited = set(wordList)
        if endWord not in visited:
            return 0

        queue = deque([Pair(beginWord, 1)])
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while queue:
            pair = queue.popleft()
            word , level = pair.word, pair.level
            for i in range(len(word)):
                for j in alphabet:
                    newWord = word[:i] + j + word[i+1:]
                    if newWord == endWord:
                        return level + 1
                    elif newWord in visited:
                        visited.remove(newWord)
                        queue.append(Pair(newWord, level + 1))
        return 0
    
obj = Solution()
print(obj.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))