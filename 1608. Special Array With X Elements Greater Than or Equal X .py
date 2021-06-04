#Time: O(NlogN)
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n  = len(nums)
        nums.sort()
        nums.insert(0, -1)
        for i in range(1, n + 1):
            if (nums[i-1] < n+1 - i <= nums[i]):
                return n + 1 - i
        return -1