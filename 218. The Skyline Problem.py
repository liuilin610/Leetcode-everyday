class Solution:
    def getSkyline(self,  buildings: List[List[int]]):
        '''
        1. combine the same height buildings as the same rctangle.
        2. record the height and return the maximum height if mutiple buildings overlap.
        3. consider the edge cases if two neighboring building with different heights 
        '''

        # 1. combine the buildings with the same height 
        n = len(buildings)
        buildings.sort( key = lambda u:( u[0] ))
        for i in range(n-1, 0, -1):
            if (buildings[i][2] == buildings[i-1][2]) and (buildings[i][0] <= buildings[i-1][1]):
                buildings[i-1][1] = buildings[i][1]
                buildings.pop(i)

        #2. record the beginning and end of the buildings
        # position[i][2] = 0 : beginning; position[i][2] = 1 : end
        positions = []

        for x1, x2, y1 in buildings:
            positions.append(x1, y1, 0)
            positions.append(x2, y1, 1)
        positions.sort( key = lambda, u:( u[0] ))

        # set the initial start : [-1, 0, 0]; 
        # preset to store the mutiple heights, we prestore zero as the default
        tmp = [-1, 0, 0]
        res = []
        preset = [0]
        for i in range(len(positions)):
            # input the height if we scan the beginning of the building
            # output the height if we finish the end of the building
            if (positions[i][2] == 0):
                preset.append(positions[i][1])
            if (positions[i][2] == 1):
                preset.pop(positions[i][1])

            # 3 edge cases if two nighboring building with different heights
            if (positions[i][0] == tmp[0]):
                if (positions[i][1] == tmp[1]):
                    res.pop()
                    tmp = positions[i]
                else:
                    res[-1][1] = positions[i][1]
                    tmp = positions[i]

            # record the left cornor if the new higher building pops
            elif (positions[i][1] > tmp[1]):
                res.append([positions[i][0], positions[i][1]])
                tmp = positions[i]

            elif (tmp[2], positions[i][2] == 0, 1) and (positions[i][1] == tmp[1]):
                res.append([positions[i][0], max(preset)])
                tmp = [positions[i][0], max(preset), 0 ]
        return res