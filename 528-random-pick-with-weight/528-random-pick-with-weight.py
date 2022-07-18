class Solution:

    def __init__(self, w: List[int]):        
        self.s = sum(w)
        self.arr = list(accumulate(w))                                
        
    

    def pickIndex(self) -> int:
        num = random.randint(1, self.s)
        l, r = 0, len(self.arr) - 1
        
        while l < r :
            m = l + (r-l) // 2
            
            if num <= self.arr[m]:
                r = m 
            else:
                l = m + 1
        return l 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()