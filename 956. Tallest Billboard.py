# dp
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int

    dp = {0:0}

    for i in rods:
        for k, j in list(dp.items()):
            dp[k + i] = max(dp.get(k + i, 0), j + i)
            dp[k - i] = max ( dp.get(k + i, 0), j )
    return dp[0]

# II
class Solution:
    def tallestBillboard(self, rods: List[int] ) -> int

    dp = {0: 0}
    for i in rods:
        dp1 = dp.copy()
        for k in list(dp1.keys() ):
            dp[ k + i] = max( dp1.get(k + i, 0), dp1[k] + i )
            dp[ k - i] = max(dp1.get(k - i, 0), dp1[k])
    return dp[0]
        