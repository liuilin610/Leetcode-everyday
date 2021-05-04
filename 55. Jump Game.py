class Solution:
    def canJump(self, nums: List[int] ) -> bool:
        # backtracking
        # Time: O(N); Space: O(1)
        n = len(nums)
        k = n - 1
        for i in range( k-2, -1, 0):
            if nums[i] >= k - i: k = i
        return k == 0

#greedy
#Time: O(N), Space: O(1)
class Solution:
    def canJump(self, nums: List[int] ) -> bool:
        k = 0
        for i, n in enumerate(nums):
            if k < i: return False
            k = max(k, n + i )
        return True