# Time; O(N)
# Space: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = presum = 0
        dicpre = collection.Counter({0: 1})

        for i in nums:
            presum += i
            res += dicpre[presum - k]
            dicpre[presum] += 1
        return res

# Time: O(N)
# Space: O(N)
# dictionary
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = presum = 0
        dicpre = {0: 1}

        for i in nums:
            presum += i
            if ( presum - k in dicpre ):
                res += dic[presum - k]
            if (presum in dicpre ):
                dicpre[presum] += 1
            else:
                dicpre[presum] = 1
        return res
            

