class Solution:
    def minmaxGasDist(self, st: List[int], K : int) -> int:
        st = st.sort()
        L, R = 0, ( st[-1] - st[0] )

        # while we calculate the number of additional stations between two neighboring station,
        # we remove a small distance gap ( 10 ** ( -6 )) to prevent  floor devide cases
        def stcount(distance, length):
            ct = 0
            for i in range(n - 1):
                ct += (st[i + 1] -st[i] - 10 ** ( -6) ) // distance
            return ct > K

        # the difference between L and R( two gas station could be less than 1), 
        # so we select mid = ( R + L )/ 2
        # also the binary search change the next L and R to mid
        while ( L < R ):
            mid = ( L + R )/ 2
            if stcount(mid, n):
                L = mid 
            else:
                R = mid
        return L