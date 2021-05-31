# Time(10N)-test for single odd number
#space: O(1024)
class Solution:
    def longestAwesome(self, s: str) -> int:
        res, prefix, n = 0, 0, len(s)
        dp = [-1] + [n]* 1023

        for i, c in enumerate(s):
            prefix ^= (1 << int(c))
            # occurance for all digits with even occurances 
            res = max(res, i - dp[prefix])
            # flip the even/odd for one odd digit (palindrome)
            for j in range(10):
                res = max(res, i - dp[prefix ^ (1 << j)])
            dp[prefix] = min(i, dp[prefix])
        return res
        