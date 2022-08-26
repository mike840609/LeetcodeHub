class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = set()
        upper = 10**9
        cur = 1
        while cur < upper:
            s.add(tuple(sorted(str(cur))))
            cur *= 2 
        
        return tuple(sorted(str(n))) in s