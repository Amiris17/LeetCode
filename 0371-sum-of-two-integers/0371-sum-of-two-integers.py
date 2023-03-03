from math import log
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        x=pow(2,a)
        y=pow(2,b)
        z=x*y
        return int(log(z,2))
        
       
    
    
        