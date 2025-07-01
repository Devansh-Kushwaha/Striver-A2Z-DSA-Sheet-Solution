class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        temp=[-1]
        for i in range(len(nums)):
            if nums[i]%2==1:
                temp.append(i)
        temp.append(len(nums))
        ans=0
        if len(temp)-2<k:
            return 0
        for i in range(1,len(temp)-k):
            r=i+k-1
            left=temp[i]-temp[i-1]
            right=temp[r+1]-temp[r]
            ans+=left*right
        return ans
