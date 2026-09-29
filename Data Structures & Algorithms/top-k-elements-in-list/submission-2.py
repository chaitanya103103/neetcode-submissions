class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        
        sorted_seen = sorted(seen,key=seen.get,reverse = True)

        return sorted_seen[:k]