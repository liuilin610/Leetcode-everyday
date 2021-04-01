class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if ( n < m *  k ) : return -1
        
        def Bouquet( day, start, end ):
            initial = start
            res = 0
            for i in range( start, end + 1 ):
                if bloomDay[i] > day: 
                    res += (i - initial) // k
                    initial = i + 1
            res += (end - initial) // k
            return res

        R, L = max(bloomDay), min(bloomDay)
        while ( L < R ):
            mid = ( R + L) // 2
            if Bouquet(mid, 0, n - 1) >= m:
                R = mid
            else:
                L = mid + 1
        return L