class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        n = len(paths)
        if n == 1: return paths[1]
        Target, ct, i = paths[0][1], 0, 0
        while paths:
            i += 1
            if i == ct+2: 
                return Target
                break

            for i in range(1, len(paths)):
                if paths[i][0] == Target:
                    Target = paths[i][1]
                    ct += 1
                    del paths[i]
                    break

        #set is faster than hashtable
        '''
        all = set()
        begin = set()
        for path in paths:
            all.add(path[0])
            all.add(path[1])
            begin.add(path[0])
        return (all - end).pop()
        '''