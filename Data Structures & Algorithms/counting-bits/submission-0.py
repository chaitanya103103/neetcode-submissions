class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            number = int(bin(i)[2:])

            while number:
                num = number % 10
                if num == 1:
                    count+=1
                number = number // 10
            res.append(count)
        return res
