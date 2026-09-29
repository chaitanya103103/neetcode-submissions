class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.ok = True

        def trav(curr):
            if curr is None:
                return 0

            leftH = trav(curr.left)
            rightH = trav(curr.right)

            if abs(leftH - rightH) > 1:
                self.ok = False

            return max(leftH, rightH) + 1

        trav(root)
        return self.ok