"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q1 = [root]
        q2 = []
        depth = 0
        ans = []
        
        while q1 or q2:
            temp_arr = []
            if depth % 2 == 0:
                while q1:
                    temp = q1.pop()
                    temp_arr.append(temp.val)
                    if temp.left:
                        q2.append(temp.left)
                    if temp.right:
                        q2.append(temp.right)
                depth += 1
            else:
                while q2:
                    temp = q2.pop()
                    temp_arr.append(temp.val)
                    if temp.right:
                        q1.append(temp.right)
                    if temp.left:
                        q1.append(temp.left)
                depth += 1
            if temp_arr:
                ans.append(temp_arr)
                temp_arr = []
        return ans