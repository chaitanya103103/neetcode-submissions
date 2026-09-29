class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [-1] * (amount + 1)

        def dfs(diff):

            if diff == 0:
                return 0

            if diff < 0:
                return float('inf')

            if dp[diff] != -1:
                return dp[diff]

            ans = float('inf')

            for coin in coins:
                ans = min(ans,1+dfs(diff-coin))

            dp[diff] = ans
            return dp[diff]
        ans = dfs(amount)

        if ans == float('inf'):
            return -1

        return ans    