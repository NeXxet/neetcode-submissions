# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.currentIndex = 0
        self.value = None

        def inorder(root):
            if not root or self.value:
                return

            inorder(root.left)
            self.currentIndex += 1
            if self.currentIndex == k:
                self.value = root.val
            inorder(root.right)

        inorder(root)
        return self.value