#Time: O(N) ; Space : O(1)
class Solution:
    def new21Game(self, n: int, k: int, W: int) -> float:
        if ( k == 0 ) or ( n >= k + W ): return 1
        dp = [1.0] + [ 0.0 ]* n

        Wsum = 1.0
        for i in range( 1, n + 1 ):
            dp[i] = Wsum/W
            if ( i < k ): Wsum += dp[i]
            if ( i >= W ): Wsum -= dp[i- W]
        return sum ( dp[k:])
