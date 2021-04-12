class Solution:
    def findAnagrams(self, s: str, p : str) -> List[int]:
        # III two pointer & stack/ queue
        lp, ls, res = len(p), len(s), []
        if ( lp > ls): return []

        p_ct = [0]* 26
        s_ct = [0]* 26

        for i in range(lp):
            p_ct[ord(p[i]) - ord('a')] += 1
            s_ct[ord(s[i]) - ord('a')] += 1
        
        if ( s_ct == p_ct): res.append(0)

        for i in range(lp, ls):
            s_ct[ord(s[i]) - ord('a')] += 1
            s_ct[ord(s[i - lp]) - ord('a')] -= 1
            if ( s_ct == p_ct) : res.append( i - lp + 1)
        return res

        # brute force
        ls, lp = len(s), len(p)
        p = "".join( sorted(p))
        res = []

        for i in range(ls - lp + 1):
            if ( "".join(sorted(s[i: i + lp])) == p):
                res.append(i)
        return res

        # Time Complexity : O(N)
        res = []
        lp = len(p)
        cp = Counter(p)
        cs = Counter(s[: lp - 1])
        i = 0

        while i + lp < = len(s):
            cs[s[i + lp - 1]] += 1
            if ( cs == cp):
                res.append(i)
            cs[s[i]] -= 1
            if (cs[s[i]] == 0):
                del cs[s[i]]
            i += 1
        return res

        # III