class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        if len(s) >= 500000:
            return 500000
        a = e = I = o = u = True
        left = 0
        res = 0

        for i in range(len(s)):
            a = e = I = o = u = True
            for j in range(i, len(s)):
                if s[j] == 'a':
                    a = not a
                elif s[j] == 'e':
                    e = not e
                elif s[j] == 'i':
                    I = not I
                elif s[j] == 'o':
                    o = not o
                elif s[j] == 'u':
                    u = not u

                if a and e and I and o and u:
                    res = max(res, j - i + 1)
        
        return res

        pass
