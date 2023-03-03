class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        ##convert to binary
        
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000

        #this masks makes it so python has to respect the lengths of 32 BITS for maximum INT instead of dealin g with random values when overflowing
        while (b!=0):
            a,b=(a^b) %MASK,((a&b)<<1)%MASK
        return a if a<=MAX_INT else ~((a%MIN_INT)^MAX_INT)
    
#this problem sucks and is terrible becasue evey language displays 32 bits differently and in java this solution would be efficient because of the way the compiler handles we understand hte logic yet have to make ane xception by using a mask 
        
        