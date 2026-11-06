class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in set(s):
            r=s.count(i)//2
            if r>=1:
                count+=r
        
        r=count*2
        if r==len(s):
            return r
        else:
            return r+1
        