class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        mask = 00000
        mask_to_index = {0:-1}
        res = 0

        for i,c in enumerate(s):
            if c in vowels:
                mask = mask ^ ord(c)+1 - ord("a") 
            if mask in mask_to_index:
                length = i - mask_to_index[mask]
                res = max(length, res)
            else:
                mask_to_index[mask] = i

        return res
                


