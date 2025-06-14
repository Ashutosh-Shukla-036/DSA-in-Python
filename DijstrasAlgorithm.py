import heapq

class Solution:
    def DijstrasAlgo(self,adjMatrix,sourceNode):
        pq = []

        result = [1e9] * len(adjMatrix)
        result[sourceNode] = 0
        heapq.heappush(pq, (0, sourceNode))

        while pq:
            currentDistance, currentNode = heapq.heappop(pq)
            for distance, neighbour in adjMatrix[currentNode]:
                if distance + currentDistance < result[neighbour]:
                    result[neighbour] = distance + currentDistance
                    heapq.heappush(pq, (result[neighbour], neighbour))
        return result

obj = Solution()
adjMatrix = {
    0: [(4, 1), (1, 2), (7, 3)],
    1: [(4, 0), (3, 4), (6, 5)],
    2: [(1, 0), (2, 3), (5, 6)],
    3: [(7, 0), (2, 2), (3, 6)],
    4: [(3, 1), (1, 5), (8, 7)],
    5: [(6, 1), (1, 4), (2, 7), (5, 8)],
    6: [(5, 2), (3, 3), (6, 9)],
    7: [(8, 4), (2, 5), (4, 8)],
    8: [(5, 5), (4, 7), (3, 9)],
    9: [(6, 6), (3, 8)]
}
print(obj.DijstrasAlgo(adjMatrix,0))