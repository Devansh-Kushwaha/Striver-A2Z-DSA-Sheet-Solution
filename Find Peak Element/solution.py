class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 1
        right = len(nums) + 1

        nums = [float('-inf')] + nums + [float('-inf')]

        while left < right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
                return mid - 1  
            elif nums[mid - 1] < nums[mid]:
                left = mid + 1
            else:
                right = mid
