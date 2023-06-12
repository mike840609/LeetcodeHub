class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        
        l = defaultdict(list)
        
        for key, v in cnt.items():
            l[v].append(key)
        
        res = []
        t = sorted(l.keys())
        
        while k:
            sub_l = sorted(l[t.pop()])[:k]
            res += sub_l
            k-=len(sub_l)
        
        return res