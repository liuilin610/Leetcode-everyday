# Time: O(n); Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len (nums)
        if ( n == 0 ): return 0
        dp = [0] * ( n + 1 )
        dp[0] = 0
        dp[1] = nums[0]
        for i in range ( 2, n + 1 ):
            dp[i] = max( dp[i-1], dp[i-1] + nums[i-1] )
        return dp[n]

# Time : O(n); Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0

        for i in nums:
            prev, cur = cur, max( prev + i, cur)
        return cur