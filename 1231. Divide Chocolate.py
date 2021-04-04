class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        n = len (sweetness)
        L, R = min(sweetness), sum(sweetness)
        def sweety(sweet, Length):
            ct, res = 0, 0
            for i in range(n):
                if ( res + sweetness[i] >= sweet ):
                    res = 0
                    ct = 0
                else:
                    res += sweetness[i]
            return (ct + 1 if (res != 0) else ct )
            
        while ( L < R ):
            mid = ( L + R ) // 2
            if sweety(mid, n) > K:
                L = mid + 1
            else:
                R = mid
        return L