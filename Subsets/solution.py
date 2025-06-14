class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        n=len(nums)
        def traverse(l,i):
            nonlocal temp
            if l and i==n:
                temp.append(l)
            if i>=n:
                return
            
            traverse(l+[nums[i]],i+1)
            traverse(l,i+1)
            
            return
        traverse([],0)

        return [[]]+temp
