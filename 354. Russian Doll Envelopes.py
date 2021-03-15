class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n < 2: return n
        # take care of the beginning of envelopes
        envelopes = sorted(envelopes)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                # take care of the end of envelopes
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max (dp[i], dp[j]+1 )
        return max(dp)