#Time : O(N); Space: O(1)
class Solution:
    def checkValidString(sef, s: str ) -> bool:
        a,b = 0, 0

        for i in s:
            if ( i == '(' ):
                a += 1
                b += 1
            elif ( i == ')' ):
                a -= 1
                b = max(0, b - 1)
            else:
                a += 1
                b = max(0, b - 1)
            if ( a < 0 ): return False
        return (b == 0)