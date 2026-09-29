class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj_list[u].append(v)

        unvisited = 0
        visiting = 1
        visited = 2

        dp = [unvisited] * numCourses

        def dfs(node):
            state = dp[node]
            if state == visited:
                return True
            elif state == visiting:
                return False

            dp[node] = visiting

            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False

            dp[node] = visited
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True