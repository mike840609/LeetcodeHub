class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cnt = Counter()
        q = deque()
        out = defaultdict(list)
        
        for course, pre in prerequisites:
            cnt[course] += 1
            out[pre].append(course)
            
        
        for course in range(numCourses):
            if cnt[course] == 0 :
                q.append(course)
        
        res = []
        while q:
            course = q.popleft()            
            res.append(course)
            for c in out[course]:
                cnt[c] -= 1
                if cnt[c] == 0:
                    q.append(c)
        return res if len(res) == numCourses else []