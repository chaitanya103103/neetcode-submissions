# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        qu = collections.deque()
        qu.append(root)

        while qu:
            qlen = len(qu)
            level = []
            for i in range(qlen):
                node = qu.popleft()

                if node:
                    level.append(node.val)
                    qu.append(node.left)
                    qu.append(node.right)
            if level:
                res.append(level)
        return res
        