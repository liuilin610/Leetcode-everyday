class RandomizedSet:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if (val in self.dict):
            return False
        else:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # extract index of val in self.list and the value of self.dict[self.list[-1]]
        if (val in self.dict):
            idx, lastval = self.dict[val], self.list[-1]
            self.list[idx], self.dict[self.list[-1]] = lastval, idx
            self.list.pop(); self.dict.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)

