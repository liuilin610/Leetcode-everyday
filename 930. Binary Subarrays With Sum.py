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

        #sliding window
        