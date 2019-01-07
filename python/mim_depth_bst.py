# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def minDepth(self, root):
        return self._minDepth(root)
    
    def _minDepth(self, root):
        if not root:
            return 0
        if root.left == None or root.right == None:
            return max(self._minDepth(root.left), self._minDepth(root.right)) + 1
        return min(self._minDepth(root.left), self._minDepth(root.right)) + 1