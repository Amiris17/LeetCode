class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #what if we convert to int 1 acts a 9 then convert to binary
        res=""
        carry=0
        
        
        a,b=a[::-1],b[::-1] # reverse the string because we want to start from rhs
        
        #loop through the largest one 
       
        for i in range(max(len(a),len(b))):
            digitA=ord(a[i])-ord("0") if i <len(a) else 0 #giving default value of 0 if we are out of bounds
            digitB=ord(b[i])-ord("0") if i<len(b) else 0 #giving default value of 0 if we are out of bounds
            
            
            total=digitA+digitB +carry
            char=str(total %2)
            
            
            res=char+res
            carry = total // 2
        
        
        if carry:
            res="1"+res
        return res