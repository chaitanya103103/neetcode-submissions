class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = []

        adj_list = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj_list[u].append(v)

        visited = 2
        visiting = 1
        unvisited = 0

        dp = [unvisited] * numCourses

        def dfs(node):
            state = dp[node]
            if state == visited:
                return True
            elif state == visiting:
                return False

            dp[node] = visiting

            for neighbour in adj_list[node]:
                if not dfs(neighbour):
                    return False

            dp[node] = visited
            res.append(node) 
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []

        return res