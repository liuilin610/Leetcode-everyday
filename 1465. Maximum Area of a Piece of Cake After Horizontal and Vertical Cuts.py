#Time :(O(Nh log(Nh)+ Nw log(Nw) )); Space:O(1)
class Solution:
    def maxArea(self, h: int, w: int, hC: List[int], vC: List[int]) -> int:
        hC.sort()
        vC.sort()
        hC =  hC + [h]
        vC =  vC + [w]
        nh, nv = len(hC), len(vC)
        h0, v0 = hC[0], vC[0]
        for i in range(1, nh):
            h0 = max(h0, hC[i] - hC[i-1])
        for j in range(1, nv):
            v0 = max(v0, vC[j])
        return h0*v0/(10**9 +7)

