class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlen = 0
        a = set()

        for right in range(len(s)):
            while s[right] in a:
                a.remove(s[left])
                left+= 1
            a.add(s[right])
            temp = len(a)
            maxlen = max(maxlen,temp)
        return maxlen

