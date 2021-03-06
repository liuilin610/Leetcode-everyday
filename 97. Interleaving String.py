# Time: O(n1+n2)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        import functools
        n1, n2, n3 = len(s1), len(s2), len(s3)
        @functools.lru_cache(None)

        def dfs(i, j, k):
            if ( i == n1 ) and ( j == n2 ) and (k == n3): return True
            if ( k < n3 ):
                if ( i < n1 ) and ( s1[i] == s3[k] ) and (dfs(i+1, j, k+1)): return True
                elif (j < n2 ) and ( s2[j] == s3[k] ) and dfs(i, j+1, k+1): return True
            return False
        return dfs(0, 0, 0)

#dp
# Time: O(n1+n2); Space(n1*n2)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if ( n1 + n2 != n3): return False

        dp = [[False]* (n2 + 1) for i in range(n1 + 1)]
        dp[0][0] = True

        for i in range(1, n1 +1):
            dp[i][0] = (dp[i-1][0] and s1[i-1] == s3[i-1] )

        for j in range(1, n2+1):
            dp[0][j] = ( dp[0][j-1] and s2[j-1] == s3[j-1])

        for i in range(1, n1 + 1):
            for j in range(1, n2+1):
                dp[i][j] = ( dp[i-1][j] and s1[i-1] == s3[i + j -1]) or ( dp[i][j-1] and s2[j-1] == s3[i+ j -1])

        return dp[-1][-1]