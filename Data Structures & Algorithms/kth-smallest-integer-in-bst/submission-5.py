# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.currentIndex = 0
        self.kValue = None

        self.inorder(root, k)
        return self.kValue

    def inorder(self, root, k):
        if not root or self.kValue:
            return
        
        self.inorder(root.left, k)
        self.currentIndex += 1
        if (self.currentIndex == k):
            self.kValue = root.val
        self.inorder(root.right, k)
        