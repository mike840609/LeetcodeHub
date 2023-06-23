class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = defaultdict(list)
        for n in arr:
            cnt = 0 
            t = n
            while n :
                if n & 1 :
                    cnt += 1
                n >>= 1 
            d[cnt].append(t)
        
        
        res = [] 
        for k in sorted(d.keys()):
            res.extend(sorted(d[k]))
        
        return res
            
            