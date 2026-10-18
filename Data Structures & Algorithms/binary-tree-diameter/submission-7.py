# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def trav(curr):
            if curr is None:
                return 0
            
            left = trav(curr.left)
            right = trav(curr.right)

            self.res = max(self.res,left+right)
        
            return 1 + max(left,right)
        trav(root)

        return self.res
