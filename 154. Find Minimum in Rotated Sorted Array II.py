class Solution:
    def findMin(self, nums: List[int]) - > int:
        n = len(nums)
        L, R = 0, n - 1
        while (L < R):
            mid = ( L + R) // 2
            if ( nums[L] < nums[R]): return nums[L]
            elif (nums[mid] < nums[R]):
                R = mid
            elif ( nums[mid] > nums[R]):
                L = mid + 1
            else:
                R = R - 1
        return L
        