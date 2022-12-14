class Solution(object):
    def isNumber(self, s):
        dec,digit,symbol,e=False,False,False,False
      
            
        
        for char in s:
            if char in "0123456789":
                digit=True
            elif char in "-+":
                if symbol or digit or dec: #we are manually assigning these values to be true based on conditions # if we see symbol or digit or decimal before we encounter -+ then it is automatically false.
                    return False
                else:
                    symbol=True
            elif char in "eE":
                if e or not digit:
                    return False
                else:
                    e=True
                    symbol=False
                    dec=False
                    digit=False
            elif char in ".":
                if dec or e:
                    return False
                else:
                    dec=True
            else:
                return False
        return digit
            
            