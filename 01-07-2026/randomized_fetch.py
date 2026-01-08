class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set[val] = len(self.list) 
            self.list.append(val)
            return True 
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            idx = self.set[val]
            idx1 = len(self.list) - 1

            val1 = self.list[idx1]

            self.list[idx], self.list[idx1] = self.list[idx1], self.list[idx]
            self.set[val1] = idx 

            del self.set[val]
            self.list.pop() 

            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.list[int(random.random() * (len(self.list)))]
        

# return self.set[len(self.set) * Math.random(1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
