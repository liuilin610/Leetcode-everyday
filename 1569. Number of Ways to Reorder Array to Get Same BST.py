class Solution:
    def num0Ways(self, nums:List[int]) -> int:
        def f(arr):
            if ( len(arr) < 3): return 1
            left = [v for v in arr if v < arr[0]]
            right = [v for v in arr if v > arr[0]]
            return comb(len(left) + len(right), len(right)) * f(left) * f(right)
        return f(nums) % ( 10 ** 9 + 7) - 1
        