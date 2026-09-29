class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        count = 0
        n = len(temperatures)
        a = [0] * n
        
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    a[i] = (j-i)
                    break
                
        return a
