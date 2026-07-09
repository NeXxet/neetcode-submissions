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

            remaining = remaining - root.val

            if not root.left and not root.right and remaining == 0:
                self.sumExists = True

            dfs(root.left, remaining)
            dfs(root.right, remaining)
        
        dfs(root, targetSum)
        return self.sumExists