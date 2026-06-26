# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {value:index for index, value in enumerate(inorder)}
        self.preorderIndex = 0
        def dfs(left, right):
            if left > right:
                return None
            
            rootValue = preorder[self.preorderIndex]
            self.preorderIndex += 1
            root = TreeNode(rootValue)
            mid = indices[rootValue]
            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)
            return root
        
        return dfs(0, len(preorder)-1)