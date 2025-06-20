class Solution:
    def jump(self, nums: List[int]) -> int:
        ans=0
        i=0
        n=len(nums)
        if n==1:
            return 0
        while i<n:
            all_steps=min(nums[i],n-i-1)
            step=0
            ma=0
            for j in range(1,all_steps+1):
                if i+j==n-1:
                    return ans+1  
                elif ma<nums[j+i]+j:
                    ma=nums[j+i]+j
                    step=j
            i+=step
            ans+=1
        return ans
        
