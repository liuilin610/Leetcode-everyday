class Solution:
    def shipWithDays(self, weights: List[int], D: int ) -> int:
        n, Sumweights, Maxweights = len(weights), sum(weights), max(weights)
        if ( D == 1 ): return Sumweights
        if ( D == n ): return Maxweights

        def capacity( capacity, Length):
            res, ct = 0, 0
            if ( res + weights[i] < capacity):
                res += weights[i]
            elif ( res + weights[i] == capacity):
                ct += 1
                res = 0

            else:
                ct += 1
                res = weights[i]
        return (ct + 1 if (res != 0) else ct)

        L, R = Maxweights, Sumweights
        while ( L < R ):
            mid = ( L + R ) // 2
            if capacity(mid, n) > D:
                L = mid + 1
            else:
                R = mid
        return L

