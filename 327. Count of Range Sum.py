# similar as 315

# presum + hashmap
# O(n + (upper - lower + 1)*n)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presum = [0]
        for i in nums:
            presum.append(presum[-1] + i)

        record = collections.defaultdict(int)
        res = 0

        for psum in presum:
            for target in range(lower, upper + 1):
                if ( psum - target in record ):
                    res += record[psum - target]
            record[psum] += 1
        return res
            