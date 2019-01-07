"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        from collections import deque
        queue = deque()
        queue.append(root)
        ans = []
        temp_arr = []
        while queue:
            for _ in range(len(queue)):
                temp = queue.popleft()
                temp_arr.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            ans.append(temp_arr)
            temp_arr = []
        return ans[::-1]