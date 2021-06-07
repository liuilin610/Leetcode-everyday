#Time; O(N); Space: O(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0 

        for s in nums:
            if ( s- 1 not in nums):
                t = s + 1
                while ( t in nums ):
                    t += 1
                res = max(res, t-s)
        return res
        