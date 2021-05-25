#Time: O(N); Space:O(N)
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        # memorization dictionary and key '0' is for the presum = S
        dictA = collections.Counter({ 0: 1})
        presum = res = 0

        for i in A:
            presum += i
            # count the amount of partial sum = S = presum[j] - presum[i]
            # presum[i] = presum[j] - S
            res += dictA[presum - S]
            # add count for presum dictionary
            dictA[presum] += 1
        return res

# Time : O(N); Space:(O(1))
#sliding window
# function atmost(S) to count # of subarray ( sum <= S)
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def atmost(A,S):
            if ( S < 0 ): return 0
            res = i= 0
            for j in range(len(A)):
                # move of the first pointer and count the rest of sum : S- A[j]
                S -= A[j]
                # move the second pointer 
                while ( S < 0 ):
                    S += A[i]
                    i += 1
                res += j - i + 1
            return res

        return atmost(S) - atmost(S-1)


