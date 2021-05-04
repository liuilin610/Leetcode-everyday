# Time: O(N); Space: O(3)
class Solution:
    def jump(self, nums: List[int] ) -> int:
        n = len(nums)
        kmax, step, ct = 0, 0, 0

        for i in range(n-1):
            kmax = max(kmax, i + nums[i] )
            if (i == step):
                step = kmax
                ct += 1
        return ct
                