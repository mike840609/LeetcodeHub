class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        n = len(arr)        
        A = sorted([[v, k] for k,v in cnt.items()], reverse = True)
        res = 0
        for v, k in A:
            n -= v 
            res += 1
            if n <= len(arr)//2:
                return res
        return res
        
        
        
        
        