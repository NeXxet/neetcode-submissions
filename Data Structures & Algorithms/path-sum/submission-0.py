# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.currentSum = 0

        def dfs(root):
            if not root:
                return False
            
            self.currentSum += root.val

            if self.currentSum == targetSum and not root.left and not root.right:
                return True
            if dfs(root.left):
                return True
            if dfs(root.right):
                return True

            self.currentSum -= root.val
            return False
        
        return dfs(root)
            

