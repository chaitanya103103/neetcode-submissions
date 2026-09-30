class Solution:
    def canJump(self, nums):
        n = len(nums) - 1
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        return True