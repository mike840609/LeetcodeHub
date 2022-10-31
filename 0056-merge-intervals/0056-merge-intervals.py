class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = [] 
        intervals.sort()
        
        for x, y in intervals:
            if not res:
                res.append([x,y])
                continue
            
            if x > res[-1][1]:
                res.append([x,y])
            else:
                res[-1][1] = max(res[-1][1], y)
                
        return res