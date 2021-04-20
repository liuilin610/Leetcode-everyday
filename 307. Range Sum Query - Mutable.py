# segment tree, Binary indexed tree
# the tree index i += i & -i
# presum: i -= i & -i
class NumArray:
    def __init__(self, nums: List[int]):
        self.Arr = nums
        self.n = len(nums)
        self.s_tree = [0] * ( self.n + 1)
        for i, num in enumerate( nums, 1):
            self.s_update( i, num)
    
    def update(self, i: int, val: int):
        self.s_update(i + 1, val - self.Arr[i])
        self.Arr[i] = val
    
    def sumRange(self, i: int, j: int) -> int:
        return ( self.s_sum(j + 1) - self.s_sum(i) )
        
    def s_update(self, i, val):
        while ( i <= self.n ):
            self.tree[i] += val
            i += i & -i
        
    def s_sum(self, i):
        res = 0
        while ( i > 0 ):
            res += self.s_tree[i]
            i -= i & -i
        return res
        
#I
class NumArray:

    def __init__(self, nums: List[int]):
        self.Arr = nums

    def update(self, index: int, val: int) -> None:
        self.Arr[index = val]
    
    def sumRange(self, left: int, right: int) -> int:
        return ( sum(self.Arr[left, right + 1]))