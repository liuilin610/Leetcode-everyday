class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # Time & Space: O(N)
        leaves = set( tuple( map(int, str(i)[:2] )) for i in nums )
        Sums = {}

        for i in sorted(nums):
            a, b, c = [ map(int, i)]
            if ( a == 1 ): Sums[(a, b)] = c
            else:
                parent = (a - 1, (b + 1)//2 )
                Sums[(a, b)] = c + Sums[parent]
                leaves.discard(parent)
        return ( sum(Sums[k] for k in leaves))