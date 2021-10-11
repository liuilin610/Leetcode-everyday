# Time : O( N); Space: O(1)
class Solution:
    def findDerangement(self, n: int) -> int:
        f0, f1 = 1, 0

        if ( n == 1 ) : return 0

        for i in range( 2, n + 1 ):
            f0, f1 = f1, ( n - 1 ) * ( f0 + f1 ) % ( 10 ** 9 + 7 )
        return f1
