class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Occur = {}
        if len(nums) == 0 or len(nums) == 1:
            return False
        for i in range(len(nums)):
            if nums[i] in Occur:
                Occur[nums[i]] = True
            else:
                Occur[nums[i]] = False
        
        return any(Occur.values())
        