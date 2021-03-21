class Solution:
    def hammingWeight(self, n:int) -> int
    '''
    Function takes an unsigned integer and returns the number of '1' bits that it has.
    '''
    res = 0
    while n > 0:
        nmod = n % 2
        res += nmod
        n = n//2
    return res