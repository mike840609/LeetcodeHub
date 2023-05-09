class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix and matrix[0]:
            res += matrix.pop(0)
            
            if matrix and matrix[0]:
                res += [l.pop() for l in matrix]
            
            if matrix and matrix[0]:
                res += matrix.pop()[::-1]
            
            if matrix and matrix[0]:
                res += [l.pop(0) for l in matrix[::-1]]
        
        return res
                