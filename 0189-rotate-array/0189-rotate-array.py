class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        k = k % l
        e = len(nums)-1
        for i in range((l-k), l-k+(k//2)):
            nums[i], nums[e] = nums[e], nums[i]
            e -= 1
        # print(nums)
        
        e = l - k - 1
        for i in range(0, (l-k)//2):
            nums[i], nums[e] = nums[e], nums[i]
            e -= 1
        # print(nums)
        
        for i in range(len(nums)//2):
            nums[i], nums[l-i-1] = nums[l-i-1], nums[i]
        
        # print(nums)
            