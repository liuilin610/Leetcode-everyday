class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time Complexity : O ( Nlog (M)) ; M: max(piles)
        L, R, n = 1, max(piles), len(piles)
        def Hour(number):
            return sum ( (num - 1) // number + 1 for num in piles)
        
        while ( L < R):
            mid = ( L + R ) // 2
            if ( Hour(mid) > h ) :
                L = mid + 1
            else:
                R = mid
        return L
