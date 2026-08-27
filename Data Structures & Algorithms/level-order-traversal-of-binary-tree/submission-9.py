# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []

            for _ in range(len(queue)):
                new_node = queue.popleft()
                level.append(new_node.val)
                if new_node.left:
                    queue.append(new_node.left)
                if new_node.right:
                    queue.append(new_node.right)

            result.append(level.copy())

        return result



        