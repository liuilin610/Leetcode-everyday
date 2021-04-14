class RandomizedCollection:

    def __init_(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = collections.defaultdict(set)
    
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.list.append(val)
        self.dict[val].add( len(self.list) - 1)
        return (self.dict[val] == 1)
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """

        if self.dict[val]:
            idx, lastval = self.dict[val].pop(), self.list[-1]
            self.list[idx] = lastval
            if self.dict[lastval]:
                self.dict[lastval].add( idx)
                self.dict[lastval].discard( len(self.list) - 1 )
            self.list.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.list)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()