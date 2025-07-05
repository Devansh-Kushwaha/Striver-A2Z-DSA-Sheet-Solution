class Solution:
    def myAtoi(self, s: str) -> int:
        l=0
        n=len(s)
        if 0<n and s[0]==" ":
            l+=1
            while l<n and s[l]==" ":
                l+=1
        sign=1
        if l<n and s[l]=='-':
            sign=-1
            l+=1
        elif l<n and s[l]=='+':
            sign=1
            l+=1
        elif l<n and s[l].isalpha():
            return 0
        r=l
        if l< n and s[l].isnumeric():
            while r<n and s[r].isnumeric():
                r+=1
        else:
            return 0
        ans=sign*(int(s[l:r]))
        check=2**31
        if ans>check-1:
            return check-1
        elif ans<-check:
            return -check
        return sign*(int(s[l:r]))
