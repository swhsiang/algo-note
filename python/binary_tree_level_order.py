"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # attempt one, 72 ms
    def _levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q1 = [root]
        q2 = []
        ans = []
        depth = 0
        
        while q1 or q2:
            if depth % 2 == 0:
                temp_arr = []
                while q1:
                    temp = q1.pop(0)
                    temp_arr.append(temp.val)
                    if temp.left:
                        q2.append(temp.left)
                    if temp.right:
                        q2.append(temp.right)
                depth += 1
                ans.append(temp_arr)
            else:
                temp_arr = []
                while q2:
                    temp = q2.pop(0)
                    temp_arr.append(temp.val)
                    if temp.left:
                        q1.append(temp.left)
                    if temp.right:
                        q1.append(temp.right)
                depth += 1
                ans.append(temp_arr)
        return ans

    # attempt two, 64 ms
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        import collections
        q1 = collections.deque()
        q1.append(root)
        ans = []
        current = 1
        next_node = 0
        temp_arr = []
        while q1:
            #print(current, next_node, len(q1), q1)
            if current > 0:
                temp = q1.popleft()
                temp_arr.append(temp.val)
                current -= 1
                if temp.left:
                    q1.append(temp.left)
                    next_node += 1
                if temp.right:
                    q1.append(temp.right)
                    next_node += 1
            else:
                ans.append(temp_arr)
                temp_arr = []
                current = next_node
                next_node = 0
        ans.append(temp_arr)
        return ans

