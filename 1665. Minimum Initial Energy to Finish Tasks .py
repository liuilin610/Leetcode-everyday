class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key= lambda a: a[1] -a[0])
        res = 0
        for i, f in tasks:
            res = max(res+ i, f)
        return res