class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.root = TrieNode()

        for word in strs:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.endOfWord = True

        
        res = ""
        curr = self.root
        while len(curr.children) == 1 and curr.endOfWord == False:
            for char in curr.children:
                res += char
                curr = curr.children[char]
                break
        
        return res
        