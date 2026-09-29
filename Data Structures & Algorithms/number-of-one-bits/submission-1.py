class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        
        count = 0
        num = int(bin(n)[2:])

        while num:
            number = num % 10
            if number == 1:
                count+=1
            num = num // 10
        
        return count