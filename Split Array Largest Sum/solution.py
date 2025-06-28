class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)

        def solve(cap):
            count=0
            cursum=0
            for i in nums:
                cursum+=i
                if cursum>cap:
                    count+=1
                    if count>k:
                        break
                    cursum=i
            else:
                if cursum:
                    count+=1
            # print(cap,daycount)
            if count<=k:
                return True
            else:
                return False
                

        while l<r:
            mid=(l+r)//2
            if solve(mid):
                r=mid
            else:
                l=mid+1
        return l
        
        
