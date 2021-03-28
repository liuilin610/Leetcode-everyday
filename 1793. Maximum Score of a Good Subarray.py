class Solution:
    def maximumScore(self, nums: List[int], k: int ) -> int:
        # 97% time performance in python3 
        # two pointers start from nums[k]
        Lend, Rend, n = k, k, len(nums)
        res = nums[k]

        while True:
            while ( Rend < n ) and ( nums[Rend] >= nums[k] ):
                Rend += 1
            while ( Lend >= 0 ) and ( nums[Lend] >= nums[k] ):
                Lend -= 1
            res = max ( res, nums[k] * ( Rend - Lend - 1 ) )
            if ( Lend < 0 ) and ( Rend > n - 1 ):
                break
            if ( Lend >= 0 ) and ( Rend < n ):
                nums[k] = max( nums[i], nums[j] )
            elif ( Rend == n):
                nums[k] = nums[Lend]
            else:
                nums[k] = nums[Rend]
        return res

        # move two pointer to the larger one first and compare the max score everytime

        Lend, Rend, n = k, k, len(nums)
        res = MinN = nums[k]

        while ( Lend > 0 ) or ( Rend < n - 1 ):
            if ( nums[i - 1] if i else 0 ) > ( nums[j + 1] if j < n - 1 else 0):
                i -= 1
            else:
                j += 1
            MinN = min ( MinN, nums[i], nums[j])
            res = max( res, MinN * ( j - i + 1 ) )
        return res
