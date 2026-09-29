class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        arr1 = nums[0:n-1]
        arr2 = nums[1:n]

        dp = [-1] * len(arr1)
        dp2 = [-1] * len(arr2)

        if len(nums) == 1:
            return nums[0]

        def dfs(arr,dp,i):
            if i == 0:
                return arr[0]
            
            if i < 0:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            pick = arr[i] + dfs(arr,dp,i-2)
            nonpick = 0 + dfs(arr,dp,i-1)
            dp[i] = max(pick,nonpick)
            return dp[i]

        res1 = dfs(arr1,dp,len(arr1)-1)
        res2 = dfs(arr2, dp2, len(arr2)-1)
        return max(res1,res2)