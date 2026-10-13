# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 1
        def dfs(node, greatest):
            nonlocal res

            if not node:
                return None

            if node.left:
                if node.left.val >= greatest:
                    res += 1

                dfs(node.left, max(greatest, node.left.val))
                
            if node.right:
                if node.right.val >= greatest:
                    res += 1
                dfs(node.right, max(greatest, node.right.val))

        dfs(root, root.val)

        return res