class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        slots1.sort(key = lambda u:u[0])
        slots2.sort(key = lambda u:u[0])
        n1, n2 = len(slots1), len(slots2)
        i, j = 0, 0
        while i < n1 and j < n2:
            L = max(slots1[i][0], slots2[j][0])
            H = min(slots1[i][1], slots2[j][1])
            if H - L >= duration:
                return [L, L + duration]
                break
            elif L > H:
                i += 1
            else:
                j += 1
        return []
        '''
        slots1.sort(key = lambda u :(u[0]) )
        slots2.sort(key = lambda u :u[0])
        n1, n2 = len(slots1), slots2
        ct = 0
        for i  in range(n1):
            L, H = slots1[i][0], slots1[i][1]
            if ct < i: break
            for j in range(n2):
                L = max(L, slots2[i][0])
                H = min(H, slots2[i][1])
                if (H-L) >= duration:
                    return [L, Ｌ+duration]
                    break
                elif H < slots2[i][0]:
                    ct += 1
                    break        
            ct +=1
        if ct == n1: return []
        '''
        
