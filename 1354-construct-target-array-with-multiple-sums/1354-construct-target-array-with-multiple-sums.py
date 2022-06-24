class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        h = [] 
        A = [-x for x in target]
        heapq.heapify(A)
        
        while True:
            a = - heapq.heappop(A)
            
            total -= a
            
            # see case of [1,1000000000]
            if a == 1 or total ==1: return True 
            
            # [1, 1, 1, 2], 
            # [2]
            # [8, 4]
            if a < total or total == 0 or a % total == 0 :
                return False 
            
            a %= total 
            total += a 
            heapq.heappush(A, -a)
                
        
        
        
        