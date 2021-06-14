# Time: ( O(Nlog(M))); M = post[-1] - post[0]
class Solution:
    def maxDistance(self, post: List[int], m: int) -> int:
        post.sort()
        n = len( post)

        def count (d):
            res, cur = 1, post[0]
            for i in range( 1, n ):
                if ( post[i] - cur >= d ):
                    res += 1
                    cur = post[i]
            return res


        L, R = 0, post[-1] - post[0]
        while ( L < R ):
            mid = ( L + R + 1) // 2
            if ( count(mid) >= m ):
                L = mid
            else:
                R = mid - 1
        return L