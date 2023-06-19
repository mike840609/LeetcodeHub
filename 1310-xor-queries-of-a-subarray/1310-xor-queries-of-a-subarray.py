class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(arr)-1):
            arr[i+1] ^= arr[i]
        
        return [arr[i-1] ^ arr[j] if i else arr[j] for i, j in queries]