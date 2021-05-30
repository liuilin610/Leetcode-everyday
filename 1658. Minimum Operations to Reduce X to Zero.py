#Time: O(N); Space: O(1)
# The sum of left and right ends is x. The sum of the partial perfix sum is sum( nums) - x
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        S = sum(nums) - x
        n = len(nums)
        res, prefix, dp = n + 1, 0, {0: -1}

        for i, c in enumerate(nums):
            prefix += c
            dp [prefix] = i
            if ( prefix - S in dp ):
                res = min ( res, n - ( i - dp[prefix - S]))
        return res if res < n + 1 else -1

