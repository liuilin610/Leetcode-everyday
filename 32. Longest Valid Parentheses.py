# Space: O(N); Time: O(N)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp, stack = [0]*(len(s)+ 1), []
        for i in range(len(s)):
            if ( s[i] == '(' ):
                stack.append(i)
            elif stack:
                p = stack.pop()
                dp[i+1] = dp[p] + i - p + 1
        return max(dp)

#Space: O(N); Time:O(N)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res, stack = 0, [-1]
        for i, c in enumerate(s):
            if ( c == '(' ):
                stack.append(i)
            elif (len(stack) > 1 ):
                stack.pop()
                res = max( res, i - stack[-1] )
            # if initial c == ')'
            else:
                stack[0] = i
        return res