class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        map1 = {}

        for i in range(len(names)):
            map1[heights[i]] = names[i]

        res = sorted(map1.keys(), reverse=True)

        return [map1[h] for h in res]