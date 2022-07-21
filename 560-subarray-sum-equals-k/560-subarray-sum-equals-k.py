class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = list(accumulate([0] + nums))
        
        d = defaultdict(int)
        res = 0 
        for e in l:
            res += d[e-k]
            d[e] += 1
                
        return res 
                
            
            
                    