class Solution:
    def findPeak(self, nums: List[int]) -> int:
        n = len(nums)
        L, R = 0, n - 1

        while ( L < R ):
            mid = ( L + R ) // 2
            if ( nums[mid]  < nums[mid + 1]):
                L = mid + 1
            else:
                R = mid
        return L