# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root: TreeNode, k: int):
        if not root or self.value >= 0:
            return None

        self.inorder(root.left, k)

        self.currentIndex += 1
        if self.currentIndex == k:
            self.value = root.val
        self.inorder(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.currentIndex = 0
        self.value = -1
        self.inorder(root, k)
        return self.value