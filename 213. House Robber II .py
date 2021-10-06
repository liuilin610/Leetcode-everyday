# Time: O(n), Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if ( len(nums) == 1 ): return nums[0]
        def rob_max ( nums ):
            n = len(nums)
            if ( n == 0 ): return 0
            dp = [0] * ( n + 1 )
            dp[0], dp[1] = 0, nums[0]
            for i in range( 2, n + 1 ):
                dp[i] = max( dp[i - 1], dp[i - 2] + nums[i - 1] )
            return dp[n]
        return max ( rob_max(nums[1:]), rob_max(nums[:-1]) )

# Time: O(n); Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_max(nums: List[int]) -> int:
            prev, cur = 0, 0
            for i in nums:
                prev, cur = cur, max(prev + i , cur )
            return cur
        return max( rob_max( nums[1:]), rob_max(nums[:-1])) if (len(nums) != 1 ) else nums[0]
