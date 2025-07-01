class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        d=defaultdict(int)
        for i in range(len(nums)):
            if target-nums[i] in d and d[target-nums[i]]!=i:
                return [d[target-nums[i]],i]
            d[nums[i]]=i
        return []
        
