class MyHashSet:
    # Open hashing
    def __init__(self):
        self.mod = 1000
        self.table = [[] for i in range(self.mod)]

    def add(self, key: int) -> None:
        k = key % self.mod
        if key not in self.table[k]:
            self.table[k].append(key)
    def remove(self, key: int) -> None:
        k = key % self.mod
        if key in self.table[k]:
            self.table.remove(key)
        
    def contains(self, key: int) -> bool:
        k = key % self.mod
        return (key in self.table[k])

# Large enough set
    def __init__(self):
        self.set = [0]* 1000001
    
    def add(self, key: int) -> None:
        self.set[key] = 1
    
    def remove(self, key: int) -> None:
        self.set[key] = 0
    
    def conatins(self, key: int) -> bool:
        return (self.set[key] == 1)