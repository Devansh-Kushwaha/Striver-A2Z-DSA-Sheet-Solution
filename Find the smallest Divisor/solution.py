import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=max(1,sum(nums)//threshold)
        r=max(nums)
        def valid(mid):
            ans=0
            for i in nums:
                ans+=math.ceil(i/mid)
                if ans>threshold:
                    return ans
            return ans
        while l<r:
            mid=(l+r)//2
            if valid (mid)>threshold:
                l=mid+1
            else:
                r=mid
        return l
        
