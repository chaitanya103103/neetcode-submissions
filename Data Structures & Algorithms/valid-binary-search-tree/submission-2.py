# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = True
        def trav(curr,low,high):
            
            if curr == None:
                return True
            if low is not None and curr.val<=low:
                return False
            if high is not None and curr.val>=high:
                return False
            left = trav(curr.left,low,curr.val)
            right = trav(curr.right,curr.val,high)

            return left and right

        ans = trav(root,None,None)

        return ans


           