class Solution:
    def merge(self, List1: List[List[int]]) -> List[List[int]]:
        n = len(List1)
        List.sort(key = lambda u:( u[0], -u[1]))
        res = [List1[0]]

        for i in range(1, n):
            if ( res[-1][1] >= List1[i][0] ):
                L, H = min(res[-1][0], List1[i][0]), max(res[-1][1], List1[i][1])
                res.pop()
                res.append([L, H])
            else:
                res.append(List1[i])
        return res