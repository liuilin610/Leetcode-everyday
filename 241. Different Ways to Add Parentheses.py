#dfs + memorization
class Solution(object):
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        memo = {}
        if input in memo:
            return memo[input]
        res = []
        for i in range(len(input)):
            if ( input[i] in "*+-" ):
                l = self.diffWaysToCompute(input[:i])
                r = self.diffwaysToCompte(input[i+1:])
                res += [self.helper(j, k, input[i]) for j in l for k in r]
        memo[input] = res
        return res

    def helper(self, l, r, op):
        if ( op == '+' ):
            return l + r
        elif ( op == '-' ):
            return l - r
        else:
            return l * r

# Time : O(N)
class Solution(object):
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return[int(input)]
        res = []
        for i in range(len(input)):
            if (input[i] in "+-*"):
                l = self.diffWaysToCompute(input[:i])
                r = self.diffWaysToCompute(input[i+1:])
                res += [eval( str(j) + input[i] + str(k) ) for j in l for k in r]
        return res
