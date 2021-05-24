# Time( 2**N)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvalid(s):
            ct = 0
            for c in s:
                ct +=  (c == '(' ) - ( c == ')' )
                if ( ct < 0 ):
                    return False
            return ct == 0

        level = {s}
        while True:
            valid = filter(isvalid, level)
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}