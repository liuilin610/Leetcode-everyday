#Time :( O(log(R)) )
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def height(a):
            res = 0
            # index = 0
            b = max( 0, a - index )
            res += ( a + b ) * ( a - b + 1 ) / 2
            # index = n - 1
            b = max ( a - ( n - index - 1 ), 0 )
            res += ( a + b ) * ( a - b + 1 ) / 2
            # -a, since we remove a from maxSum first
            return res - a 

        L, R = 0, maxSum - a
        while ( L < R ):
            mid = ( L + R + 1 ) // 2
            if ( height(mid) <= maxSum ):
                L = mid 
            else:
                R = mid - 1
        return L + 1
