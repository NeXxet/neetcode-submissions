# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    nodeBalanced = True
    def getSubtreeHeight(self, root: TreeNode) -> int:
            if not root:
                return 0

            leftHeight = self.getSubtreeHeight(root.left)
            rightHeight = self.getSubtreeHeight(root.right)

            if abs(leftHeight-rightHeight) > 1:
                self.nodeBalanced = False

            return max(leftHeight, rightHeight) + 1
            
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.getSubtreeHeight(root)

        return self.nodeBalanced
