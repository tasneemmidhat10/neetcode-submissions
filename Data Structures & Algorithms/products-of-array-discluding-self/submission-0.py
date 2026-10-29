class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        prefixarr =[0] * len(nums)
        suffixarr = [0] * len(nums)
        res = [0] * len(nums)
        n = len(nums)
        prefixarr[0] = suffixarr[n-1] = 1

        for i in range(1, n):
            prefixarr[i] = prefixarr[i-1] * nums[i-1]
        
        for j in range(n-2, -1, -1):
            suffixarr[j] = suffixarr[j+1] * nums[j+1]

        for i in range(n):
            res[i] = prefixarr[i] * suffixarr[i]
        return res
        