#Time : O(N**2); Space: O(N)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prexor = [0]
        res, n = 0, len(arr)

        for i in range(n):
            prexor.append (prexor[-1]^arr[i])
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                if ( prefix[i-1] = prefix[j]):
                    res = j - i
        return res
       

#Time: O(N); Space: O(N)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ct, totalct = Counter(), Counter()
        res = prexor = 0

        for i, c in enumerate(arr):
            ct[prexor] += 1
            totalct[prexor] += i
            prexor ^= c
            if ( prexor in ct ):
                res += i*ct - totalct
        return res