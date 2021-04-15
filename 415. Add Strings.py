class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2, temp = len(num1) - 1, len(num2) - 1, 0
        res = ""
        i, j = n1, n2

        while ( ( i > -1 ) or ( j > -1 ) ):
            s1 = int(num1[i]) if ( i > -1 ) else 0
            s2 = int(num2[j]) if ( j > -1 ) else 0
            sums = s1 + s1 + temp
            res = str(sums % 10 ) + res
            temp = sums // 10
            i -= 1; j -= 1
        return ('1' + res if temp else res)
            