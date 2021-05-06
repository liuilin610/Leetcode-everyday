# Time : O(N); Space: O(1)
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        ct = 0
        for i in range(n - 1):
            if ( nums[i] > nums[i + 1] ):
                ct += 1
                if ( 1 <= i < n - 2) and ( nums[i - 1] > nums[i + 1]) and (nums[i] > nums[i + 2]):
                    return False
        return ( ct <= 1)