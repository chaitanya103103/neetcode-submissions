class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        words1 = s1.split()
        words2 = s2.split()
        words = words1 + words2

        dict1 = {}
        for word in words:
            dict1[word] = dict1.get(word,0)+1
        
        for word in dict1:
            if dict1[word] == 1:
                res.append(word)
        return res

        

        

            
