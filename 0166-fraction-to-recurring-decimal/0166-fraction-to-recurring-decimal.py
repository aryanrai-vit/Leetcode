class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        def integerPart(n, d):
            return str(int(n/d))
        def fractionPart(n, d):
            res = ""
            mp = dict()
            rem = n % d
            while ((rem != 0) and (rem not in mp)):
                mp[rem] = len(res)
                rem = rem * 10
                res_part = rem // d
                res += str(res_part)
                rem = rem % d
            if (rem == 0):
                return res
            else:
                non_recurring = res[0:mp[rem]]
                recurring = res[mp[rem]:]
                fractionalPart = non_recurring + "("+ recurring + ")"
                return fractionalPart
        
        sign = "-" if numerator*denominator < 0 else ""
        intPart = integerPart(abs(numerator), abs(denominator))
        fractPart = fractionPart(abs(numerator), abs(denominator))
        if fractPart == "":
            ans = sign + intPart
        else:
            ans = sign + intPart+"."+fractPart
        return ans
    
    