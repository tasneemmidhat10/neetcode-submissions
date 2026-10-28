class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexMap = {v: i for i, v in enumerate(nums)}

        for i in range(len(nums)):
            x = target - nums[i]
            if x  in indexMap.keys() and i != indexMap[x]:
                return sorted([i, indexMap[x]])
            
        