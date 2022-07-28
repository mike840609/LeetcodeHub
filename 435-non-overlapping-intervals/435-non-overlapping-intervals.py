class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:        
        
        end, res = float("-inf"), 0                 
        # print(sorted(intervals, key=lambda x: (x[1], -x[0])))
        for x, y in sorted(intervals, key=lambda x: (x[1], -x[0])):            
            if x < end :
                res += 1            
            else:
                end = y
        
        return res