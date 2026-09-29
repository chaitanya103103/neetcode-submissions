class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def dfs(i):
            if i == 0:
                return nums[0]
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]

            pick = nums[i] + dfs(i-2)
            nonpick = 0 + dfs(i-1)
            dp[i] = max(pick,nonpick)
            return dp[i]
        
        return dfs(len(nums)-1)
        