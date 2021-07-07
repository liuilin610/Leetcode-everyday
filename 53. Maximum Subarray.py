# Time: O(N)
# Space: O(2)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = res = nums[0]

        for i in range(1, len(nums) ):
            pre = max(nums[i], nums[i]+ pre )
            res = max(res, pre)
        return res