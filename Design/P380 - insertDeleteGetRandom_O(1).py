# We can use directly set for insert and remove to get O(1) but getRandom will be O(n)
# since to get random.choice we need to convert set to list which will take O(n)

# Hence we will have to use a dictionary to access elements in O(1) by tracking indexes and maintain an array to save data
from random import choice
class RandomizedSet:
    def __init__(self):
        self.indexDict = {}
        self.randomArr = []

    def insert(self, val: int) -> bool:
        if val in self.indexDict:
            return False
        self.indexDict[val] = len(self.randomArr)
        self.randomArr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexDict:
            return False
        idx = self.indexDict[val]
        last = self.randomArr[-1]
        self.randomArr[idx] = last
        self.indexDict[last] = idx
        del self.indexDict[val]
        self.randomArr.pop()
        return True
        
        
        
    def getRandom(self) -> int:
        return choice(self.randomArr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()