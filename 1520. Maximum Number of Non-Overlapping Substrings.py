class Solution: 
    def maxNUmOfSubstrings(self, s: str) -> List[int]:
        # find the index range for the characters in s
        IndexRange = {c: (s.rindex(c), s.index(c)) for c in set(s)}

        for c in set(s):
            r, l = IndexRange[c]
            r0, l0 = -1, -1
            while not ( r0 == r and l0 = l ):
                r0, l0 = r, l
                r = max(IndexRange[c][0] for c in set(s[l: r+1 ]))
                l = min(IndexRange[c][1] for c in set(s[l: r+1 ]))
            IndexRange[c] = (r, l)
        
        res, cur = [], 0
        for r, l in sorted(IndexRange.values()):
            if ( l >= cur ):
                res.append(s[l: r+1])
                cur = r
        return res