# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.currentIndex = 0
        self.kValue = 0

        self.inorder(root, k)
        return self.kValue

    def inorder(self, root, k):
        if not root or self.currentIndex > k:
            return
        
        self.inorder(root.left, k)
        self.currentIndex += 1
        if (self.currentIndex == k):
            self.kValue = root.val
        self.inorder(root.right, k)
        