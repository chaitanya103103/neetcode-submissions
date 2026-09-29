class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        n = len(nums)

        for k in range(n):
            rotated = []

            for i in range(n):
                rotated.append(arr[(k + i) % n])

            if rotated == nums:
                return True

        return False