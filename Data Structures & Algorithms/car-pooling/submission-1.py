class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        road = [0] * 1001

        for passan, start, end in trips:
            for i in range(start,end):
                road[i] = road[i] + passan
            
                if road[i] > capacity:
                    return False
        return True
