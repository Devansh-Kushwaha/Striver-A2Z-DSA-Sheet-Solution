class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        d={}
        ma=0
        while l<len(s) and r<len(s):
            if s[r] not in d or d[s[r]]==0:
                d[s[r]]=1
                r+=1
            else:
                while l<len(s) and s[l]!=s[r] and l<r:
                    d[s[l]]=0
                    l+=1
                d[s[l]]=0
                l+=1
            ma=max(ma,r-l)
        return ma
