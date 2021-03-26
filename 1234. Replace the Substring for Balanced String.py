class Solution:
    def balancedString(self, s:str) -> int:
        count = collections.Counter(s)
        n = len(s)
        res = n
        i = 0
        for k, value in enumerate(s):
            count(value) -= 1
            while (i < n) and all( n / 4 >= count[value] for value in 'QWRE'):
                res = min(res, k - i + 1)
                count(s[i]) += 1
                i += 1
        return res