# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dp = {}
        queue = [(root, 0)]
        while queue:
            for _ in range(len(queue)):
                temp = queue.pop(0)
                counter = temp[1]
                node = temp[0]
                if node:
                    if not dp.get(counter):
                        dp[counter] = [node.val]
                    else:
                        dp[counter].append(node.val)

                    if node.left:
                        queue.append((node.left, counter - 1))
                    if node.right:
                        queue.append((node.right, counter + 1))
        
        keys = list(dp.keys())
        keys.sort()
        ans = []
        for i in keys:
            ans.append(dp[i])
        
        return ans