class Solution(object):
    def isNumber(self, s):
        i = 0
        sign = 1
        dec_cnt=0 #track incorrect decimals

        try :
            float(s)
        except:
            return False
        if 'nf' in s: return False
        return True
