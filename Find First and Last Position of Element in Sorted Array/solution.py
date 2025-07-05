class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]<=target:
                l=mid+1
            else:
                r=mid
        rans=l
        l=0
        r=len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid
        lans=r
        if not nums or lans>len(nums)-1 or rans<0 or  nums[lans]!=target:
            return [-1,-1]
        return [lans,rans-1]
