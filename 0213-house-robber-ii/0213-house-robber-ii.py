class Solution:
    def rob(self, nums: List[int]) -> int:
        # Memoization
        n = len(nums)
        if n == 1:
            return nums[0]
            
        def rec(i, e, dp):
            if i > e:
                return 0
            if dp[i] != -1:
                return dp[i]
                
            dp[i] = max(nums[i] + rec(i + 2, e, dp), rec(i + 1, e, dp))
            return dp[i]
            
        return max(rec(0, n - 2, [-1] * (n + 1)), rec(1, n - 1, [-1] * (n + 1)))