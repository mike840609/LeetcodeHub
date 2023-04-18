class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x,y in points:
            heapq.heappush(h, [x**2 + y**2, x, y])
        
        return [heapq.heappop(h)[1:] for _ in range(k)]
            