class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # C(m+n-2, m-1) = C(m+n-2, n-1) = (m+n-2)! / (m-1)! / (n-1)!.
        return factorial(m+n-2) // factorial(m-1) // factorial(n-1)