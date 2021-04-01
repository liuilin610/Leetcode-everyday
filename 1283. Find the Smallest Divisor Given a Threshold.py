class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        if ( sum(nums) <= threshold ): return 1
        if ( n == threshold) : return max(nums)

        L, R = max(1, sum(nums) // threshold), max(nums)
        while ( L < R ):
            mid = ( L + R )// 2
            if ( sum((num - 1) // mid + 1 for num in nums) > threshold ):
                L = mid + 1
            else:
                R = mid
        return L