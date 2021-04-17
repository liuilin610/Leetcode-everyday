class SnapshotArray:
#
    def __init__(self, length: int):
        self.Arr = [{} for i in range(length) ]
        self.snap_id = 0

    def set(self, index, val):
        self.Arr[index][self.snap_id] = val

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        if snap_id = self.Arr[index]:
            return self.Arr[index][snap_id]
        lastval = 0
        for i in range(self.snap_id):
            if i in self.Arr[index]:
                return self.Arr[index][i]
            if i >= snap_id:
                return lastval
        return lastval

# 
    def __init__(self, length: int):
        self.Arr = [[[-1, 0]] for i in range(length) ]
        self.snap_id = 0
        
    def set(self, index, val):
        self.Arr[index].append([self.snap_id, val])
        
    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1
            
    def get(self, index, snap_id):
        i = bisect.bisect(self.Arr[index], [self.snap_id + 1]) - 1
        return self.Arr[index][i][1]
        