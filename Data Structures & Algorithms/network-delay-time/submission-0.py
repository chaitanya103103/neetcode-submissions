
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        distance = [float("inf")] * (n + 1)
        distance[k] = 0

        adj = [[] for _ in range(n + 1)]

        # Build adjacency list
        for u, v, cost in times:
            adj[u].append((v, cost))

        # Min-heap: (current distance, node)
        q = [(0, k)]

        while q:
            cost, u = heapq.heappop(q)

            # Skip outdated entries
            if cost > distance[u]:
                continue

            for nei, neiCost in adj[u]:
                newCost = cost + neiCost

                if newCost < distance[nei]:
                    distance[nei] = newCost
                    heapq.heappush(q, (newCost, nei))

        # Ignore index 0
        maxDistance = max(distance[1:])

        return maxDistance if maxDistance != float("inf") else -1
