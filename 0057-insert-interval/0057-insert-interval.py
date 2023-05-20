class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval)
        
        s, e = newInterval
        
        res = [] 
        
        for i, (x, y) in enumerate(intervals):
            if x > e:
                res += intervals[i:]
                return res 
            elif res and x <= res[-1][-1]:
                res[-1][-1] = max(res[-1][-1], y)
            
            else:
                res.append([x,y])
        return res
                