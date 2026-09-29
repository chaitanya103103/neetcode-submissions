class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        countt = {}

        for i in range(len(s)):

            chars = s[i]
            chart = t[i]

            if chars in counts:
                counts[chars] += 1
            else:
                counts[chars] = 1

            if chart in countt:
                countt[chart] += 1
            else:
                countt[chart] = 1

            
        if countt == counts:
            return True
        else:
            return False