class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        res, prefix, dp = len(nums), 0, {0: -1}

        for i, c in enumerate(nums):
            prefix = (prefix + c) % p
            dp[prefix] = i
            if ( ((prefix -target) % p) in dp ):
                res = min ( res, i - dp[((prefix - target) % p)])
        return res if ( res < len(nums)) else -1