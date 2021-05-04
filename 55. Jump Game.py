class Solution:
    def canJump(self, nums: List[int] ) -> bool:
        # backtracking
        # Time: O(N); Space: O(N)
        n = len(nums)
        k = n - 1
        for i in range( k-2, -1, 0):
            if nums[i] >= k - i: k = i
        return k == 0