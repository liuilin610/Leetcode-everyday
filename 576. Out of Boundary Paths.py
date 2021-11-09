# DFS + memory
#Time: O(N*m*n); Space: O(m*n*N)
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        @lru_cache(None)
        def dfs(i, j, N):
            if ( i < 0 ) or ( j < 0 ) or ( i >= m ) or (j >= n ):
                return 1
            if ( N == 0 ):
                return 0
            return dfs( i-1, j, N-1 ) + dfs( i, j-1, N-1 ) + dfs( i+1, j, N-1 ) + dfs( i, j+1, N-1 )
        
        return dfs(i, j, N ) %(10**9 + 7)

#dp
# Time: O(N*n*m); Space: O(N*m*n)
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[[0] * (n+2) for _ in range(m+2)] for _ in range(N+1)]

        for r in range(m+2):
            dp[0][r][0] = 1
            dp[0][r][n+1] = 1

        for c in range(n+2):
            dp[0][0][c] = 1
            dp[0][m+1][c] = 1

        for k in range(1, N+1):
            for r in range(1, m+1):
                for c in range(1, n+1):
                    dp[k][r][c] = dp[k-1][r-1][c] + dp[k-1][r][c-1] + dp[k-1][r+1][c] + dp[k-1][r][c+1]

        res = 0
        for k in range(1, N+1):
            res += dp[k][i+1][j+1]
        return res % (10**9 + 7)
        

