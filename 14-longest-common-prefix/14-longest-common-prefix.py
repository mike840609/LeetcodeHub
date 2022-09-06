class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        s = strs[0]
        
        res = ''
        for c in s:
            res += c 
            for ss in strs:
                if ss[:len(res)] != res:
                    return res[:-1]
        return res
        