class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from collections import defaultdict
        d=defaultdict(list)
        wordDict=sorted(wordDict,key=lambda x: len(x))
        for i in wordDict:
            d[i[0]].append(i)
        n=len(s)
        l=0
        dp={}
        def check(i):
            if i==n:
                return True
            if i in dp:
                return dp[i]
            if s[i] in d:
                for sub in d[s[i]]:
                    if s[i:i+len(sub)]==sub:
                        if check(i+len(sub)):
                            return True
                else:
                    dp[i]=False
                    return False
            else:
                dp[i]=False
                return False
        
        return check(0)
