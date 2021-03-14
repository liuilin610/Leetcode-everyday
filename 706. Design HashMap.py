class MyHashMap:
    # Adjustable size linked list
    def __init__(self):
        self.mod = 1009
        self.table = []* 1009    

    def put(self, key: int, value: int) -> None:
        k = key % self.mod
        self.table[k].append([key, value])

    def get(self, key: int) -> int:
        k = key % self.mod
        for item in self.table[k]:
            if item[0] == key: return item[1]
        return -1

    def remove(self, key: int) -> None:
        k = key % self.mod
        for i, item in enumerate(self.table[k]):
            if item[0] == key: self.table[k].pop(i)
    # matrix
    def __init__(self):
        self.table = [[-1]* 1000 for i in range(1001)]
        self.mod = 1000
  
    def put(self, key: int, value: int) -> None:
        r, c = key // self.mod, key % self.mod
        self.table[r][c] = value

    def get(self, key: int) -> int:
        r, c = key // self.mod, key % self.mod
        return self.table[r][c]

    def remove(self, key: int) -> None:
        r, c = key // self.mod, key % self.mod
        self.table[r][c] = -1

# lerge table
    def __init__(self):
        self.table = [-1]* 1000001

    def put(self, key: int, value: int) -> None:
        self.table[key] = value

    def get(self, key: int) -> int:
        return self.table[key]

    def remove(self, key: int) -> None:
        self.table[key] = -1