# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.dfs(root, 0)

    def dfs(self, root, count) -> int:
        if not root:
            return count
        count += 1

        max_val = max(self.dfs(root.left, count), self.dfs(root.right, count))

        return max_val