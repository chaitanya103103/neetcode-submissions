# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum1 = 0

        def trav(curr):
            nonlocal sum1
            if curr is None:
                return

            if low<=curr.val<=high:
                sum1 += curr.val
            
            trav(curr.right)
            trav(curr.left)
        
        trav(root)
        return sum1