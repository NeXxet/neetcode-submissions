# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None
        current_index = 0

        def inorder(node):
            nonlocal result, current_index

            if not node or result:
                return
            
            inorder(node.left)
            if result:
                return
            current_index += 1
            if current_index == k:
                result = node.val
                return
            inorder(node.right)

        inorder(root)
        return result