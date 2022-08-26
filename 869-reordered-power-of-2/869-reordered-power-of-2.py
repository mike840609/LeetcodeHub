class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 2^n < 10**9, n smaller than 30, no need to use set 
        res = []                                    
        for i in range(30):
            res.append(str(sorted(str(1 << i))))
        
        return str(sorted(str(n))) in res