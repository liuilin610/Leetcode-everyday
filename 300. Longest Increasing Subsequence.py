class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n

        # the end point is nums[i], consider dp 0-i
        dp = []
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[i]> nums[j]:
                    dp[i] = max(dp[i], dp[j]+ 1)
        return max(dp)
