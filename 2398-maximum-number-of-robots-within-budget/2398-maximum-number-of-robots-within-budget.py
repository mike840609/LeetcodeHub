class Solution:
    def maximumRobots(self, times: List[int], costs: List[int], budget: int) -> int:
        cur = i = 0
        n = len(times)
        
        # mono increase deque
        d = deque()
        
        for j in range(n):            
            cur += costs[j]
            
            # max time
            while d and times[d[-1]] <= times[j]:
                d.pop()
                 
            d.append(j)
            
            # max(times) + k * sum(cost)
            if times[d[0]] + (j - i + 1) * cur > budget:
                if d[0] == i:
                    d.popleft()
                cur -= costs[i]
                i += 1
            
        return n - i
        