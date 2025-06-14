class Solution:
    def countGoodNumbers(self, n: int) -> int: 
        e = n // 2
        o = e
        if n % 2 == 1:
            e += 1

        ans = 1
        MOD = 10**9 + 7

        def power(num, e):
            ans = 1
            while e > 0:
                if e % 2 == 1:
                    ans *= num
                    ans %= MOD
                    e -= 1
                else:
                    num *= num      
                    num %= MOD
                    e /= 2     
            return ans

       
        ans = power(5,e)

        ans *=power(4,o)
        ans =ans%MOD
        
        return(ans)
