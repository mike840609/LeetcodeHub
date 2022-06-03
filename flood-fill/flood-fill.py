class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        color = image[sr][sc]
        q = deque([])
        q.append((sr, sc))
        seen = set()
        
        while q :
            i, j = q.popleft()
            seen.add((i,j))
            image[i][j] = newColor
            
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < m and 0 <= y < n and image[x][y] == color and (x,y) not in seen:
                    q.append((x,y))
        return image