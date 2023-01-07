class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #what if we convert to int 1 acts a 9 then convert to binary WE USE XOR AND GATES HERE
        #AND IS OUR CARRY
        #XOR IS OUR ADDITION
        
        
        #convert to binary 
        
        a=int(a,2)
        
        b=int(b,2)
        
        
        while(b!=0):
            a,b=(a^b),(a&b) <<1
        return "{0:b}".format(a)
        
        
        
        
        
        
      