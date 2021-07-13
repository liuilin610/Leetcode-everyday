class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        nf = target[-1]
        res = []

        for i in range(nf):
            res.append("Push")
            if ( ( i + 1 ) not in target ):
                res.append("Pop")
        return res