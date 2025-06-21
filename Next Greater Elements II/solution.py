class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ma=max(nums)
        ans=[-1]*len(nums)
        n=len(nums)
        nums2=nums+nums
        for i in range(n):
            if nums[i]==ma:
                ans[i]=-1
                continue
            cur=nums[i]
            j=i+1
            while True:
                if nums2[j]>cur:
                    ans[i]=nums2[j]
                    break
                j+=1
        return ans

        
