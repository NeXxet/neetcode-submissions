# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sumExists = False

        def dfs(root, remaining):
            if not root or self.sumExists:
                return

            newRemaining = remaining - root.val

            if not root.left and not root.right and newRemaining == 0:
                self.sumExists = True

            dfs(root.left, newRemaining)
            dfs(root.right, newRemaining)
        
        dfs(root, targetSum)
        return self.sumExists