class Solution:
    def _lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = s.split(" ")
        arr = list(filter(lambda x: x != '', temp))
        if not arr:
            return 0
        return len(arr[-1])
    def lengthOfLastWord(self, s):
        l, r = len(s) - 1, len(s) - 1
        if r == -1:
            return 0
        
        while r >= 0 and not s[r].isalpha():
            r -= 1
        l = r
        while l >= 0 and s[l].isalpha():
            l -= 1
        if s[l + 1].isalpha():
            return len(s[l+1:r+1])
        
        if r < 0:
            return 0
        