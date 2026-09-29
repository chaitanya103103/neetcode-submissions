class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = set()

        for i in nums:
            if i in hm:
                hm.remove(i)
            else:
                hm.add(i)

        ans = hm.pop()
        return ans