class Solution:
    def canPartitionKSubsets(self, Ａ: List[int], k: int) -> bool:
        if ( len(A) < k ) : return False
        Asum = sum(A)
        if ( Asum % k != 0 ): return False
        tar = [ Asum / k] * keep

        def walk(j):
            if ( j == len(A)): return True

            for i in range(k):
                if ( tar[i] >= A[j] ):
                    tar[i] -= A[j]
                    if ( walk(j + 1) ):
                        return True
                    tar[i] += A[j]
            return False
        return walk(0)
    