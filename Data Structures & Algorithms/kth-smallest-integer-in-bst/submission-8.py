# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.current_index = 0

        def inorder(node):
            if not node or self.result:
                return
            
            inorder(node.left)
            self.current_index += 1
            if self.current_index == k:
                self.result = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.result