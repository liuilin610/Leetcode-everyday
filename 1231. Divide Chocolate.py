class Solution:
    def maximizeSweetness(self, A: List[int], K: int) -> int:
        def cut(nums, sweet):
            n = len(nums)
            res = ct = 0
            for a in nums:
                res += a
                if (res >= sweet ):
                    ct += 1
                    res = 0
            return ct

        L, R = 1, sum(A)//(K+1)

        while ( L < R ):
            mid = ( L + R + 1)// 2
            if ( cut(A, mid) > K ):
                L = mid -1
            else:
                R = mid
        return R

