class Solution:
    def climbStairs(self, n: int) -> int:
        ans=0
        dp=[-1]*n
        def traverse(step):
            if step==n:
                return 1
            elif step>n:
                return 0
            if dp[step]!=-1:
                return dp[step]
            
            x=traverse(step+1)
            y=traverse(step+2)
            dp[step]=x+y
            return x+y 
            
        traverse(0)
        return dp[0]
