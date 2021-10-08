#Time: O(N), Space: O(M)
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        m = max(nums)
        dp = [0] * (m + 1)
        for i in nums:
            dp[i] = dp[i] + i
        
        pre, cur = 0, dp[0]
        for j in dp:
            pre, cur = cur, max(cur, pre + j)
        return cur