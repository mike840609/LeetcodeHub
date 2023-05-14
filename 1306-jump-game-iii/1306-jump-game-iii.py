class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        seen = set()        
        q = deque([start])
        n = len(arr)
        
        while q:
            idx = q.popleft()
            
            if arr[idx] == 0: return True 
            if idx in seen: continue                 
            seen.add(idx)
            
            l, r = idx - arr[idx], idx + arr[idx]                        
            
            if 0 <= l < n:
                q.append(l)
            if 0 <= r < n:
                q.append(r)
        
        return False
            
            
            