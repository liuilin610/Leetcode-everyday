# Time: O (N)
# Space: O(N)
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        res, pre = 0, 0
        presum = {0: -1}

        for i in range( len(nums) ):
            pre += nums[i]
            # count the longest one, so not replace the first presum[pre]
            if ( pre not in presum ):
                presum[pre] = i
            if ( ( pre - k ) in presum ):
                res = max( res, i - presum[pres-k] )
        return res