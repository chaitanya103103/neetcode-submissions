class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        dp = [[-1] * 2 for _ in range(len(prices))]
        def dfs(i,buy):
            if i == len(prices):
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]
            
            if buy:
                profit = max(-prices[i]+dfs(i+1,0),
                            0+ dfs(i+1,1))
            
            else:
                profit = max(prices[i] + dfs(i+1,1),
                            0 + dfs(i+1,0))
            dp[i][buy] = profit
            return profit
        return dfs(0,1)

