class Solution:
    def searchRanch(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if ( n == 0): return [-1, -1]

        # search left end
        L, R = 0, n - 1 
        while ( L < R ):
            mid = ( L + R ) // 2
            if ( nums[mid] < target ):
                L = mid + 1
            else:
                R = mid
        left = L
        # check if no target in nums
        if ( nums[left] ! = target ): return [-1, -1]

        # search right end
        L , R = left, n - 1
        while ( L < R ):
            mid = ( L + R ) // 2
            if ( nums[mid] > target ):
                R = mid
            else:
                L = mid + 1
        right = L

        # we could find the lower bound, nums[right] >= target or the upper bound of nums[right] = target
        if ( nums[right] != target ): 
            return [left, right - 1]
        else: return [left, right]
