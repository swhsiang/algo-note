"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            arr = []
            for _ in range(len(queue)):
                temp = queue.pop(0)
                arr.append(temp.val)
                for j in temp.children:
                    queue.append(j)
            ans.append(arr)
        return ans
        