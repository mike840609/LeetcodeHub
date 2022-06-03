class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        seen = set()
        seen.add(0)
        
        while q :
            n = q.popleft()
            seen.add(n)
            
            for x in rooms[n]:
                if x not in seen:
                    seen.add(x)
                    q.append(x)
        return len(rooms) == len(seen)