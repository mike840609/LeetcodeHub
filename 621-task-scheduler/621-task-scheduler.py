class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        if n == 0 :
            return len(tasks)
        
        
        h = [[-y, x] for x,y in cnt.items()] 
        res = 0 
        heapq.heapify(h)
        
        while h :
            tmp = []
                      
            for _ in range(n+1):
                res += 1
                if h :
                    y, x = heappop(h)
                    if y != -1:
                        tmp.append([y+1, x])
                
                if not h and not tmp:
                    break
            
            for y, x in tmp:
                heappush(h, [y, x])
        return res 
                    
        