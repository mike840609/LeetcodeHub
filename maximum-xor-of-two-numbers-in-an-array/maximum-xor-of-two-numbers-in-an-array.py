class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie, ans = {}, 0
        length = max(nums).bit_length()
        for n in nums:
            curr = opposite = trie
            for c in f'{n:b}'.zfill(length):
                curr.setdefault(c, {})
                curr = curr[c]
                opposite = opposite.get(str(1-int(c))) or opposite.get(c)
                
            curr['$'] = n            
            ans = max(ans, n ^ opposite['$'])
        return ans
            
            
            
            