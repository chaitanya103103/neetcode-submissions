class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [float("inf")] *n
        distance[src] = 0

        adj_list = [[] for _ in range(n)]
        for u,v,w in flights:
            adj_list [u].append((v,w))

        q = deque()
        q.append((0,src,0))

        while q:
            stops, node,cost = q.popleft()
            if stops > k:
                continue
            for nei , price in adj_list[node]:
                new_cost = price + cost
                if new_cost < distance[nei]:
                    distance[nei] = new_cost
                    q.append((stops+1,nei,new_cost))

        if distance[dst] == float("inf"):
            return -1
        return distance[dst]