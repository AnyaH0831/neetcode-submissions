# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        visited = set()
        queue = deque([root])
        visited.add(root)
        result = []
        
        while queue:
            qLen = len(queue)
            lvl = []

            for i in range(qLen):
                curr = queue.popleft()

                if curr:
                    lvl.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)

            if lvl:
                result.append(lvl)

           

        return result