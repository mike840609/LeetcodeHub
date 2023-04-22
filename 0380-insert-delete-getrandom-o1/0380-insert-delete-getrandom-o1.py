class RandomizedSet:

    def __init__(self):
        self.nums = [] 
        self.d = {}

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.nums.append(val)
            self.d[val] = len(self.nums)-1
            return True         
        return False 
        

    def remove(self, val: int) -> bool:
        if val in self.d:
            idx = self.d[val]
            last = self.nums[-1]
            
            self.nums[idx], self.d[last] = last, idx
            
            self.nums.pop()
            self.d.pop(val)            
            return True        
        return False 
        

    def getRandom(self) -> int:
        return self.nums[random.randint(0,len(self.nums)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()