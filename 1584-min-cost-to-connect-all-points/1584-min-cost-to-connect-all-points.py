class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        h = [(0, 0)]
        res = 0 
        
        def dis(x,y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        while len(seen) < len(points):
            w, v = heapq.heappop(h)
            if v in seen:
                continue
            
            res += w 
            seen.add(v)
            
            for j in range(len(points)):
                if j not in seen:
                    heapq.heappush(h, (dis(points[v], points[j]), j))
        
        return res 