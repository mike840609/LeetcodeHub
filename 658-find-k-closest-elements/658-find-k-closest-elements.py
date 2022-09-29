class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:        
        idx = bisect.bisect_left(arr, x)
        i, j = idx-1, idx
        m = len(arr)
        
        q = deque([])        
        while len(q) < k:
            if i < 0:
                q.append(arr[j])
                j += 1
            elif j >= m:
                q.appendleft(arr[i])
                i-=1
                
            elif abs(x-arr[i]) <= abs(arr[j]-x):
                q.appendleft(arr[i])
                i-=1
            else:
                q.append(arr[j])
                j+=1
        return q