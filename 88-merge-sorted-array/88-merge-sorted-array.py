class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = m - 1
        idx2 = n - 1
        idx = len(nums1) -1
        
        while idx > -1:
            if idx1 < 0:
                nums1[idx] = nums2[idx2]
                idx2 -= 1
            elif idx2 < 0:
                nums1[idx] = nums1[idx1]
                idx1 -= 1
            else:
                n2, n1 = nums2[idx2], nums1[idx1]
                if n2 <= n1:
                    nums1[idx] = n1
                    idx1 -= 1
                else:
                    nums1[idx] = n2
                    idx2 -= 1
            
            idx -= 1
        
        