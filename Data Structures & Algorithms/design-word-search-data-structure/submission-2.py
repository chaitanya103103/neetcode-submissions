class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.endOfWord

            char = word[i]

            if char == ".":
                # wildcard: try every child at this position
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                # normal character: only one possible path
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)