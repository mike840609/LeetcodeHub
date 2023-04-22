class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G = defaultdict(list)
        
        for x, y, v in flights:
            G[x].append((y, v))
        
        h = [(0, 0, src)]
        visted = set()
        while h:
            d, curk, v = heapq.heappop(h)
            if v == dst: return d 
            if (v, curk) in visted or curk > k: continue
            
            visted.add((v,curk))
            
            for w, cost in G[v]:
                heappush(h, (d+cost, curk+1, w))
            
        return -1