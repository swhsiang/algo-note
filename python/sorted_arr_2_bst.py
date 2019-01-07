# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
Slicing an array is expensive. It's better to pass bounds of array into recursive calls!
"""

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root = None
        root = self._convertion(0, len(nums) - 1, nums)
        return root

    def _convertion(self, l, r, nums):
        if l > r:
            return None
        mid = (l + r) // 2
        node = TreeNode(nums[mid])
        node.left = self._convertion(l, mid - 1, nums)
        node.right = self._convertion(mid + 1, r, nums)
        
        return node
    
    def convertion(self, node, lnums, rnums):
        if lnums:
            lmid = len(lnums) // 2
            node.left = TreeNode(lnums[lmid])
            self.convertion(node.left, lnums[:lmid], lnums[lmid+1:])
        else:
            node.left = None
        
        if rnums:
            rmid = len(rnums) // 2
            node.right = TreeNode(rnums[rmid])
            self.convertion(node.right, rnums[:rmid], rnums[rmid+1:])
        else:
            node.right = None
