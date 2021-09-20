# import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums
        self.n = len(nums)
        self.p(nums, 0)
        
        return self.ans
    def p(self, arr: List[int], level: int):
        if level == self.n:
            self.ans.append(arr[:])
            return
        
        temp = level
        level += 1
        for i in range(temp, self.n):
            self.nums[i], self.nums[temp] = self.nums[temp], self.nums[i]
            self.p(arr, level)
            self.nums[i], self.nums[temp] = self.nums[temp], self.nums[i]
