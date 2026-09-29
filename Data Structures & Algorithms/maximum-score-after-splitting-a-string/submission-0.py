class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        best = 0
        for i in range(1, n):   # split point i: left = s[:i], right = s[i:]
            left = s[:i]
            right = s[i:]
            zeros = left.count('0')
            ones = right.count('1')
            best = max(best, zeros + ones)
        return best