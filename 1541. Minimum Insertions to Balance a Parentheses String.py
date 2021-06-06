#Time: O(n); Space: O(1)
class Solution:
    def minInsertions(self, s: str) -> int:
        res = tmp = 0
        for c in s:
            # for previous net case: "()"
            if (c == '(' ):
                if (tmp % 2):
                    tmp -= 1
                    res += 1
                tmp += 2
            # for previous net result: "))"
            elif ( c == ")" ):
                tmp -= 1
                if ( tmp < 0 ):
                    tmp += 2
                    res += 1
        return res + tmp