class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            store.append(s[i])

        for j in range(len(t)):
            if t[j] in store:
                store.remove(t[j])
            else:
                return False

        return True