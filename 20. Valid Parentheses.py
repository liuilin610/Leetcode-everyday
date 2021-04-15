class Solution:
    def isValid(self, s: str) -> bool:
        dictPa = {'(': ')', '[': ']', '{': '}'}
        n = len (s)
        res = []

        for i in range(n):
            if ( s[i] in dictPa ):
                res.append(dictPa[s[i]])
            elif ( ( res == [] ) or ( res.pop() != s[i] ) ):
                return False
        # in case that some cases only include '((', '[[', or '{{'
        return ( res == []) 