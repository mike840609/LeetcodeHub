class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        res = 0         
        rows, cols = set(), set()
        
        for t, i, v in queries[::-1]:               
            if t == 0:                
                if i in rows: continue                
                rows.add(i)
                res += v * (n - len(cols))
                                            
            if t == 1:
                if i in cols: continue                
                cols.add(i)                                
                res += v * (n - len(rows))
                
        return res      