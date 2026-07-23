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

        def bfs(queue):
            if not queue:
                return

            sublist = []

            for i in range(len(queue)):
                node = queue.popleft()
                sublist.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(sublist.copy())
            bfs(queue)
        
        bfs(queue)
        return result

        