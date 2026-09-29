class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = []

        for num in nums:
            if num in stack:
                return True
            stack.append(num)
        return False
